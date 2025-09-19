from flask import Flask, jsonify, request
import ipl
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello World!</h1>'

@app.route('/api/teams')
def teams():
    team = ipl.teamsAPI()
    return jsonify(team)

@app.route('/api/team_vs_team')
def team_vs_team():
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')
    teamvsteam = ipl.teamVteamAPI(team1, team2)
    return jsonify(teamvsteam)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render will set PORT
    app.run(host="0.0.0.0", port=port, debug=True)
