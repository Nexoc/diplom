import time
from os import path
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.artist import Artist  
import matplotlib.animation as animation 

from numpy import sin, cos, pi, linspace


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

        # The coordinates of quadrant (polygon) -> (square)
        x, y = [-1, -1, 1, 1], [-1, 1, 1, -1]
        # alpha = transparency, c = color
        self.ax.fill(x, y, alpha=0.6, c='gray')
        # s=size, marker=point style, color=color, alpha=transparency
        self._scatter = self.ax.scatter(x=0, y=0, s=5, marker='.', color='black', alpha=0.1)

                # The initialization of triangle points
        x_hypotenuse, y_hypotenuse = [0, .7], [0, .7]
        x_gegenkathete, y_gegenkathete = [.7, .7], [.7, 0]
        x_ankathete, y_ankathete = [0, .7], [0, 0]

        # triaangle plot
        self.ax.plot(x_hypotenuse, y_hypotenuse, 'o-r', alpha=0.7, label = 'Hypotenuse', lw=5, mec='b', mew=2, ms=10)
        self.ax.plot(x_gegenkathete, y_gegenkathete, 'o-g', alpha=0.7, label = 'Gegenkathete', lw=5, mec='b', mew=2, ms=10)
        self.ax.plot(x_ankathete, y_ankathete, 'o-b', alpha=0.7, label = 'Ankathete', lw=5, mec='b', mew=2, ms=10)

        # Winkel Arc
        arc_angles = linspace(0 * pi, pi/4, 20)
        arc_xs = 0.3 * cos(arc_angles)
        arc_ys = 0.3 * sin(arc_angles)
        self.ax.plot(arc_xs, arc_ys, color = 'yellow', lw = 3)


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
        arc_angles = linspace(0 * pi, pi/4, 20)
        arc_xs = 0.3 * cos(arc_angles)
        arc_ys = 0.3 * sin(arc_angles)
        self.ax.plot(arc_xs, arc_ys, color = 'yellow', lw = 3)


        self.ax.annotate('Hypotenuse', xy=(1, 1), xytext=(0.7, 1.3), arrowprops={'facecolor': 'red', 'shrink': 0.01})
        self.ax.annotate('Gegenkathete', xy=(1.5, 1), xytext=(1.7, 1), arrowprops={'facecolor': 'green', 'shrink': 0.01}, rotation = 270)
        self.ax.annotate('Ankathete', xy=(1, 0), xytext=(1, 0.3), arrowprops={'facecolor': 'blue', 'shrink': 0.01})
        self.ax.annotate('α', xy=(0.29, 0.1), xytext=(0.5, 0.3), arrowprops={'facecolor': 'yellow', 'shrink': 0.01})

        #self.ax.plot(x, f1, ':b')    # пунктирная синяя линия
        #self.ax.plot(x, f2, '--r')   # штрихованная красная линия
        #self.ax.plot(x, f1+f2, 'k')  # черная непрерывная линия

        # coordinates of quadrant (polygon)
        x, y = [0, 0, 2, 2], [0, 2, 2, 0]
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



    ###########################################################
    # Animation

    def init_animation(self):
        self.fig, self.ax = plt.subplots() 
    
        self.ax.set_xlim([-1, 1]) 
        self.ax.set_ylim([-1, 1]) 
            
        self.L = 50
        theta = np.linspace(0, 2 * np.pi, self.L) 
        r = np.ones_like(theta) 
            
        self.x = r * np.cos(theta) 
        self.y = r * np.sin(theta) 
            
        self.line, = self.ax.plot(1, 0, 'ro') 
            
        annotation = self.ax.annotate( 
            'annotation', xy =(1, 0), xytext =(-1, 0), 
            arrowprops = {'arrowstyle': "->"}
            ) 
        Artist.set_animated(annotation, False) 
    

    def update(self, i): 
        
        new_x = self.x[i % self.L] 
        new_y = self.y[i % self.L] 
        self.line.set_data(new_x, new_y) 
        
        self.annotation.set_position((-new_x, -new_y)) 
        self.annotation.xy = (new_x, new_y) 

    def run_animation(self):
        # interval 500
        ani = animation.FuncAnimation( 
        self.fig, self.update, interval = 500, blit = False 
        )        
        self.fig.suptitle('matplotlib.artist.Artist.set_animated()\
        function Example', fontweight ="bold")         
        plt.show()

    #############################################################

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


class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)   