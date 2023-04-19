import os
from bokeh.plotting import figure, output_file, save

# Define a directory to save the images
IMG_DIR = "./templates/graphs"

class Plotter():

    def __init__(self, X, Y, targets, interpolated, title):
        self.X = X
        self.Y = Y
        self.targets = targets
        self.interpolated = interpolated
        self.title = title

    def plot(self):
        p = figure(title=f"{self.title} Interpolation", x_axis_label='x', y_axis_label='y')
        p.line(self.X, self.Y, legend_label='True Function')
        p.line(self.targets, self.interpolated, legend_label=f"{self.title} Interpolation", line_color='red')
        p.legend.location = "top_left"
        img_file = os.path.join(IMG_DIR, "_".join(self.title.lower().split()) + ".html")
        output_file(img_file)
        save(p)
        return img_file
