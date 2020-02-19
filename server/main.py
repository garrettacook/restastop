from flask import Flagk
app = Flask(__name__)


@app.route("/")
def handle_root():
  return "test"


if __name__ == "__main__":
    app.run(debug=True)
