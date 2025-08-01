from flask import (Flask, request, render_template)


app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')


app.run(debug=True)