from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Root page with your WebApp interface (mining UI)
@app.route("/")
def home():
    return render_template("index.html")

# Example mining action route
@app.route("/mine", methods=["POST"])
def mine():
    # You can handle user ID, cooldowns, etc. here
    user_id = request.json.get("user_id")
    # Basic response for now
    return jsonify({"success": True, "reward": 0.001, "message": f"User {user_id} mined 0.001 DOD!"})

# You can add more API routes like /balance, /airdrop, etc.

# Gunicorn will run this app — no app.run() needed
