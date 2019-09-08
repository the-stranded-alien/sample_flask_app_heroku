from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Flair Prediction Model As Microservice (API)</h1>"

@app.route('/predict', methods=['GET'])
def predict():
    if 'post' in request.args:
        Url = request.args['post']
    else:
        return jsonify("Error : No Post URL provided !")
    
    result = ["Results"]
    return jsonify(list(result))


if __name__ == "__main__":
    app.run(debug=True)