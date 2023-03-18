from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton


class ButtonHolder(QMainWindow): # Inherits from QMainWindow (parent) class
    def __init__(self): # Constructor for ButtonHolder (daughter class)
        super().__init__() # Inheriting QMainWindows' constructor

        self.setWindowTitle("テスト")
        button = QPushButton("Press")

        # Set button as central widget
        self.setCentralWidget(button)
