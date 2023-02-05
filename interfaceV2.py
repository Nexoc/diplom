import PyQt5.QtWidgets as pq5
from PyQt5 import uic, QtGui
from PyQt5.QtCore import QPropertyAnimation


class MyGUI(pq5.QMainWindow):

    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("GUI/base.ui", self)

        self.menuButton.clicked.connect(self.menu)
        self.pushButton.clicked.connect(self.project_1)
        self.pushButton_2.clicked.connect(self.project_2)
        self.pushButton_3.clicked.connect(self.project_3)
        self.pushButton_4.clicked.connect(self.project_4)

    def menu(self):
        width = self.leftS.width()
        if width == 0:
            newWidth = 200
            self.menuButton.setIcon(QtGui.QIcon(u"pictures/del.png"))
        else:
            newWidth = 0
            self.menuButton.setIcon(QtGui.QIcon(u"pictures/menu.png"))

        self.animation = QPropertyAnimation(self.leftS, b"maximumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.start()

    def project_1(self):
        print('project 1')


    def project_2(self):
        print('project 2')

    def project_3(self):
        print('project 3')

    def project_4(self):
        print('project 4')


def main():
    app = pq5.QApplication([])
    window = MyGUI()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
