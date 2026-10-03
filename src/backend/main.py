from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submit-journey", methods=["POST"])
def submit_journey():

    data = request.get_json()

    registration = data.get("registration")
    journey = data.get("journey")

    print("Registration:", registration)
    print("Journey:", journey)

    # Do whatever processing/database work you need here

    return jsonify({
        "message": "Journey submitted successfully!"
    })


if __name__ == "__main__":
    app.run(debug=True)