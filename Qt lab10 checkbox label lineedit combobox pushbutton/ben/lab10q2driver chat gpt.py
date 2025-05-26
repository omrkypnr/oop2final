import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow
from lab10q2 import Ui_MainWindow  # .ui dosyasından pyuic5 ile çevrilen dosyanın adı

class GameApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.current_number = None
        self.score = 0

        # ComboBox index -> sayı eşleştirmesi
        self.index_to_number = {
            0: 1,
            1: 2,
            2: 3,
            3: 4,
            4: 5
        }

        # Buton bağlantıları
        self.ui.pushButton_nextnumber.clicked.connect(self.generate_number)
        self.ui.pushButton_confirm.clicked.connect(self.check_answer)

    def generate_number(self):
        self.current_number = random.randint(1, 5)
        self.ui.label_number.setText(str(self.current_number))

    def check_answer(self):
        if self.current_number is None:
            return

        selected_index = self.ui.comboBox.currentIndex()
        selected_number = self.index_to_number[selected_index]

        if selected_number == self.current_number:
            self.score += 10
            self.ui.label_0.setText(str(self.score))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = GameApp()
    win.show()
    sys.exit(app.exec_())
