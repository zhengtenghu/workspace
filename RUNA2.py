import sys
import A2
from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__=='_main_':
    app=QApplication(sys.argv)
    mainWindow=QMainWindow()
    ui=A2.ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())