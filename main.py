from PyQt5.QtWidgets import QApplication, QMainWindow
import ui_main, sys, random, string, pyperclip

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main = ui_main.Ui_Form()
        self.main.setupUi(self)
        self.main.generateButton.clicked.connect(lambda: self.generate_password())
        self.generate_password()
        
        
    def generate_password(self):
        length = 16
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        num = string.digits
        symbols = string.punctuation
        all = lower + lower + upper + upper + num + symbols
        temp = random.sample(all, length)
        password = "".join(temp)
        self.main.passOutput.setText(password)
        self.main.passOutput.selectAll()
        pyperclip.copy(password)

        
        
        
        
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
