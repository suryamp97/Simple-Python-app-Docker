from flask import Flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')
  
@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       first_name = request.form.get("fname")
       # getting input with name = lname in HTML form 
       last_name = request.form.get("lname") 
       return "Your name is "+first_name + last_name
    return render_template("form.html")


if __name__ == "__main__":
    app.run()
