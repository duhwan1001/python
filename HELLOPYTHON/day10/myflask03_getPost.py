from flask import Flask
from flask.globals import request
from flask.templating import render_template
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if(request.method == "POST"):
        value = request.form.get('a',"하하하")
        return '출력값(post) : {}'.format(value)
    else:
        tmp = request.args.get("a","initValue") 
        return '출력값(get) : {}'.format(tmp)

if __name__ == '__main__':
    app.run(debug=True)