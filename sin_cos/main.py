
import sys
import time
import random
from os import path
import math 

import numpy as np

from matplotlib.backends.qt_compat import QtWidgets
import matplotlib.pyplot as plt
from matplotlib_sin import CircleAnimation, SinusAnimation
import matplotlib.ticker as ticker

from PyQt5.QtCore import Qt, QSize, QRect, QCoreApplication, QCoreApplication, QMetaObject, QPropertyAnimation, QTimer
from PyQt5.QtGui import QFont, QIcon, QPixmap, QIntValidator
from PyQt5.QtWidgets import QTextBrowser, QLineEdit, QLabel

import sin_matplotlib as main_animation
from canvas import Canvas, MplCanvas


# http://schulphysikwiki.de/index.php/Animation:_Sinus_und_Cosinus_im_Einheitskreis


class ApplicationWindow(QtWidgets.QMainWindow):
    """
    This "window" is a QWidget.
    It will appear as a free-floating window.
    """
    def __init__(self, *args, **kwargs):
        self.frame_content = 0 # where we are now
        super().__init__(*args, **kwargs)
        self.text_content = '<div>sin(a) = Gegenkathete durch Hypotenuse<div/><div>cos(a) = Ankathete durch Hypotenuse<div/>'
        self.ankathete = None
        self.gegenkathete = None
        self.degrie = None

        #######################################################################################
         #                              matplotlib initialization                            # 
        #######################################################################################
        self.canvas = Canvas()

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
        top, left, width, height = 50, 50, 1100, 380
        self.horizontalWidget_content.setGeometry(QRect(top, left, width, height))
        self.horizontalWidget_content.setObjectName("horizontalWidget_content")

        #######################################################################################
         #                       Horizontal Box layout for main content                      # 
        ####################################################################################### 
        # QGridLayout QHBoxLayout
        # // addWidget(*Widget, row, column, rowspan, colspan)
        # // 0th row
        # gridLayout->addWidget(b1,0,0,1,1);
        self.horizontalLayout_main = QtWidgets.QGridLayout(self.horizontalWidget_content)
        self.horizontalLayout_main.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_main.setObjectName("horizontalLayout_main")

        #######################################################################################
         #                                  Widget main for Content                          #
        #######################################################################################
        self.widget_main = QtWidgets.QWidget(self.horizontalWidget_content)
        self.widget_main.setObjectName("widget_main")

        #######################################################################################
         #                                  Widget 2 for Content                             #
        #######################################################################################
        self.widget_2 = QtWidgets.QWidget(self.widget_main)
        top1, left1, width1, height1 = 10, 100, 300, 300
        self.widget_2.setGeometry(QRect(top1, left1, width1, height1))
        self.widget_2.setObjectName("widget_2")

        # addWidget to main content
        self.horizontalLayout_main.addWidget(self.widget_main, 0, 0, 1, 1)

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

        ##########################################################################
        # text_content
        self.text = QTextBrowser()
        self.text.setAcceptRichText(True)
        self.text.setOpenExternalLinks(True)
        # addWidget(*Widget, row, column, rowspan, colspan)
        self.horizontalLayout_main.addWidget(self.text, 0, 0, 4, 2)
        self.text_content = """ 
            <div>
                <b style='color:blue'>Sinus</b> und <b style='color:blue'>Cosinus</b> sind zwei mathematische Funktionen, 
                die häufig in der Trigonometrie verwendet werden, einem Zweig der Mathematik, 
                der sich mit den Beziehungen zwischen den Seiten und Winkeln von Dreiecken befasst.
                <br><br>
                Die Sinusfunktion (sin) bezieht sich auf das Verhältnis 
                der Länge der Seite gegenüber einem Winkel in einem rechtwinkligen Dreieck zur Länge der Hypotenuse (der längsten Seite) des Dreiecks. 
                <br>
                Mit anderen Worten, <b style='color:blue'>sin(α) = Gegenkathete(gegenüberliegende Seite) / Hypotenuse.</b>
                <br><br>
                Die Kosinusfunktion (cos) bezieht sich auf das Verhältnis 
                der Länge der anliegenden Seite (der Seite, die an den Winkel angrenzt) zur Hypotenuse des Dreiecks. 
                <br>Mit anderen Worten, <b style='color:blue'>cos(α) = Ankathete(anliegende Seite) / Hypotenuse.</b>
                <br><br>
                Diese Funktionen sind in einer Vielzahl von Bereichen 
                wie Ingenieurwissenschaften, Physik und Navigation nützlich. 
                <br>
                Sie können verwendet werden, um die Länge einer Seite oder das Maß eines Winkels in einem Dreieck zu bestimmen, 
                sowie um periodische Phänomene wie Wellen und Vibrationen zu modellieren.
            </div>
            """
        self.text.setFixedWidth(600)       
        self.text.append(self.text_content)


        self.canvas.graph()

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
        self.text.setFixedWidth(500)  


        #########################################################################################
         #                                Canvas(matplotlib)                                   #
        #########################################################################################  

        # remove old
        self.remove_canvas()  
        
        # init new
        if self.ankathete == None:
            self.text_content = """
                    Der Sinus ist eine trigonometrische Funktion, die sich auf das Verhältnis der Länge der Seite gegenüber einem Winkel in einem rechtwinkligen Dreieck zur Länge der Hypotenuse (der längsten Seite) des Dreiecks bezieht. Mit anderen Worten, der Sinus eines Winkels theta ist das Verhältnis der Länge der gegenüberliegenden Seite zu der Länge der Hypotenuse.

                    Die Sinusfunktion wird oft als sin abgekürzt und ist eine periodische Funktion mit einer Periode von 2π (radian). Das bedeutet, dass der Sinus einer bestimmten Winkelgröße in einem rechtwinkligen Dreieck gleich ist wie der Sinus des gleichen Winkels, der um 360 Grad (oder 2π) erhöht oder verringert ist.

                    Der Sinus ist in vielen Bereichen der Mathematik und Wissenschaften nützlich. Zum Beispiel kann er verwendet werden, um die Höhe eines Objekts zu berechnen, wenn die Entfernung und der Winkel zur Spitze des Objekts bekannt sind. Er kann auch verwendet werden, um die Auslenkung eines schwingenden Objekts zu modellieren, wie zum Beispiel bei einem Pendel.

                    Es gibt auch eine Reihe von Identitäten und Formeln, die den Sinus betreffen. Eine bekannte Identität ist die Sinus-Addition-Formel, die das Verhältnis von Sinus und Cosinus für die Summe oder Differenz von zwei Winkeln beschreibt. Eine andere wichtige Formel ist die Sinus-Regel, die das Verhältnis von Seiten und Winkeln in einem allgemeinen Dreieck beschreibt.

                    Insgesamt ist der Sinus eine wichtige Funktion in der Mathematik und den Wissenschaften, die in vielen Anwendungen verwendet wird.
                    """
            self.text.append(self.text_content)
            self.canvas.graph(x_hypotenuse=[0, .7], y_hypotenuse=[0, .7], x_gegenkathete=[.7, .7], y_gegenkathete=[.7, 0], x_ankathete=[0, .7], y_ankathete=[0, 0])
        else:
            self.canvas.graph(x_hypotenuse=[0, self.gegenkathete], y_hypotenuse=[0, self.ankathete], 
                              x_gegenkathete=[self.gegenkathete, self.gegenkathete], y_gegenkathete=[self.ankathete, 0], 
                              x_ankathete=[0, self.gegenkathete], y_ankathete=[0, 0], arc=self.degrie)     
        
        # addWidget(*Widget, row, column, rowspan, colspan)
        self.horizontalLayout_main.addWidget(self.canvas.dynamic_canvas, 0, 2, 4, 2)

        self.text.clear()
        self.text.append(self.text_content)

        # init input
        self.grad = QLineEdit()
        self.grad.setFixedWidth(90)
        self.grad.setAlignment(Qt.AlignRight)
        self.grad.setValidator(QIntValidator())
        self.grad.setFont(QFont("Arial",20))
        # addWidget(*Widget, row, column, rowspan, colspan)
        self.horizontalLayout_main.addWidget(self.grad, 0, 4, 1, 1)

        self.label_grad = QLabel(self)
        self.label_grad.setText("<b>° Grad</b>")
        self.label_grad.setFont(QFont("Arial",20))
        self.label_grad.setAlignment(Qt.AlignRight)
        self.label_grad.setBuddy(self.grad)
        # addWidget(*Widget, row, column, rowspan, colspan)
        self.horizontalLayout_main.addWidget(self.label_grad, 1, 4, 1, 1)

        self.grad.returnPressed.connect(self.update_text)  
        # self.grad.textChanged.connect(self.update_text)    

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
        self.text.setFixedWidth(550)  
        # check if we are one the same Canvas
        if self.frame_content != 2:
            # The initialization of the new canvas
            self.canvas.triangle()
            # delete the old canvas
            self.remove_canvas() 
            # add the new canvas
            # addWidget(*Widget, row, column, rowspan, colspan)
            self.horizontalLayout_main.addWidget(self.canvas.triangle_canvas, 0, 1, 1, 1)
            
            cos_text = """
            In einem rechtwinkligen Dreieck gibt es drei Seiten: die Hypotenuse, die Ankathete und die Gegenkathete.

            Die Hypotenuse ist die längste Seite des Dreiecks und liegt gegenüber vom rechten Winkel. Sie wird oft mit dem Buchstaben c bezeichnet.

            Die Ankathete ist die Seite, die den Winkel enthält, auf den sich die Frage bezieht. Sie wird oft mit dem Buchstaben a bezeichnet.

            Die Gegenkathete ist die Seite, die dem Winkel gegenüberliegt. Sie wird oft mit dem Buchstaben b bezeichnet.

            Die Beziehungen zwischen diesen Seiten und Winkeln können mit den trigonometrischen Funktionen Sinus, Cosinus und Tangens beschrieben werden. Der Sinus eines Winkels ist das Verhältnis der Länge der Gegenkathete zur Länge der Hypotenuse, der Cosinus eines Winkels ist das Verhältnis der Länge der Ankathete zur Länge der Hypotenuse und der Tangens eines Winkels ist das Verhältnis der Länge der Gegenkathete zur Länge der Ankathete.

            Zusammen bilden die Hypotenuse, die Ankathete und die Gegenkathete ein wichtiges Konzept in der Trigonometrie und sind in vielen Anwendungen nützlich, wie zum Beispiel in der Geometrie, der Physik und der Navigation.
            """
            self.text.clear()
            self.text.append(cos_text)

        # The initialization or changing of variable into "2"
        self.frame_content = 2

    def folmeln_samlung(self):
        '''
        description
        '''
        print('sinus button') 
        # Set the window title and the main label
        self.setWindowTitle(self._translate("MainWindow", "animation"))
        self.label.setText(self._translate("MainWindow", "SAnimation"))
        # text Feld width 200
        self.text.setFixedWidth(200)   
        #########################################################################################
         #                                Canvas(matplotlib)                                   #
        ######################################################################################### 
        # remove old
        self.remove_canvas()          
      
        self.text_content = """
                Der Sinus ist eine trigonometrische Funktion, 
                die sich auf das Verhältnis der Länge der Seite gegenüber 
                einem Winkel in einem rechtwinkligen Dreieck zur Länge 
                der Hypotenuse (der längsten Seite) des Dreiecks bezieht. 
                Mit anderen Worten, der Sinus eines Winkels theta ist 
                das Verhältnis der Länge der gegenüberliegenden Seite zu der Länge der Hypotenuse.
                """
        self.text.append(self.text_content)

        # canvas
        self.animation_m = MplCanvas(self, width=5, height=5, dpi=80)   
        self.horizontalLayout_main.addWidget(self.animation_m, 0, 1, 4, 2)

        self.xdata = np.arange(0, 36, 0.1)
        self.ydata = np.arange(start=0, stop=3, step=0.02777777779)
        self.update_canvas()
        self.show()
        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_canvas)
        self.timer.start()

        self.frame_content = 3


    def update_canvas(self):
        # Drop off the first y element, append a new one.
        if len(self.xdata) == 1:
            self.xdata = np.arange(0, 36, 0.1)
        if len(self.ydata) == 1:
            self.ydata = np.arange(start=0, stop=3, step=0.02777777779)
        self.xdata = self.xdata[1:] 
        self.ydata = self.ydata[1:] 

        if self.animation_m != None:
            # first plot
            self.animation_m.axes.cla()  # Clear the canvas.
            self.animation_m.axes.plot([0, np.cos(self.xdata[0])], [0, np.sin(self.xdata[0])], 'o-r', alpha=0.7, lw=5, mec='b', mew=2, ms=10)
            self.animation_m.axes.plot([1, np.cos(self.xdata[0])], [np.sin(self.xdata[0]), np.sin(self.xdata[0])], 'o-g', alpha=0.7, lw=2, mew=1, ms=5)
            self.animation_m.axes.set_ylim([-1, 1])
            self.animation_m.axes.set_xlim([-1, 1])
            self.animation_m.axes.set_title("Graph")
            self.animation_m.axes.set_xlabel('X Axe')
            self.animation_m.axes.set_ylabel('Y Axe')
            circle1 = plt.Circle((0, 0), 1, color='r', fill=False, alpha=0.7)
            self.animation_m.axes.add_patch(circle1)
            #self.animation_m.axes.set_aspect('equal', 'box') 
            self.animation_m.axes.axhline(y=0, color='k')
            self.animation_m.axes.axvline(x=0, color='k')
            self.animation_m.axes.grid(axis='both', color='k', linestyle='-', linewidth=.3, alpha=0.7)

            # second plot
            self.animation_m.axes2.cla() 
            self.animation_m.axes2.plot([0, self.ydata[0]], [np.sin(self.xdata[0]), np.sin(self.xdata[0])], 'o-g', alpha=0.7, lw=2, mew=1, ms=5)
            self.animation_m.axes2.set_ylim([-1, 1])
            self.animation_m.axes2.set_xlim([0, 3])
            self.animation_m.axes2.set_title("Sinus")
            #self.animation_m.axes2.set_aspect('equal', 'box') 
            self.animation_m.axes2.axhline(y=0, color='k')
            self.animation_m.axes2.axvline(x=0, color='k')
            self.animation_m.axes2.grid(axis='both', color='k', linestyle='-', linewidth=.3, alpha=0.7)
            self.animation_m.axes2.get_yaxis().set_visible(False)

            ##########################################

            
            #  Устанавливаем интервал основных и
            #  вспомогательных делений:
            self.animation_m.axes2.xaxis.set_major_locator(ticker.MultipleLocator(2))
            self.animation_m.axes2.xaxis.set_minor_locator(ticker.MultipleLocator(1))
            self.animation_m.axes2.yaxis.set_major_locator(ticker.MultipleLocator(50))
            self.animation_m.axes2.yaxis.set_minor_locator(ticker.MultipleLocator(10))


            #  Настраиваем вид основных тиков:
            self.animation_m.axes2.tick_params(axis = 'both',    #  Применяем параметры к обеим осям
                        which = 'major',    #  Применяем параметры к основным делениям
                        direction = 'inout',    #  Рисуем деления внутри и снаружи графика
                        length = 20,    #  Длинна делений
                        width = 4,     #  Ширина делений
                        color = 'm',    #  Цвет делений
                        pad = 10,    #  Расстояние между черточкой и ее подписью
                        labelsize = 15,    #  Размер подписи
                        labelcolor = 'r',    #  Цвет подписи
                        bottom = True,    #  Рисуем метки снизу
                        top = True,    #   сверху
                        left = True,    #  слева
                        right = True,    #  и справа
                        labelbottom = True,    #  Рисуем подписи снизу
                        labeltop = True,    #  сверху
                        labelleft = True,    #  слева
                        labelright = True,    #  и справа
                        labelrotation = 45)    #  Поворот подписей


            #  Настраиваем вид вспомогательных тиков:
            self.animation_m.axes2.tick_params(axis = 'both',    #  Применяем параметры к обеим осям
                        which = 'minor',    #  Применяем параметры к вспомогательным делениям
                        direction = 'out',    #  Рисуем деления внутри и снаружи графика
                        length = 10,    #  Длинна делений
                        width = 2,     #  Ширина делений
                        color = 'm',    #  Цвет делений
                        pad = 10,    #  Расстояние между черточкой и ее подписью
                        labelsize = 15,    #  Размер подписи
                        labelcolor = 'r',    #  Цвет подписи
                        bottom = True,    #  Рисуем метки снизу
                        top = True,    #   сверху
                        left = True,    #  слева
                        right = True)    #  и справа
                        
            #  Добавляем линии основной сетки:
            self.animation_m.axes2.grid(which='major',
                    color = 'm')

            #  Включаем видимость вспомогательных делений:
            self.animation_m.axes2.minorticks_on()

            #  Теперь можем отдельно задавать внешний вид
            #  вспомогательной сетки:
            self.animation_m.axes2.grid(which='minor',
                    color = 'm',
                    linestyle = ':')


            ##########################################




            # Trigger the canvas to update and redraw.
            self.animation_m.draw()


    def update_text(self):
        self.text_content = self.grad.text()
        self.text.clear()

        #print(type(text)) # str
        if self.text_content == '':
            self.degrie = 0
        else:
            self.degrie = int(self.text_content) # with validator is always int max from 0 to 999
        self.counting()
        self.text_content = f"<div style='text-align: right;'>Sie haben {self.text_content}° gegeben.</div>\
                         <div style='text-align: right;'>Sinus von {self.degrie}° ist {round(self.ankathete, 2)}</div>\
                         <div style='text-align: right;'>Cosinus von {self.degrie}° ist {round(self.gegenkathete, 2)}</div>\
                         <div style='text-align: right; color:red'>Hypotenuse ist Radiud = 1 </div>\
                        <div style='text-align: right; color:blue'>Ankathete = sin({self.degrie}) * radius</div>\
                         <div style='text-align: right; color:green'>Gegenkathete = cos({self.degrie}) * radius</div>\
                         <div style='text-align: right;'>Ankathete ist {round(self.ankathete, 2)}</div>\
                         <div style='text-align: right;'>Gegenkathete ist {round(self.gegenkathete, 2)}</div>\
                            "
        self.text.append(self.text_content)
        if self.frame_content == 1:
            self.sinus()

    def counting(self, r=1):
        self.ankathete = math.sin(math.radians(self.degrie))
        self.gegenkathete = math.cos(math.radians(self.degrie))
         
    def remove_canvas(self):
        # remove dynamic_canvas and input field
        if self.frame_content == 1:
            self.horizontalLayout_main.removeWidget(self.canvas.dynamic_canvas)
            self.canvas.dynamic_canvas.deleteLater()
            self.canvas.dynamic_canvas = None

            self.horizontalLayout_main.removeWidget(self.grad)
            self.grad.deleteLater()
            self.grad = None

            self.horizontalLayout_main.removeWidget(self.label_grad)
            self.label_grad.deleteLater()
            self.label_grad = None

        # remove triangle_canvas
        elif self.frame_content == 2:            
            self.horizontalLayout_main.removeWidget(self.canvas.triangle_canvas)
            self.canvas.triangle_canvas.deleteLater()
            self.canvas.triangle_canvas = None

            # remove animation_m
        elif self.frame_content == 3:
            self.horizontalLayout_main.removeWidget(self.animation_m)
            self.animation_m.deleteLater()
            self.animation_m = None 

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
        #uic.loadUi("GUI/base.ui", self) 
        #self.menuButton.clicked.connect(self.menu)


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

