from PyQt5 import uic
from PyQt5.QtWidgets import *


def main(main_window):
    '''
    description
    '''
    print('2')

    uic.loadUi("GUI/sin_cos/sin_cos.ui", main_window)

    # menu buttons
    main_window.setWindowTitle("Sinus Cosinus Tangens")
    main_window.menuButton.clicked.connect(main_window.menu)
    main_window.pushButton.clicked.connect(main_window.project_1)
    main_window.pushButton_2.clicked.connect(main_window.project_2)
    main_window.pushButton_3.clicked.connect(main_window.project_3)
    main_window.pushButton_4.clicked.connect(main_window.project_4)
    main_window.btn_back.clicked.connect(main_window.back_button)


    # buttons in sinus project
    main_window.sinus_button.clicked.connect(sinus_button)
    main_window.cosinus_button.clicked.connect(cosinus_button)
    main_window.folmeln_samlung_button.clicked.connect(formeln_button)

    # tabs



def sinus_button():
    '''
    description
    '''
    print('sinus button') 


def cosinus_button():
    '''
    description
    '''
    print('cosinus button') 


def formeln_button():
    '''
    description
    '''
    print('formeln button') 

