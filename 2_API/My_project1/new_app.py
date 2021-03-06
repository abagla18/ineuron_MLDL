from flask.globals import request
from flask.json import jsonify

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST']) # To render Homepage
def home_page():
    return render_template('index.html')

@app.route('/square', methods=['POST'])
def my_square():
    if (request.method=='POST'):
        num1=int(request.form['num1'])
        result = num1**2
    return render_template('results.html',result=result)

    
if __name__ == '__main__':
    app.run(debug=True)