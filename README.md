# Interpolation Plotter

## Getting Started

To get started with this project, follow the steps below:

1. Clone this repository to your local machine.
2. Install the required dependencies using  (`pip install -r requirements.txt`).
3. Run the Flask application using (`python app.py`) or (`flask run`).
4. Open a web browser and navigate to http://localhost:5000/.

## Usage
This is a simple web application that allows users to plot and compare different interpolation methods for a given function or set of points. All methods except PCHIP require even spaced data points. Stirling & Everett are designed to work correctly near the midpoint of given data. Newton Forward shows greatest accuracy at the start, while the backward method is accurate near the end. PCHIP is a Cubic Spline method that shows high accuracy in general.

The available methods are:
1.    Stirling Interpolation
2.    Newton Forward Interpolation
3.    Newton Backward Interpolation
4.    PCHIP Interpolation
5.    Everett Interpolation

The plots are generated using the Bokeh library and are displayed on a results page. Clicking on a plot will open a new tab displaying the plot in more detail.

## Additional Projects

### 3D Spline Graphics
This project builds on the spline interpolation techniques used in the Interpolation Plotter to create 3D graphics. The goal is to create smooth and realistic animations of 3D objects. The cubic spline interpolation method is used to create smooth curves and surfaces.

### Network Traffic Data Interpolation
This project demonstrates how spline interpolation can be used to fill in missing data in network traffic. The data is first smoothed using a moving average filter and then a cubic spline is fit to the smoothed data. The interpolated data is then plotted to visualize the original and interpolated data. This can improve the accuracy of prediction techniques that rely on network traffic data.