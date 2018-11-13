from flask import Flask,request
from flask_cors import CORS
app = Flask(__name__)
CORS(app, support_credentials=True)
@app.route('/')
def one():
    return "hello"

@app.route('/testA', methods=['GET','POST'])
def test_action():
    usr = request.args['usr']
    ps = request.args['ps']
    if usr != 'abc' or ps != '123':
        return "log no success"
    else:
        return "log yes"
