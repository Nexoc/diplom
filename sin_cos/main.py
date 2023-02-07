
import sys
import time
from os import path
from matplotlib.backends.qt_compat import QtWidgets
from PyQt5.QtCore import Qt, QSize, QRect, QCoreApplication, QCoreApplication, QMetaObject, QPropertyAnimation
from PyQt5.QtGui import QFont, QIcon, QPixmap


class ApplicationWindow(QtWidgets.QMainWindow):
    """
    This "window" is a QWidget.
    It will appear as a free-floating window.
    """
    def __init__(self):
        super().__init__()


        self.setWindowTitle("Physic - Sinus and Cosinus")
        # main window: size width height and margin top left:
        top, left, width, height = 150, 100, 1194, 503
        self.setGeometry(left, top, width, height)
        self._main = QtWidgets.QWidget()
        self.setCentralWidget(self._main)
        self.layout = QtWidgets.QVBoxLayout(self._main)

        # matplotlib initial
        # self.canvas = Canvas()
        # self.canvas.graph()

        # qt5 initial
        self.qt5_init()

        # buttons in sinus project
        self.sinus_button.clicked.connect(self.sinus)
        self.cosinus_button.clicked.connect(self.cosinus)
        self.folmeln_samlung_button.clicked.connect(self.folmeln_samlung)

        # menu left
        self.menuButton.clicked.connect(self.menu)
        # projectes
        self.pushButton.clicked.connect(self.project_1)
        self.pushButton_2.clicked.connect(self.project_2)
        self.pushButton_3.clicked.connect(self.project_3)
        self.pushButton_4.clicked.connect(self.project_4)
        self.btn_back.clicked.connect(self.back_button)

    def qt5_init(self):
        """
        main window UI
        """
        self.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget(self)

        self.centralwidget.setStyleSheet(".QWidget{\n"
        "    border: none;\n"
        "}\n"
        ".QFrame{\n"
        "    border: none;\n"
        "}\n"
        "#top_frame{\n"
        "    background-color: rgb(181, 222, 255);\n"
        "}\n"
        "#bot_frame{\n"
        "    background-color: rgb(181, 222, 255);\n"
        "}")

        # ?
        self.centralwidget.setObjectName("centralwidget")


        # layout of left menu 
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        # margin window frame
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0) 
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        # ?
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        # layout of main frame 
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        # margin other frame
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        ################################################################
        # Frame  left site 
        self.leftS = QtWidgets.QFrame(self.frame)
        self.leftS.setMaximumSize(QSize(0, 16777215))
        self.leftS.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.leftS.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftS.setObjectName("leftS")
        # layout 3
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.leftS)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_4 = QtWidgets.QFrame(self.leftS)
        self.frame_4.setMinimumSize(QSize(200, 0))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setMaximumSize(QSize(16777215, 36))

        font = QFont()
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        # addWidget
        self.verticalLayout_3.addWidget(self.label_2)


        #####################################################
        # Buttons in left menu
        self.pushButton = QtWidgets.QPushButton(self.frame_4)
        self.pushButton.setObjectName("pushButton")
        # addWidget
        self.verticalLayout_3.addWidget(self.pushButton)

        self.pushButton_2 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_2.setObjectName("pushButton_2")
        # addWidget
        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_3 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_3.setObjectName("pushButton_3")
        # addWidget
        self.verticalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_4 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_4.setObjectName("pushButton_4")
        # addWidget
        self.verticalLayout_3.addWidget(self.pushButton_4)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.btn_back = QtWidgets.QPushButton(self.frame_4)
        self.btn_back.setObjectName("btn_back")
        # addWidget
        self.verticalLayout_3.addWidget(self.btn_back)
        self.horizontalLayout_3.addWidget(self.frame_4)
        self.horizontalLayout_2.addWidget(self.leftS)


        # ?
        self.rightS = QtWidgets.QFrame(self.frame)
        self.rightS.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rightS.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rightS.setObjectName("rightS")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.rightS)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_frame = QtWidgets.QFrame(self.rightS)
        self.top_frame.setMaximumSize(QSize(16777215, 36))
        self.top_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_frame.setObjectName("top_frame")

        ################################################################
        # layout 4 (menu button)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.top_frame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_8 = QtWidgets.QFrame(self.top_frame)
        self.frame_8.setMinimumSize(QSize(36, 36))
        self.frame_8.setMaximumSize(QSize(36, 36))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")

        # vertical layout
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")


        ###############'''''''''''''''''''''''''''''''''''''''''''''''''''''
        # MENU button
        self.menuButton = QtWidgets.QPushButton(self.frame_8)
        self.menuButton.setMinimumSize(QSize(36, 36))
        self.menuButton.setMaximumSize(QSize(36, 36))
        self.menuButton.setText("")
        # icon
        icon = QIcon()
        icon.addPixmap(QPixmap("pictures/menu.png"), QIcon.Normal, QIcon.Off)
        self.menuButton.setIcon(icon)
        self.menuButton.setObjectName("menuButton")
        # addWidget
        self.verticalLayout_2.addWidget(self.menuButton)

        # add to Widget frame 8 (menu button)
        self.horizontalLayout_4.addWidget(self.frame_8)
        spacerItem1 = QtWidgets.QSpacerItem(178, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.top_frame)
        font = QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setObjectName("label")
        # addWidget
        self.horizontalLayout_4.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(179, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        # addWidget
        self.verticalLayout.addWidget(self.top_frame)


        ###### ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
        ###################################################################

        # frame for buttons Sin Cos (main frame)
        self.frame_main = QtWidgets.QFrame(self.rightS)
        self.frame_main.setMinimumSize(QSize(0, 100))
        self.frame_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main.setObjectName("frame_main")

        # layout for buttons Sin Cos
        # add to main frame
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame_main)
        self.horizontalLayoutWidget.setGeometry(QRect(70, -1, 1071, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_buttons = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_buttons.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_buttons.setObjectName("horizontalLayout_buttons")

        #####''''''''''''''''
        # buttons
        # sin
        self.sinus_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.sinus_button.setObjectName("sinus_button")        
        self.horizontalLayout_buttons.addWidget(self.sinus_button)

        # cos
        self.cosinus_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.cosinus_button.setObjectName("cosinus_button")
        self.horizontalLayout_buttons.addWidget(self.cosinus_button)

        # folmeln_samlung_button
        self.folmeln_samlung_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.folmeln_samlung_button.setObjectName("folmeln_samlung_button")
        self.horizontalLayout_buttons.addWidget(self.folmeln_samlung_button)


        ###############################################
        # Tabs layout
        # add to main frame
        self.horizontalLayoutWidget_tabs = QtWidgets.QWidget(self.frame_main)
        self.horizontalLayoutWidget_tabs.setGeometry(QRect(70, 50, 1071, 371))
        self.horizontalLayoutWidget_tabs.setObjectName("horizontalLayoutWidget_tabs")

        # add to tabs layout
        self.horizontalLayout_main = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_tabs)
        self.horizontalLayout_main.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_main.setObjectName("horizontalLayout_main")

        # add to tabs layout
        self.widget_main = QtWidgets.QWidget(self.horizontalLayoutWidget_tabs)
        self.widget_main.setObjectName("widget_main")
        # add to widget_main
        self.widget_2 = QtWidgets.QWidget(self.widget_main)
        self.widget_2.setGeometry(QRect(540, 50, 491, 311))
        self.widget_2.setObjectName("widget_2")

        # Tabs
        # add to widget_main
        self.tabWidget = QtWidgets.QTabWidget(self.widget_main)
        self.tabWidget.setGeometry(QRect(26, 10, 1011, 31))
        self.tabWidget.setObjectName("tabWidget")

        # tab1
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        # add tab_1 to tabWidget
        self.tabWidget.addTab(self.tab_1, "")

        # tab2
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        # add tab_2 to tabWidget
        self.tabWidget.addTab(self.tab_2, "")

        # addWidget
        self.horizontalLayout_main.addWidget(self.widget_main)
        self.verticalLayout.addWidget(self.frame_main)

        self.bot_frame = QtWidgets.QFrame(self.rightS)
        self.bot_frame.setMinimumSize(QSize(0, 36))
        self.bot_frame.setMaximumSize(QSize(16777215, 36))
        self.bot_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bot_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bot_frame.setObjectName("bot_frame")

        # addWidget
        self.verticalLayout.addWidget(self.bot_frame)
        self.horizontalLayout_2.addWidget(self.rightS)
        self.horizontalLayout.addWidget(self.frame)

        self.setCentralWidget(self.centralwidget)

        # function for all textes
        self.retranslateUi()

        self.tabWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        """
        Naming 
        """
        self._translate = QCoreApplication.translate
        # Window Name
        self.setWindowTitle(self._translate("MainWindow", "Sinus"))

        self.label_2.setText(self._translate("MainWindow", "Menu"))        
        self.pushButton.setText(self._translate("MainWindow", "projekt1"))
        self.pushButton_2.setText(self._translate("MainWindow", "projekt2"))
        self.pushButton_3.setText(self._translate("MainWindow", "projekt3"))
        self.pushButton_4.setText(self._translate("MainWindow", "projekt4"))
        self.btn_back.setText(self._translate("MainWindow", "back"))
        self.label.setText(self._translate("MainWindow", "Sinus Cosinus Tangens title"))
        self.sinus_button.setText(self._translate("MainWindow", "Sinus"))
        self.cosinus_button.setText(self._translate("MainWindow", "Cosinus"))
        self.folmeln_samlung_button.setText(self._translate("MainWindow", "Formeln Samlung"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), self._translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), self._translate("MainWindow", "Tab 2"))


    def sinus(self):
        '''
        description
        '''
        print('sinus button') 
                # Window Name
        self.setWindowTitle(self._translate("MainWindow", "Sinus"))
        self.label.setText(self._translate("MainWindow", "Sinus"))



    def cosinus(self):
        '''
        description
        '''
        print('cosinus button')
        self.setWindowTitle(self._translate("MainWindow", "Cosinus"))
        self.label.setText(self._translate("MainWindow", "Cosinus"))

    def folmeln_samlung(self):
        '''
        description
        '''
        print('folmeln_samlung_button')  
        self.setWindowTitle(self._translate("MainWindow", "Formeln Samlung"))
        self.label.setText(self._translate("MainWindow", "Formeln Samlung"))


    def menu(self):
        '''
        description
        '''
        width = self.leftS.width()
        if width == 0:
            newWidth = 200
            self.menuButton.setIcon(QIcon(u"pictures/del.png"))
        else:
            newWidth = 0
            self.menuButton.setIcon(QIcon(u"pictures/menu.png"))

        self.animation = QPropertyAnimation(self.leftS, b"maximumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.start()


    def project_1(self):
        '''
        description
        '''
        print('project 1')



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
        uic.loadUi("GUI/base.ui", self) 
        self.menuButton.clicked.connect(self.menu)


def main():
    # Check whether there is already a running QApplication   
    qapp = QtWidgets.QApplication.instance()
    if not qapp:
        qapp = QtWidgets.QApplication(sys.argv)
    app = ApplicationWindow()
    app.show()
    app.activateWindow()
    app.raise_()
    qapp.exec()


if __name__ == "__main__":
    main()

