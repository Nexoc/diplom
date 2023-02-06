import PyQt5.QtWidgets as pq5
from PyQt5 import uic, QtGui
from PyQt5.QtCore import QPropertyAnimation
import sin_cos.main_1 as marat



class MyGUI(pq5.QMainWindow):

    def __init__(self):
        '''
        description
        '''
        super(MyGUI, self).__init__()
        uic.loadUi("GUI/base.ui", self)   
        # menu left
        self.menuButton.clicked.connect(self.menu)
        # projectes
        self.pushButton.clicked.connect(self.project_1)
        self.pushButton_2.clicked.connect(self.project_2)
        self.pushButton_3.clicked.connect(self.project_3)
        self.pushButton_4.clicked.connect(self.project_4)
        self.btn_back.clicked.connect(self.back_button)
    def menu(self):
        '''
        description
        '''
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
        '''
        description
        '''

        print('1')
        marat.main(self) # to check if it works
        # sys.exit()

  

    def project_2(self):
        '''
        description
        '''
        print('project 2')

    def project_3(self):
        '''
        description
        '''
        print('project 3')

    def project_4(self):
        '''
        description
        '''
        print('project 4')

    def back_button(self):
        '''
        description
        '''
        print('back_ button')
        self.setWindowTitle("???????????????????????????")
        self.menuButton.clicked.connect(self.menu)


def main():
    app = pq5.QApplication([])
    window = MyGUI()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
