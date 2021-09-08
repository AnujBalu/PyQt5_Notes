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
        self.setLayout(qtw.QVBoxLayout())

        # set Horizontal Layout
        # self.setLayout(QHBoxLayout)

        # create a Label
        label = qtw.QLabel("Enter your name")
        # add the layout to window
        self.layout().addWidget(label)

        # change the font size in label
        self.setFont(qtg.QFont('times',25))    # 'time' is font style & 25 is font size

        # create a Text box
        my_text = qtw.QTextEdit(self,
                            acceptRichText= True,                   # you can access bold and colour text
                            #plainText="this is for real",        # it can be used as starting text in text box
                            #html="<h1>Big Title</h1>",           # Even you can access html in this text box
                            #html="<h1><em>second Title</em></h1>",     # italic style in html
                            #html="<center><h1>Third Title</h1></center>",  # To make the title centeral using html
                            lineWrapMode=qtw.QTextEdit.FixedColumnWidth,     # to keep our text fixed
                            lineWrapColumnOrWidth=30,                        # width of text inside text box
                            placeholderText="Type your comments",        # this will be transeferent words in text box
                            readOnly=False)          # by defult it will false if you want you can change to True
                            # if "readOnly=" changed to true then you cann't type anything, only you can read the text.
        self.layout().addWidget(my_text)

        # create a button
        my_button = qtw.QPushButton("Continue..",clicked= lambda :press_it())
        # 'clicked=' defines after the button is clicked, it opens the function


        self.layout().addWidget(my_button)


        def press_it():
            # add name to label
            label.setText(f'your text "{my_text.toPlainText()}"')
            my_text.setPlainText("successfully committed")

app = qtw.QApplication([])
window = mymainwindow()
window.show()
app.exec()