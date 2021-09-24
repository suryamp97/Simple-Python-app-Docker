from flask import Flask, request, render_template ,jsonify
import mysql.connector
import tweepy
app = Flask(__name__)
mysql = MySQL()

# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = ''
# app.config['MYSQL_DATABASE_DB'] = 'test'
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# mysql.init_app(app)


auth = tweepy.OAuthHandler("AC7WkBbTptQM1F9vPvaWMnPu0", "6Kv4MuuLHX3FvB0PxNLZaa1ajyIIrnGqVQriBvmYzGD8u2fD3O")
auth.set_access_token("1433835629763338242-SMviK8BJ5FcBnrrYBj9CMWIoDRX8Uu", "8hcho5OJ03WadpgMjfEgvUhzX3sOJ3DNWoIvOAyqc0sdc")
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


@app.route("/")
def main():
    config = {
        'user': 'root',
        'password': '',
        'host': 'localhost',
        'database': 'test'
    }
    connection = mysql.connector.connect(**config)
    cur = connection.cursor()
    operation= 'select * from history order by id desc limit 10'
    cur.execute(operation)
    data=cur.fetchall()
    print(type(data))
    ll=[]
    for i in data:
        dt={}
        dt["keyw"]=i[1]
        ll.append(dt)
        
    conn.commit()        
    cur.close()
    return render_template('index.html',data=ll)
  
@app.route('/', methods =["GET", "POST"])
def srch():
    if request.method == "POST":
        kw = request.form.get("search")
        config = {
            'user': 'root',
            'password': '',
            'host': 'localhost',
            'database': 'test'
        }
        connection = mysql.connector.connect(**config)
        cur = connection.cursor()
        x=0
        cur.execute("INSERT INTO History(id, keyw) VALUES (%s, %s)", (x, kw))
        conn.commit()
        
        cur.close()
        
        tweets = []
        c=0
        for tweet in tweepy.Cursor(api.search,q=kw, count=10).items(10):  
            tj=tweet._json
            tweets.append(tj["text"])
        str_='TOP TWEETS FOR THE KEYWORD: '+kw+"\n\n"
        for i in range(len(tweets)):
            str_= str_ + str(i+1) + ")  " + tweets[i]+ "\n"
            
        return  str_
    return render_template("index.html")


if __name__ == "__main__":
    
    app.run()
