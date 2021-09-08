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
        label = qtw.QLabel("Enter your number")
        # add the layout to window
        label.setFont(qtg.QFont('times', 25))  # 'time' is font style & 25 is font size

        self.layout().addWidget(label)

        # change the font size in label

        # create a spin box
        my_spin = qtw.QSpinBox(self,
                               value=10 ,          # this value will show us first when the screen pop-up
                               maximum=100,        # we can not go above this maximum value
                               minimum=0,          # we can not go below the minimum value
                               singleStep=5,       # this is spin botton value to increase and decrease the value
                               prefix="#",         # this will be printed front of value in box
                               suffix=" order" )   # this will be printed after the value in box
                                                # this prefix and suffix will not be passed to next stage or function
                                                # this prefix & suffix are optional either you can use
                                                # both or any one or no need to use it
        # To step up and down in floating digit:

        #my_spin = qtw.QDoubleSpinBox(self,
        #                       value=10,
        #                       maximum=100,
        #                       minimum=0,
        #                       singleStep=5.25,
        #                       prefix="#",
        #                       suffix=" order")

        my_spin.setFont(qtg.QFont('times', 20))
        # put spin box on screen
        self.layout().addWidget(my_spin)


        # create a button
        my_button = qtw.QPushButton("Continue..",clicked= lambda :press_it())
        # 'clicked=' defines after the button is clicked, it opens the function


        self.layout().addWidget(my_button)


        def press_it():
            # add name to label
            label.setText(f" Picked number {my_spin.value()}")

app = qtw.QApplication([])
window = mymainwindow()
window.show()
app.exec()