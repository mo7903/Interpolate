from flask import Flask, render_template, request
from methods import *
from scipy.interpolate import pchip_interpolate
from plotter import Plotter

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

@app.route("/graph", methods=["GET", "POST"])
def graph():
    if request.method == "POST":
        # Define the function to be interpolated
        f = lambda x: np.sin(x)
        # Define the range of x values
        X = np.linspace(1, 10, 100)

        # Compute the true function values
        Y = [f(x) for x in X]
        start = float(request.form["start"])
        end = float(request.form["end"])
        targets = np.linspace(start, end, 50)

        # Compute the values using the interpolation methods
        Y_true = [f(x) for x in targets]
        Y_newton_forward = [newton_forward(X, Y)(x) for x in targets]
        Y_newton_backward = [newton_backward(X, Y)(x) for x in targets]
        Y_pchip = [pchip_interpolate(X, Y, x) for x in targets]
        Y_everett = [everett_interpolation(X, Y, x) for x in targets]

        # Generate the plots using bokeh
        plots = []
        p1 = Plotter(X, Y, targets, Y_everett, title="Everett Function")
        plots.append(p1.plot())
        p2 = Plotter(X, Y, targets, Y_newton_forward, title="Newton Forward Interpolation")
        plots.append(p2.plot())
        p3 = Plotter(X, Y, targets, Y_newton_backward, title="Newton Backward Interpolation")
        plots.append(p3.plot())
        p4 = Plotter(X, Y, targets, Y_pchip, title="PCHIP Interpolation")
        plots.append(p4.plot())

        # Render the graph_results.html template with the list of plot srcs
        return render_template("graph_results.html", plots=plots)
    else:
        return render_template("graph.html")

@app.route("/template/<path>")
def template(path):
    return render_template("/graphs/" + path)


if __name__ == '__main__':
    app.run(debug=True)
