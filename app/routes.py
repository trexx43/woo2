from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/quiz_result', methods = ["GET", "POST"])
def quix():
    if request.method == "GET":
         return "hello u use a car"
    else:
        print("world")
        user_data = request.form
        print(user_data)
        transport = user_data["transportation"]
        recycle = user_data["recycle"]
        animal = user_data["animal"]
        name = user_data["name"]
        print("your transpo method is " +transport+ " and you " +recycle+ "  recycle and eat animal products " +animal+ ". your name is " +name)
        final_score = model.carbon_footprint(transport, recycle, animal)
        suggestion = model.suggestion(transport, recycle, animal)
        print(final_score)
        print(suggestion)
        return render_template("quiz.html", final_score = final_score, name = name, suggestion = suggestion)

