from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def test_get():
    return "success neww 111", 200


@app.route("/", methods=["POST"])
def test_post():
    return "post success", 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")