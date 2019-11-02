import sys
import example4
from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__=='_main_':
    app=QApplication(sys.argv)
    mainWindow=QMainWindow()
    ui=example4.ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())