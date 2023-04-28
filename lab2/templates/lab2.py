from flask import Flask, render_template, request

app = Flask(__name__)



@app.route('/')
def hello():
    user_data={
        "name":"Мочиева Хадидже",
        "link":"@ghstrl20",
        "img":"luna.jpg",
        "object":"Moon",
        "char":"Прекрасная",
        "description":"Единственный естесственный и самый красивый спутник Земли"
        }
    return render_template("sam.html", user=user_data)
app.run(debug=True)