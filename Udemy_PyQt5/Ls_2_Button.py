from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
class display(QMainWindow):
    def __init__(self):
        super(display,self).__init__()

        # lets work on app
        self.setWindowTitle("hello world")
        self.resize(400,300)

        # Layout
        # vertical layout:
        layout = QVBoxLayout()            # this line is used to alignment the output of our program

        # Horizontal layout:
        #layout = QHBoxLayout()

        btn1 = QPushButton("Button 1", clicked= lambda : btn1_clicked())
        btn2 = QPushButton("Button 2", clicked= lambda : btn2_clicked())
        label = QLabel("What are you going to chick")
        font = label.font()
        font.setPointSize(15)
        label.setFont(font)
        label.setAlignment(Qt.AlignCenter)  # to make the text place at center

        # add stuff to layout:
        layout.addWidget(label)
        layout.addWidget(btn1)
        layout.addWidget(btn2)

        widget = QWidget()
        widget.setLayout(layout)            # here layout is converted into a widget because only widgets can be
        self.setCentralWidget(widget)       # displayed on screen , not a layout. Thats why layout is converted into
                                            # widget using "QWidget()" method.

        def btn1_clicked():
            label.setText("Thank you for clicking btn 1")

        def btn2_clicked():
            label.setText("Thank you for clicking btn 2")

app = QApplication([])
window = display()
window.show()
app.exec()