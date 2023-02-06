from PyQt5 import uic


def main(main_window):
    '''
    description
    '''
    print('2')

    uic.loadUi("GUI/sin_cos.ui", main_window)

    # menu buttons
    main_window.setWindowTitle("Sinus Cosinus Tangens")
    main_window.menuButton.clicked.connect(main_window.menu)
    main_window.pushButton.clicked.connect(main_window.project_1)
    main_window.pushButton_2.clicked.connect(main_window.project_2)
    main_window.pushButton_3.clicked.connect(main_window.project_3)
    main_window.pushButton_4.clicked.connect(main_window.project_4)
    main_window.btn_back.clicked.connect(main_window.back_button)



    # marat.main(self) # to check if it works
    # sys.exit()