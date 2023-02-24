from PyQt6.QtWidgets import QApplication
from views.main_view import MainWindow
import sys

class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)

        self.main_view = MainWindow()
        self.main_view.show()

if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec())