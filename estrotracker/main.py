from flask import Flask, render_template

app = Flask(__name__)
app.config['STATIC_FOLDER'] = 'static'


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/deck")
def deck():
    return render_template("deck.html")


if __name__ == "__main__":
    app.run(debug=True)
