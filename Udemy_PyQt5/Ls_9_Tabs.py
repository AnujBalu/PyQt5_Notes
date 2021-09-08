from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class display(QMainWindow):
    def __init__(self):
        super(display, self).__init__()
        self.setWindowTitle("Tabs")
        self.resize(500,400)

        layout = QVBoxLayout()
        tab = QTabWidget()
        
        tab.setMovable(True)
        # ".setMovable" by default it will be false , if changed to True then you can move all the tabs or re-arrange it

        tab.addTab(QLabel("hello there\nhow are you"),"Tab 1")
        tab.addTab(QLabel("22\n2222\n222222"), "Tab 2")
        tab.addTab(QLabel("this is how tab works"), "Tab 3")

        layout.addWidget(tab)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication([])
window = display()
window.show()
app.exec()