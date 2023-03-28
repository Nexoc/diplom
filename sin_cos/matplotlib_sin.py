import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class SinusAnimation:

    def __init__(self):
        #self.animation_canvas = FigureCanvas(Figure(figsize=(3, 15), dpi=100))
        #self.ax = self.animation_canvas.figure.subplots()
        
        self.x = np.linspace(0, 30, 100)
        self.y = np.sin(self.x)

        self.fig, self.ax = plt.subplots(1,1)
        self.ax.set_xlim([0, 30])
        self.ax.set_ylim([-1.1, 1.1])
        self.ax.set_title("Graph")
        self.ax.set_xlabel('X Axe')
        self.ax.set_ylabel('Y Axe')
        print(self.x)

    def sinus_animation(self):
        self.sinus_graph, = self.ax.plot([], [])
        self.dot, = self.ax.plot([], [], 'o', color='red')
        anim = FuncAnimation(self.fig, self.sine, frames=len(self.x), interval=50)
        plt.show()

    def sine(self, i):
        self.sinus_graph.set_data(self.x[:i],self.y[:i])
        self.dot.set_data(self.x[i],self.y[i])
"""

if __name__ == "__main__":
    a = SinusAnimation()
    a.sinus_animation()

"""
class CircleAnimation:

    def __init__(self):
        self.x = np.linspace(0, 30, 100)
        self.y = np.sin(self.x)

        self.fig, self.ax = plt.subplots(1,1)
        
        self.ax.set_ylim([-1, 1])
        self.ax.set_xlim([-1, 1])
        self.ax.set_title("Graph")
        self.ax.set_xlabel('X Axe')
        self.ax.set_ylabel('Y Axe')
        # plt.grid(color='r', linestyle='dotted', linewidth=1)

        # x = 0, y = 0, radius = 1 color = red, alpha = transparency
        circle = plt.Circle((0, 0), 1, color='r', fill=False, alpha=0.7)
        self.ax.add_patch(circle)

    def sinus_animation(self):
        self.sinus_graph, = self.ax.plot([], [])
        self.dot, = self.ax.plot([], [], 'o', color='red')
        anim = FuncAnimation(self.fig, self.sinus, frames=len(self.x), interval=50)
        plt.show()

    def sinus(self, i):
        self.sinus_graph.set_data(self.x[:i],self.y[:i])
        self.dot.set_data(self.x[i],self.y[i])


if __name__ == "__main__":
    a = SinusAnimation()
    a.sinus_animation()
    
