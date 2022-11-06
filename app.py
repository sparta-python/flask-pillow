from flask import Flask
from flask import render_template
from flask import request

from PIL import Image

import process

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["uploadFile"]
    img = Image.open(file)
    img = process.image()
    return img


if __name__ == "__main__":
    app.run(debug=True)
