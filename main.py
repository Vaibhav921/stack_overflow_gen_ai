# main.py

from controller import fetch_stackoverflow_answers
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/answers", methods=["POST"])
def get_answers():
    if request.is_json:
        data = request.get_json()
        question = data.get("question")
    else:
        question = request.form.get("question")
    if not question:
        return jsonify({"error": "Missing question parameter"}), 400
    answers = fetch_stackoverflow_answers(question)
    return jsonify(answers)


def main():
    app.run(host="0.0.0.0", port=5000, debug=True)


if __name__ == "__main__":
    main()
