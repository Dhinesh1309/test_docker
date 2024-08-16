from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def test():
    return "success", 200


@app.route("/", methods=["POST"])
def test():
    return "post success", 200


@app.route("/", methods=["PUT"])
def test_put():
    return "post success", 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")