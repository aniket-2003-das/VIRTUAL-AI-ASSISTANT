from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1538, 922)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1541, 931))
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.neurons = QtWidgets.QLabel(self.centralwidget)
        self.neurons.setGeometry(QtCore.QRect(0, 0, 1541, 921))
        self.neurons.setStyleSheet("border: 6px Solid White")
        self.neurons.setText("")
        self.neurons.setPixmap(QtGui.QPixmap("c:\\Users\\anike\\OneDrive\\Desktop\\Python\\Virtual-AI-Assistant\\Gui_Gifs/neurons.gif"))
        self.neurons.setScaledContents(True)
        self.neurons.setObjectName("neurons")

        self.brain = QtWidgets.QLabel(self.centralwidget)
        self.brain.setGeometry(QtCore.QRect(50, 40, 311, 241))
        self.brain.setStyleSheet("border: 5px Solid White")
        self.brain.setText("")
        self.brain.setPixmap(QtGui.QPixmap("c:\\Users\\anike\\OneDrive\\Desktop\\Python\\Virtual-AI-Assistant\\Gui_Gifs/brain.gif"))
        self.brain.setScaledContents(True)
        self.brain.setObjectName("brain")

        self.face = QtWidgets.QLabel(self.centralwidget)
        self.face.setGeometry(QtCore.QRect(430, 40, 541, 361))
        self.face.setStyleSheet("border: 5px Solid White\n"
"")
        self.face.setText("")
        self.face.setPixmap(QtGui.QPixmap("c:\\Users\\anike\\OneDrive\\Desktop\\Python\\Virtual-AI-Assistant\\Gui_Gifs/face.gif"))
        self.face.setScaledContents(True)
        self.face.setObjectName("face")

        self.speed = QtWidgets.QLabel(self.centralwidget)
        self.speed.setGeometry(QtCore.QRect(1000, 40, 501, 181))
        self.speed.setStyleSheet("border: 4px Solid White")
        self.speed.setText("")
        self.speed.setPixmap(QtGui.QPixmap("c:\\Users\\anike\\OneDrive\\Desktop\\Python\\Virtual-AI-Assistant\\Gui_Gifs/speed.gif"))
        self.speed.setScaledContents(True)
        self.speed.setObjectName("speed")

        self.close = QtWidgets.QPushButton(self.centralwidget)
        self.close.setGeometry(QtCore.QRect(720, 450, 231, 61))
        self.close.setStyleSheet("background-color: rgb(0, 25, 255);\n"
"font: 28pt \"Algerian\";\n"
"text-decoration: underline;\n"
"border: 5px Solid White")
        self.close.setObjectName("close")

        self.micon = QtWidgets.QPushButton(self.centralwidget)
        self.micon.setGeometry(QtCore.QRect(720, 540, 231, 61))
        self.micon.setStyleSheet("background-color: rgb(0, 25, 255);\n"
"font: 28pt \"Algerian\";\n"
"text-decoration: underline;\n"
"border: 5px Solid White\n"
"")
        self.micon.setObjectName("micon")

        self.loading = QtWidgets.QLabel(self.centralwidget)
        self.loading.setGeometry(QtCore.QRect(20, 810, 511, 91))
        self.loading.setStyleSheet("border: 5px Solid White")
        self.loading.setText("")
        self.loading.setPixmap(QtGui.QPixmap("c:\\Users\\anike\\OneDrive\\Desktop\\Python\\Virtual-AI-Assistant\\Gui_Gifs/loading.gif"))
        self.loading.setScaledContents(True)
        self.loading.setObjectName("loading")

        self.voiceball = QtWidgets.QLabel(self.centralwidget)
        self.voiceball.setGeometry(QtCore.QRect(460, 430, 231, 191))
        self.voiceball.setStyleSheet("border: 5px Solid White")
        self.voiceball.setText("")
        self.voiceball.setPixmap(QtGui.QPixmap("c:\\Users\\anike\\OneDrive\\Desktop\\Python\\Virtual-AI-Assistant\\Gui_Gifs/voiceball.gif"))
        self.voiceball.setScaledContents(True)
        self.voiceball.setObjectName("voiceball")

        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(30, 310, 371, 271))
        self.textBrowser_2.setStyleSheet("background-color: rgb(29, 0, 255);\n"
"border:4px Solid White")
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.soundwave = QtWidgets.QLabel(self.centralwidget)
        self.soundwave.setGeometry(QtCore.QRect(960, 790, 561, 111))
        self.soundwave.setStyleSheet("border: 5px Solid White")
        self.soundwave.setText("")
        self.soundwave.setPixmap(QtGui.QPixmap("c:\\Users\\anike\\OneDrive\\Desktop\\Python\\Virtual-AI-Assistant\\Gui_Gifs/soundwaves.gif"))
        self.soundwave.setScaledContents(True)
        self.soundwave.setObjectName("soundwave")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "VIRTUAL AI-ASSISTANT-: EMILLY"))
        self.close.setText(_translate("MainWindow", "CLOSE"))
        self.micon.setText(_translate("MainWindow", "MIC ON"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; text-decoration: underline;\">AI-ASSISTANT-: EMILLY.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600; text-decoration: underline;\">-MACHINE LEARNING.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600; text-decoration: underline;\">-DEEP LEARNING.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600; text-decoration: underline;\">-NEURAL NETWORKING.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600; text-decoration: underline;\">-NATURAL LANGUAGE PROCESSING.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600; text-decoration: underline;\">-WEB SCRAPING.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600; text-decoration: underline;\">-HOME AUTOMATION.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600; text-decoration: underline;\">-OPEN-AI CHATBOT.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600; text-decoration: underline;\">-SPACE EXPLORATION.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600; text-decoration: underline;\">-PERSIONALISED OS OPERATIONS.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600; text-decoration: underline;\">-TEXT MESSEGING.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; text-decoration: underline;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec_())