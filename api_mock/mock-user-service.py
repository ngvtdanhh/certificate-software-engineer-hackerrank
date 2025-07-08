# mock-user-service.py
from flask import Flask, jsonify, request
import time

app = Flask(__name__)

# Sample mock user database
users = {
    "alice": {"valid": True, "role": "admin"},
    "bob": {"valid": True, "role": "user"},
    "charlie": {"valid": False, "role": "suspended"}
}

@app.route("/api/user/<username>", methods=["GET"])
def validate_user(username):
    # Simulate latency
    time.sleep(0.5)

    user = users.get(username)
    if user:
        return jsonify({"status": "ok", "user": user}), 200
    return jsonify({"status": "error", "message": "User not found"}), 404

@app.route("/api/ping", methods=["GET"])
def ping():
    return jsonify({"status": "alive"}), 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)
