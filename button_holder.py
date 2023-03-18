from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton


class ButtonHolder(QMainWindow): # Inherits from QMainWindow (parent) class
    def __init__(self): # Constructor
        super().__init__() 
        self.setWindowTitle("テスト")
        button = QPushButton("Press")

        # Set button as central widget
        self.setCentralWidget(button)
