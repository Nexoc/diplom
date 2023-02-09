
import sys
import time
from os import path
from matplotlib.backends.qt_compat import QtWidgets
from PyQt5.QtCore import Qt, QSize, QRect, QCoreApplication, QCoreApplication, QMetaObject, QPropertyAnimation
from PyQt5.QtGui import QFont, QIcon, QPixmap, QPalette, QColor
from canvas import Canvas


from canvas import Canvas
# from canvas_1 import MplCanvas


class ApplicationWindow(QtWidgets.QMainWindow):
    """
    This "window" is a QWidget.
    It will appear as a free-floating window.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #######################################################################################
         #                              matplotlib initial                                   # 
        #######################################################################################
        self.canvas = Canvas()
        self.canvas.graph()

        #######################################################################################
         #                                 qt5 initial                                       # 
        #######################################################################################
        self.qt5_init()

 
        # buttons in physic project
        #self.sinus_button.clicked.connect(self.sinus)
        #self.cosinus_button.clicked.connect(self.cosinus)
        #self.folmeln_samlung_button.clicked.connect(self.folmeln_samlung)

        # menu button animated
        self.menuButton.clicked.connect(self.menu)
        # project buttons
        self.pushButton.clicked.connect(self.project_1)
        self.pushButton_2.clicked.connect(self.project_2)
        self.pushButton_3.clicked.connect(self.project_3)
        self.pushButton_4.clicked.connect(self.project_4)
        self.btn_back.clicked.connect(self.back_button)

    def qt5_init(self):

        """
        main window UI
        """

        self.setWindowTitle("Physic - Sinus and Cosinus")
        # main window: size width height and margin top left:
        top, left, width, height = 150, 100, 1194, 503
        self.setGeometry(left, top, width, height)        
        self.setObjectName("MainWindow")

        #######################################################################################
         #                         Main Widget (all objects are inside it)                   # 
        ####################################################################################### 
        self.centralwidget = QtWidgets.QWidget(self)
        # StyleSheet
        self.centralwidget.setStyleSheet(
        ".QWidget{\n"
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

        #######################################################################################
         #                       Horizontal Box - QHBoxLayout (menu left)                    # 
        #######################################################################################      
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        # margin window frame
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0) 
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        #######################################################################################
         #                      frame insite central widget                                  # 
        #######################################################################################          
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        #######################################################################################
         #                       Horizontal Box 2 QHBoxLayout                                # 
        ####################################################################################### 
        # layout of main frame 
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        # margin other frame
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        #######################################################################################
         #                      frame leftS  (menu for animation func)                       # 
        ####################################################################################### 
        self.leftS = QtWidgets.QFrame(self.frame)
        self.leftS.setMaximumSize(QSize(0, 16777215))
        self.leftS.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.leftS.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftS.setObjectName("leftS")

        #######################################################################################
         #                       Horizontal Box 3 QHBoxLayout                                # 
        ####################################################################################### 

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.leftS)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        #######################################################################################
         #                      frame                                                        # 
        ####################################################################################### 
        self.frame_4 = QtWidgets.QFrame(self.leftS)
        self.frame_4.setMinimumSize(QSize(200, 0))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")

        #######################################################################################
         #                       vertical Box 2 QVBoxLayout (menu buttons)                   # 
        ####################################################################################### 
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        # label
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setMaximumSize(QSize(16777215, 36))
        font = QFont()
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        # add label to VL3
        self.verticalLayout_3.addWidget(self.label_2)


        #######################################################################################
         #                        Buttons for left menu                                      # 
        ####################################################################################### 

        self.pushButton = QtWidgets.QPushButton(self.frame_4)
        self.pushButton.setObjectName("pushButton")
        # add button to VL3
        self.verticalLayout_3.addWidget(self.pushButton)

        self.pushButton_2 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_2.setObjectName("pushButton_2")
        # add button to VL3
        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_3 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_3.setObjectName("pushButton_3")
        # add button to VL3
        self.verticalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_4 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_4.setObjectName("pushButton_4")
        # add button to VL3
        self.verticalLayout_3.addWidget(self.pushButton_4)

        # Spacer between buttons and button back
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        # add spacer to VL3
        self.verticalLayout_3.addItem(spacerItem)

        self.btn_back = QtWidgets.QPushButton(self.frame_4)
        self.btn_back.setObjectName("btn_back")
        # add button to VL3
        self.verticalLayout_3.addWidget(self.btn_back)
        self.horizontalLayout_3.addWidget(self.frame_4)
        self.horizontalLayout_2.addWidget(self.leftS)


        #######################################################################################
         #                              Frame right                                         # 
        ####################################################################################### 

        self.rightS = QtWidgets.QFrame(self.frame)
        self.rightS.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rightS.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rightS.setObjectName("rightS")

        #######################################################################################
         #                       Vertical Box QVBoxLayout                                    # 
        ####################################################################################### 
        self.verticalLayout = QtWidgets.QVBoxLayout(self.rightS)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_frame = QtWidgets.QFrame(self.rightS)
        self.top_frame.setMaximumSize(QSize(16777215, 36))
        self.top_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_frame.setObjectName("top_frame")

        #######################################################################################
         #                       Horizontal Box 4 QHBoxLayout                                # 
        ####################################################################################### 
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.top_frame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        #######################################################################################
         #                       Frame 8                                                     # 
        ####################################################################################### 
        self.frame_8 = QtWidgets.QFrame(self.top_frame)
        self.frame_8.setMinimumSize(QSize(36, 36))
        self.frame_8.setMaximumSize(QSize(36, 36))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")

        #######################################################################################
         #                      Vertical Box 2 QVBoxLayout                                   # 
        ####################################################################################### 
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")


        #######################################################################################
         #                      MENU button - animated(+png)                                 # 
        ####################################################################################### 
        self.menuButton = QtWidgets.QPushButton(self.frame_8)
        self.menuButton.setMinimumSize(QSize(36, 36))
        self.menuButton.setMaximumSize(QSize(36, 36))
        self.menuButton.setText("")

        # init and add icon
        icon = QIcon()
        icon.addPixmap(QPixmap("pictures/menu.png"), QIcon.Normal, QIcon.Off)
        self.menuButton.setIcon(icon)
        self.menuButton.setObjectName("menuButton")
        # add menu button to VL2
        self.verticalLayout_2.addWidget(self.menuButton)

        # add to Widget frame 8 (menu button)
        self.horizontalLayout_4.addWidget(self.frame_8)

        # spacer
        spacerItem1 = QtWidgets.QSpacerItem(178, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # add spaser item 1 to horizontalLayout 4
        self.horizontalLayout_4.addItem(spacerItem1)

        # label
        self.label = QtWidgets.QLabel(self.top_frame)
        font = QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setObjectName("label")
        # add label to horizontalLayout 4
        self.horizontalLayout_4.addWidget(self.label)

        # spacer 2
        spacerItem2 = QtWidgets.QSpacerItem(179, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # add label 2 to horizontalLayout 4
        self.horizontalLayout_4.addItem(spacerItem2)
        # add top_frame to verticalLayout
        self.verticalLayout.addWidget(self.top_frame)


        ##############################################################################################
         # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
          #                                    Content Frame                                       # 
         # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
        ##############################################################################################

        layout = QtWidgets.QGridLayout()
        layout.setContentsMargins(80, 80, 30, 30)

        layout.addWidget(Color('red'), 0, 0)
        layout.addWidget(Color('green'), 1, 0)
        layout.addWidget(Color('blue'), 1, 1)
        layout.addWidget(Color('purple'), 2, 1)

        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)



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


class Color(QtWidgets.QWidget):

    def __init__(self, color):
        super(Color, self).__init__()

        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

        if color == "green":
            self.canvas = Canvas()
            self.canvas.graph()

            self.horizontalWidget_content = QtWidgets.QWidget(self)
            # geometry
            top, left, width, height = 100, 50, 380, 380
            self.horizontalWidget_content.setGeometry(QRect(top, left, width, height))
            self.horizontalWidget_content.setObjectName("horizontalWidget_content")

            #######################################################################################
            #                       Horizontal Box layout for main content                      # 
            ####################################################################################### 
            self.horizontalLayout_main = QtWidgets.QHBoxLayout(self.horizontalWidget_content)
            self.horizontalLayout_main.setContentsMargins(0, 0, 0, 0)
            self.horizontalLayout_main.setObjectName("horizontalLayout_main")

            #########################################################################################
            #                                Canvas(matplotlib)                                   #
            #########################################################################################        
            self.horizontalLayout_main.addWidget(self.canvas.dynamic_canvas)
            # just for greed layout
            # addWidget(label,0,0,1,0,QtCore.Qt.AlignCenter) AlignRight Qt.AlignLeft
                

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

