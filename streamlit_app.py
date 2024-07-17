from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    data = {'name': 'Alice', 'email': '[email protected]'}
    return jsonify(data)

if __name__ == '__main__':
    app.run()
