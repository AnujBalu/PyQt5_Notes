from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class display(QMainWindow):
    def __init__(self):
        super(display,self).__init__()
        self.setWindowTitle("Combo Box")
        self.resize(500,600)
        layout = QVBoxLayout()

        combo = QComboBox()

        combo.addItem("apple")
        combo.addItem("orange")
        combo.addItem("Banana")
        btn1 = QPushButton("continue", pressed= lambda: press_me(combo))
        # adding list in combo
        combo.addItems(["lemon", "mango","chocolate"])

        layout.addWidget(combo)
        layout.addWidget(btn1)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        def press_me(combo):
            print(combo.currentText())




app = QApplication([])
window = display()
window.show()
app.exec()