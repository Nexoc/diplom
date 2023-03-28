#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib



class Matplot_Animation():    
    def __init__(self):        
        self.fig = plt.figure()
        self.ax = plt.axes(xlim=(-3.5, 3.5), ylim=(-5, 2))
        self.line, = self.ax.plot([], [], lw=2)


    def set_data(self, data):
        self.data = data

    def ani_init(self):
        self.line.set_data([], [])
        return self.line

    def ani_update(self, i):
        x = self.data[i][0]
        y = self.data[i][1]
        self.line.set_data(x, y)
        return self.line

    def animate(self):
        self.anim = animation.FuncAnimation(self.fig, self.ani_update, init_func=self.ani_init, frames=4, interval=250, blit=False)
        plt.show()

# ------------------------------ #

'''data = [
[[0, 0, 1, 0], [0, -1, -2, -3]],
[[0, 0, 0, 0.1], [0, -1, -3, -4]],
[[0, 0, 0.5, 0], [0, -1, -2.5,- 3.5]],
[[0, 0, 1,2], [0, -1, -2, -2.5]]
        ]
myani = Matplot_Animation()
myani.set_data(data)
myani.animate()'''



class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Set Matplotlib Chart Value with QLineEdit Widget')
        self.window_width, self.window_height = 1200, 800
        self.setMinimumSize(self.window_width, self.window_height)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.input = QLineEdit()

        
        self.input.textChanged.connect(self.update_chart)
        layout.addWidget(self.input)

        self.canvas = FigureCanvas(plt.Figure(figsize=(15, 6)))
        layout.addWidget(self.canvas)

        self.insert_ax()

    def insert_ax(self):
        font = {
            'weight': 'normal',
            'size': 16
        }
        matplotlib.rc('font', **font)

        self.ax = self.canvas.figure.subplots()
        self.ax.set_ylim([0, 100])
        self.ax.set_xlim([0, 1])
        self.bar = None

    def update_chart(self):
        value = self.input.text()
        try:
            value = float(value)
        except ValueError:
            value = 0

        x_position = [0.5]

        if self.bar:
            self.bar.remove()
        self.bar = self.ax.bar(x_position, value, width=0.2, color='g')
        self.canvas.draw()

"""if __name__ == '__main__':
    # don't auto scale when drag app to a different monitor.
    # QApplication.setAttribute(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    
    app = QApplication(sys.argv)
    app.setStyleSheet('''
        QWidget {
            font-size: 30px;
        }
    ''')
    
    myApp = MyApp()
    myApp.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')"""



import sys
import random
import matplotlib
matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.setCentralWidget(self.canvas)

        n_data = 50
        self.xdata = list(range(n_data))
        self.ydata = [random.randint(0, 10) for i in range(n_data)]
        self.update_plot()

        self.show()

        # Setup a timer to trigger the redraw by calling update_plot.
        self.timer = QtCore.QTimer()
        self.timer.setInterval(300)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

    def update_plot(self):
        # Drop off the first y element, append a new one.
        self.ydata = self.ydata[1:] + [random.randint(0, 10)]
        self.canvas.axes.cla()  # Clear the canvas.
        self.canvas.axes.plot(self.xdata, self.ydata, 'r')
        # Trigger the canvas to update and redraw.
        self.canvas.draw()

"""
app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()

"""