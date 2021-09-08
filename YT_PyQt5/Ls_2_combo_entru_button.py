import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class mymainwindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # title of our window
        self.setWindowTitle("my second PyQt5 project")

        # size of our window
        #self.resize(500,400)

        # set Vertical Layout
        self.setLayout(Qt.QVBoxLayout())

        # set Horizontal Layout
        #self.setLayout(qtw.QHBoxLayout())

        # create a Label
        label = qtw.QLabel("Enter a place to visit ?")
        # add the layout to window
        self.layout().addWidget(label)

        # change the font size in label
        self.setFont(qtg.QFont('times',25))    # 'time' is font style & 50 is font size

        # create a combo box
        #my_combo = qtw.QComboBox(self)   # it is for normal combo box
                                        # In default "editable=" will be false, so that you cann't edit or text new item

        # To create a combo box and text a new item at top of combo box:
        my_combo = qtw.QComboBox(self , editable= True, insertPolicy=qtw.QComboBox.InsertAtTop)
                                        # here we changed "editaple=" to true, so that we can add or text on screen.
                                        # if "inserPolicy=" code is not written by defult it will insert at bottom.
        #To create a combo box and text a new item at bottom of combo box:
        #my_combo = qtw.QComboBox(self, editable=True, insertPolicy=qtw.QComboBox.InsertAtBottom)


        # add items in combo box
        my_combo.addItem("chennai","its good place ")  # here the first name<"chennai"> is text and
                                                       # second name <"its good place"> is Data Type
        my_combo.addItem("coimbatore" , 23)              # Data Type can be string, integer, function and can be empty.
        my_combo.addItem("sathyamagalam", qtw.QWidget)
        my_combo.addItem("tiruppur")                    # this is example of empty Data Type

        # <.addItem> will display single item
        # <.addItems> will display multiple item
        my_combo.addItems(["vkl","trichy","Erode"])

        # To insert a new item
        my_combo.insertItem(1,"tamil nadu") # "1" is the index to be inserted and "tamil nadu" is the Text

        # To insert a list of items
        my_combo.insertItems(2,["india", "USA", "Japan"])

        # put combo box on the screen
        self.layout().addWidget(my_combo)

        # create a button
        my_button = qtw.QPushButton("Continue..",clicked= lambda :press_it())
        # 'clicked=' defines after the button is clicked, it opens the function


        self.layout().addWidget(my_button)


        def press_it():
            # add name to label
            label.setText(f"Are you confirm to vist this place {my_combo.currentText()}")
            # currentText() will show the selected text in from combo box in screen
            #label.setText(f"Are you confirm to vist this place {my_combo.currentData()}")
            # cu
            #label.setText(f"Are you confirm to vist this place {my_combo.currentIndex()}")
            # clear the entry box
            #my_entry.setText("")
app = qtw.QApplication([])
window = mymainwindow()
window.show()
app.exec()