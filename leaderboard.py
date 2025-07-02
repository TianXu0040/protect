# leaderboard.py

import json, os
from config import LEADERBOARD_FILE, LEADERBOARD_MAX_ENTRIES

LB_PATH = os.path.join(os.path.dirname(__file__), LEADERBOARD_FILE)

def get_leaderboard():
    if not os.path.exists(LB_PATH):
        return []
    with open(LB_PATH, 'r') as f:
        data = json.load(f)
    return data

def save_score(name,score):
    lb = get_leaderboard()
    lb.append({"name": name, "score": score})
    lb = sorted(lb, key=lambda x: -x["score"])[:LEADERBOARD_MAX_ENTRIES]
    with open(LB_PATH, 'w') as f:
        json.dump(lb, f)
