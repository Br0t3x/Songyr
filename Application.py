from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QWidget
from Functions import *


class Application(QMainWindow):
    def __init__(self):
        super().__init__()

        download_ytvid_as_mp3("https://www.youtube.com/watch?v=5dKQA8l893k")

        self.show()
