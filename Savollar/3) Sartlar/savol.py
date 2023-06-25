import json
from tkinter import filedialog
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import sip
a=42
b=12
b=a+b
a=b-a
b=b-a
print(a,b)
f={
        "savol":"",
        "tek":[],
        "objects":"",
}
n=0
class Ui_MainWindow(object):
        def delete_case(self,n):
                global f
                try:
                        _translate = QtCore.QCoreApplication.translate
                        sip.delete(self.cases[n])
                        (f['tek']).pop(n)
                        self.textBrowser.setText(_translate("MainWindow",json.dumps(f,indent=4)))

                except:
                        pass
        def open_fileset(self):
                global f
                try:
                        _translate = QtCore.QCoreApplication.translate
                        fg=filedialog.askopenfilename(title="Savolni belgilang",initialfile=".")

                        f=json.loads(open(fg,"r").read())
                        self.textEdit.setText(_translate("MainWindow", f["savol"]))
                        self.lineEdit_4.setText(_translate("MainWindow", fg[:-5]))
                        self.lineEdit_3.setText(_translate("MainWindow", f["objects"]))
                        for i in self.cases:
                                sip.delete(i)
                        self.cases.clear()
                        n=0
                        for i in f["tek"]:
                                print(i)
                                frame_5 = QtWidgets.QFrame(self.frame_7)
                                frame_5.setStyleSheet("border-radius: 5px;\n"
                                                      "background-color: rgb(225, 214, 0);")
                                frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
                                frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
                                frame_5.setObjectName("frame_5")
                                self.horizontalLayout_5 = QtWidgets.QHBoxLayout(frame_5)
                                self.horizontalLayout_5.setObjectName("horizontalLayout_5")
                                self.label_6 = QtWidgets.QLabel(frame_5)
                                self.label_6.setMaximumSize(QtCore.QSize(40, 16777215))
                                self.label_6.setObjectName("label_6")
                                self.horizontalLayout_5.addWidget(self.label_6)
                                self.label_8 = QtWidgets.QLabel(frame_5)
                                self.label_8.setObjectName("label_8")
                                self.horizontalLayout_5.addWidget(self.label_8)
                                self.label_7 = QtWidgets.QLabel(frame_5)
                                self.label_7.setMaximumSize(QtCore.QSize(40, 16777215))
                                self.label_7.setObjectName("label_7")
                                self.horizontalLayout_5.addWidget(self.label_7)
                                self.label_5 = QtWidgets.QLabel(frame_5)
                                self.label_5.setObjectName("label_5")
                                self.button_x = QtWidgets.QPushButton(frame_5)
                                self.button_x.setMinimumSize(QtCore.QSize(40, 25))
                                self.button_x.setMaximumSize(QtCore.QSize(50, 30))
                                self.button_x.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                                self.button_x.setStyleSheet("QPushButton{\n"
                                                                "font: 16pt \"MS Shell Dlg 2\";\n"
                                                                "border-radius: 10px;\n"
                                                                "color: rgb(255,0,0);\n"
                                                                "background-color: rgb(170, 255, 127);}\n"
                                                                "QPushButton:hover{\n"
                                                                "color: rgb(0,0,0);\n"
                                                                "background-color: rgb(255, 0, 0);\n"
                                                                "}")
                                ac=partial(self.delete_case,n)
                                self.button_x.clicked.connect(ac)
                                self.horizontalLayout_5.addWidget(self.label_5)
                                self.horizontalLayout_5.addWidget(self.button_x)
                                self.verticalLayout_3.addWidget(frame_5)


                                self.label_6.setText(_translate("MainWindow", "input"))
                                self.label_8.setText(_translate("MainWindow", str(i["input"])[1:-1]))
                                self.label_7.setText(_translate("MainWindow", "output"))
                                self.label_5.setText(_translate("MainWindow", str(i["output"])))
                                self.textBrowser.setText(_translate("MainWindow", json.dumps(f,indent=4)))
                                self.lineEdit.setText(_translate("QLineEdit_test", ""))
                                self.lineEdit_2.setText(_translate("QLineEdit_test", ""))
                                self.button_x.setText(_translate("MainWindow", "X"))
                                self.cases.append(frame_5)
                                n+=1
                except:
                        pass
        def save(self):
                try:
                        global f
                        _translate = QtCore.QCoreApplication.translate
                        s = self.textEdit.toPlainText()
                        f['savol'] = s
                        i = self.lineEdit_3.displayText()
                        f['objects'] = i
                        self.textBrowser.setText(_translate("MainWindow", json.dumps(f,indent=4)))
                except:
                        pass
        def savol_saqlash(self):
                global f
                _translate = QtCore.QCoreApplication.translate
                try:
                        if f["savol"]!="" and f["tek"]!=[] and f["objects"]!="":
                                open(self.lineEdit_4.displayText() + ".json", "w").write(json.dumps(f, indent=4))
                                f = {
                                        "savol": "",
                                        "tek": [],
                                        "objects": "",
                                }

                                self.textBrowser.setText(_translate("MainWindow", json.dumps(f,indent=4)))
                                self.lineEdit_4.setText(_translate("MainWindow", ""))
                                self.lineEdit.setText(_translate("MainWindow", ""))
                                self.lineEdit_2.setText(_translate("MainWindow", ""))
                                self.lineEdit_3.setText(_translate("MainWindow", ""))
                                self.textEdit.setText((_translate("MainWindow","")))
                                for i in self.cases:
                                        sip.delete(i)
                                self.cases.clear()

                except:
                        pass
        def add_test_case(self):
                global f, n
                try:
                        inputt=self.lineEdit.displayText()
                        output=self.lineEdit_2.displayText()
                        n += 1
                        s = {
                                "input": json.loads("["+inputt+"]"),
                                "output": json.loads(output),
                        }
                        f["tek"].append(s)
                        _translate = QtCore.QCoreApplication.translate
                        frame_5 = QtWidgets.QFrame(self.frame_7)
                        frame_5.setStyleSheet("border-radius: 5px;\n"
                                                   "background-color: rgb(225, 214, 0);")
                        frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
                        frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
                        frame_5.setObjectName("frame_5")
                        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(frame_5)
                        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
                        self.label_6 = QtWidgets.QLabel(frame_5)
                        self.label_6.setMaximumSize(QtCore.QSize(40, 16777215))
                        self.label_6.setObjectName("label_6")
                        self.horizontalLayout_5.addWidget(self.label_6)
                        self.label_8 = QtWidgets.QLabel(frame_5)
                        self.label_8.setObjectName("label_8")
                        self.horizontalLayout_5.addWidget(self.label_8)
                        self.label_7 = QtWidgets.QLabel(frame_5)
                        self.label_7.setMaximumSize(QtCore.QSize(40, 16777215))
                        self.label_7.setObjectName("label_7")
                        self.horizontalLayout_5.addWidget(self.label_7)
                        self.label_5 = QtWidgets.QLabel(frame_5)
                        self.label_5.setObjectName("label_5")
                        self.button_x = QtWidgets.QPushButton(frame_5)
                        self.button_x.setMinimumSize(QtCore.QSize(40, 25))
                        self.button_x.setMaximumSize(QtCore.QSize(50, 30))
                        self.button_x.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                        self.button_x.setStyleSheet("QPushButton{\n"
                                                        "font: 16pt \"MS Shell Dlg 2\";\n"
                                                        "border-radius: 10px;\n"
                                                        "color: rgb(255,0,0);\n"
                                                        "background-color: rgb(170, 255, 127);}\n"
                                                        "QPushButton:hover{\n"
                                                        "color: rgb(0,0,0);\n"
                                                        "background-color: rgb(255, 0, 0);\n"
                                                        "}")
                        print(len(self.cases))
                        ac=partial(self.delete_case,len(self.cases))
                        self.button_x.clicked.connect(ac)
                        self.horizontalLayout_5.addWidget(self.label_5)
                        self.horizontalLayout_5.addWidget(self.button_x)
                        self.verticalLayout_3.addWidget(frame_5)
                        self.label_6.setText(_translate("MainWindow", "input"))
                        self.label_8.setText(_translate("MainWindow", inputt))
                        self.label_7.setText(_translate("MainWindow", "output"))
                        self.label_5.setText(_translate("MainWindow", output))
                        self.textBrowser.setText(_translate("MainWindow", json.dumps(f,indent=4)))
                        self.lineEdit.setText(_translate("QLineEdit_test", ""))
                        self.lineEdit_2.setText(_translate("QLineEdit_test", ""))
                        self.button_x.setText(_translate("MainWindow", "X"))
                        self.cases.append(frame_5)
                except:
                        pass

        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(950, 750)
                self.cases=[]
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
                self.verticalLayout.setObjectName("verticalLayout")
                self.frame_4 = QtWidgets.QFrame(self.centralwidget)
                self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_4.setObjectName("frame_4")
                self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
                self.horizontalLayout_4.setObjectName("horizontalLayout_4")
                self.open_button = QtWidgets.QPushButton(self.frame_4)
                self.open_button.setMinimumSize(QtCore.QSize(60, 30))
                self.open_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.open_button.setStyleSheet("QPushButton{\n"
                                               "font: 16pt \"MS Shell Dlg 2\";\n"
                                               "border-radius: 8px;\n"
                                               "background-color: rgb(170, 255, 127);}\n"
                                               "QPushButton:hover{\n"
                                               "background-color: rgb(105, 156, 77);\n"
                                               "}")
                self.open_button.setObjectName("save_button")
                self.horizontalLayout_4.addWidget(self.open_button)
                self.label_4 = QtWidgets.QLabel(self.frame_4)
                self.label_4.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
                self.label_4.setObjectName("label_4")
                self.horizontalLayout_4.addWidget(self.label_4)
                self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_4)
                self.lineEdit_4.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
                                              "color: rgb(170, 255, 0);\n"
                                              "border-radius: 10px;\n"
                                              "background-color: rgb(107, 103, 0);\n"
                                              "padding-left:5px;")
                self.lineEdit_4.setObjectName("lineEdit_4")
                self.horizontalLayout_4.addWidget(self.lineEdit_4)
                self.save_button = QtWidgets.QPushButton(self.frame_4)
                self.save_button.setMinimumSize(QtCore.QSize(60, 30))
                self.save_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.save_button.setStyleSheet("QPushButton{\n"
                                               "font: 16pt \"MS Shell Dlg 2\";\n"
                                               "border-radius: 8px;\n"
                                               "background-color: rgb(170, 255, 127);}\n"
                                               "QPushButton:hover{\n"
                                               "background-color: rgb(105, 156, 77);\n"
                                               "}")
                self.save_button.setObjectName("save_button")
                self.horizontalLayout_4.addWidget(self.save_button)
                self.verticalLayout.addWidget(self.frame_4)
                self.frame_8 = QtWidgets.QFrame(self.centralwidget)
                self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_8.setObjectName("frame_8")
                self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_8)
                self.horizontalLayout_7.setObjectName("horizontalLayout_7")
                self.textEdit = QtWidgets.QTextEdit(self.frame_8)
                self.textEdit.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
                                            "border-radius: 10px;\n"
                                            "background-color: rgb(181, 172, 0);")
                self.textEdit.setObjectName("textEdit")
                self.horizontalLayout_7.addWidget(self.textEdit)
                self.frame_9 = QtWidgets.QFrame(self.frame_8)
                self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_9.setObjectName("frame_9")
                self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_9)
                self.verticalLayout_4.setObjectName("verticalLayout_4")
                self.label_9 = QtWidgets.QLabel(self.frame_9)
                self.label_9.setObjectName("label_9")
                self.verticalLayout_4.addWidget(self.label_9)
                self.textBrowser = QtWidgets.QTextBrowser(self.frame_9)
                self.textBrowser.setStyleSheet("border-radius:10px;\n"
                                               "background-color: rgba(255, 255, 127, 200);")
                self.textBrowser.setObjectName("textBrowser")
                self.verticalLayout_4.addWidget(self.textBrowser)
                self.horizontalLayout_7.addWidget(self.frame_9)
                self.verticalLayout.addWidget(self.frame_8)
                self.frame_3 = QtWidgets.QFrame(self.centralwidget)
                self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_3.setObjectName("frame_3")
                self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
                self.horizontalLayout_3.setObjectName("horizontalLayout_3")
                self.label = QtWidgets.QLabel(self.frame_3)
                self.label.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
                self.label.setObjectName("label")
                self.horizontalLayout_3.addWidget(self.label)
                self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_3)
                self.lineEdit_3.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
                                              "border-radius: 10px;\n"
                                              "background-color: rgb(107, 103, 0);")
                self.lineEdit_3.setObjectName("lineEdit_3")
                self.horizontalLayout_3.addWidget(self.lineEdit_3)
                self.verticalLayout.addWidget(self.frame_3)
                self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
                self.scrollArea.setMinimumSize(QtCore.QSize(0, 200))
                self.scrollArea.setMaximumSize(QtCore.QSize(16777215, 200))
                self.scrollArea.setWidgetResizable(True)
                self.scrollArea.setObjectName("scrollArea")
                self.scrollAreaWidgetContents = QtWidgets.QWidget()
                self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 930, 198))
                self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
                self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
                self.verticalLayout_2.setObjectName("verticalLayout_2")
                self.frame_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
                self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_2.setObjectName("frame_2")
                self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
                self.horizontalLayout_2.setObjectName("horizontalLayout_2")
                self.label_2 = QtWidgets.QLabel(self.frame_2)
                self.label_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
                self.label_2.setObjectName("label_2")
                self.horizontalLayout_2.addWidget(self.label_2)
                self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
                self.lineEdit.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
                                            "border-radius: 10px;\n"
                                            "background-color: rgb(107, 103, 0);")
                self.lineEdit.setObjectName("lineEdit")
                self.horizontalLayout_2.addWidget(self.lineEdit)
                self.label_3 = QtWidgets.QLabel(self.frame_2)
                self.label_3.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
                                           "")
                self.label_3.setObjectName("label_3")
                self.horizontalLayout_2.addWidget(self.label_3)
                self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_2)
                self.lineEdit_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
                                              "border-radius: 10px;\n"
                                              "background-color: rgb(107, 103, 0);")
                self.lineEdit_2.setObjectName("lineEdit_2")
                self.horizontalLayout_2.addWidget(self.lineEdit_2)
                self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
                self.pushButton_2.setMinimumSize(QtCore.QSize(40, 30))
                self.pushButton_2.setMaximumSize(QtCore.QSize(16777215, 30))
                self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.pushButton_2.setStyleSheet("QPushButton{\n"
                                                "font: 16pt \"MS Shell Dlg 2\";\n"
                                                "border-radius: 10px;\n"
                                                "background-color: rgb(170, 255, 127);}\n"
                                                "QPushButton:hover{\n"
                                                "background-color: rgb(105, 156, 77);\n"
                                                "}")
                self.pushButton_2.setObjectName("pushButton_2")
                self.horizontalLayout_2.addWidget(self.pushButton_2)
                self.verticalLayout_2.addWidget(self.frame_2)
                self.frame_7 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
                self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_7.setObjectName("frame_7")
                self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_7)
                self.verticalLayout_3.setObjectName("verticalLayout_3")
                self.verticalLayout_2.addWidget(self.frame_7)
                spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                                   QtWidgets.QSizePolicy.Expanding)
                self.verticalLayout_2.addItem(spacerItem)
                self.scrollArea.setWidget(self.scrollAreaWidgetContents)
                self.verticalLayout.addWidget(self.scrollArea)
                self.pushButton = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton.setMinimumSize(QtCore.QSize(0, 50))
                self.pushButton.setMaximumSize(QtCore.QSize(16777215, 70))
                self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.pushButton.setStyleSheet("QPushButton{\n"
                                              "font: 16pt \"MS Shell Dlg 2\";\n"
                                              "border-radius: 8px;\n"
                                              "background-color: rgb(0, 255, 0);}\n"
                                              "QPushButton:hover{\n"
                                              "background-color: rgb(170, 255, 127);\n"
                                              "}")
                self.pushButton.setObjectName("pushButton")
                self.verticalLayout.addWidget(self.pushButton)
                MainWindow.setCentralWidget(self.centralwidget)

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)
        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.label_4.setText(_translate("MainWindow", "Savol Nomi"))
                self.save_button.setText(_translate("MainWindow", "Save"))
                self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
                self.label_9.setText(_translate("MainWindow", "     Natija json"))
                self.label.setText(_translate("MainWindow", "objectlar"))
                self.label_2.setText(_translate("MainWindow", "input"))
                self.label_3.setText(_translate("MainWindow", "output"))
                self.open_button.setText(_translate("MainWindow", "Load"))
                self.pushButton_2.setText(_translate("MainWindow", "+"))
                self.pushButton.setText(_translate("MainWindow", "Savol Yaratish"))
                self.pushButton_2.clicked.connect(self.add_test_case)
                self.pushButton.clicked.connect(self.savol_saqlash)
                self.save_button.clicked.connect(self.save)
                self.textBrowser.setText(_translate("MainWindow", json.dumps(f,indent=4)))
                self.open_button.clicked.connect(self.open_fileset)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
