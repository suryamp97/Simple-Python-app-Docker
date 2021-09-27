from flask import Flask, request, render_template ,jsonify
import mysql.connector
import tweepy

app = Flask(__name__)
auth = tweepy.OAuthHandler("AC7WkBbTptQM1F9vPvaWMnPu0", "6Kv4MuuLHX3FvB0PxNLZaa1ajyIIrnGqVQriBvmYzGD8u2fD3O")
auth.set_access_token("1433835629763338242-SMviK8BJ5FcBnrrYBj9CMWIoDRX8Uu", "8hcho5OJ03WadpgMjfEgvUhzX3sOJ3DNWoIvOAyqc0sdc")
api = tweepy.API(auth, wait_on_rate_limit=True)



@app.route('/search', methods =["GET", "POST"])
def srch():
    if request.method == "POST":
        kw = request.form.get("search")
        config = {'user': 'root','password': 'root','host': 'db','port': '3306','database': 'htest'}
        connection = mysql.connector.connect(**config)
        cur = connection.cursor()
        x=0
        print("rtdgfgfchgvjh")
        cur.execute("INSERT INTO History(id, keyw) VALUES (%s, %s)", (x, kw))
        connection.commit()
        
        cur.close()
        
        tweets = []
        c=0
        for tweet in tweepy.Cursor(api.search,q=kw, count=10).items(10):  
            tj=tweet._json
            tweets.append(tj["text"])
        str_='TOP TWEETS FOR THE KEYWORD: '+kw+"<br/><br/>"
        for i in range(len(tweets)):
            str_= str_ + str(i+1) + ")  " + tweets[i]+ "<br/><br/>"
            
        return  str_
    return render_template("index.html")


@app.route('/')
def index():
	config = {'user': 'root','password': 'root','host': 'db','port': '3306','database': 'htest'}
	connection = mysql.connector.connect(**config)
	cur = connection.cursor()
	cur.execute('select * from History order by id desc limit 10')
	data=cur.fetchall()
	print(type(data))
	ll=[]
	for i in data:
	    dt={}
	    dt['keyw']=i[1]
	    ll.append(dt)
	connection.commit()
	cur.close()
	return render_template('index.html',data=ll)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
