from flask import Flask
from flask.globals import request
from flask.templating import render_template
app = Flask(__name__)

@app.route('/')
def home():
    mylist = {'aaa','bbb','ccc','ddd'}
    objlist = []
    objlist.append(
                    {
                    "e_id" : "a1",
                    "e_name" : "a2",
                    "birth" : "a3" 
                    }
                )
    objlist.append(
                    {
                    "e_id" : "b1",
                    "e_name" : "b2",
                    "birth" : "b3" 
                    }
                )
    test = "야ㅗㅎ"
    return render_template('ans.html', title=mylist, str=str(test), objlist=objlist)

if __name__ == '__main__':
    app.run(debug=True)