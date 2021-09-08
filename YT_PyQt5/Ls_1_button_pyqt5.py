import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class mymainwindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # title of our window
        self.setWindowTitle("my first PyQt5 project")

        # size of our window
        #self.resize(500,400)

        # set Vertical Layout
        self.setLayout(qtw.QVBoxLayout())

        # set Horizontal Layout
        # self.setLayout(QHBoxLayout)

        # create a Label
        label = qtw.QLabel("Enter your name")
        # add the layout to window
        self.layout().addWidget(label)

        # change the font size in label
        self.setFont(qtg.QFont('times',25))    # 'time' is font style & 25 is font size

        # create a entry box
        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("user_name")
        my_entry.setText("")                # if you want text inside your box
        self.layout().addWidget(my_entry)

        # create a button
        my_button = qtw.QPushButton("Continue..",clicked= lambda :press_it())
        # 'clicked=' defines after the button is clicked, it opens the function


        self.layout().addWidget(my_button)


        def press_it():
            # add name to label
            label.setText(f"Hello {my_entry.text()}, how's your day")
            # clear the entry box
            my_entry.setText("")
app = qtw.QApplication([])
window = mymainwindow()
window.show()
app.exec()