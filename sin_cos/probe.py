
import sys
import time
from os import path
from matplotlib.backends.qt_compat import QtWidgets
from PyQt5.QtCore import Qt, QSize, QRect, QCoreApplication, QCoreApplication, QMetaObject, QPropertyAnimation
from PyQt5.QtGui import QFont, QIcon, QPixmap

from canvas import Canvas
# from canvas_1 import MplCanvas


class ApplicationWindow(QtWidgets.QMainWindow):
    """
    This "window" is a QWidget.
    It will appear as a free-floating window.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("Physic - Sinus and Cosinus")
        # main window: size width height and margin top left:
        top, left, width, height = 150, 100, 1194, 503
        self.setGeometry(left, top, width, height)
        self._main = QtWidgets.QWidget()
        self.setCentralWidget(self._main)
        # Horizontal Box - QHBoxLayout
        self.layout = QtWidgets.QVBoxLayout(self._main)
        self.layout.addStretch()

        #######################################################################################
         #                              matplotlib initial                                   # 
        #######################################################################################
        self.canvas = Canvas()
        self.canvas.graph()

        # qt5 initial
        self.qt5_init()

 
        # buttons in sinus project
        #self.sinus_button.clicked.connect(self.sinus)
        #self.cosinus_button.clicked.connect(self.cosinus)
        #self.folmeln_samlung_button.clicked.connect(self.folmeln_samlung)

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


        ##############################################################################################
         #                        frame for buttons Sin Cos (main frame)                            # 
        ##############################################################################################

        self.frame_main = QtWidgets.QFrame(self.rightS)
        self.frame_main.setMinimumSize(QSize(0, 100))
        self.frame_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main.setObjectName("frame_main")

        ##############################################################################################




        ############################################################################################### PROBE
        # the "main" layout, used to ensure that the actual layout containing
        # all widgets stays in the center
        ####################################################################################################

        layout = QtWidgets.QGridLayout(self)
        groupbox = QtWidgets.QGroupBox("Files to Convert", checkable=False)
        layout.addWidget(groupbox)

        groupLayout = QtWidgets.QGridLayout()
        groupbox.setLayout(groupLayout)
        groupLayout.setColumnStretch(0, 1)
        groupLayout.setColumnStretch(2, 1)
        groupLayout.setRowStretch(0, 1)
        groupLayout.setRowStretch(2, 1)





        # this is the actual layout used to add widgets
        centerLayout = QtWidgets.QVBoxLayout()
        groupLayout.addLayout(centerLayout, 1, 1)

        label = QtWidgets.QLabel()
        pixmap = QPixmap('pictures/del.png')
        label.setPixmap(pixmap)
        # this won't work
        # label.resize(pixmap.width(), pixmap.height())
        pathBox = QtWidgets.QLineEdit(self)
        pathBox.setPlaceholderText("Enter the Path Here")
        # this won't work either, the layout will try to move and resize it anyway
        # pathBox.setGeometry(QRect(160, 150, 201, 20))
        # use minimum width instead
        pathBox.setMinimumWidth(200)
        selectFileBtn = QtWidgets.QPushButton("Select")
        convertButton = QtWidgets.QPushButton("Convert")
        good_radiobutton = QtWidgets.QRadioButton("Invoices")
        naive_radiobutton = QtWidgets.QRadioButton("Credit Notes")

        centerLayout.addWidget(label, alignment=Qt.AlignCenter)

        # the second row has more than one widget, use a nested horizontal layout
        inputLayout = QtWidgets.QHBoxLayout()
        centerLayout.addLayout(inputLayout)
        inputLayout.addWidget(pathBox)
        inputLayout.addWidget(selectFileBtn)

        # the same for the radio buttons
        radioLayout = QtWidgets.QHBoxLayout()
        centerLayout.addLayout(radioLayout)
        # use horizontal alignment to keep buttons closer, otherwise the layout
        # will try to expand them as much as possible (depending on the other
        # widgets in the centerLayout)
        radioLayout.addWidget(good_radiobutton, alignment=Qt.AlignRight)
        radioLayout.addWidget(naive_radiobutton, alignment=Qt.AlignLeft)

        
        ######################################################################################################## END probe


        # function for all textes
        self.retranslateUi()

        # self.tabWidget.setCurrentIndex(0)
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
        #self.sinus_button.setText(self._translate("MainWindow", "Sinus"))
        #self.cosinus_button.setText(self._translate("MainWindow", "Cosinus"))
        #self.folmeln_samlung_button.setText(self._translate("MainWindow", "Formeln Samlung"))
        #self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), self._translate("MainWindow", "Tab 1"))
        #self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), self._translate("MainWindow", "Tab 2"))

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

