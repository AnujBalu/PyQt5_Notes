import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class mymainwindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # title of our window
        self.setWindowTitle("my first PyQt5 project")

        # size of our window
        self.resize(500,400)

        # set Vertical Layout
        #self.setLayout(qtw.QVBoxLayout())

        # set Horizontal Layout
        #self.setLayout(qtw.QHBoxLayout())

        form_layout= qtw.QFormLayout()
        self.setLayout(form_layout)

        # add stuff/ widgets:
        label_1 = qtw.QLabel("I am first")
        label_1.setFont(qtg.QFont("Times",25))

        f_name = qtw.QLineEdit(self)
        l_name = qtw.QLineEdit(self)

        # add rows to top
        form_layout.addRow(label_1)
        form_layout.addRow("first name",f_name)
        form_layout.addRow("last name",l_name)
        form_layout.addRow(qtw.QPushButton("continue..",clicked=lambda :press_me()))

        def press_me():
            label_1.setText(f" you clicked  {f_name.text()}{l_name.text()}")

app = qtw.QApplication([])
window = mymainwindow()
window.show()
app.exec()