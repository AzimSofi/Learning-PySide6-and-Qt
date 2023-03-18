# Sys module, processing command line arguments
import sys
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from button_holder import ButtonHolder

# App object that acts as a wrapper to the application
app = QApplication(sys.argv)


# Create object
window = ButtonHolder()

# Windows of QT in windows is usually hidden |-> show() to show 
# Start event loop, to check i/o
window.show()
app.exec()
