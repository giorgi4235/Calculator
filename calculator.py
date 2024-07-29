from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(361, 579)
        MainWindow.setWindowIcon(QtGui.QIcon('assets\\calc_icon.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        MainWindow.setMinimumSize(QtCore.QSize(361, 579))
        MainWindow.setMaximumSize(QtCore.QSize(361, 579))

        self.mainLayout = QtWidgets.QVBoxLayout(self.centralwidget)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 341, 91))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")

        self.gridLayout = QtWidgets.QGridLayout()

        self.cButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("C"))
        self.cButton.setGeometry(QtCore.QRect(10, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.cButton.setFont(font)
        self.cButton.setObjectName("cButton")
        self.percentButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.percent_it())
        self.percentButton.setGeometry(QtCore.QRect(100, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.percentButton.setFont(font)
        self.percentButton.setObjectName("percentButton")
        self.squareButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.remove_it())
        self.squareButton.setGeometry(QtCore.QRect(190, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.squareButton.setFont(font)
        self.squareButton.setObjectName("squareButton")
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("/"))
        self.deleteButton.setGeometry(QtCore.QRect(280, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.deleteButton.setFont(font)
        self.deleteButton.setObjectName("divisionButton")
        self.multipleButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("*"))
        self.multipleButton.setGeometry(QtCore.QRect(280, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.multipleButton.setFont(font)
        self.multipleButton.setObjectName("multipleButton")
        self.nineButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("9"))
        self.nineButton.setGeometry(QtCore.QRect(190, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.nineButton.setFont(font)
        self.nineButton.setObjectName("nineButton")
        self.eightButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("8"))
        self.eightButton.setGeometry(QtCore.QRect(100, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.eightButton.setFont(font)
        self.eightButton.setObjectName("eightButton")
        self.sevenButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("7"))
        self.sevenButton.setGeometry(QtCore.QRect(10, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sevenButton.setFont(font)
        self.sevenButton.setObjectName("psevenButton")
        self.oneButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("1"))
        self.oneButton.setGeometry(QtCore.QRect(10, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.oneButton.setFont(font)
        self.oneButton.setObjectName("oneButton")
        self.sixButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("6"))
        self.sixButton.setGeometry(QtCore.QRect(190, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sixButton.setFont(font)
        self.sixButton.setObjectName("sixButton")
        self.plusButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("+"))
        self.plusButton.setGeometry(QtCore.QRect(280, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.plusButton.setFont(font)
        self.plusButton.setObjectName("plusButton")
        self.fiveButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("5"))
        self.fiveButton.setGeometry(QtCore.QRect(100, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.fiveButton.setFont(font)
        self.fiveButton.setObjectName("fiveButton")
        self.minusButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("-"))
        self.minusButton.setGeometry(QtCore.QRect(280, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.minusButton.setFont(font)
        self.minusButton.setObjectName("minusButton")
        self.twoButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("2"))
        self.twoButton.setGeometry(QtCore.QRect(100, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.twoButton.setFont(font)
        self.twoButton.setObjectName("twoButton")
        self.threeButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("3"))
        self.threeButton.setGeometry(QtCore.QRect(190, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.threeButton.setFont(font)
        self.threeButton.setObjectName("threeButton")
        self.fourButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("4"))
        self.fourButton.setGeometry(QtCore.QRect(10, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.fourButton.setFont(font)
        self.fourButton.setObjectName("fourButton")
        self.decimalButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.dot_it())
        self.decimalButton.setGeometry(QtCore.QRect(190, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.decimalButton.setFont(font)
        self.decimalButton.setObjectName("decimalButton")
        self.plusminusButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.change_it())
        self.plusminusButton.setGeometry(QtCore.QRect(10, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.plusminusButton.setFont(font)
        self.plusminusButton.setObjectName("plusminusButton")
        self.zeroButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("0"))
        self.zeroButton.setGeometry(QtCore.QRect(100, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.zeroButton.setFont(font)
        self.zeroButton.setObjectName("zeroButton")
        self.equalButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.math_it())
        self.equalButton.setGeometry(QtCore.QRect(280, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.equalButton.setFont(font)
        self.equalButton.setObjectName("equalButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 361, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #do math
    def math_it(self):
        screen = self.label.text()
        try:
            answer = eval(screen)
            self.label.setText(str(answer))
        except:
            self.label.setText("ERROR")

    #calculate percent
    def percent_it(self):
        screen = self.label.text()
        try:
            answer = float(screen)
            self.label.setText(str(answer/100))
        except:
            self.label.setText("ERROR")

    #change from positive/negativ
    def change_it(self):
        screen = self.label.text()
        if screen[0] == "-":
            self.label.setText(f"{screen[1:]}")
        else:
            self.label.setText(f"-{screen}")

    #remove character
    def remove_it(self):
        #SevinaxoT rac aris ukve ekranze
        screen = self.label.text()
        #remove last item
        screen = screen[:-1]
        #output back to the screen
        self.label.setText(screen)

    #add decimal
    def dot_it(self):
        screen = self.label.text()
        possible_chars_list = ['*', '/', '-', '+']
        is_valid = True
        for i in screen:
            if i in possible_chars_list:
                is_valid = True
            elif i == ".":
                is_valid = False
        if is_valid:
            self.label.setText(f'{screen}.')

# make functions
    def press_it(self, press):
        if press == "C":
            self.label.setText("0")
        else:
            #vamowmebt tu iwyeba teqsti nulit waishalos
            if self.label.text() == "0":
                self.label.setText("")
           #sxva danarchen shemtxvevashi rac iyo ghilaki eg gamoitanos
            self.label.setText(f"{self.label.text()}{press}")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.label.setText(_translate("MainWindow", "0"))
        self.cButton.setText(_translate("MainWindow", "C"))
        self.percentButton.setText(_translate("MainWindow", "%"))
        self.squareButton.setText(_translate("MainWindow", "<<"))
        self.deleteButton.setText(_translate("MainWindow", "/"))
        self.multipleButton.setText(_translate("MainWindow", "X"))
        self.nineButton.setText(_translate("MainWindow", "9"))
        self.eightButton.setText(_translate("MainWindow", "8"))
        self.sevenButton.setText(_translate("MainWindow", "7"))
        self.oneButton.setText(_translate("MainWindow", "1"))
        self.sixButton.setText(_translate("MainWindow", "6"))
        self.plusButton.setText(_translate("MainWindow", "+"))
        self.fiveButton.setText(_translate("MainWindow", "5"))
        self.minusButton.setText(_translate("MainWindow", "-"))
        self.twoButton.setText(_translate("MainWindow", "2"))
        self.threeButton.setText(_translate("MainWindow", "3"))
        self.fourButton.setText(_translate("MainWindow", "4"))
        self.decimalButton.setText(_translate("MainWindow", "."))
        self.plusminusButton.setText(_translate("MainWindow", "+/-"))
        self.zeroButton.setText(_translate("MainWindow", "0"))
        self.equalButton.setText(_translate("MainWindow", "="))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())