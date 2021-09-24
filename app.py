from flask import Flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!"
  
if __name__ == "__main__":
    return render_template('index.html')
