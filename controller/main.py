__author__ = 'charles'

import sys
from ui.MainDialog import MainDialog
from PyQt4.QtGui import QApplication, QDialog


def main():
    app = QApplication(sys.argv)
    dialog = MainDialog(app)
    dialog.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
