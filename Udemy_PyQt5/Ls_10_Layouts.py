from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class display(QMainWindow):
    def __init__(self):
        super(display,self).__init__()
        self.setWindowTitle("Combo Box")
        self.resize(500,600)

        #layout = QVBoxLayout   # here all thing's position are fixed vertically

        #layout = QHBoxLayout   # here all thing's position are fixed Horizontally

        grid = QGridLayout()   # using this method, position of things can be placed anywhere on screen
                                # just we have to give coordinates to fix that perticular position

        grid.addWidget(QLabel("hi"), 1,2 )
        grid.addWidget(QLabel("hello"), 2,7)
        grid.addWidget(QLabel("hey"), 5,3)
        grid.addWidget(QLabel("bye"), 4,1)

        widget = QWidget()
        widget.setLayout(grid)
        self.setCentralWidget(widget)


app = QApplication([])
window = display()
window.show()
app.exec()