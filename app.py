from flask import Flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')
  
@app.route('/', methods =["GET", "POST"])
def srch():
    if request.method == "POST":
       kw = request.form.get("search")
       return "Your name is " + kw
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
