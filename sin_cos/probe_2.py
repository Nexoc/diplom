
import sys
import time
from os import path
from matplotlib.backends.qt_compat import QtWidgets
from PyQt5.QtCore import Qt, QSize, QRect, QCoreApplication, QCoreApplication, QMetaObject, QPropertyAnimation
from PyQt5.QtGui import QFont, QIcon, QPixmap, QPalette, QColor
from canvas import Canvas


from canvas import Canvas
# from canvas_1 import MplCanvas



"""
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

        # remove old
        self.remove_canvas()  
        
        # init new
        if self.ankathete == None:
            self.text_content = '''
                    Der Sinus ist eine trigonometrische Funktion, die sich auf das Verhältnis der Länge der Seite gegenüber einem Winkel in einem rechtwinkligen Dreieck zur Länge der Hypotenuse (der längsten Seite) des Dreiecks bezieht. Mit anderen Worten, der Sinus eines Winkels theta ist das Verhältnis der Länge der gegenüberliegenden Seite zu der Länge der Hypotenuse.

                    Die Sinusfunktion wird oft als sin abgekürzt und ist eine periodische Funktion mit einer Periode von 2π (radian). Das bedeutet, dass der Sinus einer bestimmten Winkelgröße in einem rechtwinkligen Dreieck gleich ist wie der Sinus des gleichen Winkels, der um 360 Grad (oder 2π) erhöht oder verringert ist.

                    Der Sinus ist in vielen Bereichen der Mathematik und Wissenschaften nützlich. Zum Beispiel kann er verwendet werden, um die Höhe eines Objekts zu berechnen, wenn die Entfernung und der Winkel zur Spitze des Objekts bekannt sind. Er kann auch verwendet werden, um die Auslenkung eines schwingenden Objekts zu modellieren, wie zum Beispiel bei einem Pendel.

                    Es gibt auch eine Reihe von Identitäten und Formeln, die den Sinus betreffen. Eine bekannte Identität ist die Sinus-Addition-Formel, die das Verhältnis von Sinus und Cosinus für die Summe oder Differenz von zwei Winkeln beschreibt. Eine andere wichtige Formel ist die Sinus-Regel, die das Verhältnis von Seiten und Winkeln in einem allgemeinen Dreieck beschreibt.

                    Insgesamt ist der Sinus eine wichtige Funktion in der Mathematik und den Wissenschaften, die in vielen Anwendungen verwendet wird.
                    '''
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
        
        # self._timer = self.canvas.dynamic_canvas.new_timer(1)
        # self._timer.add_callback(self._update_canvas)
        # self._timer.start()

        # change the frame_content into "1"
        self.frame_content = 1




    def folmeln_samlung(self):
        '''
        description
        '''
        print('folmeln_samlung_button')  
        self.setWindowTitle(self._translate("MainWindow", "Formeln Samlung"))
        self.label.setText(self._translate("MainWindow", "Formeln Samlung"))
  
        if self.frame_content != 3:
            self.remove_canvas()  
            self.frame_content = 3

            samlung_text = '''
            Zusammen bilden die Hypotenuse, die Ankathete und die Gegenkathete 
            ein wichtiges Konzept in der Trigonometrie und sind in vielen Anwendungen nützlich, 
            wie zum Beispiel in der Geometrie, der Physik und der Navigation.
            '''
            self.text.clear()
            self.text.append(samlung_text)

            # The initialization of the new canvas  
            self.animation_m = MplCanvas(self, width=5, height=4, dpi=100)   
            # addWidget(*Widget, row, column, rowspan, colspan)
            self.horizontalLayout_main.addWidget(self.animation_m, )

            # self.xdata = list(range(100))
            self.xdata = np.arange(0, 30, 0.1)

            self.update_canvas()
            self.show()
            self.timer = QTimer()
            self.timer.setInterval(1000)
            self.timer.timeout.connect(self.update_canvas)
            self.timer.start()


"""




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

################################################

        self.frame_main = QtWidgets.QFrame(self.rightS)
        self.frame_main.setMinimumSize(QSize(0, 100))
        self.frame_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main.setObjectName("frame_main")


        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame_main)
        self.horizontalLayoutWidget.setGeometry(QRect(70, -1, 1071, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")


        ##############################################################################################
         # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
          #                                    Content Frame                                       # 
         # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
        ##############################################################################################

        self.pagelayout = QtWidgets.QVBoxLayout()

        # geometry
        top, left, width, height = 100, 50, 380, 380
        self.pagelayout.setGeometry(QRect(top, left, width, height))


        button_layout = QtWidgets.QHBoxLayout()
        self.stacklayout = QtWidgets.QStackedLayout()

        self.pagelayout.addLayout(button_layout)
        self.pagelayout.addLayout(self.stacklayout)

        btn = QtWidgets.QPushButton("red")
        btn.pressed.connect(self.activate_tab_1)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(Color("red"))

        btn = QtWidgets.QPushButton("green")
        btn.pressed.connect(self.activate_tab_2)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(Color("green"))

        btn = QtWidgets.QPushButton("yellow")
        btn.pressed.connect(self.activate_tab_3)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(Color("yellow"))

        widget = QtWidgets.QWidget()
        widget.setLayout(self.pagelayout)
        self.setCentralWidget(widget)

    def activate_tab_1(self):
        self.stacklayout.setCurrentIndex(0)

    def activate_tab_2(self):
        self.stacklayout.setCurrentIndex(1)

    def activate_tab_3(self):
        self.stacklayout.setCurrentIndex(2)


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

