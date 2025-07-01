# leaderboard.py

import json, os
from config import LEADERBOARD_FILE, LEADERBOARD_MAX_ENTRIES

def get_leaderboard():
    if not os.path.exists(LEADERBOARD_FILE): return []
    with open(LEADERBOARD_FILE,'r') as f: data=json.load(f)
    return data

def save_score(name,score):
    lb=get_leaderboard()
    lb.append({"name":name,"score":score})
    lb=sorted(lb,key=lambda x:-x["score"])[:LEADERBOARD_MAX_ENTRIES]
    with open(LEADERBOARD_FILE,'w') as f: json.dump(lb,f)
