from flask import Flask,render_template,request
import requests
import os

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get('http://127.0.0.1:5000/api/teams')
    teams = response.json()['teams']
    return render_template('index.html',teams = sorted(teams))

@app.route('/teamvteam')
def team_vs_team():
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')

    response = requests.get('http://127.0.0.1:5000/api/team_vs_team?team1={}&team2={}'.format(team1,team2))
    response = response.json()

    response1 = requests.get('http://127.0.0.1:5000/api/teams')
    teams = response1.json()['teams']

    return render_template('index.html',result = response,teams = sorted(teams))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7000))  # default for local dev
    app.run(host="0.0.0.0", port=port, debug=True)