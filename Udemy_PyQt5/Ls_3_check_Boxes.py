from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class display(QMainWindow):
    def __init__(self):
        super(display,self).__init__()
        self.setWindowTitle("Check Box")
        self.resize(500,600)
        layout = QVBoxLayout()

        label = QLabel("your chose please")
        font = label.font()
        font.setPointSize(30)
        label.setFont(font)
        check1 = QCheckBox("I am right", toggled=lambda: press_me())
        check2 = QCheckBox("I am a boy", toggled=lambda: boy(check2))
        check3 = QCheckBox("I am a girl", toggled=lambda: girl(check3))
        check4 = QCheckBox("I will work hard", toggled=lambda: work(check4))
        check5 = QCheckBox("I am lazy", toggled=lambda: work(check5))

        layout.addWidget(label)
        layout.addWidget(check1)
        layout.addWidget(check2)
        layout.addWidget(check3)
        layout.addWidget(check4)
        layout.addWidget(check5)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        def press_me():
            print("hello")
        def boy(x):
            print(x.text())                 # ".text()" will show us the text in the check box
        def girl(y):
            print(y.isChecked())           # ".isChecked()" will return boolean type (True/False)

        checked_stuff = []
        def work(check):

            if check.isChecked():
                checked_stuff.append(check.text())
            else:
                checked_stuff.remove(check.text())
            print(checked_stuff)


app = QApplication([])
window = display()
window.show()
app.exec()