import time
from os import path
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.patches as plt_arc
import numpy as np
from matplotlib.animation import FuncAnimation

from numpy import sin, cos, pi, linspace


class Canvas(FigureCanvas):
    """
    matplotlib
    """
    def __init__(self, figure=None):
        super().__init__(figure)
        self.dynamic_canvas = None
        self.static_canvas = None


    def graph(self, x_hypotenuse=[0, .7], y_hypotenuse=[0, .7], x_gegenkathete=[.7, .7], y_gegenkathete=[.7, 0], x_ankathete=[0, .7], y_ankathete=[0, 0], arc = 45):

        # dpi = size
        self.dynamic_canvas = FigureCanvas(Figure(figsize=(3, 15), dpi=100))
        self.ax = self.dynamic_canvas.figure.subplots()
        self.ax.set_ylim([-1, 1])
        self.ax.set_xlim([-1, 1])
        self.ax.set_title("Graph")
        self.ax.set_xlabel('X Axe')
        self.ax.set_ylabel('Y Axe')
        # plt.grid(color='r', linestyle='dotted', linewidth=1)

        # margin
        self.dynamic_canvas.move(10, 15)
        # x = 0, y = 0, radius = 1 color = red, alpha = transparency
        circle1 = plt.Circle((0, 0), 1, color='r', fill=False, alpha=0.7)
        self.ax.add_patch(circle1)
        # to fix equel x and y
        self.ax.set_aspect('equal', 'box')
        # axes
        self.ax.axhline(y=0, color='k')
        self.ax.axvline(x=0, color='k')
        # grid
        self.ax.grid(axis='both', color='k', linestyle='-', linewidth=.3, alpha=0.7)
        ############# axes
        #self.ax.plot([0, 0], [-1, 1], alpha=0.3)
        #self.ax.plot([1, -1], [0, 0], alpha=0.3)

        # The coordinates of quadrant (polygon) -> (square)
        x, y = [-1, -1, 1, 1], [-1, 1, 1, -1]
        # alpha = transparency, c = color
        self.ax.fill(x, y, alpha=0.6, c='gray')
        # s=size, marker=point style, color=color, alpha=transparency
        self._scatter = self.ax.scatter(x=0, y=0, s=5, marker='.', color='black', alpha=0.1)

        # triaangle plot
        self.ax.plot(x_hypotenuse, y_hypotenuse, 'o-r', alpha=0.7, label = 'Hypotenuse', lw=5, mec='b', mew=2, ms=10)
        self.ax.plot(x_gegenkathete, y_gegenkathete, 'o-g', alpha=0.7, label = 'Gegenkathete', lw=5, mec='b', mew=2, ms=10)
        self.ax.plot(x_ankathete, y_ankathete, 'o-b', alpha=0.7, label = 'Ankathete', lw=5, mec='b', mew=2, ms=10)

        # self.ax.annotate('Hypotenuse', xy=(x_hypotenuse[0], y_hypotenuse[0]), xytext=(x_hypotenuse[1], y_hypotenuse[1]), arrowprops={'facecolor': 'red', 'shrink': 0.01})

        # fix 0 radius
        # self.ax.plot([0, 1], [0, 0], 'y', alpha=0.7, lw=5, mec='b', mew=2, ms=10)
        
        # Winkel Arc (Alternative .Arc)
        arc_draw = plt_arc.Wedge(center=0, r=1, theta1=0, theta2=arc, width=0.7, fill=True, color='yellow', edgecolor="green", alpha=0.2)        
        self.ax.add_patch(arc_draw)

    def triangle(self):
        """
        """
        # dpi = size
        self.triangle_canvas = FigureCanvas(Figure(figsize=(5, 5), dpi=90))
        self.ax = self.triangle_canvas.figure.subplots()
        self.ax.set_ylim([-0.2, 2])
        self.ax.set_xlim([-0.2, 2])
        self.ax.set_title("Triangle")
        self.ax.set_xlabel('X Axe')
        self.ax.set_ylabel('Y Axe')
        # margin
        self.triangle_canvas.move(10, 15)

        # The initialization of triangle points
        x_hypotenuse, y_hypotenuse = [0, 1.5], [0, 1.5]
        x_gegenkathete, y_gegenkathete = [1.5, 1.5], [1.5, 0]
        x_ankathete, y_ankathete = [0, 1.5], [0, 0]

        # triaangle plot
        self.ax.plot(x_hypotenuse, y_hypotenuse, 'o-r', alpha=0.7, label = 'Hypotenuse', lw=5, mec='b', mew=2, ms=10)
        self.ax.plot(x_gegenkathete, y_gegenkathete, 'o-g', alpha=0.7, label = 'Gegenkathete', lw=5, mec='b', mew=2, ms=10)
        self.ax.plot(x_ankathete, y_ankathete, 'o-b', alpha=0.7, label = 'Ankathete', lw=5, mec='b', mew=2, ms=10)

        # Winkel Arc
        """
        arc_angles = linspace(0 * pi, pi/4, 30)
        arc_xs = 0.3 * cos(arc_angles)
        arc_ys = 0.3 * sin(arc_angles)
        self.ax.plot(arc_xs, arc_ys, color = 'yellow', lw = 3)
        """
        arc_draw = plt_arc.Wedge(center=0, r=.3, theta1=0, theta2=45, width=0.03, fill=True, color='black', edgecolor="green")  
        self.ax.add_patch(arc_draw)
    
        # annotates
        self.ax.annotate('Hypotenuse', xy=(1, 1), xytext=(0.7, 1.3), arrowprops={'facecolor': 'red', 'shrink': 0.01})
        self.ax.annotate('Gegenkathete', xy=(1.5, 1), xytext=(1.7, 1), arrowprops={'facecolor': 'green', 'shrink': 0.01}, rotation = 270)
        self.ax.annotate('Ankathete', xy=(1, 0), xytext=(1, 0.3), arrowprops={'facecolor': 'blue', 'shrink': 0.01})
        self.ax.annotate('Winkel α', xy=(0.29, 0.1), xytext=(0.5, 0.3), arrowprops={'facecolor': 'yellow', 'shrink': 0.04})

    def circle(self):
        self.x = np.linspace(0, 30, 100)
        self.y = np.sin(self.x)
         # dpi = size
        self.animation_canvas = FigureCanvas(Figure(figsize=(3, 15), dpi=100))
        self.ax = self.animation_canvas.figure.subplots()
        self.ax.set_ylim([-1, 1])
        self.ax.set_xlim([-1, 1])
        self.ax.set_title("Graph")
        self.ax.set_xlabel('X Axe')
        self.ax.set_ylabel('Y Axe')

        # margin
        self.animation_canvas.move(10, 15)
        # x = 0, y = 0, radius = 1 color = red, alpha = transparency
        circle1 = plt.Circle((0, 0), 1, color='r', fill=False, alpha=0.7)
        self.ax.add_patch(circle1)
        # to fix equel x and y
        self.ax.set_aspect('equal', 'box')
        # axes
        self.ax.axhline(y=0, color='k')
        self.ax.axvline(x=0, color='k')
        # grid
        self.ax.grid(axis='both', color='k', linestyle='-', linewidth=.3, alpha=0.7)
        ############# axes
        #self.ax.plot([0, 0], [-1, 1], alpha=0.3)
        #self.ax.plot([1, -1], [0, 0], alpha=0.3)

        # The coordinates of quadrant (polygon) -> (square)
        x, y = [-1, -1, 1, 1], [-1, 1, 1, -1]
        # alpha = transparency, c = color
        self.ax.fill(x, y, alpha=0.6, c='gray') 

    def sinus_animation(self):
        self.sinus_graph, = self.ax.plot([], [])
        self.dot, = self.ax.plot([], [], 'o', color='red')
        anim = FuncAnimation(self.fig, self.sinus, frames=len(self.x), interval=50)

    def sinus(self, i):
        self.sinus_graph.set_data(self.x[:i],self.y[:i])
        self.dot.set_data(self.x[i],self.y[i])   


    def anim(self):
        self.anim_canvas = MplCanvas(self, width=5, height=4, dpi=100)



class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(121)   
        self.axes2 = fig.add_subplot(122)
        super(MplCanvas, self).__init__(fig)   
 