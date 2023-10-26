from flask import Flask, request, jsonify, Response
import requests
import os

app = Flask(__name__)

game_states = {
    "current_team": 1,
    "team_money": [3000, 3000, 3000, 3000]   
}

@app.route('/', methods = ['GET'])
def get_index():
    return ''.join(open('./index.html').readlines())

@app.route('/reload', methods = ['POST'])
def game_reload():
    game_states["current_team"] = 1
    game_states["team_money"] = [3000, 3000, 3000, 3000]
    return ''

@app.route('/set_current_team', methods = ['POST'])
def set_team():
    body = request.get_json()
    game_states["current_team"] = body['team']
    return ''

@app.route('/team_money', methods = ['POST'])
def set_team_money():
    body = request.get_json()
    game_states["team_money"][body["team"] - 1] = body["money"]
    return ''

@app.route('/team_money', methods = ['GET'])
def get_team_money(team_id):
    team_id = request.args.get('team_id', 0, int)
    if team_id != 0:
        return jsonify({"money": game_states["team_money"][team_id - 1]})
    else:
        return jsonify({"money": -1})

@app.route('/roll', methods = ['POST'])
def roll():
    body = request.get_json()
    if body["team"] == game_states["current_team"]:
        requests.post("http://127.0.0.1:5000")
        game_states["current_team"] += 1
        if game_states["current_team"] > 4:
            game_states["current_team"] = 0
        return jsonify({"state": "Ok", "Description" : "Succeed"})
    else:
        return jsonify({"state": "Reject", "Description" : "Not Current_team"})

app.run('127.0.0.1', 4000, True)