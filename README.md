![image](https://github.com/user-attachments/assets/23024b13-852a-437d-bfa5-c08922a0cb3b)

import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from lab8q2 import Ui_MainWindow  # ui dosyandan çevrilen PyQt5 UI class

class Calculator(QMainWindow):

    def __init__(self):
    
        super().__init__()
        
        self.ui = Ui_MainWindow()
        
        self.ui.setupUi(self)
        
        
        


if __name__ == "__main__":

    app = QApplication(sys.argv)
    
    win = Calculator()
    
    win.show()
    
    sys.exit(app.exec_())
    
