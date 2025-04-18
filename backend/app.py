from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow frontend access

@app.route("/api", methods=["GET"])
def get_message():
    return jsonify({"message": "Hello from the backend!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
