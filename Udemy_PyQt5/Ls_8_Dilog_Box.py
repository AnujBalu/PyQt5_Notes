from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class mydialog(QDialog):
    def __init__(self):
        super(mydialog, self).__init__()
        self.setWindowTitle("my second window")
        self.resize(200,300)

        layout = QVBoxLayout()
        self.label = QLabel(" hello my friend")
        layout.addWidget(self.label)
        self.setLayout(layout)

class display(QMainWindow):
    def __init__(self):
        super(display,self).__init__()
        self.setWindowTitle("Combo Box")
        self.resize(500,600)
        layout = QVBoxLayout()

        # we can create a second screen using two mathod

        # first method: here calling a class when pushbutton clicked using sindle line
        btn1 = QPushButton("press me" , clicked= lambda: mydialog().exec())
        # here we calling a class (mydialog())and executing it when we pressed the pushbutton

        # second method: calling a function when pushbutton is clicked and executing dialog class inside that function
        btn2 = QPushButton("continue" , clicked = lambda : screen(self))

        layout.addWidget(btn1)
        layout.addWidget(btn2)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        def screen(self):
            dialog = mydialog()
            dialog.label.setText("My world")     # even here also you can edit the class
            dialog.exec()


app = QApplication([])
window = display()
window.show()
app.exec()