from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QWidget
from playsound import playsound


class Application(QMainWindow):
    def __init__(self):
        super().__init__()

        self.show()
