from flask import Flask, render_template, request
import matplotlib.pyplot as plt
from methods import *
from scipy.interpolate import pchip_interpolate

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def result():
    X = list(map(float, request.form["X"].split(",")))
    Y = list(map(float, request.form["Y"].split(",")))
    targets = list(map(float, request.form["targets"].split(",")))

    Y_newton_forward = [newton_forward(X, Y)(x) for x in targets]
    Y_newton_backward = [newton_backward(X, Y)(x) for x in targets]
    Y_pchip = [pchip_interpolate(X, Y, x) for x in targets]
    Y_everett = [everett_interpolation(X, Y, x) for x in targets]


    return render_template('results.html', targets=targets, n=len(targets), forward=Y_newton_forward, backward=Y_newton_backward, everett=Y_everett, pchip=Y_pchip)

if __name__ == '__main__':
    app.run(debug=True)
