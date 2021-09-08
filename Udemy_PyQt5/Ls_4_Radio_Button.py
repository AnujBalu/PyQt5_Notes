from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class display(QMainWindow):
    def __init__(self):
        super(display,self).__init__()
        self.setWindowTitle("Radio Box")
        self.resize(500,600)
        layout = QVBoxLayout()

        label = QLabel("your chose please")
        font = label.font()
        font.setPointSize(30)
        label.setFont(font)

        male_btn = QRadioButton("male" , toggled= lambda: press(male_btn))
        female_btn = QRadioButton("female", toggled= lambda: press(female_btn))

        layout.addWidget(label)
        layout.addWidget(male_btn)
        layout.addWidget(female_btn)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        def press(x):
            label.setText(f"Now I know you are a {x.text()}")


app = QApplication([])
window = display()
window.show()
app.exec()