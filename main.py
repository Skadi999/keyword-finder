import sys

from PySide6 import QtWidgets
from gui import KeywordFinderWidget

if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    widget = KeywordFinderWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
