'''
This system was created using PyQt6 Designer that easily generates UI elements

The programmers converted the GUI Form into a Python Code by using pyuic6

Download first all the libraries and dependencies such as PyQt6 and PySide6
'''


from PyQt6 import QtCore, QtGui, QtWidgets #Importing all the Libraries and Dependencies to properly run the program

#This is the home page class 
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(651, 467)
        Form.setMinimumSize(QtCore.QSize(651, 467))
        Form.setMaximumSize(QtCore.QSize(651, 467))
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 61))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/Enverga-logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_7 = QtWidgets.QLabel(parent=Form)
        self.label_7.setGeometry(QtCore.QRect(80, 10, 61, 61))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/icons/ccmslogo.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(160, 0, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(parent=Form)
        self.label_6.setGeometry(QtCore.QRect(160, 30, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_6.setObjectName("label_6")
        self.exits = QtWidgets.QPushButton(parent=Form)
        self.exits.setGeometry(QtCore.QRect(560, 10, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.exits.setFont(font)
        self.exits.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.exits.setStyleSheet("QPushButton{color: white;\n"
"background-color: rgb(138, 6, 9);\n"
"border:2px solid rgb(138, 6, 9);}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: rgb(138, 6, 9);\n"
"}\n"
"")
        self.exits.setObjectName("exit")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(-10, 80, 671, 161))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/icons/Screenshot 2024-10-03 123823.png"))
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.pushTruncated = QtWidgets.QPushButton(parent=Form)
        self.pushTruncated.setGeometry(QtCore.QRect(10, 340, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        self.pushTruncated.setFont(font)
        self.pushTruncated.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushTruncated.setStyleSheet("QPushButton{color: white;\n"
"background-color: rgb(138, 6, 9);\n"
"border:2px solid rgb(138, 6, 9);\n"
"border-radius:15px;}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: rgb(138, 6, 9);\n"
"}\n"
"")
        self.pushTruncated.setObjectName("pushTruncated")
        self.pushLinear = QtWidgets.QPushButton(parent=Form)
        self.pushLinear.setGeometry(QtCore.QRect(70, 270, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        self.pushLinear.setFont(font)
        self.pushLinear.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushLinear.setStyleSheet("QPushButton{color: white;\n"
"background-color: rgb(138, 6, 9);\n"
"border:2px solid rgb(138, 6, 9);\n"
"border-radius:15px;}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: rgb(138, 6, 9);\n"
"}\n"
"")
        self.pushLinear.setObjectName("pushLinear")
        self.pushCombination = QtWidgets.QPushButton(parent=Form)
        self.pushCombination.setGeometry(QtCore.QRect(260, 270, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        self.pushCombination.setFont(font)
        self.pushCombination.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushCombination.setStyleSheet("QPushButton{color: white;\n"
"background-color: rgb(138, 6, 9);\n"
"border:2px solid rgb(138, 6, 9);\n"
"border-radius:15px;}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: rgb(138, 6, 9);\n"
"}\n"
"")
        self.pushCombination.setObjectName("pushCombination")
        self.pushRepeated = QtWidgets.QPushButton(parent=Form)
        self.pushRepeated.setGeometry(QtCore.QRect(340, 340, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        self.pushRepeated.setFont(font)
        self.pushRepeated.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushRepeated.setStyleSheet("QPushButton{color: white;\n"
"background-color: rgb(138, 6, 9);\n"
"border:2px solid rgb(138, 6, 9);\n"
"border-radius:15px;}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: rgb(138, 6, 9);\n"
"}\n"
"")
        self.pushRepeated.setObjectName("pushRepeated")
        self.pushCircular = QtWidgets.QPushButton(parent=Form)
        self.pushCircular.setGeometry(QtCore.QRect(440, 270, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        self.pushCircular.setFont(font)
        self.pushCircular.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushCircular.setAutoFillBackground(False)
        self.pushCircular.setStyleSheet("QPushButton{color: white;\n"
"background-color: rgb(138, 6, 9);\n"
"border:2px solid rgb(138, 6, 9);\n"
"border-radius:15px;}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: rgb(138, 6, 9);\n"
"}\n"
"")
        self.pushCircular.setObjectName("pushCircular")
        self.label_8 = QtWidgets.QLabel(parent=Form)
        self.label_8.setGeometry(QtCore.QRect(0, 400, 651, 41))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/icons/Screenshot 2024-10-03 131509.png"))
        self.label_8.setObjectName("label_8")
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setGeometry(QtCore.QRect(10, 440, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=Form)
        self.label_5.setGeometry(QtCore.QRect(80, 440, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);\n"
"")
        self.label_5.setObjectName("label_5")
        self.contacts = QtWidgets.QPushButton(parent=Form)
        self.contacts.setGeometry(QtCore.QRect(470, 10, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.contacts.setFont(font)
        self.contacts.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.contacts.setStyleSheet("QPushButton{color: white;\n"
"background-color: rgb(138, 6, 9);\n"
"border:2px solid rgb(138, 6, 9);}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: rgb(138, 6, 9);\n"
"}\n"
"")
        self.contacts.setObjectName("contacts")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MAIN"))
        self.label_2.setText(_translate("Form", "Manuel S. Enverga University"))
        self.label_6.setText(_translate("Form", "Foundation"))
        self.exits.setText(_translate("Form", "EXIT"))
        self.pushTruncated.setText(_translate("Form", "Permutation with Truncated Elements"))
        self.pushLinear.setText(_translate("Form", "Linear Permutation"))
        self.pushCombination.setText(_translate("Form", "Combination"))
        self.pushRepeated.setText(_translate("Form", "Permutation with Repeated Elements"))
        self.pushCircular.setText(_translate("Form", "Circular Permutation"))
        self.label_4.setText(_translate("Form", "Created By:"))
        self.label_5.setText(_translate("Form", "Martirez, Cabalsa and Alpuerto"))
        self.contacts.setText(_translate("Form", "Contacts"))



#-------------------------------------------------------------------------------------------------
#This is the class for the members widget
#-------------------------------------------------------------------------------------------------

class Ui_Members(object):
    def setupUi(self, Members):
        Members.setObjectName("Members")
        Members.resize(480, 640)
        
        Members.setMinimumSize(QtCore.QSize(480, 640))
        Members.setMaximumSize(QtCore.QSize(480, 640))
        Members.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_9 = QtWidgets.QLabel(parent=Members)
        self.label_9.setGeometry(QtCore.QRect(80, 20, 331, 61))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.back = QtWidgets.QPushButton(parent=Members)
        self.back.setGeometry(QtCore.QRect(390, 10, 75, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.back.setFont(font)
        self.back.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.back.setStyleSheet("QPushButton{color: white;\n"
"background-color: rgb(138, 6, 9);\n"
"border:2px solid rgb(138, 6, 9);}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: rgb(138, 6, 9);\n"
"}\n"
"")
        self.back.setObjectName("back")
        self.label_10 = QtWidgets.QLabel(parent=Members)
        self.label_10.setGeometry(QtCore.QRect(30, 110, 141, 141))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap(":/icons/gab.jpg"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(parent=Members)
        self.label_11.setGeometry(QtCore.QRect(30, 290, 141, 141))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap(":/icons/jef.jpg"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(parent=Members)
        self.label_12.setGeometry(QtCore.QRect(30, 470, 141, 141))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap(":/icons/jp.jpg"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.label = QtWidgets.QLabel(parent=Members)
        self.label.setGeometry(QtCore.QRect(200, 120, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Members)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 71, 61))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/icons/Enverga-logo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QLabel(parent=Members)
        self.label_7.setGeometry(QtCore.QRect(90, 10, 61, 61))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/icons/ccmslogo.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_3 = QtWidgets.QLabel(parent=Members)
        self.label_3.setGeometry(QtCore.QRect(200, 300, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=Members)
        self.label_4.setGeometry(QtCore.QRect(200, 470, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=Members)
        self.label_5.setGeometry(QtCore.QRect(200, 150, 171, 16))
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=Members)
        self.label_6.setGeometry(QtCore.QRect(200, 180, 171, 16))
        self.label_6.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(parent=Members)
        self.label_8.setGeometry(QtCore.QRect(200, 330, 171, 16))
        self.label_8.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_8.setObjectName("label_8")
        self.label_13 = QtWidgets.QLabel(parent=Members)
        self.label_13.setGeometry(QtCore.QRect(200, 360, 191, 16))
        self.label_13.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(parent=Members)
        self.label_14.setGeometry(QtCore.QRect(200, 500, 171, 16))
        self.label_14.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(parent=Members)
        self.label_15.setGeometry(QtCore.QRect(200, 530, 171, 16))
        self.label_15.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_15.setObjectName("label_15")
        self.gabfb = QtWidgets.QPushButton(parent=Members)
        self.gabfb.setGeometry(QtCore.QRect(200, 210, 41, 41))
        self.gabfb.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.gabfb.setStyleSheet("border: none;")
        self.gabfb.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/fb.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.gabfb.setIcon(icon)
        self.gabfb.setIconSize(QtCore.QSize(40, 40))
        self.gabfb.setObjectName("gabfb")
        self.gabig = QtWidgets.QPushButton(parent=Members)
        self.gabig.setGeometry(QtCore.QRect(250, 210, 41, 41))
        self.gabig.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.gabig.setStyleSheet("border: none;")
        self.gabig.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/instagram.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.gabig.setIcon(icon1)
        self.gabig.setIconSize(QtCore.QSize(40, 40))
        self.gabig.setObjectName("gabig")
        self.jeffb = QtWidgets.QPushButton(parent=Members)
        self.jeffb.setGeometry(QtCore.QRect(200, 390, 41, 41))
        self.jeffb.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.jeffb.setStyleSheet("border: none;")
        self.jeffb.setText("")
        self.jeffb.setIcon(icon)
        self.jeffb.setIconSize(QtCore.QSize(40, 40))
        self.jeffb.setObjectName("jeffb")
        self.jefig = QtWidgets.QPushButton(parent=Members)
        self.jefig.setGeometry(QtCore.QRect(250, 390, 41, 41))
        self.jefig.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.jefig.setStyleSheet("border: none;")
        self.jefig.setText("")
        self.jefig.setIcon(icon1)
        self.jefig.setIconSize(QtCore.QSize(40, 40))
        self.jefig.setObjectName("jefig")
        self.jpig = QtWidgets.QPushButton(parent=Members)
        self.jpig.setGeometry(QtCore.QRect(250, 560, 41, 41))
        self.jpig.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.jpig.setStyleSheet("border: none;")
        self.jpig.setText("")
        self.jpig.setIcon(icon1)
        self.jpig.setIconSize(QtCore.QSize(40, 40))
        self.jpig.setObjectName("jpig")
        self.jpfb = QtWidgets.QPushButton(parent=Members)
        self.jpfb.setGeometry(QtCore.QRect(200, 560, 41, 41))
        self.jpfb.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.jpfb.setStyleSheet("border: none;")
        self.jpfb.setText("")
        self.jpfb.setIcon(icon)
        self.jpfb.setIconSize(QtCore.QSize(40, 40))
        self.jpfb.setObjectName("jpfb")
        self.label_16 = QtWidgets.QLabel(parent=Members)
        self.label_16.setGeometry(QtCore.QRect(0, 260, 481, 16))
        self.label_16.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(parent=Members)
        self.label_17.setGeometry(QtCore.QRect(0, 440, 481, 16))
        self.label_17.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_17.setObjectName("label_17")

        self.retranslateUi(Members)
        QtCore.QMetaObject.connectSlotsByName(Members)

    def retranslateUi(self, Members):
        _translate = QtCore.QCoreApplication.translate
        Members.setWindowTitle(_translate("Members", "Form"))
        self.label_9.setText(_translate("Members", "MEMBERS"))
        self.back.setText(_translate("Members", "BACK"))
        self.label.setText(_translate("Members", "CONTRIBUTIONS:"))
        self.label_3.setText(_translate("Members", "CONTRIBUTIONS:"))
        self.label_4.setText(_translate("Members", "CONTRIBUTIONS:"))
        self.label_5.setText(_translate("Members", "- Documentation and Support"))
        self.label_6.setText(_translate("Members", "- Equipment Assessment"))
        self.label_8.setText(_translate("Members", "- UI Implementation"))
        self.label_13.setText(_translate("Members", "- UI Designer and Problem Maker"))
        self.label_14.setText(_translate("Members", "- Programmer"))
        self.label_15.setText(_translate("Members", "- Researcher"))
        self.label_16.setText(_translate("Members", "-------------------------------------------------------------------------------------------------------"))
        self.label_17.setText(_translate("Members", "-------------------------------------------------------------------------------------------------------"))



#-------------------------------------------------------------------------------------------------
#This is the class for the linear permutations
#-------------------------------------------------------------------------------------------------
class Ui_Linear(object):
    def setupUi(self, start):
        start.setObjectName("start")
        start.resize(367, 369)
        start.setMinimumSize(QtCore.QSize(367, 369))
        start.setMaximumSize(QtCore.QSize(367, 369))
        start.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(parent=start)
        self.label.setGeometry(QtCore.QRect(10, 10, 51, 51))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/Enverga-logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=start)
        self.label_2.setGeometry(QtCore.QRect(70, 10, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=start)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 331, 61))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.meaning = QtWidgets.QPushButton(parent=start)
        self.meaning.setGeometry(QtCore.QRect(50, 180, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        self.meaning.setFont(font)
        self.meaning.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.meaning.setStyleSheet("QPushButton{color: white;\n"
"background-color: rgb(138, 6, 9);\n"
"border:2px solid rgb(138, 6, 9);\n"
"border-radius:15px;}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: rgb(138, 6, 9);\n"
"}\n"
"")
        self.meaning.setObjectName("meaning")
        self.application = QtWidgets.QPushButton(parent=start)
        self.application.setGeometry(QtCore.QRect(50, 250, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        self.application.setFont(font)
        self.application.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.application.setStyleSheet("QPushButton{color: white;\n"
"background-color: rgb(138, 6, 9);\n"
"border:2px solid rgb(138, 6, 9);\n"
"border-radius:15px;}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: rgb(138, 6, 9);\n"
"}\n"
"")
        self.application.setObjectName("application")
        self.label_4 = QtWidgets.QLabel(parent=start)
        self.label_4.setGeometry(QtCore.QRect(10, 340, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=start)
        self.label_5.setGeometry(QtCore.QRect(80, 340, 171, 16))
        self.label_5.setStyleSheet("color: black;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=start)
        self.label_6.setGeometry(QtCore.QRect(70, 30, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(parent=start)
        self.pushButton.setGeometry(QtCore.QRect(290, 10, 75, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{color: white;\n"
"background-color: rgb(138, 6, 9);\n"
"border:2px solid rgb(138, 6, 9);}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: rgb(138, 6, 9);\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(start)
        QtCore.QMetaObject.connectSlotsByName(start)

    def retranslateUi(self, start):
        _translate = QtCore.QCoreApplication.translate
        start.setWindowTitle(_translate("start", "Linear Permutation"))
        self.label_2.setText(_translate("start", "Manuel S. Enverga University"))
        self.label_3.setText(_translate("start", "LINEAR PERMUTATION"))
        self.meaning.setText(_translate("start", "MEANING OF LINEAR PERMUTATION"))
        self.application.setText(_translate("start", "APPLICATION"))
        self.label_4.setText(_translate("start", "Created By:"))
        self.label_5.setText(_translate("start", "Martirez, Cabalsa and Alpuerto"))
        self.label_6.setText(_translate("start", "Foundation"))
        self.pushButton.setText(_translate("start", "BACK"))

class Ui_LinearMeaning(object):
    def setupUi(self, LinearMeaning):
        LinearMeaning.setObjectName("LinearMeaning")
        LinearMeaning.resize(500, 600)
        LinearMeaning.setMinimumSize(QtCore.QSize(500, 600))
        LinearMeaning.setMaximumSize(QtCore.QSize(500, 600))
        LinearMeaning.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_7 = QtWidgets.QLabel(parent=LinearMeaning)
        self.label_7.setGeometry(QtCore.QRect(90, 50, 331, 61))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.back = QtWidgets.QPushButton(parent=LinearMeaning)
        self.back.setGeometry(QtCore.QRect(410, 20, 75, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.back.setFont(font)
        self.back.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.back.setStyleSheet("QPushButton{color: white;\n"
"background-color: rgb(138, 6, 9);\n"
"border:2px solid rgb(138, 6, 9);}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: rgb(138, 6, 9);\n"
"}\n"
"")
        self.back.setObjectName("back")
        self.textBrowser = QtWidgets.QTextBrowser(parent=LinearMeaning)
        self.textBrowser.setGeometry(QtCore.QRect(30, 130, 431, 421))
        font = QtGui.QFont()
        font.setFamily("Pristina")
        font.setPointSize(20)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("border: none;\n"
"color: black;")
        self.textBrowser.setObjectName("textBrowser")
        self.label_8 = QtWidgets.QLabel(parent=LinearMeaning)
        self.label_8.setGeometry(QtCore.QRect(10, 10, 51, 51))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/icons/Enverga-logo.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label = QtWidgets.QLabel(parent=LinearMeaning)
        self.label.setGeometry(QtCore.QRect(80, 520, 341, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=LinearMeaning)
        self.label_2.setGeometry(QtCore.QRect(180, 550, 141, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_9 = QtWidgets.QLabel(parent=LinearMeaning)
        self.label_9.setGeometry(QtCore.QRect(70, 10, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_9.setFont(font)
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(":/icons/ccmslogo.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")

        self.retranslateUi(LinearMeaning)
        QtCore.QMetaObject.connectSlotsByName(LinearMeaning)

    def retranslateUi(self, LinearMeaning):
        _translate = QtCore.QCoreApplication.translate
        LinearMeaning.setWindowTitle(_translate("LinearMeaning", "Meaning of Linear Permutation"))
        self.label_7.setText(_translate("LinearMeaning", "LINEAR PERMUTATION"))
        self.back.setText(_translate("LinearMeaning", "BACK"))
        self.textBrowser.setHtml(_translate("LinearMeaning", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Pristina\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt;\">    Linear permutation refers to the arrangement of a set of items in a specific order. In mathematical terms, it often involves finding the number of ways to arrange </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-style:italic;\">n</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt;\"> distinct objects. The formula for linear permutations is </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-style:italic;\">n!</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt;\"> (n factorial), which represents the product of all positive integers up to </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-style:italic;\">n</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt;\">. For example, the linear permutations of three objects </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-style:italic;\">A, B, C</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt;\"> can be listed as </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-style:italic;\">ABC, ACB, BAC, BCA, CAB, and CBA,</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt;\"> totaling six arrangements. Linear permutations are commonly used in probability, statistics, and combinatorial problems. They are different from combinations, where the order of items does not matter. Understanding linear permutations is essential in fields such as computer science, cryptography, and operations research.</span></p></body></html>"))
        self.label.setText(_translate("LinearMeaning", "\"Mathematics is the science of patterns.\""))
        self.label_2.setText(_translate("LinearMeaning", "-William Paul Thurston"))

class Ui_LinearApplication(object):
    def setupUi(self, LinearApplication):
        LinearApplication.setObjectName("LinearApplication")
        LinearApplication.resize(543, 372)
        LinearApplication.setMinimumSize(QtCore.QSize(543, 372))
        LinearApplication.setMaximumSize(QtCore.QSize(543, 372))
        LinearApplication.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(parent=LinearApplication)
        self.label.setGeometry(QtCore.QRect(20, 70, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=LinearApplication)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 501, 221))
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.backLinear = QtWidgets.QPushButton(parent=LinearApplication)
        self.backLinear.setGeometry(QtCore.QRect(140, 290, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.backLinear.setFont(font)
        self.backLinear.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.backLinear.setStyleSheet("QPushButton{color: white;\n"
"background-color: rgb(138, 6, 9);\n"
"border:2px solid rgb(138, 6, 9);}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: rgb(138, 6, 9);\n"
"}\n"
"")
        self.backLinear.setObjectName("backLinear")
        self.label_3 = QtWidgets.QLabel(parent=LinearApplication)
        self.label_3.setGeometry(QtCore.QRect(20, 170, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=LinearApplication)
        self.label_4.setGeometry(QtCore.QRect(20, 200, 501, 51))
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.tryLinear = QtWidgets.QPushButton(parent=LinearApplication)
        self.tryLinear.setGeometry(QtCore.QRect(300, 290, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.tryLinear.setFont(font)
        self.tryLinear.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.tryLinear.setStyleSheet("QPushButton{color: white;\n"
"background-color: rgb(138, 6, 9);\n"
"border:2px solid rgb(138, 6, 9);}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: rgb(138, 6, 9);\n"
"}\n"
"")
        self.tryLinear.setObjectName("tryLinear")
        self.label_8 = QtWidgets.QLabel(parent=LinearApplication)
        self.label_8.setGeometry(QtCore.QRect(10, 10, 71, 61))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/icons/Enverga-logo.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(parent=LinearApplication)
        self.label_10.setGeometry(QtCore.QRect(480, 10, 61, 61))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap(":/icons/ccmslogo.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.label_9 = QtWidgets.QLabel(parent=LinearApplication)
        self.label_9.setGeometry(QtCore.QRect(20, 80, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_9.setObjectName("label_9")

        self.retranslateUi(LinearApplication)
        QtCore.QMetaObject.connectSlotsByName(LinearApplication)

    def retranslateUi(self, LinearApplication):
        _translate = QtCore.QCoreApplication.translate
        LinearApplication.setWindowTitle(_translate("LinearApplication", "Application of Linear Permutation"))
        self.label.setText(_translate("LinearApplication", "Real-Life Application"))
        self.label_2.setText(_translate("LinearApplication", "Classroom Seating Arrangements:\n"
"Teachers can use this tool to create random seating orders for students. \n"
"It ensures fairness and can be used to mix students for collaborative learning sessions."))
        self.backLinear.setText(_translate("LinearApplication", "Back"))
        self.label_3.setText(_translate("LinearApplication", "How to use:"))
        self.label_4.setText(_translate("LinearApplication", "1. Input student names separated by commas.\n"
"2. Click the \"Generate Arrangements\" button.\n"
"3. The tool will automatically calculate and display all possible seating arrangements. "))
        self.tryLinear.setText(_translate("LinearApplication", "Try"))
        self.label_9.setText(_translate("LinearApplication", "Real-life Application"))

class Ui_LinearSystem(object):
    def setupUi(self, LinearSystem):
        LinearSystem.setObjectName("LinearSystem")
        LinearSystem.resize(500, 570)
        LinearSystem.setMinimumSize(QtCore.QSize(500, 570))
        LinearSystem.setMaximumSize(QtCore.QSize(500, 570))
        LinearSystem.setStyleSheet("background-color: white;")
        self.label_8 = QtWidgets.QLabel(parent=LinearSystem)
        self.label_8.setGeometry(QtCore.QRect(30, 10, 71, 61))
        self.label_8.setStyleSheet("")
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/icons/Enverga-logo.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(parent=LinearSystem)
        self.label_10.setGeometry(QtCore.QRect(410, 10, 61, 61))
        self.label_10.setStyleSheet("")
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap(":/icons/ccmslogo.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.label = QtWidgets.QLabel(parent=LinearSystem)
        self.label.setGeometry(QtCore.QRect(100, 20, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.name_input = QtWidgets.QLineEdit(parent=LinearSystem)
        self.name_input.setGeometry(QtCore.QRect(60, 100, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.name_input.setFont(font)
        self.name_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: black;\n"
"border:1px solid black;\n"
"padding-left: 15px;\n"
"border-radius: 15px;")
        self.name_input.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.name_input.setObjectName("name_input")
        self.generate_button = QtWidgets.QPushButton(parent=LinearSystem)
        self.generate_button.setGeometry(QtCore.QRect(60, 170, 371, 41))
        font = QtGui.QFont()
        font.setBold(True)
        self.generate_button.setFont(font)
        self.generate_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.generate_button.setStyleSheet("QPushButton{\n"
"color: white;\n"
"background-color:#800000;\n"
"border:2px solid #800000;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: rgb(138, 6, 9);\n"
"}\n"
"")
        self.generate_button.setObjectName("generate_button")
        self.output_area = QtWidgets.QTextEdit(parent=LinearSystem)
        self.output_area.setGeometry(QtCore.QRect(70, 230, 351, 231))
        font = QtGui.QFont()
        font.setBold(True)
        self.output_area.setFont(font)
        self.output_area.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 10px;\n"
"padding: 10px;")
        self.output_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.output_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.output_area.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.output_area.setReadOnly(True)
        self.output_area.setObjectName("output_area")
        self.back = QtWidgets.QPushButton(parent=LinearSystem)
        self.back.setGeometry(QtCore.QRect(190, 480, 101, 41))
        font = QtGui.QFont()
        font.setBold(True)
        self.back.setFont(font)
        self.back.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.back.setStyleSheet("QPushButton{\n"
"color: white;\n"
"background-color:#800000;\n"
"border:2px solid #800000;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: rgb(138, 6, 9);\n"
"}\n"
"")
        self.back.setObjectName("back")

        self.retranslateUi(LinearSystem)
        QtCore.QMetaObject.connectSlotsByName(LinearSystem)

    def retranslateUi(self, LinearSystem):
        _translate = QtCore.QCoreApplication.translate
        LinearSystem.setWindowTitle(_translate("LinearSystem", "Seating Arrangement Tool"))
        self.label.setText(_translate("LinearSystem", "SEATING ARRANGEMENT \n"
"TOOL"))
        self.name_input.setPlaceholderText(_translate("LinearSystem", "Enter student names, separated by commas"))
        self.generate_button.setText(_translate("LinearSystem", "GENERATE ARRANGEMENTS"))
        self.output_area.setHtml(_translate("LinearSystem", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:700; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.back.setText(_translate("LinearSystem", "BACK"))




#-------------------------------------------------------------------------------------------------
#This is the class for the combinations
#-------------------------------------------------------------------------------------------------
class Ui_Combinations(object):
    def setupUi(self, start):
        start.setObjectName("start")
        start.resize(367, 369)
        start.setMinimumSize(QtCore.QSize(367, 369))
        start.setMaximumSize(QtCore.QSize(367, 369))
        start.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(parent=start)
        self.label.setGeometry(QtCore.QRect(10, 10, 51, 51))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/Enverga-logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=start)
        self.label_2.setGeometry(QtCore.QRect(70, 10, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=start)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 331, 61))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.meaning = QtWidgets.QPushButton(parent=start)
        self.meaning.setGeometry(QtCore.QRect(50, 180, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        self.meaning.setFont(font)
        self.meaning.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.meaning.setStyleSheet("QPushButton{color: white;\n"
"background-color: rgb(138, 6, 9);\n"
"border:2px solid rgb(138, 6, 9);\n"
"border-radius:15px;}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: rgb(138, 6, 9);\n"
"}\n"
"")
        self.meaning.setObjectName("meaning")
        self.application = QtWidgets.QPushButton(parent=start)
        self.application.setGeometry(QtCore.QRect(50, 250, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        self.application.setFont(font)
        self.application.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.application.setStyleSheet("QPushButton{color: white;\n"
"background-color: rgb(138, 6, 9);\n"
"border:2px solid rgb(138, 6, 9);\n"
"border-radius:15px;}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: rgb(138, 6, 9);\n"
"}\n"
"")
        self.application.setObjectName("application")
        self.label_4 = QtWidgets.QLabel(parent=start)
        self.label_4.setGeometry(QtCore.QRect(10, 340, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=start)
        self.label_5.setGeometry(QtCore.QRect(80, 340, 171, 16))
        self.label_5.setStyleSheet("color: black;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=start)
        self.label_6.setGeometry(QtCore.QRect(70, 30, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_6.setObjectName("label_6")
        self.back = QtWidgets.QPushButton(parent=start)
        self.back.setGeometry(QtCore.QRect(290, 10, 75, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.back.setFont(font)
        self.back.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.back.setStyleSheet("QPushButton{color: white;\n"
"background-color: rgb(138, 6, 9);\n"
"border:2px solid rgb(138, 6, 9);}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: rgb(138, 6, 9);\n"
"}\n"
"")
        self.back.setObjectName("back")

        self.retranslateUi(start)
        QtCore.QMetaObject.connectSlotsByName(start)

    def retranslateUi(self, start):
        _translate = QtCore.QCoreApplication.translate
        start.setWindowTitle(_translate("start", "Combination"))
        self.label_2.setText(_translate("start", "Manuel S. Enverga University"))
        self.label_3.setText(_translate("start", "COMBINATION"))
        self.meaning.setText(_translate("start", "MEANING OF COMBINATION"))
        self.application.setText(_translate("start", "APPLICATION"))
        self.label_4.setText(_translate("start", "Created By:"))
        self.label_5.setText(_translate("start", "Martirez, Cabalsa and Alpuerto"))
        self.label_6.setText(_translate("start", "Foundation"))
        self.back.setText(_translate("start", "BACK"))

class Ui_CombinationMean(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 600)
        Form.setMinimumSize(QtCore.QSize(500, 600))
        Form.setMaximumSize(QtCore.QSize(500, 600))
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_8 = QtWidgets.QLabel(parent=Form)
        self.label_8.setGeometry(QtCore.QRect(10, 10, 51, 51))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/icons/Enverga-logo.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=Form)
        self.label_9.setGeometry(QtCore.QRect(70, 10, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_9.setFont(font)
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(":/icons/ccmslogo.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.back = QtWidgets.QPushButton(parent=Form)
        self.back.setGeometry(QtCore.QRect(390, 20, 75, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.back.setFont(font)
        self.back.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.back.setStyleSheet("QPushButton{color: white;\n"
"background-color: rgb(138, 6, 9);\n"
"border:2px solid rgb(138, 6, 9);}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: rgb(138, 6, 9);\n"
"}\n"
"")
        self.back.setObjectName("back")
        self.label_7 = QtWidgets.QLabel(parent=Form)
        self.label_7.setGeometry(QtCore.QRect(90, 60, 331, 61))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.textBrowser = QtWidgets.QTextBrowser(parent=Form)
        self.textBrowser.setGeometry(QtCore.QRect(40, 120, 431, 421))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("border: none;\n"
"color: black;")
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(110, 510, 291, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(180, 550, 141, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(20, 530, 471, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.back.setText(_translate("Form", "BACK"))
        self.label_7.setText(_translate("Form", "COMBINATION"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:700; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:400;\">    Combinations refer to the selection of items from a larger set where the order of selection does not matter. Unlike permutations, which consider the arrangement of elements, combinations focus solely on the group itself. For example, choosing 3 fruits from a selection of 5 is a combination, as picking apples, bananas, and cherries is the same as picking cherries, apples, and bananas. The total number of combinations can be determined by considering the total items available and how many are to be selected, without worrying about their arrangement. This concept is widely used in statistics, probability, and various real-life applications, such as forming committees or selecting teams, where the order of selection is irrelevant.</span></p></body></html>"))
        self.label.setText(_translate("Form", "\"Combinatorial mathematics"))
        self.label_2.setText(_translate("Form", "-Anonymous"))
        self.label_3.setText(_translate("Form", "is a most fascinating area of study.\""))

class Ui_CombinationApplication(object):
    def setupUi(self, LinearApplication):
        LinearApplication.setObjectName("LinearApplication")
        LinearApplication.resize(543, 372)
        LinearApplication.setMinimumSize(QtCore.QSize(543, 372))
        LinearApplication.setMaximumSize(QtCore.QSize(543, 372))
        LinearApplication.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(parent=LinearApplication)
        self.label.setGeometry(QtCore.QRect(20, 70, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=LinearApplication)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 501, 221))
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.backLinear = QtWidgets.QPushButton(parent=LinearApplication)
        self.backLinear.setGeometry(QtCore.QRect(140, 310, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.backLinear.setFont(font)
        self.backLinear.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.backLinear.setStyleSheet("QPushButton{color: white;\n"
"background-color: rgb(138, 6, 9);\n"
"border:2px solid rgb(138, 6, 9);}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: rgb(138, 6, 9);\n"
"}\n"
"")
        self.backLinear.setObjectName("backLinear")
        self.label_3 = QtWidgets.QLabel(parent=LinearApplication)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=LinearApplication)
        self.label_4.setGeometry(QtCore.QRect(20, 180, 501, 101))
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.tryLinear = QtWidgets.QPushButton(parent=LinearApplication)
        self.tryLinear.setGeometry(QtCore.QRect(300, 310, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.tryLinear.setFont(font)
        self.tryLinear.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.tryLinear.setStyleSheet("QPushButton{color: white;\n"
"background-color: rgb(138, 6, 9);\n"
"border:2px solid rgb(138, 6, 9);}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: rgb(138, 6, 9);\n"
"}\n"
"")
        self.tryLinear.setObjectName("tryLinear")
        self.label_8 = QtWidgets.QLabel(parent=LinearApplication)
        self.label_8.setGeometry(QtCore.QRect(10, 10, 71, 61))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/icons/Enverga-logo.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(parent=LinearApplication)
        self.label_10.setGeometry(QtCore.QRect(480, 10, 61, 61))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap(":/icons/ccmslogo.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.label_9 = QtWidgets.QLabel(parent=LinearApplication)
        self.label_9.setGeometry(QtCore.QRect(20, 70, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_9.setObjectName("label_9")
        self.label_6 = QtWidgets.QLabel(parent=LinearApplication)
        self.label_6.setGeometry(QtCore.QRect(20, 280, 501, 16))
        self.label_6.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_6.setObjectName("label_6")

        self.retranslateUi(LinearApplication)
        QtCore.QMetaObject.connectSlotsByName(LinearApplication)

    def retranslateUi(self, LinearApplication):
        _translate = QtCore.QCoreApplication.translate
        LinearApplication.setWindowTitle(_translate("LinearApplication", "Application of Combination"))
        self.label.setText(_translate("LinearApplication", "Real-Life Application"))
        self.label_2.setText(_translate("LinearApplication", "Personalized Diet Plans:\n"
"Individuals looking to create varied meals using ingredients they enjoy or need\n"
"for their dietary goals"))
        self.backLinear.setText(_translate("LinearApplication", "Back"))
        self.label_3.setText(_translate("LinearApplication", "How to use:"))
        self.label_4.setText(_translate("LinearApplication", "1. Enter the options in each field, separated by commas.\n"
"2. Example input:\n"
"    Proteins: Chicken, Tofu\n"
"    Vegetables: Broccoli, Carrots\n"
"    Grains: Rice, Quinoa\n"
"    Fruits: Apples, Berries"))
        self.tryLinear.setText(_translate("LinearApplication", "Try"))
        self.label_9.setText(_translate("LinearApplication", "Real-life Application"))
        self.label_6.setText(_translate("LinearApplication", "3. After entering the dietary options, click the \"Generate Meal Combinations\" button."))

class Ui_CombinationSystem(object):
    def setupUi(self, CombinationSystem):
        CombinationSystem.setObjectName("CombinationSystem")
        CombinationSystem.resize(500, 700)
        CombinationSystem.setMinimumSize(QtCore.QSize(500, 700))
        CombinationSystem.setMaximumSize(QtCore.QSize(500, 700))
        CombinationSystem.setStyleSheet("background-color: white;")
        self.label_8 = QtWidgets.QLabel(parent=CombinationSystem)
        self.label_8.setGeometry(QtCore.QRect(30, 10, 71, 61))
        self.label_8.setStyleSheet("")
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/icons/Enverga-logo.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(parent=CombinationSystem)
        self.label_10.setGeometry(QtCore.QRect(410, 10, 61, 61))
        self.label_10.setStyleSheet("")
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap(":/icons/ccmslogo.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.label = QtWidgets.QLabel(parent=CombinationSystem)
        self.label.setGeometry(QtCore.QRect(100, 20, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.protein_input = QtWidgets.QLineEdit(parent=CombinationSystem)
        self.protein_input.setGeometry(QtCore.QRect(60, 100, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.protein_input.setFont(font)
        self.protein_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: black;\n"
"border:1px solid black;\n"
"padding-left: 5px;\n"
"border-radius: 15px;")
        self.protein_input.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.protein_input.setObjectName("protein_input")
        self.generate_button = QtWidgets.QPushButton(parent=CombinationSystem)
        self.generate_button.setGeometry(QtCore.QRect(60, 340, 371, 41))
        font = QtGui.QFont()
        font.setBold(True)
        self.generate_button.setFont(font)
        self.generate_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.generate_button.setStyleSheet("QPushButton{\n"
"color: white;\n"
"background-color:#800000;\n"
"border:2px solid #800000;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: rgb(138, 6, 9);\n"
"}\n"
"")
        self.generate_button.setObjectName("generate_button")
        self.output_area = QtWidgets.QTextEdit(parent=CombinationSystem)
        self.output_area.setGeometry(QtCore.QRect(70, 400, 351, 201))
        font = QtGui.QFont()
        font.setBold(True)
        self.output_area.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 10px;\n"
"padding: 10px;")
        self.output_area.setFont(font)
        self.output_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.output_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.output_area.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.output_area.setReadOnly(True)
        self.output_area.setObjectName("output_area")
        self.back = QtWidgets.QPushButton(parent=CombinationSystem)
        self.back.setGeometry(QtCore.QRect(190, 620, 101, 41))
        font = QtGui.QFont()
        font.setBold(True)
        self.back.setFont(font)
        self.back.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.back.setStyleSheet("QPushButton{\n"
"color: white;\n"
"background-color:#800000;\n"
"border:2px solid #800000;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: rgb(138, 6, 9);\n"
"}\n"
"")
        self.back.setObjectName("back")
        self.veg_input = QtWidgets.QLineEdit(parent=CombinationSystem)
        self.veg_input.setGeometry(QtCore.QRect(60, 160, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.veg_input.setFont(font)
        self.veg_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: black;\n"
"border:1px solid black;\n"
"padding-left: 5px;\n"
"border-radius: 15px;")
        self.veg_input.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.veg_input.setObjectName("veg_input")
        self.grain_input = QtWidgets.QLineEdit(parent=CombinationSystem)
        self.grain_input.setGeometry(QtCore.QRect(60, 220, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.grain_input.setFont(font)
        self.grain_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: black;\n"
"border:1px solid black;\n"
"padding-left: 5px;\n"
"border-radius: 15px;")
        self.grain_input.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.grain_input.setObjectName("grain_input")
        self.fruit_input = QtWidgets.QLineEdit(parent=CombinationSystem)
        self.fruit_input.setGeometry(QtCore.QRect(60, 280, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.fruit_input.setFont(font)
        self.fruit_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: black;\n"
"border:1px solid black;\n"
"padding-left: 5px;\n"
"border-radius: 15px;")
        self.fruit_input.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.fruit_input.setObjectName("fruit_input")

        self.retranslateUi(CombinationSystem)
        QtCore.QMetaObject.connectSlotsByName(CombinationSystem)

    def retranslateUi(self, CombinationSystem):
        _translate = QtCore.QCoreApplication.translate
        CombinationSystem.setWindowTitle(_translate("CombinationSystem", "Combination"))
        self.label.setText(_translate("CombinationSystem", "PERSONALIZED DIET PLAN"))
        self.protein_input.setPlaceholderText(_translate("CombinationSystem", "Enter protein options, separated by commas (e.g., Chicken, Tofu)"))
        self.generate_button.setText(_translate("CombinationSystem", "GENERATE MEAL COMBINATIONS"))
        self.back.setText(_translate("CombinationSystem", "BACK"))
        self.veg_input.setPlaceholderText(_translate("CombinationSystem", "Enter vegetable options, separated by commas (e.g., Broccoli, etc)"))
        self.grain_input.setPlaceholderText(_translate("CombinationSystem", "Enter grain options, separated by commas (e.g., Rice, Quinoa)"))
        self.fruit_input.setPlaceholderText(_translate("CombinationSystem", "Enter fruit options, separated by commas (e.g., Apples, Berries)"))




#-------------------------------------------------------------------------------------------------
#This is the class for circular permutation
#-------------------------------------------------------------------------------------------------
class Ui_Circular(object):
    def setupUi(self, start):
        start.setObjectName("start")
        start.resize(367, 369)
        start.setMinimumSize(QtCore.QSize(367, 369))
        start.setMaximumSize(QtCore.QSize(367, 369))
        start.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(parent=start)
        self.label.setGeometry(QtCore.QRect(10, 10, 51, 51))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/Enverga-logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=start)
        self.label_2.setGeometry(QtCore.QRect(70, 10, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=start)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 331, 61))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.meaning = QtWidgets.QPushButton(parent=start)
        self.meaning.setGeometry(QtCore.QRect(50, 180, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        self.meaning.setFont(font)
        self.meaning.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.meaning.setStyleSheet("QPushButton{color: white;\n"
"background-color: rgb(138, 6, 9);\n"
"border:2px solid rgb(138, 6, 9);\n"
"border-radius:15px;}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: rgb(138, 6, 9);\n"
"}\n"
"")
        self.meaning.setObjectName("meaning")
        self.application = QtWidgets.QPushButton(parent=start)
        self.application.setGeometry(QtCore.QRect(50, 250, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        self.application.setFont(font)
        self.application.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.application.setStyleSheet("QPushButton{color: white;\n"
"background-color: rgb(138, 6, 9);\n"
"border:2px solid rgb(138, 6, 9);\n"
"border-radius:15px;}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: rgb(138, 6, 9);\n"
"}\n"
"")
        self.application.setObjectName("application")
        self.label_4 = QtWidgets.QLabel(parent=start)
        self.label_4.setGeometry(QtCore.QRect(10, 340, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=start)
        self.label_5.setGeometry(QtCore.QRect(80, 340, 171, 16))
        self.label_5.setStyleSheet("color: black;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=start)
        self.label_6.setGeometry(QtCore.QRect(70, 30, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_6.setObjectName("label_6")
        self.back = QtWidgets.QPushButton(parent=start)
        self.back.setGeometry(QtCore.QRect(290, 10, 75, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.back.setFont(font)
        self.back.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.back.setStyleSheet("QPushButton{color: white;\n"
"background-color: rgb(138, 6, 9);\n"
"border:2px solid rgb(138, 6, 9);}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: rgb(138, 6, 9);\n"
"}\n"
"")
        self.back.setObjectName("back")

        self.retranslateUi(start)
        QtCore.QMetaObject.connectSlotsByName(start)

    def retranslateUi(self, start):
        _translate = QtCore.QCoreApplication.translate
        start.setWindowTitle(_translate("start", "Circular Permutation"))
        self.label_2.setText(_translate("start", "Manuel S. Enverga University"))
        self.label_3.setText(_translate("start", "CIRCULAR PERMUTATION"))
        self.meaning.setText(_translate("start", "MEANING OF CIRCULAR PERMUTATION"))
        self.application.setText(_translate("start", "APPLICATION"))
        self.label_4.setText(_translate("start", "Created By:"))
        self.label_5.setText(_translate("start", "Martirez, Cabalsa and Alpuerto"))
        self.label_6.setText(_translate("start", "Foundation"))
        self.back.setText(_translate("start", "BACK"))
        
class Ui_CircularMean(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 600)
        Form.setMinimumSize(QtCore.QSize(500, 600))
        Form.setMaximumSize(QtCore.QSize(500, 600))
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_7 = QtWidgets.QLabel(parent=Form)
        self.label_7.setGeometry(QtCore.QRect(80, 60, 331, 61))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=Form)
        self.label_8.setGeometry(QtCore.QRect(10, 10, 51, 51))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/icons/Enverga-logo.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=Form)
        self.label_9.setGeometry(QtCore.QRect(70, 10, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_9.setFont(font)
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(":/icons/ccmslogo.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.back = QtWidgets.QPushButton(parent=Form)
        self.back.setGeometry(QtCore.QRect(390, 20, 75, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.back.setFont(font)
        self.back.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.back.setStyleSheet("QPushButton{color: white;\n"
"background-color: rgb(138, 6, 9);\n"
"border:2px solid rgb(138, 6, 9);}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: rgb(138, 6, 9);\n"
"}\n"
"")
        self.back.setObjectName("back")
        self.textBrowser = QtWidgets.QTextBrowser(parent=Form)
        self.textBrowser.setGeometry(QtCore.QRect(40, 130, 431, 421))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(True)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("border: none;\n"
"color: black;")
        self.textBrowser.setObjectName("textBrowser")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(40, 500, 431, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(180, 530, 141, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_7.setText(_translate("Form", "CIRCULAR PERMUTATION"))
        self.back.setText(_translate("Form", "BACK"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:700; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:400;\">    Circular permutations refer to the arrangements of objects in a circular format, where the order matters but rotations of the same arrangement are considered identical. Unlike linear permutations, where each arrangement is unique, circular permutations treat configurations that can be rotated into one another as the same. The formula for calculating circular permutations of nnn distinct objects is </span><span style=\" font-size:14pt; font-weight:400; font-style:italic;\">(n−1)!</span><span style=\" font-size:14pt; font-weight:400;\">, since one object can be fixed to eliminate duplicates. This concept is useful in various fields, including combinatorics and probability, especially for problems like seating arrangements at round tables. Overall, circular permutations highlight the importance of relative positioning in a closed loop.</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "\"Everything in the universe is arranged in a circular pattern.\""))
        self.label_2.setText(_translate("Form", "-Anonymous"))

class Ui_CircularApplication(object):
    def setupUi(self, LinearApplication):
        LinearApplication.setObjectName("LinearApplication")
        LinearApplication.resize(543, 372)
        LinearApplication.setMinimumSize(QtCore.QSize(543, 372))
        LinearApplication.setMaximumSize(QtCore.QSize(543, 372))
        LinearApplication.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(parent=LinearApplication)
        self.label.setGeometry(QtCore.QRect(20, 70, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=LinearApplication)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 501, 221))
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.backCircular = QtWidgets.QPushButton(parent=LinearApplication)
        self.backCircular.setGeometry(QtCore.QRect(140, 290, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.backCircular.setFont(font)
        self.backCircular.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.backCircular.setStyleSheet("QPushButton{color: white;\n"
"background-color: rgb(138, 6, 9);\n"
"border:2px solid rgb(138, 6, 9);}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: rgb(138, 6, 9);\n"
"}\n"
"")
        self.backCircular.setObjectName("backCircular")
        self.label_3 = QtWidgets.QLabel(parent=LinearApplication)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=LinearApplication)
        self.label_4.setGeometry(QtCore.QRect(20, 180, 501, 101))
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.tryCircular = QtWidgets.QPushButton(parent=LinearApplication)
        self.tryCircular.setGeometry(QtCore.QRect(300, 290, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.tryCircular.setFont(font)
        self.tryCircular.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.tryCircular.setStyleSheet("QPushButton{color: white;\n"
"background-color: rgb(138, 6, 9);\n"
"border:2px solid rgb(138, 6, 9);}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: rgb(138, 6, 9);\n"
"}\n"
"")
        self.tryCircular.setObjectName("tryCircular")
        self.label_8 = QtWidgets.QLabel(parent=LinearApplication)
        self.label_8.setGeometry(QtCore.QRect(10, 10, 71, 61))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/icons/Enverga-logo.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(parent=LinearApplication)
        self.label_10.setGeometry(QtCore.QRect(480, 10, 61, 61))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap(":/icons/ccmslogo.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.label_9 = QtWidgets.QLabel(parent=LinearApplication)
        self.label_9.setGeometry(QtCore.QRect(20, 70, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_9.setObjectName("label_9")

        self.retranslateUi(LinearApplication)
        QtCore.QMetaObject.connectSlotsByName(LinearApplication)

    def retranslateUi(self, LinearApplication):
        _translate = QtCore.QCoreApplication.translate
        LinearApplication.setWindowTitle(_translate("LinearApplication", "Application of Circular Permutation"))
        self.label.setText(_translate("LinearApplication", "Real-Life Application"))
        self.label_2.setText(_translate("LinearApplication", "Dance Planning & Choreography:\n"
"Useful for dance instructors or choreographers organizing circular group formations."))
        self.backCircular.setText(_translate("LinearApplication", "Back"))
        self.label_3.setText(_translate("LinearApplication", "How to use:"))
        self.label_4.setText(_translate("LinearApplication", "1. Enter the names of the dancers separated by commas.\n"
"2. Click the \"Generate Arrangements\" button.\n"
"3. The tool will display all possible circular permutations of the dancers.\n"
"    Each arrangement starts with the first dancer as fixed, and the rest are arranged\n"
"    in different orders around them. "))
        self.tryCircular.setText(_translate("LinearApplication", "Try"))
        self.label_9.setText(_translate("LinearApplication", "Real-life Application"))

class Ui_CircularSystem(object):
    def setupUi(self, CIrcularSystem):
        CIrcularSystem.setObjectName("CIrcularSystem")
        CIrcularSystem.resize(500, 570)
        CIrcularSystem.setMinimumSize(QtCore.QSize(500, 570))
        CIrcularSystem.setMaximumSize(QtCore.QSize(500, 570))
        CIrcularSystem.setStyleSheet("background-color: white;")
        self.label_8 = QtWidgets.QLabel(parent=CIrcularSystem)
        self.label_8.setGeometry(QtCore.QRect(30, 10, 71, 61))
        self.label_8.setStyleSheet("")
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/icons/Enverga-logo.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(parent=CIrcularSystem)
        self.label_10.setGeometry(QtCore.QRect(410, 10, 61, 61))
        self.label_10.setStyleSheet("")
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap(":/icons/ccmslogo.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.label = QtWidgets.QLabel(parent=CIrcularSystem)
        self.label.setGeometry(QtCore.QRect(100, 20, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.name_input = QtWidgets.QLineEdit(parent=CIrcularSystem)
        self.name_input.setGeometry(QtCore.QRect(60, 100, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.name_input.setFont(font)
        self.name_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: black;\n"
"border:1px solid black;\n"
"padding-left: 15px;\n"
"border-radius: 15px;")
        self.name_input.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.name_input.setObjectName("name_input")
        self.generate_button = QtWidgets.QPushButton(parent=CIrcularSystem)
        self.generate_button.setGeometry(QtCore.QRect(60, 170, 371, 41))
        font = QtGui.QFont()
        font.setBold(True)
        self.generate_button.setFont(font)
        self.generate_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.generate_button.setStyleSheet("QPushButton{\n"
"color: white;\n"
"background-color:#800000;\n"
"border:2px solid #800000;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: rgb(138, 6, 9);\n"
"}\n"
"")
        self.generate_button.setObjectName("generate_button")
        self.output_area = QtWidgets.QTextEdit(parent=CIrcularSystem)
        self.output_area.setGeometry(QtCore.QRect(70, 230, 351, 231))
        font = QtGui.QFont()
        font.setBold(True)
        self.output_area.setFont(font)
        self.output_area.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 10px;\n"
"padding: 10px;")
        self.output_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.output_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.output_area.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.output_area.setReadOnly(True)
        self.output_area.setObjectName("output_area")
        self.back = QtWidgets.QPushButton(parent=CIrcularSystem)
        self.back.setGeometry(QtCore.QRect(190, 480, 101, 41))
        font = QtGui.QFont()
        font.setBold(True)
        self.back.setFont(font)
        self.back.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.back.setStyleSheet("QPushButton{\n"
"color: white;\n"
"background-color:#800000;\n"
"border:2px solid #800000;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: rgb(138, 6, 9);\n"
"}\n"
"")
        self.back.setObjectName("back")

        self.retranslateUi(CIrcularSystem)
        QtCore.QMetaObject.connectSlotsByName(CIrcularSystem)

    def retranslateUi(self, CIrcularSystem):
        _translate = QtCore.QCoreApplication.translate
        CIrcularSystem.setWindowTitle(_translate("CIrcularSystem", "Circular Formation System"))
        self.label.setText(_translate("CIrcularSystem", "CIRCULAR DANCE FORMATION \n"
"SYSTEM"))
        self.name_input.setPlaceholderText(_translate("CIrcularSystem", "Enter dancer names, separated by commas"))
        self.generate_button.setText(_translate("CIrcularSystem", "GENERATE ARRANGEMENTS"))
        self.output_area.setHtml(_translate("CIrcularSystem", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:700; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.back.setText(_translate("CIrcularSystem", "BACK"))


#-------------------------------------------------------------------------------------------------
#This is the class for truncated permutations
#-------------------------------------------------------------------------------------------------     
class Ui_Truncated(object):
    def setupUi(self, start):
        start.setObjectName("start")
        start.resize(367, 369)
        start.setMinimumSize(QtCore.QSize(367, 369))
        start.setMaximumSize(QtCore.QSize(367, 369))
        start.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(parent=start)
        self.label.setGeometry(QtCore.QRect(10, 10, 51, 51))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/Enverga-logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=start)
        self.label_2.setGeometry(QtCore.QRect(70, 10, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=start)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 331, 61))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.meaning = QtWidgets.QPushButton(parent=start)
        self.meaning.setGeometry(QtCore.QRect(50, 180, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        self.meaning.setFont(font)
        self.meaning.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.meaning.setStyleSheet("QPushButton{color: white;\n"
"background-color: rgb(138, 6, 9);\n"
"border:2px solid rgb(138, 6, 9);\n"
"border-radius:15px;}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: rgb(138, 6, 9);\n"
"}\n"
"")
        self.meaning.setObjectName("meaning")
        self.application = QtWidgets.QPushButton(parent=start)
        self.application.setGeometry(QtCore.QRect(50, 250, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        self.application.setFont(font)
        self.application.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.application.setStyleSheet("QPushButton{color: white;\n"
"background-color: rgb(138, 6, 9);\n"
"border:2px solid rgb(138, 6, 9);\n"
"border-radius:15px;}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: rgb(138, 6, 9);\n"
"}\n"
"")
        self.application.setObjectName("application")
        self.label_4 = QtWidgets.QLabel(parent=start)
        self.label_4.setGeometry(QtCore.QRect(10, 340, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=start)
        self.label_5.setGeometry(QtCore.QRect(80, 340, 171, 16))
        self.label_5.setStyleSheet("color: black;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=start)
        self.label_6.setGeometry(QtCore.QRect(70, 30, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_6.setObjectName("label_6")
        self.back = QtWidgets.QPushButton(parent=start)
        self.back.setGeometry(QtCore.QRect(290, 10, 75, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.back.setFont(font)
        self.back.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.back.setStyleSheet("QPushButton{color: white;\n"
"background-color: rgb(138, 6, 9);\n"
"border:2px solid rgb(138, 6, 9);}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: rgb(138, 6, 9);\n"
"}\n"
"")
        self.back.setObjectName("back")

        self.retranslateUi(start)
        QtCore.QMetaObject.connectSlotsByName(start)

    def retranslateUi(self, start):
        _translate = QtCore.QCoreApplication.translate
        start.setWindowTitle(_translate("start", "Truncated"))
        self.label_2.setText(_translate("start", "Manuel S. Enverga University"))
        self.label_3.setText(_translate("start", "PERMUTATION WITH TRUNCATED \n"
"ELEMENTS"))
        self.meaning.setText(_translate("start", "MEANING OF PERMUTATION \n"
"WITH TRUNCATED ELEMENTS"))
        self.application.setText(_translate("start", "APPLICATION"))
        self.label_4.setText(_translate("start", "Created By:"))
        self.label_5.setText(_translate("start", "Martirez, Cabalsa and Alpuerto"))
        self.label_6.setText(_translate("start", "Foundation"))
        self.back.setText(_translate("start", "BACK"))

class Ui_TruncatedMeaning(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 600)
        Form.setMinimumSize(QtCore.QSize(500, 600))
        Form.setMaximumSize(QtCore.QSize(500, 600))
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_8 = QtWidgets.QLabel(parent=Form)
        self.label_8.setGeometry(QtCore.QRect(10, 10, 51, 51))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/icons/Enverga-logo.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=Form)
        self.label_9.setGeometry(QtCore.QRect(70, 10, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_9.setFont(font)
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(":/icons/ccmslogo.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.back = QtWidgets.QPushButton(parent=Form)
        self.back.setGeometry(QtCore.QRect(400, 20, 75, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.back.setFont(font)
        self.back.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.back.setStyleSheet("QPushButton{color: white;\n"
"background-color: rgb(138, 6, 9);\n"
"border:2px solid rgb(138, 6, 9);}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: rgb(138, 6, 9);\n"
"}\n"
"")
        self.back.setObjectName("back")
        self.label_7 = QtWidgets.QLabel(parent=Form)
        self.label_7.setGeometry(QtCore.QRect(80, 70, 331, 61))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.textBrowser = QtWidgets.QTextBrowser(parent=Form)
        self.textBrowser.setGeometry(QtCore.QRect(30, 160, 431, 421))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("border: none;\n"
"color: black;")
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(10, 490, 481, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(170, 510, 141, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.back.setText(_translate("Form", "BACK"))
        self.label_7.setText(_translate("Form", "PERMUTATIONS WITH TRUNCATED \n"
"ELEMENTS"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt;\">    In discrete mathematics, &quot;truncated&quot; refers to the process of shortening a set, sequence, or mathematical object by removing elements from the end. This can apply to sequences where only a finite portion is considered, effectively discarding the later terms. For example, a truncated sequence might take the first five terms of an infinite series. Truncation is also used in combinations to limit the selection from a larger set, focusing on a specific subset of elements. Overall, truncation simplifies computations and analyses by narrowing the scope to a more manageable size.</span></p></body></html>"))
        self.label.setText(_translate("Form", "\"To be a mathematician is to be willing to put oneself on the line.\""))
        self.label_2.setText(_translate("Form", "-Anonymous"))

class Ui_TruncatedApplication(object):
    def setupUi(self, TruncatedApplication):
        TruncatedApplication.setObjectName("TruncatedApplication")
        TruncatedApplication.resize(543, 372)
        TruncatedApplication.setMinimumSize(QtCore.QSize(543, 372))
        TruncatedApplication.setMaximumSize(QtCore.QSize(543, 372))
        TruncatedApplication.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(parent=TruncatedApplication)
        self.label.setGeometry(QtCore.QRect(20, 80, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=TruncatedApplication)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 501, 71))
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.backTruncated = QtWidgets.QPushButton(parent=TruncatedApplication)
        self.backTruncated.setGeometry(QtCore.QRect(140, 290, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.backTruncated.setFont(font)
        self.backTruncated.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.backTruncated.setStyleSheet("QPushButton{color: white;\n"
"background-color: rgb(138, 6, 9);\n"
"border:2px solid rgb(138, 6, 9);}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: rgb(138, 6, 9);\n"
"}\n"
"")
        self.backTruncated.setObjectName("backTruncated")
        self.label_3 = QtWidgets.QLabel(parent=TruncatedApplication)
        self.label_3.setGeometry(QtCore.QRect(20, 180, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.tryTruncated = QtWidgets.QPushButton(parent=TruncatedApplication)
        self.tryTruncated.setGeometry(QtCore.QRect(300, 290, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.tryTruncated.setFont(font)
        self.tryTruncated.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.tryTruncated.setStyleSheet("QPushButton{color: white;\n"
"background-color: rgb(138, 6, 9);\n"
"border:2px solid rgb(138, 6, 9);}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: rgb(138, 6, 9);\n"
"}\n"
"")
        self.tryTruncated.setObjectName("tryTruncated")
        self.label_8 = QtWidgets.QLabel(parent=TruncatedApplication)
        self.label_8.setGeometry(QtCore.QRect(10, 10, 71, 61))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/icons/Enverga-logo.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(parent=TruncatedApplication)
        self.label_10.setGeometry(QtCore.QRect(480, 10, 61, 61))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap(":/icons/ccmslogo.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.label_9 = QtWidgets.QLabel(parent=TruncatedApplication)
        self.label_9.setGeometry(QtCore.QRect(20, 200, 471, 21))
        self.label_9.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(parent=TruncatedApplication)
        self.label_11.setGeometry(QtCore.QRect(20, 220, 571, 16))
        self.label_11.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(parent=TruncatedApplication)
        self.label_12.setGeometry(QtCore.QRect(20, 240, 491, 31))
        self.label_12.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_12.setObjectName("label_12")

        self.retranslateUi(TruncatedApplication)
        QtCore.QMetaObject.connectSlotsByName(TruncatedApplication)

    def retranslateUi(self, TruncatedApplication):
        _translate = QtCore.QCoreApplication.translate
        TruncatedApplication.setWindowTitle(_translate("TruncatedApplication", "Application of Truncated Permutation"))
        self.label.setText(_translate("TruncatedApplication", "Real-Life Application"))
        self.label_2.setText(_translate("TruncatedApplication", "Assigning volunteers during search and rescue mission to three critical roles: \n"
"1. First Aid Responder\n"
"2.Search Operations Specialist\n"
"3.Supply Delivery Coordinator"))
        self.backTruncated.setText(_translate("TruncatedApplication", "Back"))
        self.label_3.setText(_translate("TruncatedApplication", "How to use:"))
        self.tryTruncated.setText(_translate("TruncatedApplication", "Try"))
        self.label_9.setText(_translate("TruncatedApplication", "1. Enter the names of the volunteers in the input field, separated by commas."))
        self.label_11.setText(_translate("TruncatedApplication", "2. Click the \"Generate Task Assignments\" button."))
        self.label_12.setText(_translate("TruncatedApplication", "3. The tool will display all possible task assignments for the specified volunteers\n"
"    (with at least 3 volunteers), along with the total number of permutations."))

class Ui_TruncatedSystem(object):
        def setupUi(self, Truncated):
                Truncated.setObjectName("Truncated")
                Truncated.resize(500, 700)
                Truncated.setMinimumSize(QtCore.QSize(500, 700))
                Truncated.setMaximumSize(QtCore.QSize(500, 700))
                Truncated.setStyleSheet("background-color: white;")
                self.label_8 = QtWidgets.QLabel(parent=Truncated)
                self.label_8.setGeometry(QtCore.QRect(30, 10, 71, 61))
                self.label_8.setStyleSheet("")
                self.label_8.setText("")
                self.label_8.setPixmap(QtGui.QPixmap(":/icons/Enverga-logo.png"))
                self.label_8.setScaledContents(True)
                self.label_8.setObjectName("label_8")
                self.label_10 = QtWidgets.QLabel(parent=Truncated)
                self.label_10.setGeometry(QtCore.QRect(410, 10, 61, 61))
                self.label_10.setStyleSheet("")
                self.label_10.setText("")
                self.label_10.setPixmap(QtGui.QPixmap(":/icons/ccmslogo.png"))
                self.label_10.setScaledContents(True)
                self.label_10.setObjectName("label_10")
                self.label = QtWidgets.QLabel(parent=Truncated)
                self.label.setGeometry(QtCore.QRect(100, 20, 301, 41))
                font = QtGui.QFont()
                font.setPointSize(11)
                font.setBold(True)
                self.label.setFont(font)
                self.label.setStyleSheet("color: rgb(0, 0, 0);")
                self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.label.setObjectName("label")
                self.volunteer_input = QtWidgets.QLineEdit(parent=Truncated)
                self.volunteer_input.setGeometry(QtCore.QRect(60, 100, 371, 51))
                font = QtGui.QFont()
                font.setPointSize(8)
                font.setBold(True)
                self.volunteer_input.setFont(font)
                self.volunteer_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "color: black;\n"
        "border:1px solid black;\n"
        "padding: 0px auto;\n"
        "border-radius: 15px;")
                self.volunteer_input.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
                self.volunteer_input.setObjectName("volunteer_input")
                self.generate_button = QtWidgets.QPushButton(parent=Truncated)
                self.generate_button.setGeometry(QtCore.QRect(120, 170, 251, 41))
                font = QtGui.QFont()
                font.setBold(True)
                self.generate_button.setFont(font)
                self.generate_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
                self.generate_button.setStyleSheet("QPushButton{\n"
        "color: white;\n"
        "background-color:#800000;\n"
        "border:2px solid #800000;\n"
        "border-radius: 8px;\n"
        "}\n"
        "\n"
        "QPushButton::hover {\n"
        "    background-color: white;\n"
        "    color: rgb(138, 6, 9);\n"
        "}\n"
        "")
                
                self.generate_button.setObjectName("generate_button")
                self.generate_button.clicked.connect(self.generate_task_assignments)
                self.output_area = QtWidgets.QTextEdit(parent=Truncated)
                self.output_area.setGeometry(QtCore.QRect(70, 270, 351, 331))
                self.output_area.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "color: black;\n"
        "border: 1px solid black;\n"
        "border-radius: 10px;\n"
        "padding: 10px;")
                self.output_area.setFont(font)
                self.output_area.setReadOnly(True)
                self.output_area.setObjectName("output_area")
                self.label_2 = QtWidgets.QLabel(parent=Truncated)
                self.label_2.setGeometry(QtCore.QRect(160, 250, 161, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                self.label_2.setFont(font)
                self.label_2.setStyleSheet("color: rgb(0, 0, 0);")
                self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.label_2.setObjectName("label_2")
                self.back = QtWidgets.QPushButton(parent=Truncated)
                self.back.setGeometry(QtCore.QRect(190, 620, 101, 41))
                font = QtGui.QFont()
                font.setBold(True)
                self.back.setFont(font)
                self.back.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
                self.back.setStyleSheet("QPushButton{\n"
        "color: white;\n"
        "background-color:#800000;\n"
        "border:2px solid #800000;\n"
        "border-radius: 8px;\n"
        "}\n"
        "\n"
        "QPushButton::hover {\n"
        "    background-color: white;\n"
        "    color: rgb(138, 6, 9);\n"
        "}\n"
        "")
                self.back.setObjectName("back")

                self.retranslateUi(Truncated)
                QtCore.QMetaObject.connectSlotsByName(Truncated)

        def retranslateUi(self, Truncated):
                _translate = QtCore.QCoreApplication.translate
                Truncated.setWindowTitle(_translate("Truncated", "Permutation With Truncated Elements"))
                self.label.setText(_translate("Truncated", "SEARCH AND RESCUE MISSION \n"
        "COORDINATOR"))
                self.volunteer_input.setPlaceholderText(_translate("Truncated", "Enter the names of volunteers separated by commas"))
                self.generate_button.setText(_translate("Truncated", "GENERATE TASK ASSIGNMENTS"))
                self.label_2.setText(_translate("Truncated", "Possible Workers Tasks:"))
                self.back.setText(_translate("Truncated", "BACK"))

        
#-------------------------------------------------------------------------------------------------
#This is the class for repeated permutations
#-------------------------------------------------------------------------------------------------   
class Ui_Repeated(object):
    def setupUi(self, start):
        start.setObjectName("start")
        start.resize(367, 369)
        start.setMinimumSize(QtCore.QSize(367, 369))
        start.setMaximumSize(QtCore.QSize(367, 369))
        start.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(parent=start)
        self.label.setGeometry(QtCore.QRect(10, 10, 51, 51))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/Enverga-logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=start)
        self.label_2.setGeometry(QtCore.QRect(70, 10, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=start)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 331, 61))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.meaning = QtWidgets.QPushButton(parent=start)
        self.meaning.setGeometry(QtCore.QRect(50, 180, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        self.meaning.setFont(font)
        self.meaning.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.meaning.setStyleSheet("QPushButton{color: white;\n"
"background-color: rgb(138, 6, 9);\n"
"border:2px solid rgb(138, 6, 9);\n"
"border-radius:15px;}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: rgb(138, 6, 9);\n"
"}\n"
"")
        self.meaning.setObjectName("meaning")
        self.application = QtWidgets.QPushButton(parent=start)
        self.application.setGeometry(QtCore.QRect(50, 250, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        self.application.setFont(font)
        self.application.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.application.setStyleSheet("QPushButton{color: white;\n"
"background-color: rgb(138, 6, 9);\n"
"border:2px solid rgb(138, 6, 9);\n"
"border-radius:15px;}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: rgb(138, 6, 9);\n"
"}\n"
"")
        self.application.setObjectName("application")
        self.label_4 = QtWidgets.QLabel(parent=start)
        self.label_4.setGeometry(QtCore.QRect(10, 340, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=start)
        self.label_5.setGeometry(QtCore.QRect(80, 340, 171, 16))
        self.label_5.setStyleSheet("color: black;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=start)
        self.label_6.setGeometry(QtCore.QRect(70, 30, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_6.setObjectName("label_6")
        self.back = QtWidgets.QPushButton(parent=start)
        self.back.setGeometry(QtCore.QRect(290, 10, 75, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.back.setFont(font)
        self.back.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.back.setStyleSheet("QPushButton{color: white;\n"
"background-color: rgb(138, 6, 9);\n"
"border:2px solid rgb(138, 6, 9);}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: rgb(138, 6, 9);\n"
"}\n"
"")
        self.back.setObjectName("back")

        self.retranslateUi(start)
        QtCore.QMetaObject.connectSlotsByName(start)

    def retranslateUi(self, start):
        _translate = QtCore.QCoreApplication.translate
        start.setWindowTitle(_translate("start", "Repeated Permutation"))
        self.label_2.setText(_translate("start", "Manuel S. Enverga University"))
        self.label_3.setText(_translate("start", "PERMUTATIONS WITH REPEATED \n"
"ELEMENTS"))
        self.meaning.setText(_translate("start", "MEANING OF PERMUTATIONS WITH \n"
"REPEATED ELEMENTS"))
        self.application.setText(_translate("start", "APPLICATION"))
        self.label_4.setText(_translate("start", "Created By:"))
        self.label_5.setText(_translate("start", "Martirez, Cabalsa and Alpuerto"))
        self.label_6.setText(_translate("start", "Foundation"))
        self.back.setText(_translate("start", "BACK"))

class Ui_RepMeaning(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 600)
        Form.setMinimumSize(QtCore.QSize(500, 600))
        Form.setMaximumSize(QtCore.QSize(500, 600))
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_8 = QtWidgets.QLabel(parent=Form)
        self.label_8.setGeometry(QtCore.QRect(10, 10, 51, 51))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/icons/Enverga-logo.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=Form)
        self.label_9.setGeometry(QtCore.QRect(70, 10, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_9.setFont(font)
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(":/icons/ccmslogo.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.back = QtWidgets.QPushButton(parent=Form)
        self.back.setGeometry(QtCore.QRect(410, 20, 75, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.back.setFont(font)
        self.back.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.back.setStyleSheet("QPushButton{color: white;\n"
"background-color: rgb(138, 6, 9);\n"
"border:2px solid rgb(138, 6, 9);}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: rgb(138, 6, 9);\n"
"}\n"
"")
        self.back.setObjectName("back")
        self.label_7 = QtWidgets.QLabel(parent=Form)
        self.label_7.setGeometry(QtCore.QRect(10, 70, 481, 61))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.textBrowser = QtWidgets.QTextBrowser(parent=Form)
        self.textBrowser.setGeometry(QtCore.QRect(30, 130, 431, 421))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("border: none;\n"
"color: black;")
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(30, 520, 431, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(170, 560, 141, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(30, 540, 431, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.back.setText(_translate("Form", "BACK"))
        self.label_7.setText(_translate("Form", "PERMUTATIONS WITH REPEATED ELEMENTS"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:700; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:400;\">    Permutations with repeating elements involve arranging items where some elements are identical, which limits the number of unique arrangements. When calculating these permutations, the focus is on how many ways we can order a set of items, considering that identical items cannot be distinguished from one another. For instance, in the word &quot;apple,&quot; the letters \'p\' repeat, meaning some arrangements will look the same. To find the total number of distinct permutations, we consider the total number of items and account for the repetitions by simply adjusting our counting method. This concept is essential in combinatorics, as it helps determine possible configurations in situations where duplication exists among the elements.</span></p></body></html>"))
        self.label.setText(_translate("Form", "\"Mathematics is the art of giving "))
        self.label_2.setText(_translate("Form", "-Henri Poincaré"))
        self.label_3.setText(_translate("Form", " the same name to different things.\""))

class Ui_RepApp(object):
    def setupUi(self, RepeatedApplication):
        RepeatedApplication.setObjectName("RepeatedApplication")
        RepeatedApplication.resize(543, 372)
        RepeatedApplication.setMinimumSize(QtCore.QSize(543, 372))
        RepeatedApplication.setMaximumSize(QtCore.QSize(543, 372))
        RepeatedApplication.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_7 = QtWidgets.QLabel(parent=RepeatedApplication)
        self.label_7.setGeometry(QtCore.QRect(70, 10, 51, 41))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("../Downloads/461167316_888636739426595_2882253921330181362_n.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.backRepeated = QtWidgets.QPushButton(parent=RepeatedApplication)
        self.backRepeated.setGeometry(QtCore.QRect(100, 290, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.backRepeated.setFont(font)
        self.backRepeated.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.backRepeated.setStyleSheet("QPushButton{color: white;\n"
"background-color: rgb(138, 6, 9);\n"
"border:2px solid rgb(138, 6, 9);}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: rgb(138, 6, 9);\n"
"}\n"
"")
        self.backRepeated.setObjectName("backRepeated")
        self.tryRepeated = QtWidgets.QPushButton(parent=RepeatedApplication)
        self.tryRepeated.setGeometry(QtCore.QRect(320, 290, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.tryRepeated.setFont(font)
        self.tryRepeated.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.tryRepeated.setStyleSheet("QPushButton{color: white;\n"
"background-color: rgb(138, 6, 9);\n"
"border:2px solid rgb(138, 6, 9);}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: rgb(138, 6, 9);\n"
"}\n"
"")
        self.tryRepeated.setObjectName("tryRepeated")
        self.label_3 = QtWidgets.QLabel(parent=RepeatedApplication)
        self.label_3.setGeometry(QtCore.QRect(20, 70, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(parent=RepeatedApplication)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 501, 241))
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(parent=RepeatedApplication)
        self.label_4.setGeometry(QtCore.QRect(20, 160, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(parent=RepeatedApplication)
        self.label_6.setGeometry(QtCore.QRect(20, 190, 501, 71))
        self.label_6.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_6.setObjectName("label_6")
        self.label = QtWidgets.QLabel(parent=RepeatedApplication)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 61))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/Enverga-logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_9 = QtWidgets.QLabel(parent=RepeatedApplication)
        self.label_9.setGeometry(QtCore.QRect(470, 10, 61, 61))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(":/icons/ccmslogo.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_5 = QtWidgets.QLabel(parent=RepeatedApplication)
        self.label_5.setGeometry(QtCore.QRect(20, 70, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_5.setObjectName("label_5")

        self.retranslateUi(RepeatedApplication)
        QtCore.QMetaObject.connectSlotsByName(RepeatedApplication)

    def retranslateUi(self, RepeatedApplication):
        _translate = QtCore.QCoreApplication.translate
        RepeatedApplication.setWindowTitle(_translate("RepeatedApplication", "Application of Repeated Permutation"))
        self.backRepeated.setText(_translate("RepeatedApplication", "Back"))
        self.tryRepeated.setText(_translate("RepeatedApplication", "Try"))
        self.label_3.setText(_translate("RepeatedApplication", "Real-Life Application"))
        self.label_2.setText(_translate("RepeatedApplication", "Arranging Books with the same Genre on a Bookshelf:\n"
"By calculating all possible arrangements of books, the tool helps users\n"
"make the most efficient use of shelf space, allowing for better organization and accessibility."))
        self.label_4.setText(_translate("RepeatedApplication", "How to use:"))
        self.label_6.setText(_translate("RepeatedApplication", "1. Enter the genres of the books you want to arrange.\n"
"2. Click the \"Generate Arrangements\" button.\n"
"3. The generated arrangements will be displayed in the text area below."))
        self.label_5.setText(_translate("RepeatedApplication", "Real-life Application"))
        
class Ui_RepeatedSystem(object):
    def setupUi(self, CIrcularSystem):
        CIrcularSystem.setObjectName("CIrcularSystem")
        CIrcularSystem.resize(500, 570)
        CIrcularSystem.setMinimumSize(QtCore.QSize(500, 570))
        CIrcularSystem.setMaximumSize(QtCore.QSize(500, 570))
        CIrcularSystem.setStyleSheet("background-color: white;")
        self.label_8 = QtWidgets.QLabel(parent=CIrcularSystem)
        self.label_8.setGeometry(QtCore.QRect(30, 10, 71, 61))
        self.label_8.setStyleSheet("")
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/icons/Enverga-logo.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(parent=CIrcularSystem)
        self.label_10.setGeometry(QtCore.QRect(410, 10, 61, 61))
        self.label_10.setStyleSheet("")
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap(":/icons/ccmslogo.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.label = QtWidgets.QLabel(parent=CIrcularSystem)
        self.label.setGeometry(QtCore.QRect(100, 20, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.category_input = QtWidgets.QLineEdit(parent=CIrcularSystem)
        self.category_input.setGeometry(QtCore.QRect(40, 100, 421, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.category_input.setFont(font)
        self.category_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: black;\n"
"border:1px solid black;\n"
"padding-left: 15px;\n"
"border-radius: 15px;")
        self.category_input.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.category_input.setObjectName("category_input")
        self.generate_button = QtWidgets.QPushButton(parent=CIrcularSystem)
        self.generate_button.setGeometry(QtCore.QRect(60, 170, 381, 41))
        font = QtGui.QFont()
        font.setBold(True)
        self.generate_button.setFont(font)
        self.generate_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.generate_button.setStyleSheet("QPushButton{\n"
"color: white;\n"
"background-color:#800000;\n"
"border:2px solid #800000;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: rgb(138, 6, 9);\n"
"}\n"
"")
        self.generate_button.setObjectName("generate_button")
        self.output_area = QtWidgets.QTextEdit(parent=CIrcularSystem)
        self.output_area.setGeometry(QtCore.QRect(70, 230, 361, 231))
        font = QtGui.QFont()
        font.setBold(True)
        self.output_area.setFont(font)
        self.output_area.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 10px;\n"
"padding: 10px;")
        self.output_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.output_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.output_area.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.output_area.setReadOnly(True)
        self.output_area.setObjectName("output_area")
        self.back = QtWidgets.QPushButton(parent=CIrcularSystem)
        self.back.setGeometry(QtCore.QRect(190, 480, 111, 41))
        font = QtGui.QFont()
        font.setBold(True)
        self.back.setFont(font)
        self.back.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.back.setStyleSheet("QPushButton{\n"
"color: white;\n"
"background-color:#800000;\n"
"border:2px solid #800000;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: white;\n"
"    color: rgb(138, 6, 9);\n"
"}\n"
"")
        self.back.setObjectName("back")

        self.retranslateUi(CIrcularSystem)
        QtCore.QMetaObject.connectSlotsByName(CIrcularSystem)

    def retranslateUi(self, CIrcularSystem):
        _translate = QtCore.QCoreApplication.translate
        CIrcularSystem.setWindowTitle(_translate("CIrcularSystem", "Books Arrangement"))
        self.label.setText(_translate("CIrcularSystem", "BOOKSHELF ARRANGEMENT TOOL"))
        self.category_input.setPlaceholderText(_translate("CIrcularSystem", "Enter book categories, separated by commas (e.g., Fiction, History, Fantasy)"))
        self.generate_button.setText(_translate("CIrcularSystem", "GENERATE ARRANGEMENTS"))
        self.output_area.setHtml(_translate("CIrcularSystem", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:700; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.back.setText(_translate("CIrcularSystem", "BACK"))

