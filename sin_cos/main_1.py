# from GUI.sin_cos.sin_cos import Ui_Mainwindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPropertyAnimation


class Physic():

    def __init__(self, main_window):

        self.setupUi(main_window)
        # self.retranslateUi()
        # sin_cos = Ui_mainwindow()
        # sin_cos.setupUi(main_window)

        # uic.loadUi("GUI/sin_cos/sin_cos.ui", main_window)
        # TODO
        # menu buttons

              
        self.menuButton.clicked.connect(self.menu)
        self.pushButton.clicked.connect(main_window.project_1)
        self.pushButton_2.clicked.connect(main_window.project_2)
        self.pushButton_3.clicked.connect(main_window.project_3)
        self.pushButton_4.clicked.connect(main_window.project_4)
        self.btn_back.clicked.connect(main_window.back_button)


        # buttons in sinus project
        # self.setWindowTitle("Sinus Cosinus Tangens")
        self.sinus_button.clicked.connect(self.sinus)
        self.cosinus_button.clicked.connect(self.cosinus)
        self.folmeln_samlung_button.clicked.connect(self.folmeln_samlung)
        

    def sinus(self):
        '''
        description
        '''
        print('sinus button') 
        # self.sin_cos.label.setText(_translate("mainwindow", "Sinus"))


    def cosinus(self):
        '''
        description
        '''
        print('cosinus button')

    def folmeln_samlung(self):
        '''
        description
        '''
        print('folmeln_samlung_button')  



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



    
    def setupUi(self, mainwindow):
        '''
        description
        '''

        mainwindow.setObjectName("mainwindow")
        mainwindow.resize(1194, 503)
        self.centralwidget = QtWidgets.QWidget(mainwindow)
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

        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)

        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.leftS = QtWidgets.QFrame(self.frame)
        self.leftS.setMaximumSize(QtCore.QSize(0, 16777215))
        self.leftS.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.leftS.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftS.setObjectName("leftS")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.leftS)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_4 = QtWidgets.QFrame(self.leftS)
        self.frame_4.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 36))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)



        # menu buttons
        self.pushButton = QtWidgets.QPushButton(self.frame_4)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)

        self.pushButton_2 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_3 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_4 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_3.addWidget(self.pushButton_4)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.btn_back = QtWidgets.QPushButton(self.frame_4)
        self.btn_back.setObjectName("btn_back")
        self.verticalLayout_3.addWidget(self.btn_back)




        self.horizontalLayout_3.addWidget(self.frame_4)
        self.horizontalLayout_2.addWidget(self.leftS)
        self.rightS = QtWidgets.QFrame(self.frame)
        self.rightS.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rightS.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rightS.setObjectName("rightS")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.rightS)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_frame = QtWidgets.QFrame(self.rightS)
        self.top_frame.setMaximumSize(QtCore.QSize(16777215, 36))
        self.top_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_frame.setObjectName("top_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.top_frame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_8 = QtWidgets.QFrame(self.top_frame)
        self.frame_8.setMinimumSize(QtCore.QSize(36, 36))
        self.frame_8.setMaximumSize(QtCore.QSize(36, 36))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # menu button
        self.menuButton = QtWidgets.QPushButton(self.frame_8)
        self.menuButton.setMinimumSize(QtCore.QSize(36, 36))
        self.menuButton.setMaximumSize(QtCore.QSize(36, 36))
        self.menuButton.setText("")

        # icon for menu button
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("GUI/sin_cos/menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuButton.setIcon(icon)
        self.menuButton.setObjectName("menuButton")


        self.verticalLayout_2.addWidget(self.menuButton)
        self.horizontalLayout_4.addWidget(self.frame_8)
        spacerItem1 = QtWidgets.QSpacerItem(178, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.top_frame)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(179, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.top_frame)
        self.frame_3 = QtWidgets.QFrame(self.rightS)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 100))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")


        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame_3)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(70, -1, 1071, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_buttons = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_buttons.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_buttons.setObjectName("horizontalLayout_buttons")


        # Buttons:
            # Sinus
        self.sinus_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.sinus_button.setObjectName("sinus_button")
        self.horizontalLayout_buttons.addWidget(self.sinus_button)
 
            # Cosinus
        self.cosinus_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.cosinus_button.setObjectName("cosinus_button")
        self.horizontalLayout_buttons.addWidget(self.cosinus_button)

            # Formel samlung
        self.folmeln_samlung_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.folmeln_samlung_button.setObjectName("folmeln_samlung_button")
        self.horizontalLayout_buttons.addWidget(self.folmeln_samlung_button)


        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.frame_3)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(70, 50, 1071, 371))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_main = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_main.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_main.setObjectName("horizontalLayout_main")
        self.widget_main = QtWidgets.QWidget(self.horizontalLayoutWidget_2)
        self.widget_main.setObjectName("widget_main")
        self.widget_2 = QtWidgets.QWidget(self.widget_main)
        self.widget_2.setGeometry(QtCore.QRect(540, 50, 491, 311))
        self.widget_2.setObjectName("widget_2")


        # Tabs
        self.tabWidget = QtWidgets.QTabWidget(self.widget_main)
        self.tabWidget.setGeometry(QtCore.QRect(26, 10, 1011, 31))
        self.tabWidget.setObjectName("tabWidget")

        # tab1
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.tabWidget.addTab(self.tab_1, "")

        # tab2
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout_main.addWidget(self.widget_main)
        self.verticalLayout.addWidget(self.frame_3)
        self.bot_frame = QtWidgets.QFrame(self.rightS)
        self.bot_frame.setMinimumSize(QtCore.QSize(0, 36))
        self.bot_frame.setMaximumSize(QtCore.QSize(16777215, 36))
        self.bot_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bot_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bot_frame.setObjectName("bot_frame")
        self.verticalLayout.addWidget(self.bot_frame)
        self.horizontalLayout_2.addWidget(self.rightS)
        self.horizontalLayout.addWidget(self.frame)
        mainwindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainwindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainwindow)

    def retranslateUi(self, mainwindow):
        _translate = QtCore.QCoreApplication.translate
        mainwindow.setWindowTitle(_translate("mainwindow", "Sinus"))
        self.label_2.setText(_translate("mainwindow", "Menu"))
        
        self.pushButton.setText(_translate("mainwindow", "projekt1"))
        self.pushButton_2.setText(_translate("mainwindow", "projekt2"))
        self.pushButton_3.setText(_translate("mainwindow", "projekt3"))
        self.pushButton_4.setText(_translate("mainwindow", "projekt4"))
        self.btn_back.setText(_translate("mainwindow", "back"))

        self.label.setText(_translate("mainwindow", "Sinus Cosinus Tangens title"))

        self.sinus_button.setText(_translate("mainwindow", "Sinus"))
        self.cosinus_button.setText(_translate("mainwindow", "Cosinus"))
        self.folmeln_samlung_button.setText(_translate("mainwindow", "Formeln Samlung"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("mainwindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("mainwindow", "Tab 2"))
    









"""

def main(main_window):
    '''
    description
    '''
    sin_cos = Ui_mainwindow()
    sin_cos.setupUi(main_window)


    # uic.loadUi("GUI/sin_cos/sin_cos.ui", main_window)
    # TODO
    # menu buttons
    sin_cos.menuButton.clicked.connect(main_window.menu)
    sin_cos.pushButton.clicked.connect(main_window.project_1)
    sin_cos.pushButton_2.clicked.connect(main_window.project_2)
    sin_cos.pushButton_3.clicked.connect(main_window.project_3)
    sin_cos.pushButton_4.clicked.connect(main_window.project_4)
    sin_cos.btn_back.clicked.connect(main_window.back_button)



    # buttons in sinus project
    # sin_cos.setWindowTitle("Sinus Cosinus Tangens")
    sin_cos.sinus_button.clicked.connect(sinus)
    sin_cos.cosinus_button.clicked.connect(cosinus)
    sin_cos.folmeln_samlung_button.clicked.connect(folmeln_samlung_button)


def sinus():
    '''
    description
    '''
    print('sinus button') 
    sin_cos.label.setText(_translate("mainwindow", "Sinus"))


def cosinus():
    '''
    description
    '''
    print('cosinus button')

def folmeln_samlung_button():
    '''
    description
    '''
    print('folmeln_samlung_button')  """



