from flask import Flask, render_template
import os

app = Flask(__name__)

IMG_FOLDER = os.path.join("static", "IMG")

app.config["UPLOAD_FOLDER"] = IMG_FOLDER


@app.route("/")
def Display_IMG():
    Flask_Logo = os.path.join(app.config["UPLOAD_FOLDER"], "logo_flask.png")
    return render_template("index.html", user_image=Flask_Logo)



app.run(host="0.0.0.0")



