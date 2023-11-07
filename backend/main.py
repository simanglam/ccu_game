from flask import Flask, request, jsonify, Response
import requests
import os
import json

app = Flask(__name__)

game_states = {
    "current_team": 1,
    "team": [
        {"score": 0,
         "money": 3000
        },
        {"score": 0,
         "money": 3000
        },
        {"score": 0,
         "money": 3000
        },
        {"score": 0,
         "money": 3000
        },
    ]
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

@app.route('/states', methods = ['GET'])
def get_states():
    return jsonify(game_states)

@app.route('/team/<int:team_id>', methods = ['GET'])
def get_team_money(team_id):
    if not team_id > len(game_states["team"]) and team_id > 0:
        return jsonify({"money": game_states["team"][team_id - 1]["money"], "score": game_states["team"][team_id - 1]["score"], "current": team_id == game_states["current_team"]})
    else:
        return Response(status = 404, response = json.dumps({"message": f"隊伍 {team_id} 不存在"}), content_type = "application/json")

@app.route('/team/<int:team_id>/money', methods = ['POST'])
def set_team_money(team_id):
    if not team_id > len(game_states["team"]) and team_id > 0:
        body = request.get_json()
        game_states["team"][team_id - 1]["money"] = body["money"]
        return jsonify({"money": game_states["team"][team_id - 1]["money"]})
    else:
        return Response(status = 404, response = json.dumps({"message": f"隊伍 {team_id} 不存在"}), content_type = "application/json")
    
@app.route('/team/<int:team_id>/score', methods = ['POST'])
def set_team_score(team_id):
    if not team_id > len(game_states["team"]) and team_id > 0:
        body = request.get_json()
        game_states["team"][team_id - 1]["score"] = body["score"]
        return jsonify({"score": game_states["team"][team_id - 1]["score"]})
    else:
        return Response(status = 404, response = json.dumps({"message": f"隊伍 {team_id} 不存在"}), content_type = "application/json")


@app.route('/roll', methods = ['POST'])
def roll():
    print(request.get_json())
    body = request.get_json()
    if body["team"] == game_states["current_team"]:
        requests.post("http://127.0.0.1:5000", timeout=1)
        game_states["current_team"] = -1
        return jsonify({"state": "Ok", "Description" : "Succeed"})
    else:
        return Response(status = 400, response = json.dumps({"message" : "Not current team"}), content_type = "application/json")

if __name__ == "__main__":
    app.run('0.0.0.0', 4000, False, threaded = True)