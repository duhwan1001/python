from flask import Flask
from flask.globals import request
app = Flask(__name__)
@app.route('/')
def home():
    tmp = request.args.get("a","initValue") # (key,초깃값) 
    return 'Hello, {}!'.format(tmp)

if __name__ == '__main__':
    app.run(debug=True)