from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Flair Prediction Model As Microservice (API)</h1>"

if __name__ == "__main__":
    app.run(debug=True)