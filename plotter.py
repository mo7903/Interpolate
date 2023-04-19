import os
from bokeh.plotting import figure, output_file, save

# Define a directory to save the images
IMG_DIR = "static/images"

class Plotter():

    def __init__(self, X, Y, targets, interpolated, name):
        self.X = X
        self.Y = Y
        self.targets = targets
        self.interpolated = interpolated
        self.name = name

    def plot(self):
        p = figure(title=f"{self.name} Interpolation", x_axis_label='x', y_axis_label='y')
        p.line(self.X, self.Y, legend_label='True Function')
        p.line(self.targets, self.interpolated, legend_label=f"{self.name} Interpolation", line_color='red')
        p.legend.location = "top_left"
        img_file4 = os.path.join(IMG_DIR, self.name + ".html")
        output_file(img_file4)
        save(p)
