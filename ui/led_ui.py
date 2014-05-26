# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'led_ui.ui'
#
# Created: Thu May  1 15:55:26 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_LedDialog(object):
    def setupUi(self, LedDialog):
        LedDialog.setObjectName(_fromUtf8("LedDialog"))
        LedDialog.resize(428, 337)
        self.groupBoxLeds = QtGui.QGroupBox(LedDialog)
        self.groupBoxLeds.setGeometry(QtCore.QRect(25, 25, 376, 261))
        self.groupBoxLeds.setAutoFillBackground(True)
        self.groupBoxLeds.setStyleSheet(_fromUtf8("border-color: rgb(0, 0, 0);"))
        self.groupBoxLeds.setObjectName(_fromUtf8("groupBoxLeds"))
        self.led18 = QtGui.QRadioButton(self.groupBoxLeds)
        self.led18.setGeometry(QtCore.QRect(260, 175, 21, 21))
        self.led18.setText(_fromUtf8(""))
        self.led18.setAutoExclusive(False)
        self.led18.setObjectName(_fromUtf8("led18"))
        self.led9 = QtGui.QRadioButton(self.groupBoxLeds)
        self.led9.setGeometry(QtCore.QRect(125, 75, 21, 21))
        self.led9.setText(_fromUtf8(""))
        self.led9.setAutoExclusive(False)
        self.led9.setObjectName(_fromUtf8("led9"))
        self.led6 = QtGui.QRadioButton(self.groupBoxLeds)
        self.led6.setGeometry(QtCore.QRect(120, 105, 21, 21))
        self.led6.setText(_fromUtf8(""))
        self.led6.setAutoExclusive(False)
        self.led6.setObjectName(_fromUtf8("led6"))
        self.led1 = QtGui.QRadioButton(self.groupBoxLeds)
        self.led1.setGeometry(QtCore.QRect(95, 190, 21, 21))
        self.led1.setText(_fromUtf8(""))
        self.led1.setAutoExclusive(False)
        self.led1.setObjectName(_fromUtf8("led1"))
        self.led14 = QtGui.QRadioButton(self.groupBoxLeds)
        self.led14.setGeometry(QtCore.QRect(215, 100, 21, 21))
        self.led14.setText(_fromUtf8(""))
        self.led14.setAutoExclusive(False)
        self.led14.setObjectName(_fromUtf8("led14"))
        self.led3 = QtGui.QRadioButton(self.groupBoxLeds)
        self.led3.setGeometry(QtCore.QRect(155, 190, 21, 21))
        self.led3.setText(_fromUtf8(""))
        self.led3.setAutoExclusive(False)
        self.led3.setObjectName(_fromUtf8("led3"))
        self.led8 = QtGui.QRadioButton(self.groupBoxLeds)
        self.led8.setGeometry(QtCore.QRect(145, 55, 21, 21))
        self.led8.setText(_fromUtf8(""))
        self.led8.setAutoExclusive(False)
        self.led8.setObjectName(_fromUtf8("led8"))
        self.led12 = QtGui.QRadioButton(self.groupBoxLeds)
        self.led12.setGeometry(QtCore.QRect(185, 100, 21, 21))
        self.led12.setText(_fromUtf8(""))
        self.led12.setAutoExclusive(False)
        self.led12.setObjectName(_fromUtf8("led12"))
        self.led11 = QtGui.QRadioButton(self.groupBoxLeds)
        self.led11.setGeometry(QtCore.QRect(165, 115, 21, 21))
        self.led11.setText(_fromUtf8(""))
        self.led11.setAutoExclusive(False)
        self.led11.setObjectName(_fromUtf8("led11"))
        self.led15 = QtGui.QRadioButton(self.groupBoxLeds)
        self.led15.setGeometry(QtCore.QRect(195, 150, 21, 21))
        self.led15.setText(_fromUtf8(""))
        self.led15.setAutoExclusive(False)
        self.led15.setObjectName(_fromUtf8("led15"))
        self.led4 = QtGui.QRadioButton(self.groupBoxLeds)
        self.led4.setGeometry(QtCore.QRect(180, 175, 21, 21))
        self.led4.setText(_fromUtf8(""))
        self.led4.setAutoExclusive(False)
        self.led4.setObjectName(_fromUtf8("led4"))
        self.led2 = QtGui.QRadioButton(self.groupBoxLeds)
        self.led2.setGeometry(QtCore.QRect(125, 195, 21, 21))
        self.led2.setText(_fromUtf8(""))
        self.led2.setAutoExclusive(False)
        self.led2.setObjectName(_fromUtf8("led2"))
        self.led5 = QtGui.QRadioButton(self.groupBoxLeds)
        self.led5.setGeometry(QtCore.QRect(140, 130, 21, 21))
        self.led5.setText(_fromUtf8(""))
        self.led5.setAutoExclusive(False)
        self.led5.setObjectName(_fromUtf8("led5"))
        self.led16 = QtGui.QRadioButton(self.groupBoxLeds)
        self.led16.setGeometry(QtCore.QRect(240, 120, 21, 21))
        self.led16.setText(_fromUtf8(""))
        self.led16.setAutoExclusive(False)
        self.led16.setObjectName(_fromUtf8("led16"))
        self.led13 = QtGui.QRadioButton(self.groupBoxLeds)
        self.led13.setGeometry(QtCore.QRect(185, 125, 21, 21))
        self.led13.setText(_fromUtf8(""))
        self.led13.setAutoExclusive(False)
        self.led13.setObjectName(_fromUtf8("led13"))
        self.led7 = QtGui.QRadioButton(self.groupBoxLeds)
        self.led7.setGeometry(QtCore.QRect(170, 40, 21, 21))
        self.led7.setText(_fromUtf8(""))
        self.led7.setAutoExclusive(False)
        self.led7.setObjectName(_fromUtf8("led7"))
        self.led17 = QtGui.QRadioButton(self.groupBoxLeds)
        self.led17.setGeometry(QtCore.QRect(250, 145, 21, 21))
        self.led17.setText(_fromUtf8(""))
        self.led17.setAutoExclusive(False)
        self.led17.setObjectName(_fromUtf8("led17"))
        self.led10 = QtGui.QRadioButton(self.groupBoxLeds)
        self.led10.setGeometry(QtCore.QRect(165, 135, 21, 21))
        self.led10.setText(_fromUtf8(""))
        self.led10.setAutoExclusive(False)
        self.led10.setObjectName(_fromUtf8("led10"))
        self.buttonClose = QtGui.QPushButton(LedDialog)
        self.buttonClose.setGeometry(QtCore.QRect(300, 300, 92, 24))
        self.buttonClose.setObjectName(_fromUtf8("buttonClose"))
        self.buttonAllOff = QtGui.QPushButton(LedDialog)
        self.buttonAllOff.setGeometry(QtCore.QRect(30, 300, 99, 25))
        self.buttonAllOff.setObjectName(_fromUtf8("buttonAllOff"))

        self.retranslateUi(LedDialog)
        QtCore.QMetaObject.connectSlotsByName(LedDialog)

    def retranslateUi(self, LedDialog):
        LedDialog.setWindowTitle(_translate("LedDialog", "Dialog", None))
        self.groupBoxLeds.setTitle(_translate("LedDialog", "PiGlow LEDs", None))
        self.buttonClose.setText(_translate("LedDialog", "Close", None))
        self.buttonAllOff.setText(_translate("LedDialog", "All Off", None))

