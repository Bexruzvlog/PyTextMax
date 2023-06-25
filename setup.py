import time
from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
import json
from glob import glob
from PyQt5 import sip
try:
    yoz = open("obb.json", "r").read()
except:
    obb_json_setup=open("obb.json", "w")
    obb_json_uchun={"":""}
    obb_json_uchun.clear()
    for i in glob(f"savollar/*"):
        obb_json_uchun[i[9:]] = {"soni": len(glob(i+"/*.json")),"ishlanganlar": []}
    obb_json_setup.write(json.dumps(obb_json_uchun,indent=4))
    obb_json_setup.close()
    del obb_json_setup
mavzu=""
old=""
menyu=1
class Ui_MainWindow(object):
    def get_Buttons(self,qaysi):
        _translate = QtCore.QCoreApplication.translate
        yoz=open(f"savollar/{mavzu}/{qaysi}.json","r").read()
        f=json.loads(yoz)
        f["savol"]=(f["savol"]).replace("\n","<br>")
        self.label.setText(_translate("MainWindow", "0"))
        self.label_3.setText(_translate("MainWindow", "Natija"))
        self.label_4.setText(_translate("MainWindow", (qaysi.split(")"))[-1][1:]))
        self.label.setStyleSheet("color: rgb(255,255,255); background-color: rgb(40,40,40); padding-left:20px;border-radius:10px")
        self.label_3.setStyleSheet("color: rgb(255,255,255); background-color: rgb(40,40,40); padding-left:20px;border-radius:10px")
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\np, li { white-space: pre-wrap; }\n"+f"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:{self.sh}pt; font-weight:400; font-style:normal;\">\n<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">{f['savol']}</p></body></html>"))
        self.textEdit.setStyleSheet("border-radius: 10px;\n"
                                    "background-color: rgb(50, 50, 50);\n"
                                    "color:rgb(255, 255, 255);\n"
                                    f"font: {self.sh}pt \"Courier New\";")
        self.textEdit.setText(_translate("MainWindow","# " + f["objects"]+"\n"))
        self.ishlanayotgan_misol=f.copy()
        try:
            yoz = open("obb.json", "r").read()
            fg = json.loads(yoz)
            if qaysi not in fg[mavzu]["ishlanganlar"]:
                (self.buttons[qaysi]).setStyleSheet("QPushButton {\n"
                                                        "text-align: left;\n"
                                                         "border: 2px solid rgb(0, 255, 255);\n"
                                                         "background-color: rgb(40, 40, 40);\n"
                                                         "color: rgb(0, 255, 255);\n"
                                                         "font-size: 14px;\n"
                                                         "border-radius:10px;\n"
                                                        "padding: 8px;\n"
                                                        "margin-right: 25px;\n"
                                                         "}\n")
            else:
                (self.buttons[qaysi]).setStyleSheet("QPushButton {\n"
                                                        "text-align: left;\n"
                                                         "border: 2px solid rgb(0, 255, 100);\n"
                                                         "background-color: rgb(40, 40, 40);\n"
                                                         "color: rgb(0, 255, 255);\n"
                                                         "font-size: 14px;\n"
                                                         "border-radius:10px;\n"
                                                        "padding: 8px;\n"
                                                        "margin-right: 25px;\n"
                                                         "}\n")
            if self.ishlanayotgan!=qaysi:
                if self.ishlanayotgan not in fg[mavzu]["ishlanganlar"]:
                    (self.buttons[self.ishlanayotgan]).setStyleSheet("QPushButton {\n"
                                                "text-align: left;\n"
                                                "padding: 8px;\n"
                                                 "border: 2px solid rgb(40, 40, 40);\n"
                                                 "font-size: 14px;\n"
                                                 "color: rgb(255, 255, 127);\n"
                                                 "border-radius:10px;\n"
                                                 "}\n"
                                                "QPushButton:hover{\n"
                                                 "color: rgb(255, 255, 200);\n"
                                                "background-color: rgb(40, 40, 40);\n"
                                                 "}\n")
                else:
                    (self.buttons[self.ishlanayotgan]).setStyleSheet("QPushButton {\n"
                                                    "text-align: left;\n"
                                                     "border: 2px solid rgb(150, 255, 150);\n"
                                                     "color: rgb(0, 0,200);\n"
                                                     "font-size: 14px;\n"
                                                     "border-radius:10px;\n"
                                                    "background-color: rgb(150, 255, 150);\n"
                                                    "padding: 8px;\n"
                                                     "}\n"
                                                    "QPushButton:hover{\n"
                                                     "color: rgb(255, 255, 200);\n"
                                                    "background-color: rgb(40, 40, 40);\n"
                                                     "}\n")
        except:
            pass
        self.ishlanayotgan=qaysi
    def Run(self):
        _translate = QtCore.QCoreApplication.translate
        try:
            n=0
            f=self.ishlanayotgan_misol
            code=self.textEdit.toPlainText()
            code_def=f'''def get({f["objects"]}):\n'''
            for i in code.split("\n"):
                code_def+="    "+i+"\n"
            code_def=code_def.replace("print","return")
            exec(code_def+"\nself.gett=get")
            res="To'g'ri"
            for i in f["tek"]:
                n+=1
                d=i["input"]
                h=i["output"]
                dggdg=self.gett(*d)
                if str(type(dggdg))=="<class 'tuple'>":
                    if h==list(dggdg):
                        pass
                    else:
                        res="xato"
                        break
                else:
                    if h==dggdg:
                        pass
                    else:
                        res="xato"
                        break
            if res!="xato":
                time.sleep(0.6)
                self.label.setText(_translate("MainWindow", str(n)))
                self.label_3.setText(_translate("MainWindow",
                                                "Accept"))
                self.label.setStyleSheet("color: rgb(0,255,0); background-color: rgb(40,40,40); padding-left:20px;border-radius:10px")
                self.label_3.setStyleSheet("color: rgb(0,255,0); background-color: rgb(40,40,40); padding-left:20px;border-radius:10px")
                yoz = open("obb.json", "r").read()
                fg = json.loads(yoz)
                if self.ishlanayotgan not in fg[mavzu]["ishlanganlar"]:
                    (fg[mavzu]["ishlanganlar"]).append(self.ishlanayotgan)
                open("obb.json", "w").write(json.dumps(fg,indent=4))
                (self.buttons[self.ishlanayotgan]).setStyleSheet("QPushButton {\n"
                                                    "text-align: left;\n"
                                                     "border: 2px solid rgb(150, 255, 150);\n"
                                                     "color: rgb(0, 0,200);\n"
                                                     "font-size: 14px;\n"
                                                     "border-radius:10px;\n"
                                                    "background-color: rgb(150, 255, 150);\n"
                                                    "padding: 8px;\n"
                                                     "}\n"
                                                    "QPushButton:hover{\n"
                                                     "color: rgb(255, 255, 200);\n"
                                                    "background-color: rgb(40, 40, 40);\n"
                                                     "}\n")
            else:
                time.sleep(0.3)
                self.label.setText(_translate("MainWindow", str(n)))
                self.label_3.setText(_translate("MainWindow", "xato"))
                self.label.setStyleSheet("color: rgb(255,0,0)")
                self.label_3.setStyleSheet("color: rgb(255,0,0)")
                self.label.setStyleSheet("color: rgb(255,0,0); background-color: rgb(40,40,40); padding-left:20px;border-radius:10px")
                self.label_3.setStyleSheet("color: rgb(255,0,0); background-color: rgb(40,40,40); padding-left:20px;border-radius:10px")
        except:
            self.label.setText(_translate("MainWindow", str(n)))
            self.label_3.setText(_translate("MainWindow", "dastur xato tuzilagan"))
            self.label.setStyleSheet("color: rgb(255,0,0)")
            self.label_3.setStyleSheet("color: rgb(255,0,0)")
            self.label.setStyleSheet("color: rgb(255,0,0); background-color: rgb(40,40,40); padding-left:20px;border-radius:10px")
            self.label_3.setStyleSheet("color: rgb(255,0,0); background-color: rgb(40,40,40); padding-left:20px;border-radius:10px")
    def get_mavzu(self,mavz,ful):
        global mavzu,old
        _translate = QtCore.QCoreApplication.translate
        for i in self.buttons.keys():
            sip.delete(self.buttons[i])
        self.buttons.clear()
        yoz = open("obb.json", "r").read()
        fg = json.loads(yoz)
        mavzu=ful
        self.tons={"":""}
        self.tons.clear()
        for i in glob(f"savollar/{ful}/*.json"):
            self.pushButton_8 = QtWidgets.QPushButton(self.frame_are)
            self.pushButton_8.setMinimumSize(QtCore.QSize(50, 35))
            self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            if i[10 + len(mavzu):-5] in fg[ful]["ishlanganlar"]:
                self.pushButton_8.setStyleSheet("QPushButton {\n"
                                                "text-align: left;\n"
                                                 "border: 2px solid rgb(150, 255, 150);\n"
                                                 "color: rgb(0, 0,200);\n"
                                                 "font-size: 14px;\n"
                                                 "border-radius:10px;\n"
                                                "background-color: rgb(150, 255, 150);\n"
                                                "padding: 8px;\n"
                                                 "}\n"
                                                "QPushButton:hover{\n"
                                                 "color: rgb(255, 255, 200);\n"
                                                "background-color: rgb(40, 40, 40);\n"
                                                 "}\n")
            else:
                self.pushButton_8.setStyleSheet("QPushButton {\n"
                                                "text-align: left;\n"
                                                "padding: 8px;\n"
                                                 "border: 2px solid rgb(40, 40, 40);\n"
                                                 "font-size: 14px;\n"
                                                 "color: rgb(255, 255, 127);\n"
                                                 "border-radius:10px;\n"
                                                 "}\n"
                                                "QPushButton:hover{\n"
                                                 "color: rgb(255, 255, 200);\n"
                                                "background-color: rgb(40, 40, 40);\n"
                                                 "}\n")
            self.pushButton_8.setObjectName("pushButton_8")
            number=i[10 + len(mavzu):-5]
            self.pushButton_8.setText(_translate("MainWindow", i[10 + len(mavzu):-5]))
            action_with_args = partial(self.get_Buttons, number)
            self.pushButton_8.clicked.connect(action_with_args)
            self.buttons[number] = self.pushButton_8
            self.tons[int(number.split(")")[0])] = self.pushButton_8
        keys=list(self.tons.keys())
        keys.sort()
        for i in keys:
            self.verticalLayout_2ar.addWidget(self.tons[i])
        if old!=mavz:
            (self.buttons_m[mavz]).setStyleSheet("QPushButton {\n"
                                                "text-align: left;\n"
                                                "padding-left: 10px;\n"
                                                "background-color: rgb(100, 255, 100);\n"
                                                "border-radius:5px;\n"
                                                "color: rgb(40, 40, 40);\n"
                                                "font-size: 16px;\n"
                                                "cursor: cursor;\n"
                                                "}\n")
            try:
                (self.buttons_m[old]).setStyleSheet("QPushButton {\n"
                                                    "text-align: left;\n"
                                                    "padding-left: 10px;\n"
                                                    "background-color: rgb(40, 40, 40);\n"
                                                    "border-radius:5px;\n"
                                                    "color: rgb(255,255,200);\n"
                                                    "font-size: 16px;\n"
                                                    "}\n"
                                                    "QPushButton:hover{\n"
                                                    "background-color: rgb(100, 255, 100);\n"
                                                     "color: rgb(40, 40, 40);\n"
                                                     "}\n")
            except:
                pass
            old=mavz

    def menuss(self):
        _translate = QtCore.QCoreApplication.translate
        if self.sh>9:
            self.sh-=1
        self.textEdit.setStyleSheet("border-radius: 10px;\n"
                                    "background-color: rgb(50, 50, 50);\n"
                                    "color:rgb(255, 255, 255);\n"
                                    f"font: {self.sh}pt \"Courier New\";")
        ser=(self.textBrowser.toPlainText()).replace("\n","<br>")
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                    "p, li { white-space: pre-wrap; }\n"
                                    f"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:{self.sh}pt; font-weight:400; font-style:normal;\">\n"
                                    f'<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">{ser}</p></body></html>'))
    def pluss(self):
        _translate = QtCore.QCoreApplication.translate
        if self.sh<26:
            self.sh+=1
        self.textEdit.setStyleSheet("border-radius: 10px;\n"
                                    "background-color: rgb(50, 50, 50);\n"
                                    "color:rgb(255, 255, 255);\n"
                                    f"font: {self.sh}pt \"Courier New\";")
        ser=(self.textBrowser.toPlainText()).replace("\n","<br>")
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                    "p, li { white-space: pre-wrap; }\n"
                                    f"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:{self.sh}pt; font-weight:400; font-style:normal;\">\n"
                                    f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">{ser}</p></body></html>"))

    def get_menyu(self):
        global menyu
        if menyu:
            self.frame_are1.setMaximumSize(QtCore.QSize(0, 16777215))
            self.scrollArea1.setMaximumSize(QtCore.QSize(68, 16777215))
            menyu=0
        else:
            self.frame_are1.setMaximumSize(QtCore.QSize(300, 16777215))
            self.scrollArea1.setMaximumSize(QtCore.QSize(300, 16777215))
            menyu=1
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 650)
        MainWindow.setWindowIcon(QtGui.QIcon('ivon1.png'))
        _translate = QtCore.QCoreApplication.translate
        self.ishlanayotgan_misol=""
        self.sh=12
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("* { background-color: rgb(100,100,100);}")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.scrollArea1 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea1.setMaximumSize(QtCore.QSize(300, 16777215))
        self.scrollArea1.setStyleSheet("")
        self.scrollArea1.setWidgetResizable(True)
        self.scrollArea1.setObjectName("scrollArea")
        self.scrollAreaWidgetContents1 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents1.setGeometry(QtCore.QRect(0, 0, 298, 566))
        self.scrollAreaWidgetContents1.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents1)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setMaximumSize(QtCore.QSize(400, 16777215))
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 298, 566))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_are = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_are.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_are.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_are.setObjectName("frame")
        self.frame_are1 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_are1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_are1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_are1.setObjectName("frame1")
        self.verticalLayout_2.addWidget(self.frame_are)
        self.verticalLayout_2ar = QtWidgets.QVBoxLayout(self.frame_are)
        self.verticalLayout_21.addWidget(self.frame_are)
        self.verticalLayout_2ar1 = QtWidgets.QVBoxLayout(self.frame_are1)
        self.verticalLayout_2ar1.setObjectName("verticalLayout_2ar")
        self.scrollArea1.setStyleSheet("background-color: rgb(150,150,150);border-radius:10px;")
        self.scrollArea.setStyleSheet("border-top:1px solid rgb(0,255,255);border-bottom:1px solid rgb(0,255,255);")
        self.frame_are.setStyleSheet("border:0;")
        self.b_menyu = QtWidgets.QPushButton(self.scrollAreaWidgetContents1)
        self.b_menyu.setMinimumSize(QtCore.QSize(50, 60))
        self.b_menyu.setMaximumSize(QtCore.QSize(100, 60))
        self.b_menyu.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b_menyu.setStyleSheet("QPushButton {\n"
                                        "text-align: left;\n"
                                        "padding-left: 10px;\n"
                                        "background-color: rgb(40, 40, 40);\n"
                                        "border-radius:10px;\n"
                                        "color: rgb(100, 255, 100);\n"
                                        "font-size: 25px;\n"
                                        "padding-bottom: 5px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "background-color: rgb(100, 255, 100);\n"
                                        "color: rgb(40, 40, 40);\n"
                                        "}\n")
        self.b_menyu.setObjectName("pushButton_8")
        self.b_menyu.setText(_translate("MainWindow", "|||"))
        self.b_menyu.clicked.connect(self.get_menyu)
        self.verticalLayout_21.addWidget(self.b_menyu)
        self.verticalLayout_21.addWidget(self.frame_are1)

        _translate = QtCore.QCoreApplication.translate
        self.buttons={
            "":""
        }
        self.buttons_m = {
            "":""
        }
        self.buttons.clear()
        self.buttons_m.clear()
        try:
            mavzu
        except:
            exit()


        for i in glob(f"savollar/*"):
            if i[9:] not in ["ui_add_quiz.ui"]:
                self.pushButton_8 = QtWidgets.QPushButton(self.scrollAreaWidgetContents1)
                self.pushButton_8.setMinimumSize(QtCore.QSize(50, 40))
                self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.pushButton_8.setStyleSheet("QPushButton {\n"
                                                "text-align: left;\n"
                                                "padding-left: 10px;\n"
                                                "background-color: rgb(40, 40, 40);\n"
                                                "border-radius:5px;\n"
                                                "color: rgb(255,255,200);\n"
                                                "font-size: 16px;\n"
                                                "}\n"
                                                "QPushButton:hover{\n"
                                                "background-color: rgb(100, 255, 100);\n"
                                                 "color: rgb(40, 40, 40);\n"
                                                 "}\n")
                self.pushButton_8.setObjectName("pushButton_8")
                self.pushButton_8.setText(_translate("MainWindow", ((i[9:]).split(")"))[-1]))
                action_with_args = partial(self.get_mavzu, int(((i[9:]).split(")"))[0]),i[9:])
                self.pushButton_8.clicked.connect(action_with_args)
                self.buttons_m[int(((i[9:]).split(")"))[0])] = self.pushButton_8
        keys=list(self.buttons_m.keys())
        keys.sort()
        for i in keys:
            self.verticalLayout_2ar1.addWidget(self.buttons_m[i])
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_21.addItem(spacerItem)

        self.scrollArea1.setWidget(self.scrollAreaWidgetContents1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.addWidget(self.scrollArea1)
        self.horizontalLayout_3.addWidget(self.scrollArea)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 300))
        self.frame_2.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(40, 40, 40);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_3.addWidget(self.frame_4)
        self.textBrowser = QtWidgets.QTextBrowser(self.frame_2)
        self.textBrowser.setStyleSheet(f"background-color: rgb(80, 80, 80); color:rgb(255, 255, 200); font-size: {self.sh}")
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_3.addWidget(self.textBrowser)
        self.verticalLayout.addWidget(self.frame_2)

        self.frame_a = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_a.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_a.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_a.setObjectName("frame")
        self.verticalLayout_2.addWidget(self.frame_are)
        self.verticalLayout_2r = QtWidgets.QHBoxLayout(self.frame_a)
        self.verticalLayout_2r.setObjectName("verticalLayout_2ar")
        self.verticalLayout.addWidget(self.frame_a)

        self.label_2 = QtWidgets.QLabel(self.frame_a)
        self.label_2.setObjectName("label_2")

        self.plus = QtWidgets.QPushButton(self.frame_a)
        self.plus.setMinimumSize(QtCore.QSize(40, 25))
        self.plus.setMaximumSize(QtCore.QSize(40, 25))
        self.plus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.plus.setStyleSheet("QPushButton {\n"
                                  "background-color: rgb(200,200,200);\n"
                                  "border-radius:10px;\n"
                                "font-size:16px;\n"
                                "}")
        self.menus = QtWidgets.QPushButton(self.frame_a)
        self.menus.setMinimumSize(QtCore.QSize(40, 25))
        self.menus.setMaximumSize(QtCore.QSize(40, 25))
        self.menus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menus.setStyleSheet("QPushButton {\n"
                                 "color:rgb(200,200,200);\n"
                                "background-color: rgb(70,70,70);\n"
                                "border-radius:10px;\n"
                                "font-size:20px;\n"
                                "}")
        self.plus.clicked.connect(self.pluss)
        self.menus.clicked.connect(self.menuss)

        self.verticalLayout_2r.addWidget(self.label_2)
        self.verticalLayout_2r.addWidget(self.plus)
        self.verticalLayout_2r.addWidget(self.menus)

        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(50, 50, 50);\n"
"color:rgb(255, 255, 255);\n"
f"font: {self.sh}pt \"Courier New\";")
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 80))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setObjectName("label_3")
        self.label_3.setMaximumSize(QtCore.QSize(100000, 40))
        self.label.setMaximumSize(QtCore.QSize  (100000, 40))
        self.horizontalLayout.addWidget(self.label_3)
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton {\n"
"background-color: rgb(170, 255, 0);\n"
"color: rgb(0, 0, 0);\n"
"border-radius:10px;\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"}")
        self.label_4.setStyleSheet("color: rgb(0, 255, 255);\n"
                                   "background-color: rgb(150, 150, 150);\n"
                                   "padding: 2px 20px;\n"
                                   "font: 75 12pt \"MS Shell Dlg 2\";\n")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ivon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(20,20))
        self.label.setStyleSheet("color: rgb(255,255,255); background-color: rgb(40,40,40); padding-left:20px;border-radius:10px")
        self.label_3.setStyleSheet("color: rgb(255,255,255); background-color: rgb(40,40,40); padding-left:20px;border-radius:10px")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.frame_3)
        self.horizontalLayout_3.addWidget(self.frame)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.frame_3.setStyleSheet("color: rgb(0,255,0); background-color: rgb(60,60,60);border-radius:10px")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", mavzu))
        self.label_4.setText(_translate("MainWindow", "Masala Nomi"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
f"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:{self.sh}pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">shart_matni</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Python codini kiriting"))
        self.label.setText(_translate("MainWindow", "0"))
        self.label_3.setText(_translate("MainWindow", "Natija"))
        self.plus.setText(_translate("MainWindow", "+"))
        self.menus.setText(_translate("MainWindow", "-"))
        self.pushButton.clicked.connect(self.Run)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
