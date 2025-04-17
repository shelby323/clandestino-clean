from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

@app.route("/v1/chat/completions", methods=["POST"])
def chat_completions():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON payload received"}), 400

    print("[proxy] Incoming data:", data)

    try:
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENAI_API_KEY}",
                "Content-Type": "application/json"
            },
            json=data,
            timeout=15
        )
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        print("[proxy] Request error:", str(e))
        return jsonify({"error": "Request to OpenAI failed", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=10000)
