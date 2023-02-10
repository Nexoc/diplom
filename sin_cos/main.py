
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
        self.frame_content = 0 # where we are now
        super().__init__(*args, **kwargs)

        #######################################################################################
         #                              matplotlib initialization                            # 
        #######################################################################################
        self.canvas = Canvas()
        # self.canvas.graph()
        # self.canvas.three()

        #######################################################################################
         #                                 qt5 initialization                                # 
        #######################################################################################
        self.qt5_init()

 
        # buttons in physic project
        self.sinus_button.clicked.connect(self.sinus)
        self.cosinus_button.clicked.connect(self.cosinus)
        self.folmeln_samlung_button.clicked.connect(self.folmeln_samlung)

        # An animated button of the menu
        self.menuButton.clicked.connect(self.menu)
        # The buttons of the projects
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

        "#content_frame{\n"
        "    background-color: rgb(181, 222, 255);\n"
        "}")     
        self.centralwidget.setObjectName("centralwidget")

        #######################################################################################
         #                       Horizontal Layout- QHBoxLayout (the left menu)              # 
        #######################################################################################      
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        # margin window frame
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0) 
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        #######################################################################################
         #                     The frame is inside the central widget                        # 
        #######################################################################################          
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        #######################################################################################
         #                       Horizontal Box 2 QHBoxLayout                                # 
        ####################################################################################### 
        # HorizontalLayout_2 is added into the self.frame
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        # margin
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        #######################################################################################
         #       The initialization of the leftS frame                                       # 
        ####################################################################################### 
        self.leftS = QtWidgets.QFrame(self.frame)
        self.leftS.setMaximumSize(QSize(0, 16777215))
        self.leftS.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.leftS.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftS.setObjectName("leftS")

        #######################################################################################
         #                    The initialization of the horizontal_Layout_3 (QHBoxLayout)    # 
        ####################################################################################### 

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.leftS)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        #######################################################################################
         #                The initialization of the horizontal_Layout_3 (QHBoxLayout)        # 
        ####################################################################################### 
        self.frame_4 = QtWidgets.QFrame(self.leftS)
        self.frame_4.setMinimumSize(QSize(200, 0))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")

        #######################################################################################
         #The initialization of the verticalLayout_3 (QVBoxLayout) for the buttons of the menu # 
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
        # The label is added into the verticalLayout_3
        self.verticalLayout_3.addWidget(self.label_2)


        #######################################################################################
         #              The initialization the left buttons of the menu                      # 
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
         #           The initialization of the rightS frame                                   # 
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
         #                   The initialization of one animated button for the menu          # 
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

        # add the horizontalLayout_4 into frame 8 (menu button)
        self.horizontalLayout_4.addWidget(self.frame_8)

        #  The initialization of then spacer
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

############################################

        self.label_right = QtWidgets.QLabel(self.top_frame)
        font = QFont()
        font.setPointSize(24)
        self.label_right.setFont(font)
        self.label_right.setAlignment(Qt.AlignCenter)
        self.label_right.setObjectName("label")
        # add label to horizontalLayout 4
        self.horizontalLayout_4.addWidget(self.label_right)
########################################################################

        # spacer 2
        spacerItem2 = QtWidgets.QSpacerItem(179, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # add label to horizontalLayout 4
        self.horizontalLayout_4.addItem(spacerItem2)
        # add top_frame to verticalLayout
        self.verticalLayout.addWidget(self.top_frame)


        ##############################################################################################
         # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
          #                                    Content Frame                                       # 
         # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
        ##############################################################################################

        self.frame_main = QtWidgets.QFrame(self.rightS)
        self.frame_main.setMinimumSize(QSize(0, 100))
        self.frame_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main.setObjectName("frame_main")

        #######################################################################################
         #                      Widget for right site (content)                              # 
        ####################################################################################### 

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame_main)
        self.horizontalLayoutWidget.setGeometry(QRect(70, -1, 1071, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        #######################################################################################
         #                       Horizontal Layout for Buttons QHBoxLayout                   # 
        ####################################################################################### 
        self.horizontalLayout_buttons = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_buttons.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_buttons.setObjectName("horizontalLayout_buttons")

        #######################################################################################
         #                       Buttons init and add                                        # 
        ####################################################################################### 
        # sin button 
        self.sinus_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.sinus_button.setObjectName("sinus_button")        
        self.horizontalLayout_buttons.addWidget(self.sinus_button)

        # cos button
        self.cosinus_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.cosinus_button.setObjectName("cosinus_button")
        self.horizontalLayout_buttons.addWidget(self.cosinus_button)

        # folmeln_samlung button
        self.folmeln_samlung_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.folmeln_samlung_button.setObjectName("folmeln_samlung_button")
        self.horizontalLayout_buttons.addWidget(self.folmeln_samlung_button)


        #######################################################################################
         #                                  Widget for Content                              #
        #######################################################################################
        self.horizontalWidget_content = QtWidgets.QWidget(self.frame_main)
        # geometry of main content
        top, left, width, height = 50, 50, 800, 380
        self.horizontalWidget_content.setGeometry(QRect(top, left, width, height))
        self.horizontalWidget_content.setObjectName("horizontalWidget_content")

        #######################################################################################
         #                       Horizontal Box layout for main content                      # 
        ####################################################################################### 
        self.horizontalLayout_main = QtWidgets.QHBoxLayout(self.horizontalWidget_content)
        self.horizontalLayout_main.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_main.setObjectName("horizontalLayout_main")

        #######################################################################################
         #                                  Widget 2 for Content                             #
        #######################################################################################
        self.widget_main = QtWidgets.QWidget(self.horizontalWidget_content)
        self.widget_main.setObjectName("widget_main")

        #######################################################################################
         #                                  Widget 3 for Content                             #
        #######################################################################################
        self.widget_2 = QtWidgets.QWidget(self.widget_main)
        top1, left1, width1, height1 = 10, 100, 300, 300
        self.widget_2.setGeometry(QRect(top1, left1, width1, height1))
        self.widget_2.setObjectName("widget_2")

        # addWidget to HL main content
        self.horizontalLayout_main.addWidget(self.widget_main)



        self.verticalLayout.addWidget(self.frame_main)

        #######################################################################################
         #                                  frame for right site                            #
        #######################################################################################
        self.content_frame = QtWidgets.QFrame(self.rightS)
        self.content_frame.setMinimumSize(QSize(0, 36))
        self.content_frame.setMaximumSize(QSize(16777215, 36))
        self.content_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content_frame.setObjectName("content_frame")

        # add verticalLayout to content_frame 
        self.verticalLayout.addWidget(self.content_frame)
        # add rightS frame to horizontalLayout_2
        self.horizontalLayout_2.addWidget(self.rightS)


        # trying ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
        self.canvas.graph()
        # self.horizontalLayout.addWidget(self.canvas.dynamic_canvas) # left before menu
        # self.horizontalLayout_4.addWidget(self.canvas.dynamic_canvas) # title main
        # self.horizontalLayout_buttons.addWidget(self.canvas.dynamic_canvas) # buttons
        # self.horizontalLayout_2.addWidget(self.canvas.dynamic_canvas) # right
        # self.horizontalLayout_3.addWidget(self.canvas.dynamic_canvas) # menu buttons
        # self.horizontalLayout_main.addWidget(self.canvas.dynamic_canvas) # ?
        # self.verticalLayout.addWidget(self.canvas.dynamic_canvas) # menu button (Button)
        # self.verticalLayout_2.addWidget(self.canvas.dynamic_canvas) # ?
        # self.verticalLayout_3.addWidget(self.canvas.dynamic_canvas) # ?

        # add rightS frame to horizontalLayout_2
        self.horizontalLayout.addWidget(self.frame)

        self.setCentralWidget(self.centralwidget)

        # The function for all labels, strings of text etc
        self.retranslateUi()

        # The initialization of the context menu
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.on_context_menu)

    def on_context_menu(self, pos):
        context = QtWidgets.QMenu(self)

        # The initialization of the sinus button
        sin = QtWidgets.QAction("sinus", self)
        sin.triggered.connect(self.sinus)
        context.addAction(sin)
        # The initialization of the cosinus button
        cos = QtWidgets.QAction("cosinus", self)
        cos.triggered.connect(self.cosinus)
        # maybe for the future
        # cos.triggered.connect(lambda: label.setText("cosinus button triggered"))
        context.addAction(cos)
        # The initialization of the folmeln button
        formeln = QtWidgets.QAction("formeln", self)
        formeln.triggered.connect(self.folmeln_samlung)
        context.addAction(formeln)

        context.exec(self.mapToGlobal(pos))

    def mousePressEvent(self, e):

        if e.button() == Qt.LeftButton:
            # handle the left-button press in here
            self.label_right.setText(" -> mouse Press Event LEFT")
            x_position = e.x()
            y_position = e.y()
            position = e.pos()
            print(f" -> mouse Press Event LEFT and {x_position=}, {y_position=} --- {position=}")


        elif e.button() == Qt.MiddleButton:
            # handle the middle-button press in here.
            self.label_right.setText(" -> mousePressEvent MIDDLE")
            print(" -> mousePressEvent MIDDLE")

        elif e.button() == Qt.RightButton:
            # handle the right-button press in here.
            self.label_right.setText(" -> mousePressEvent RIGHT")
            print(" -> mousePressEvent RIGHT")

    def mouseReleaseEvent(self, e):
        
        if e.button() == Qt.LeftButton:
            self.label_right.setText(" -> mouseReleaseEvent LEFT")

        elif e.button() == Qt.MiddleButton:
            self.label_right.setText(" -> mouseReleaseEvent MIDDLE")

        elif e.button() == Qt.RightButton:
            self.label_right.setText(" -> mouseReleaseEvent RIGHT")

        x_position = e.x()
        y_position = e.y()
        print(f"{x_position=}, {y_position=} ")

    def mouseDoubleClickEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.label_right.setText(" -> mouseDoubleClickEvent LEFT")
            print(" -> mouseDoubleClickEvent LEFT")

        elif e.button() == Qt.MiddleButton:
            self.label_right.setText(" -> mouseDoubleClickEvent MIDDLE")
            print(" -> mouseDoubleClickEvent MIDDLE")

        elif e.button() == Qt.RightButton:
            self.label_right.setText(" -> mouseDoubleClickEvent RIGHT")
            print(" -> mouseDoubleClickEvent RIGHT")

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

    def sinus(self):
        '''
        description
        '''
        print('sinus button') 
        # Set the window title and the main label
        self.setWindowTitle(self._translate("MainWindow", "Sinus"))
        self.label.setText(self._translate("MainWindow", "Sinus"))

        #########################################################################################
         #                                Canvas(matplotlib)                                   #
        #########################################################################################  

        # Check whether there is already a running sinus canvas
        if self.frame_content != 1:
            # init new
            self.canvas.graph()
            # remove old
            self.remove_canvas(1)  
            # add new 
            self.horizontalLayout_main.addWidget(self.canvas.dynamic_canvas)
            # change the frame_content into "1"
            self.frame_content = 1

    def cosinus(self):
        '''
        Set the window title and the main label
        Run Matplotlib Canvas
        '''
        print('cosinus button')
        self.setWindowTitle(self._translate("MainWindow", "Cosinus"))
        self.label.setText(self._translate("MainWindow", "Cosinus"))
        # check if we are one the same Canvas
        if self.frame_content != 2:
            # The initialization of the new canvas
            self.canvas.triangle()
            # delete the old canvas
            self.remove_canvas(2) 
            # add the new canvas
            self.horizontalLayout_main.addWidget(self.canvas.triangle_canvas)
            # The initialization or changing of variable into "2"
            self.frame_content = 2

    def folmeln_samlung(self):
        '''
        description
        '''
        print('folmeln_samlung_button')  
        self.setWindowTitle(self._translate("MainWindow", "Formeln Samlung"))
        self.label.setText(self._translate("MainWindow", "Formeln Samlung"))
        if self.frame_content != 3:
            self.remove_canvas(3)  
            self.frame_content = 3

    def remove_canvas(self, check):
        # 
        if self.frame_content == 2:
            # remove 
            self.horizontalLayout_main.removeWidget(self.canvas.triangle_canvas)
            self.canvas.triangle_canvas.deleteLater()
            self.canvas.triangle_canvas = None
        elif self.frame_content == 1:
            # remove
            self.horizontalLayout_main.removeWidget(self.canvas.dynamic_canvas)
            self.canvas.dynamic_canvas.deleteLater()
            self.canvas.dynamic_canvas = None
        elif self.frame_content == 3:
            pass     

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

