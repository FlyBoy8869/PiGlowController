__author__ = 'charles'

from led_ui import Ui_LedDialog
import PyQt4
from PyQt4.QtGui import QDialog, QRadioButton
from PyQt4.QtCore import SIGNAL

class MainDialog(QDialog, Ui_LedDialog):

    def __init__(self, app, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)
        self.app = app

        self.connect(self.buttonClose, SIGNAL("clicked()"), self.app.exit)
        self.connect(self.buttonAllOff, SIGNAL("clicked()"), self.button_all_off_clicked)

        self.connect_led_radiobuttons()

        self.setWindowTitle("PiGlow Controller")

    def button_all_off_clicked(self):
            leds = self.groupBoxLeds.children()

            #print leds
            for led in leds:
                if isinstance(led, QRadioButton):
                    led.setChecked(False)
                    print led.objectName()

    def connect_led_radiobuttons(self):
        leds = self.groupBoxLeds.children()
        for led in leds:
            self.connect(led, SIGNAL("clicked()"), self.led_radiobutton_toggled)

    def led_radiobutton_toggled(self):
        print "led toggled..."