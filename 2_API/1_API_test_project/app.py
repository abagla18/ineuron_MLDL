import sys
import platform

from flask.globals import request
from flask.json import jsonify
print(f"Executable Python: {sys.executable}")
print(f"Python Version: {platform.python_version()}")

from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route('/math_route',methods=['POST'])
def math_operation_via_flask():
    if(request.method=='POST'):
        operation=request.json['operation']
        num1=int(request.json['num1'])
        num2=int(request.json['num2'])

    if(operation =='add'):
        r = num1 + num2
        result = 'The sum of ' + str(num1) + 'and' + str(num2) + 'is' + str(r)
    if(operation =='Sub'):
        r = num1 - num2
        result = 'The sub of ' + str(num1) + 'and' + str(num2) + 'is' + str(r)
    if(operation =='mul'):
        r = num1 * num2
        result = 'The mul of ' + str(num1) + 'and' + str(num2) + 'is' + str(r)
    if(operation =='div'):
        r = num1 / num2
        result = 'The div of ' + str(num1) + ' and ' + str(num2) + 'is' + str(r)

    return jsonify(result)

if __name__ =='__main__':
    app.run()
# print(math_operation_via_flask("add",4,5))



