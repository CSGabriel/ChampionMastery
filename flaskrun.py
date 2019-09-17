from flask import Flask, render_template, url_for, request
import playerMastery
app = Flask(__name__)

@app.route("/", methods = ["POST", "GET"])
def home():
    if request.method == "POST":
        nameForum = request.form['summoner']
        championList = playerMastery.getChampionData(nameForum)
        return render_template('summoner.html', title='Summoner', list = championList, name = nameForum)
    return render_template('home.html', title='Home')

@app.route("/about")
def about():
    return render_template('about.html', title='About')



if __name__ == "__main__":
    app.run(port = 5000, debug=True)
