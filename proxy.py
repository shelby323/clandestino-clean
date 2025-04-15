from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

@app.route("/v1/chat/completions", methods=["POST"])
def chat_completions():
    data = request.get_json()
    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json"
        },
        json=data
    )
    return jsonify(response.json()), response.status_code

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=10000)
