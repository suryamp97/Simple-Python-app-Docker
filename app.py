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
    return render_template('index.html')
  
@app.route('/', methods =["GET", "POST"])
def srch():
    if request.method == "POST":
        kw = request.form.get("search")
        conn = mysql.connect()
        cur = conn.cursor()
        x=0
        cur.execute("INSERT INTO History(x, kw) VALUES (%d, %s)", (x, kw))
        mysql.connection.commit()
        
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
