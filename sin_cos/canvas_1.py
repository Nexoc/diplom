from matplotlib.backends.qt_compat import QtWidgets
from PyQt5.QtCore import Qt, QSize, QRect, QCoreApplication, QCoreApplication, QMetaObject, QPropertyAnimation
from PyQt5.QtGui import QFont, QIcon, QPixmap


class GroupBox(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(QRect(20, 20, 900, 700))
        self.setWindowTitle("InvoiceMee - Split Documents")
        ####################################################################################################
        layout = QtWidgets.QGridLayout(self)
        groupbox = QtWidgets.QGroupBox("Files to Convert", checkable=False)
        layout.addWidget(groupbox)

        # the "main" layout, used to ensure that the actual layout containing
        # all widgets stays in the center
        ####################################################################################################
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