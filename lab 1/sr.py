from flask import Flask

app = Flask(__name__)

@app.route("/resurs/")
def page_resurs():
   return '<a href = "https://www.youtube.com/watch?v=bMEr3VnIh54">Ссылка </a>'


@app.route("/pages/int:<pid>")
def profile(pid):
    print (type(pid))
    return f"Hello{pid}"

app.run(debug=True)