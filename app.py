from flask import Flask, render_template, request, redirect, session, flash
from flask_session import Session
import os
import uuid

app = Flask(__name__)

#Session Settings
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

file_save_location = "static/images"
allowed_types = [".png", ".jpg"]

#Homepage
@app.route("/", methods=["GET"])
def index():
    if "videoGames" not in session:
        print("clearing games")
        session["videoGames"] = []
    print(session.get("videoGames"))
    total_value = 0.0
    for game in session.get("videoGames"):
        try:
            total_value += float(game.get("price", 0))
        except (ValueError, TypeError):
            print(f"Price entered was invalid for {game}")
    return render_template("index.html", games=session.get("videoGames"), file_location=file_save_location,total_value=total_value)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")