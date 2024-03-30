from PyQt5.QtWidgets import QApplication, QMainWindow

from ui.all_froms import Ui_MainForm as login_form

import sys

login=""
password=""
name=""

def main(app,window,new_win):
    focus_form=login_form()
    focus_form.setupUi(window)
    focus_form.set_new_window(new_win,app)
    window.show()
    sys.exit(app.exec_())

    
if __name__=="__main__":
    app = QApplication(sys.argv)
    mainWindow=QMainWindow()
    startWindow=QMainWindow()
    main(app,startWindow,mainWindow)
    