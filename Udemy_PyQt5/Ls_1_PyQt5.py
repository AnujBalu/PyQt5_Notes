from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication

class display(QMainWindow):
    def __init__(self):                             # we cann't add widgets in main class so that we are creatinf a
        super(display,self).__init__()              # sub-class using super() method to add extra stuffs
        self.setWindowTitle("my first programme")
        self.resize(500,300)

        label = QLabel("Hey Hello")
        font = label.font()
        font.setPointSize(40)              # adjusting font size using ".setPointSize()"
        self.setFont(font)
        self.setCentralWidget(label)      # displays text on screen

app = QApplication([])
window = display()
window.show()
app.exec()