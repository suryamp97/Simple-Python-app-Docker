from flask import Flask, request, render_template 
import tweepy

app = Flask(__name__)

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
        tweets = []
        c=0
        for tweet in tweepy.Cursor(api.search,q=kw, count=10).items(10):  
            tj=tweet._json
            tweets.append(tj["text"])
        return "TWEETS: " + tweets
    return render_template("index.html")


if __name__ == "__main__":
    
    app.run()
