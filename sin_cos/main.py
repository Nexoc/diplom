import sin_cos.count as counted
from sin_cos.canvas import Canvas
# import count as counted
# from canvas import Canvas
import sys
import time
from os import path
# If NavigationToolbar will be needed comment out next line and lines 113 and 244
# from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.qt_compat import QtWidgets
from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel, QRadioButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QIntValidator, QFont


class ApplicationWindow(QtWidgets.QMainWindow):
    """
    This "window" is a QWidget.
    It will appear as a free-floating window.
    """
    def __init__(self):
        super().__init__()
        self.animation = True       # animation
        self.pi_accuracy = None     # if accuracy 3 -> pi = 3,141
        self.accuracy = None        # accuracy
        self.window_hist = None     # No external window yet. (Histogram)
        self.quantity = 0           # quantity
        self.count = 0
        self.points_in = 0          # count of all inside points
        self.points_out = 0         # count of all inside points
        self.points_x = []          # all x (for histogram)
        self.points_y = []          # all y (for histogram)

        self.setWindowTitle("Pi counter")
        # main window: size width height and margin top left:
        top, left, width, height = 150, 800, 1200, 800
        self.setGeometry(left, top, width, height)
        self._main = QtWidgets.QWidget()
        self.setCentralWidget(self._main)
        self.layout = QtWidgets.QVBoxLayout(self._main)

        # matplotlib initial
        self.canvas = Canvas()
        self.canvas.graph()

        # qt5 initial
        self.qt5_init()

    def qt5_init(self):
        """
        main window UI
        """
        # Button Start
        button_start = QPushButton('Start count', self)
        button_start.setToolTip('Start')
        button_start.clicked.connect(self.on_click_start)

        # Button shows histogram
        button_show = QPushButton('Show Histogram', self)
        button_show.setToolTip('Show')
        button_show.clicked.connect(self.on_click_show)

        # Button quit
        button_quit = QPushButton('Quit', self)
        button_quit.setToolTip('Quit')
        button_quit.clicked.connect(self.on_click_quit)

        # Button save
        button_save = QPushButton('Save as *png', self)
        button_save.setToolTip('Save')
        button_save.clicked.connect(self.save)

        # Radio button
        self.radiobutton = QRadioButton("animation")
        self.radiobutton.setChecked(True)
        self.radiobutton.country = "with animation"

        # input Quantity
        label1 = QLabel(self)
        label1.setText('<font color=" green", size=6>Quantity</font>')
        label1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.lightGray)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)

        self.input_quantity = QLineEdit(self)
        # font and font size
        self.input_quantity.setFont(QFont("Arial", 20))
        # Integer Validator
        self.input_quantity.setValidator(QIntValidator())
        # max number 999 999 999 999
        self.input_quantity.setMaxLength(12)
        # margin right 0
        self.input_quantity.setAlignment(Qt.AlignRight)

        # Output PI
        self.pi_output = QLabel(self)
        pi = 3.141592653589793
        self.set_pi(pi)

        # accuracy
        label3 = QLabel(self)
        label3.setText(f'<font color="green", size=6>accuracy</font>')
        label3.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.lightGray)
        label3.setPalette(palette)
        label3.setAlignment(Qt.AlignCenter)

        self.input_accuracy = QLineEdit(self)
        self.input_accuracy.setFont(QFont("Arial", 20))
        self.input_accuracy.setValidator(QIntValidator())
        self.input_accuracy.setMaxLength(6)
        self.input_accuracy.setAlignment(Qt.AlignRight)

        # if we need NavigationToolbar uncomment next line and import
        # self.layout.addWidget(NavigationToolbar(self.canvas.dynamic_canvas, self))
        self.layout.addWidget(self.canvas.dynamic_canvas)
        self.layout.addWidget(label1)
        self.layout.addWidget(self.input_quantity)
        self.layout.addWidget(label3)
        self.layout.addWidget(self.input_accuracy)
        self.layout.addWidget(self.pi_output)
        self.layout.addWidget(self.radiobutton)
        self.layout.addWidget(button_start)
        self.layout.addWidget(button_show)
        self.layout.addWidget(button_save)
        self.layout.addWidget(button_quit)

    def on_click_start(self):
        # read quantity line
        quantity = self.input_quantity.text()
        # read accuracy line
        accuracy = self.input_accuracy.text()
        if accuracy:
            self.accuracy = int(accuracy)+2
            # cut pi according accuracy
            self.pi_accuracy = counted.pi_number(self.accuracy)
        if quantity:
            self.quantity = int(quantity)
        # speed 1 = 0,001 sec (it only works without animation), with animation normal speed is about 10 (0,01 sek)
        self._timer = self.canvas.dynamic_canvas.new_timer(1)
        self._timer.add_callback(self._update_canvas)
        self._timer.start()

    def set_pi(self, pi):
        pi = str(pi)
        self.pi_output.setText(f'<font color="green", size=10>π = {pi}</font>')
        self.pi_output.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.lightGray)
        self.pi_output.setPalette(palette)
        self.pi_output.setAlignment(Qt.AlignLeft)

    def on_click_quit(self):
        try:
            # main window close
            self.close()
            # histogram close
            self.window_hist.close()
        except:
            print('done')

    # show the new window
    def on_click_show(self):
        if self.window_hist is None:
            self.window_hist = Histogram(self.points_x, self.points_y)
            self.window_hist.show()
        else:
            # Close window
            self.window_hist.close()
            # Discard reference
            self.window_hist = None

    def _update_canvas(self):
        x, y = counted.x_y_random()
        color = counted.out_in(x, y)
        if color:
            self.points_in += 1
        else:
            self.points_out += 1
        self.points_x.append(x)
        self.points_y.append(y)
        pi = counted.count_pi(self.points_in, self.points_out)
        self.set_pi(pi)

        # check if animation is true
        if self.radiobutton.isChecked():
            # s = size in pixel
            # marker = . see https://matplotlib.org/stable/api/markers_api.html#module-matplotlib.markers
            if color:
                self.canvas.ax.scatter(x=x, y=y, s=4, marker='h', color="yellow")
            else:
                self.canvas.ax.scatter(x=x, y=y, s=4, marker='h', color="green")

            # to draw the point on the canvas
            self.canvas._scatter.figure.canvas.draw()
        self.count += 1

        if self.quantity <= self.count or pi[:self.accuracy] == self.pi_accuracy:
            self.count = 0
            self.quantity = 0
            self._timer.stop()

    def save(self):
        name = time.asctime(time.localtime(time.time())).replace(' ', '_').replace(':', '-')
        self.canvas.dynamic_canvas.figure.savefig(f"graph_{name}.png", dpi=200)
        picture = path.exists(f'graph_{name}.png')
        if picture:
            print(f'graph_{name}.png has been saved successfully')
        else:
            print(f"graph_{name}.png hasn't been saved\nDo you have a problem with saving?")


class Histogram(QtWidgets.QMainWindow):
    """
    This "window" is a QWidget.
    It will appear as a free-floating window.
    """
    def __init__(self, points_x, points_y):
        super().__init__()
        self.label = QLabel("New Window")

        left, top, width, height = 150, 150, 600, 600
        self.setGeometry(top, left, width, height)
        self._main = QtWidgets.QWidget()
        self.setCentralWidget(self._main)
        self.layout = QtWidgets.QVBoxLayout(self._main)
        self.title = "Histogram of my random numbers"
        self.setWindowTitle(self.title)

        self.canvas = Canvas()
        self.canvas.histogram(points_x=points_x, points_y=points_y)
        # place of canvas -> margin left: 25 margin top: 25
        self.canvas.move(25, 25)
        self.window_hist = QtWidgets.QWidget()
        self.layout.addWidget(self.canvas)

        # Button Save
        button_save = QPushButton('Save', self)
        button_save.setToolTip('Save')
        button_save.clicked.connect(self.save)

        # Button quit
        button_quit = QPushButton('Quit', self)
        button_quit.setToolTip('Quit')
        button_quit.clicked.connect(self.on_click_quit)

        self.layout.addWidget(button_save)
        self.layout.addWidget(button_quit)
        # if we need NavigationToolbar uncomment next line and import
        # self.layout.addWidget(NavigationToolbar(self.canvas, self))

    def on_click_quit(self):
        self.close()

    def save(self):
        self.canvas.save(type='historgam')


def main(gui):
    # Check whether there is already a running QApplication
    
    print(gui)
    
    '''    qapp = QtWidgets.QApplication.instance()
    if not qapp:
        qapp = QtWidgets.QApplication(sys.argv)
    app = ApplicationWindow()
    app.show()
    app.activateWindow()
    app.raise_()
    qapp.exec()'''


if __name__ == "__main__":
    main()

