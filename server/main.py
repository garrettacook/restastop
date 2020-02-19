from flask import Flask, jsonify
import json

app = Flask(__name__)

data = json.load(open('data.json', 'r'))


@app.route("/")
def handle_root():
  return "test"

@app.route("/items"):
  return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
