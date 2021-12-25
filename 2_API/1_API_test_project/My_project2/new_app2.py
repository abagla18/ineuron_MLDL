
# import sys
# import platform
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
import plotly.graph_objects as go
import plotly as py
import plotly.tools as tls
import yfinance as yf

from flask.globals import request
from flask.json import jsonify

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST']) # To render Homepage
def home_page():
    return render_template('index.html')

@app.route('/stock',methods=['Post'])
def stock_chart():











if __name__ == '__main__':
    app.run(debug=True)