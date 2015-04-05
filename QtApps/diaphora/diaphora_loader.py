# -*- coding: utf-8 -*-

import PySide
from PySide import QtCore, QtGui

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

class Ui_TabWidget(object):
    def setupUi(self, TabWidget):
        TabWidget.setObjectName(_fromUtf8("TabWidget"))
        TabWidget.resize(400, 300)
        TabWidget.setStyleSheet(_fromUtf8("QWidget { \n"
"    background-color: #363636;\n"
"    color: #ddd;\n"
"}\n"
"\n"
"QCheckBox {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"\n"
"QTextEdit {\n"
"    background-color: #2d2d2d;\n"
"    border: 1px solid #363636;\n"
"}\n"
"\n"
"QMenuBar, QMenuBar::item {\n"
"    background-color: #444444;\n"
"    color: #ddd;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: 1px solid #474747;\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QLineEdit:hover, QLineEdit:focus {\n"
"    border: 1px solid #00aaaa;    \n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #555555, stop: 1 #444444);\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background-color: #777777;\n"
"}\n"
"\n"
"QTreeView::item {\n"
"    font-size: 8px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #444;\n"
"    border-left: 3px solid #666;\n"
"\n"
"}\n"
"\n"
"QTableView {\n"
"    border: 1px solid #474747;\n"
"}\n"
"\n"
"QTableView {\n"
"    background-color: #2d2d2d;\n"
"}\n"
"\n"
"IDAView, hexview_t, CustomIDAMemo {\n"
"    font-family: \"Consolas\";\n"
"    font-size: 9pt;\n"
"    border: none;\n"
"}\n"
"\n"
"QScrollBar {\n"
"    background-color: #363636;\n"
"    width: 20px;\n"
"    margin: 0 0 0 0;\n"
"}\n"
"\n"
"QScrollBar::sub-line, QScrollBar::add-line {\n"
"    background: none;\n"
"}\n"
"\n"
"/*\n"
"QScrollBar:horizontal {\n"
"    padding: 0 20px 0 20px;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    padding: 20px 0 20px 0;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    image: url(%down-arrow.png%);\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"    width: 20px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"    width: 20px;\n"
"}*/\n"
"\n"
"QScrollBar::add-page, QScrollBar::sub-page {\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    min-width: 20px;\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"    background-color: #585858;\n"
"    margin: 3px;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QToolBar {\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: 1px solid #077;\n"
"    text-align: center;\n"
"    min-height: 20px;\n"
"    min-width: 50px;\n"
"    \n"
"    padding: 0 6px 0 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 1px solid #0aa;\n"
"}\n"
"\n"
"QPushButton::text {\n"
"    background-color: red;\n"
"}\n"
"\n"
"QComboBox {\n"
"    border: 1px solid #474747;\n"
"}\n"
"\n"
"GraphQObject {\n"
"    background-color: red;\n"
"    padding: 100px;\n"
"}\n"
"\n"
"ChooserContainer {\n"
"    border: 1px solid green;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton {\n"
"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 6px;\n"
"padding: 5px;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #888);\n"
"min-width: 80px;\n"
"}\n"
" \n"
"QPushButton:hover {\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #bbb);\n"
"}\n"
" \n"
"QPushButton:pressed {\n"
"background: qradialgradient(cx: 0.4, cy: -0.1,\n"
"fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd);\n"
"}\n"
""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.bt_Launch = QtGui.QPushButton(self.tab)
        self.bt_Launch.setGeometry(QtCore.QRect(130, 100, 111, 51))
        self.bt_Launch.setObjectName(_fromUtf8("bt_Launch"))
        TabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab1 = QtGui.QWidget()
        self.tab1.setObjectName(_fromUtf8("tab1"))
        self.bt_Inbrow = QtGui.QPushButton(self.tab1)
        self.bt_Inbrow.setGeometry(QtCore.QRect(140, 80, 94, 34))
        self.bt_Inbrow.setStyleSheet(_fromUtf8(""))
        self.bt_Inbrow.setObjectName(_fromUtf8("bt_Inbrow"))
        self.bt_Inword = QtGui.QPushButton(self.tab1)
        self.bt_Inword.setGeometry(QtCore.QRect(140, 120, 94, 34))
        self.bt_Inword.setStyleSheet(_fromUtf8(""))
        self.bt_Inword.setObjectName(_fromUtf8("bt_Inword"))
        self.bt_Pdf = QtGui.QPushButton(self.tab1)
        self.bt_Pdf.setGeometry(QtCore.QRect(140, 160, 94, 34))
        self.bt_Pdf.setObjectName(_fromUtf8("bt_Pdf"))
        TabWidget.addTab(self.tab1, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.label = QtGui.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(20, 10, 81, 51))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.bt_Githubs = QtGui.QPushButton(self.tab_2)
        self.bt_Githubs.setGeometry(QtCore.QRect(140, 32, 111, 41))
        self.bt_Githubs.setObjectName(_fromUtf8("bt_Githubs"))
        self.bt_Intieets = QtGui.QPushButton(self.tab_2)
        self.bt_Intieets.setGeometry(QtCore.QRect(140, 80, 111, 41))
        self.bt_Intieets.setObjectName(_fromUtf8("bt_Intieets"))
        self.bt_Inbloogs = QtGui.QPushButton(self.tab_2)
        self.bt_Inbloogs.setGeometry(QtCore.QRect(140, 130, 111, 41))
        self.bt_Inbloogs.setObjectName(_fromUtf8("bt_Inbloogs"))
        self.label_2 = QtGui.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 111, 41))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 101, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(10, 140, 121, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        TabWidget.addTab(self.tab_2, _fromUtf8(""))

        self.retranslateUi(TabWidget)
        TabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    def retranslateUi(self, TabWidget):
        TabWidget.setWindowTitle(_translate("TabWidget", "Diaphora BinDiffing Tool", None))
        self.bt_Launch.setToolTip(_translate("TabWidget", "<html><head/><body><p>Launch Diaphora plugin.</p></body></html>", None))
        self.bt_Launch.setText(_translate("TabWidget", "Launch Diaphora", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab), _translate("TabWidget", "Run Plugin", None))
        self.bt_Inbrow.setToolTip(_translate("TabWidget", "<html><head/><body><p>Open in Browser</p></body></html>", None))
        self.bt_Inbrow.setText(_translate("TabWidget", "Doc html", None))
        self.bt_Inword.setToolTip(_translate("TabWidget", "<html><head/><body><p>Open in Word</p></body></html>", None))
        self.bt_Inword.setText(_translate("TabWidget", "Doc Word", None))
        self.bt_Pdf.setToolTip(_translate("TabWidget", "<html><head/><body><p>Open in with adobe reader</p></body></html>", None))
        self.bt_Pdf.setText(_translate("TabWidget", "Doc Pdf", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab1), _translate("TabWidget", "Help", None))
        self.bt_Githubs.setText(_translate("TabWidget", "diaphora github", None))
        self.bt_Intieets.setText(_translate("TabWidget", "Twitter", None))
        self.bt_Inbloogs.setText(_translate("TabWidget", "Blog", None))
        self.label_2.setText(_translate("TabWidget", "Visit Github", None))
        self.label_3.setText(_translate("TabWidget", " Joxean on Twitter", None))
        self.label_4.setText(_translate("TabWidget", " Joxean Koret Blog", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_2), _translate("TabWidget", "Author", None))

        '''
        We want commands
        '''
        self.bt_Launch.clicked.connect(self.sesami)
        self.bt_Inbrow.clicked.connect(self.sesami2)
        self.bt_Inword.clicked.connect(self.sesami3)
        self.bt_Pdf.clicked.connect(self.sesami4)
        self.bt_Githubs.clicked.connect(self.sesami5)
        self.bt_Intieets.clicked.connect(self.sesami6)
        self.bt_Inbloogs.clicked.connect(self.sesami7)


        '''
        definitions
        '''
    def sesami(self):
        g = globals()
        idahome = idaapi.idadir("QTApps\\diaphora")
        IDAPython_ExecScript(idahome +  "\\diaphora.py", g)

    def sesami2(self):
        import os
        import sys
        import webbrowser
        idahome = idaapi.idadir("QTApps\\diaphora")
        import webbrowser
        webbrowser.open(idahome + '\\doc\\diaphora_help.html')

    def sesami3(self):
        import os
        import sys
        import webbrowser
        idahome = idaapi.idadir("QTApps\\diaphora")
        import webbrowser
        webbrowser.open(idahome + '\\doc\\diaphora_help.odt')

    def sesami4(self):
        import os
        import sys
        import webbrowser
        idahome = idaapi.idadir("QTApps\\diaphora")
        import webbrowser
        webbrowser.open(idahome + '\\doc\\diaphora_help.pdf')

    def sesami5(self):
        idaapi.open_url('http://github.com')

    def sesami6(self):
        idaapi.open_url('https://twitter.com/matalaz')

    def sesami7(self):
        idaapi.open_url('http://joxeankoret.com/')



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication.instance()
    if not app:
        app = QtGui.QApplication([])
    TabWidget = QtGui.QTabWidget()
    ui = Ui_TabWidget()
    ui.setupUi(TabWidget)
    TabWidget.show()
    app.exec_()

