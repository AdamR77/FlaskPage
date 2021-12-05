from flask import Flask
from flask import render_template, request, redirect, url_for
app = Flask(__name__)


@app.route("/base", methods=['GET'])
def base():
    return render_template("base.html")


@app.route("/info", methods=['GET', 'POST'])
def info():
    items = "podróże", "turystyka górska","krav-maga", "neurochemia", "rynki finansowe",\
            "technologia blockchain i kryptowaluty", "nauka programowania", "materiały kompozytowe"
    return render_template("info.html", items = items)


if __name__ == "__main__":
    app.run(debug=True)
