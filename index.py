from flask import Flask, render_template
app = Flask(__name__)
headings = ("xx", "xx", "xx")
data = 0

@app.route("/")

def display_table():
  return render_template("index.html", headings=headings, data=data)