from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton


class ButtonHolder(QMainWindow): # Inherits from QMainWindow (parent) class
    def __init__(self): # Constructor for ButtonHolder (daughter class)
        super().__init__() # Inheriting QMainWindows' constructor
        self.setWindowTitle("window_title")
        
        #Button
        button = QPushButton("Press")
        button.setCheckable(True) # Button is a toggle
        self.setCentralWidget(button) # Set button as central widget
        
    def set_window_title(self, window_title):
        self.setWindowTitle(window_title)

"""
def respond_to_slider(data):
    print ("slider moved to : ", data)

    slider = QSlider(Qt.Horizontal)
    slider.setMinimum(1)
"""
