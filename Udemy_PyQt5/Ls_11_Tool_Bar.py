from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class display(QMainWindow):
    def __init__(self):
        super(display,self).__init__()
        self.setWindowTitle("Tool Bar")
        self.resize(500,600)
        layout = QVBoxLayout()

        tool = QToolBar("toolbar")    # here a tool bar is created
        btn1 = QAction("java",self)  # hare creating a option or button in our tool bar
        btn1.setCheckable(True)
        # by default it will be in false, if you changed it into true . then your click on that button will be
        # selected until you de-select it

        # to add icon n tool bar
        btn2 = QAction(QIcon("python.jpg"), "python",self)

        tool.addAction(btn2)          # here we adding that option in our tool bar
        tool.addAction(btn1)

        tool.addSeparator()   # it helps to move your tool bar to any connor

        self.addToolBar(tool)          # hare we showing that toolbar on screen

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


app = QApplication([])
window = display()
window.show()
app.exec()