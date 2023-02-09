import time
from os import path
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np


class Canvas(FigureCanvas):
    """
    matplotlib
    """
    def __init__(self, figure=None):
        super().__init__(figure)
        self.dynamic_canvas = None
        self.static_canvas = None

    def graph(self):
        """
        """
        # dpi = size
        self.dynamic_canvas = FigureCanvas(Figure(figsize=(5, 5), dpi=90))
        self.ax = self.dynamic_canvas.figure.subplots()
        self.ax.set_ylim([-1, 1])
        self.ax.set_xlim([-1, 1])
        self.ax.set_title("Graph")
        self.ax.set_xlabel('X Axe')
        self.ax.set_ylabel('Y Axe')
        # margin
        self.dynamic_canvas.move(10, 15)
        # x = 0, y = 0, radius = 1 color = red, alpha = transparency
        circle1 = plt.Circle((0, 0), 1, color='r', fill=False, alpha=0.7)
        self.ax.add_patch(circle1)

        # coordinates of quadrant (polygon)
        x, y = [-1, -1, 1, 1], [-1, 1, 1, -1]
        # alpha = transparency, c = color
        self.ax.fill(x, y, alpha=0.6, c='gray')
        # s=size, marker=point style, color=color, alpha=transparency
        self._scatter = self.ax.scatter(x=0, y=0, s=5, marker='.', color='black', alpha=0.1)


    def three(self):
        """
        """
        # dpi = size
        self.three_canvas = FigureCanvas(Figure(figsize=(5, 5), dpi=90))
        self.ax = self.three_canvas.figure.subplots()
        self.ax.set_ylim([0, 1])
        self.ax.set_xlim([0, 1])
        self.ax.set_title("Graph")
        self.ax.set_xlabel('X Axe')
        self.ax.set_ylabel('Y Axe')
        # margin
        self.three_canvas.move(10, 15)

        # triangle points
        x_points, y_points = [0, 1, 1, 0], [0, 1, 0, 0]

        self.ax.plot(x_points, y_points, 'o-r', alpha=0.7, label="first", lw=5, mec='b', mew=2, ms=10)
        self.ax.fill_between(x_points, y_points, color='g', alpha=.7)

        #self.ax.plot(x, f1, ':b')    # пунктирная синяя линия
        #self.ax.plot(x, f2, '--r')   # штрихованная красная линия
        #self.ax.plot(x, f1+f2, 'k')  # черная непрерывная линия

        # coordinates of quadrant (polygon)
        x, y = [0, 0, 1, 1], [0, 1, 1, 0]
        # alpha = transparency, c = color
        self.ax.fill(x, y, alpha=0.6, c='gray')



    def histogram(self, points_x, points_y):
        """
        :param points_x: x axis point
        :param points_y: y axis point
        """
        self.fig = Figure(figsize=(3, 3), dpi=120)
        FigureCanvas.__init__(self, self.fig)
        self.ax = self.figure.add_subplot(111)  # Hist

        # histtype = 'bar', 'barstacked', 'step', 'stepfilled'
        # orientation = 'vertical', 'horizontal'
        # align = 'left', 'mid', 'right'
        # alpha = transparency
        self.hist = self.ax.hist(x=points_x, bins=None, range=None, weights=None, cumulative=False,
                                 bottom=None, histtype='bar', align='mid', orientation='vertical',
                                 rwidth=None, log=False, color='green', stacked=True,
                                 edgecolor="black", alpha=0.6)
        self.hist2 = self.ax.hist(x=points_y, align='mid', orientation='vertical',
                                 color='yellow', edgecolor="black", alpha=0.6)
        self.ax.set_title("x = green |^_^| y = yellow")
        self.ax.set_xlabel('Numbers')
        self.ax.set_ylabel('quantity of random numbers')
        self.ax.patch.set_facecolor('white')

    def save(self, type=""):
        """
        :param type: "histogram", "graph"
        :return:
        """
        name = time.asctime(time.localtime(time.time())).replace(' ', '_').replace(':', '-')
        # self.canvas.dynamic_canvas.figure.savefig(f"graph_{name}.png", dpi=200)
        self.figure.savefig(f"{type}_{name}.png", dpi=200)
        # check if file has been saved
        a = path.exists(f'{type}_{name}.png')
        if a:
            print(f'{type}_{name}.png has been saved successfully')
        else:
            print(f"{type}_{name}.png hasn't been saved")