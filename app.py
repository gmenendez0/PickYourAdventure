from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/start', methods=['POST'])
def start_adventure():
    return jsonify()

@app.route('/choose', methods=['POST'])
def choose_path():
    data = request.json
    choice = data.get('choice')
    return jsonify()

if __name__ == "__main__":
    app.run(debug=True)