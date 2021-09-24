from flask import Flask, request, render_template 
from flaskext.mysql import MySQL
import tweepy
app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'test'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


auth = tweepy.OAuthHandler("AC7WkBbTptQM1F9vPvaWMnPu0", "6Kv4MuuLHX3FvB0PxNLZaa1ajyIIrnGqVQriBvmYzGD8u2fD3O")
auth.set_access_token("1433835629763338242-SMviK8BJ5FcBnrrYBj9CMWIoDRX8Uu", "8hcho5OJ03WadpgMjfEgvUhzX3sOJ3DNWoIvOAyqc0sdc")
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


@app.route("/")
def main():
    conn = mysql.connect()
    cur = conn.cursor()
    operation= 'select * from history order by id desc limit 10'
    for result in cur.execute(operation):
        if result.with_rows:
            print("Rows produced by statement '{}':".format(result.statement))
            print(result.fetchall())
        else:
            print("Number of rows affected by statement '{}': {}".format(
            result.statement, result.rowcount))
    
    conn.commit()        
    cur.close()
    return render_template('index.html',data)
  
@app.route('/', methods =["GET", "POST"])
def srch():
    if request.method == "POST":
        kw = request.form.get("search")
        conn = mysql.connect()
        cur = conn.cursor()
        x=0
        cur.execute("INSERT INTO History(id, keyw) VALUES (%s, %s)", (x, kw))
        conn.commit()
        
        cur.close()
        
        tweets = []
        c=0
        for tweet in tweepy.Cursor(api.search,q=kw, count=10).items(10):  
            tj=tweet._json
            tweets.append(tj["text"])
        return "TWEETS: " + str(tweets)
    return render_template("index.html")


if __name__ == "__main__":
    
    app.run()
