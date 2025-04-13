from flask import Flask, jsonify, request
import json

app = Flask(__name__)
DATA_FILE = 'users.json'

def load_users():
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except:
        return {}

def save_users(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

@app.route('/api/mine', methods=['POST'])
def mine():
    data = request.json
    user_id = str(data.get("user_id"))
    users = load_users()

    if user_id not in users:
        users[user_id] = {"balance": 0.0}
    
    users[user_id]["balance"] += 0.001  # DOD reward
    save_users(users)

    return jsonify({"balance": users[user_id]["balance"]})

@app.route('/api/balance', methods=['GET'])
def balance():
    user_id = request.args.get("user_id")
    users = load_users()
    balance = users.get(user_id, {}).get("balance", 0.0)
    return jsonify({"balance": balance})

@app.route('/')
def home():
    return "DOD Mining API running!"

if __name__ == '__main__':
    app.run(port=5000)
