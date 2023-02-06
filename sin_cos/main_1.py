from PyQt5 import uic


def main(main_window):
    '''
    description
    '''
    print('2')
    uic.loadUi("GUI/sin_cos.ui", main_window)
    main_window.setWindowTitle("Sinus Cosinus Tangens")
    main_window.menuButton.clicked.connect(main_window.menu)

    # marat.main(self) # to check if it works
    # sys.exit()