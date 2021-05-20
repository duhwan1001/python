from flask import Flask
from flask.globals import request
from flask.json import jsonify
app = Flask(__name__, static_url_path="") # static 경로 설정

@app.route('/')
def index():
    return "Hello World"

@app.route('/ajax', methods=['POST'])
def home():
    data = request.get_json()
    print(data)
    return jsonify(result = "success", result2= data)

if __name__ == '__main__':
    app.run(debug=True)