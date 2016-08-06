from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/")
def index(user=None):
    return render_template("header-basic-light.html")

@app.route("/shopping")
def shopping():
    food = ["Cheese","Tuna","Beef","Toothpaste"]
    return render_template("shopping.html", food=food)
if __name__ == '__main__':
    app.run(debug=True)
