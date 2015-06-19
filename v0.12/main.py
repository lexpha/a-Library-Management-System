# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Fri Jun 12 23:08:54 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!
import mysql.connector
import sys
import time
from datetime import datetime
from datetime import timedelta
from PyQt4.Qt import *

reload(sys)
sys.setdefaultencoding('utf8')

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

class delblog(QtGui.QDialog):
    def __init__(self, db):
        self.db=db
        super(delblog, self).__init__()
        self.setWindowIcon(QtGui.QIcon('icon72.png'))
        #Dialog.setObjectName(_fromUtf8("Dialog"))
        #Dialog.setWindowModality(QtCore.Qt.NonModal)
        #self.setEnabled(True)
        self.resize(398, 276)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(398, 276))
        self.setMaximumSize(QtCore.QSize(398, 276))
        self.buttonBox = QtGui.QDialogButtonBox(self)
        self.buttonBox.setEnabled(True)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.widget = QtGui.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(20, 70, 337, 31))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.textEdit = QtGui.QTextEdit(self.widget)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.horizontalLayout.addWidget(self.textEdit)
        self.widget1 = QtGui.QWidget(self)
        self.widget1.setGeometry(QtCore.QRect(20, 110, 337, 31))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.widget1)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.textEdit_2 = QtGui.QTextEdit(self.widget1)
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.horizontalLayout_2.addWidget(self.textEdit_2)

        self.retranslateUi()
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.ok)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.show()

    def retranslateUi(self):
        self.setWindowTitle(_translate("Dialog", "图书归还", None))
        self.label.setText(_translate("Dialog", "读者号", None))
        self.label_2.setText(_translate("Dialog", "藏书号", None))
        
    def ok(self):
        self.db=mysql.connector.connect(user='root',password='1111yyyy',database='library',use_unicode=True,charset="utf8")
        self.stcur=self.db.cursor()
        
        self.a1=self.textEdit.toPlainText()
        #print unicode(self.a1, 'utf-8', 'ignore')
        self.a2=self.textEdit_2.toPlainText()
        #print unicode(self.a2, 'utf-8', 'ignore')
        if((self.a1!='')and(self.a2!='')):
            self.qua='delete from blog where blog.readerno="%s" and blog.bookno="%s"' %(self.a1, self.a2)
            self.judge='select * from blog where blog.readerno="%s" and blog.bookno="%s"' %(self.a1, self.a2)
            self.stcur.execute(self.judge)
            ju=self.stcur.fetchall()
            print self.qua
            
            if((len(ju))):
                self.stcur.execute(self.qua)
                self.ouch=QtGui.QMessageBox.about( self,  u"嗯..", u"还书成功~")
                self.db.commit()
                self.db.close()
                self.close()
            else:
                self.ouch=QtGui.QMessageBox.about( self,  u"Sorry..", u"还书失败，请检查读者号和藏书号！")
                self.db.close()
        #self.db.close()
        #self.close()

class delreader(QtGui.QDialog):
    def __init__(self, db):
        self.db=db
        super(delreader, self).__init__()
        #Dialog.setObjectName(_fromUtf8("Dialog"))
        #Dialog.setWindowModality(QtCore.Qt.NonModal)
        #self.setEnabled(True)
        self.resize(398, 276)
        self.setWindowIcon(QtGui.QIcon('icon72.png'))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(398, 276))
        self.setMaximumSize(QtCore.QSize(398, 276))
        self.buttonBox = QtGui.QDialogButtonBox(self)
        self.buttonBox.setEnabled(True)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.widget = QtGui.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(20, 70, 337, 31))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.textEdit = QtGui.QTextEdit(self.widget)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.horizontalLayout.addWidget(self.textEdit)
        self.widget1 = QtGui.QWidget(self)
        self.widget1.setGeometry(QtCore.QRect(20, 110, 337, 31))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.widget1)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.textEdit_2 = QtGui.QTextEdit(self.widget1)
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.horizontalLayout_2.addWidget(self.textEdit_2)

        self.retranslateUi()
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.ok)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.show()

    def retranslateUi(self):
        self.setWindowTitle(_translate("Dialog", "删除读者", None))
        self.label.setText(_translate("Dialog",   " 读者号 ", None))
        self.label_2.setText(_translate("Dialog", "读者姓名", None))
        
    def ok(self):
        self.db=mysql.connector.connect(user='root',password='1111yyyy',database='library',use_unicode=True,charset="utf8")
        self.stcur=self.db.cursor()
        
        self.a1=self.textEdit.toPlainText()
        #print unicode(self.a1, 'utf-8', 'ignore')
        self.a2=self.textEdit_2.toPlainText()
        #print unicode(self.a2, 'utf-8', 'ignore')
        if((self.a1!='')and(self.a2!='')):
            self.qua='delete from reader where readerno="%s" and rname="%s"' %(self.a1, self.a2)
            self.judge='select * from reader where readerno="%s" and rname="%s"'%(self.a1, self.a2)
            self.stcur.execute(self.judge)
            self.ju=self.stcur.fetchall()
            if(len(self.ju)):
                
                print self.qua
                self.conf=u'确定要移除 读者号为%s，姓名为%s 的读者？' %(self.a1, self.a2)
                self.reply = QtGui.QMessageBox.question(self, u'注意',self.conf, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                if self.reply == QtGui.QMessageBox.Yes:
                    self.stcur.execute(self.qua)
                    self.ouch=QtGui.QMessageBox.about( self,  u"嗯..", u"删除成功~")
                    self.db.commit()
                    self.db.close()
                    self.close()
                else:
                    self.db.close()
                
            else:
                self.ouch=QtGui.QMessageBox.about( self,  u"Sorry..", u"没有找到对应的读者！")
                self.db.close()
                self.close()
                

class delcollection(QtGui.QDialog):
    def __init__(self, db):
        self.db=db
        super(delcollection, self).__init__()
        #Dialog.setObjectName(_fromUtf8("Dialog"))
        #Dialog.setWindowModality(QtCore.Qt.NonModal)
        #self.setEnabled(True)
        self.resize(398, 276)
        self.setWindowIcon(QtGui.QIcon('icon72.png'))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(398, 276))
        self.setMaximumSize(QtCore.QSize(398, 276))
        self.buttonBox = QtGui.QDialogButtonBox(self)
        self.buttonBox.setEnabled(True)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.widget = QtGui.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(20, 70, 337, 31))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.textEdit = QtGui.QTextEdit(self.widget)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.horizontalLayout.addWidget(self.textEdit)
        self.widget1 = QtGui.QWidget(self)
        self.widget1.setGeometry(QtCore.QRect(20, 110, 337, 31))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.widget1)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.textEdit_2 = QtGui.QTextEdit(self.widget1)
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.horizontalLayout_2.addWidget(self.textEdit_2)

        self.retranslateUi()
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.ok)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.show()

    def retranslateUi(self):
        self.setWindowTitle(_translate("Dialog", "移除藏书", None))
        self.label.setText(_translate("Dialog",   "藏书号", None))
        self.label_2.setText(_translate("Dialog", " 书名 ", None))
        
    def ok(self):
        self.db=mysql.connector.connect(user='root',password='1111yyyy',database='library',use_unicode=True,charset="utf8")
        self.stcur=self.db.cursor()
        
        self.a1=self.textEdit.toPlainText()
        #print unicode(self.a1, 'utf-8', 'ignore')
        self.a2=self.textEdit_2.toPlainText()
        #print unicode(self.a2, 'utf-8', 'ignore')
        if((self.a1!='')and(self.a2!='')):
            self.qua='delete from collection where bookno="%s" and bookname="%s"' %(self.a1, self.a2)
            print self.qua
            #self.stcur.execute(self.qua)
            #self.db.commit()
            self.judge='select * from collection  where bookno="%s" and bookname="%s"'%(self.a1, self.a2)
            self.stcur.execute(self.judge)
            self.ju=self.stcur.fetchall()
            if(len(self.ju)):
                
                print self.qua
                self.conf=u'确定要移除 书号为%s，书名为%s 的藏书？' %(self.a1, self.a2)
                self.reply = QtGui.QMessageBox.question(self, u'注意：',self.conf, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                if self.reply == QtGui.QMessageBox.Yes:
                    self.stcur.execute(self.qua)
                    self.ouch=QtGui.QMessageBox.about( self,  u"嗯..", u"删除成功~")
                    self.db.commit()
                    self.db.close()
                    self.close()
                else:
                    self.db.close()
                
            else:
                self.ouch=QtGui.QMessageBox.about( self,  u"Sorry..", u"并没有找到对应的书！")
                self.db.close()
                self.close()
            
        #self.db.close()
        #self.close()

class addreader(QtGui.QDialog):
    def __init__(self, db):
        super(addreader, self).__init__()
        self.db=db
        self.initUI()
        self.a=['', '', '', '', '', '', '']
    
    def initUI(self):
        self.resize(785, 371)
        self.setWindowIcon(QtGui.QIcon('icon72.png'))
        okButton = QtGui.QPushButton("OK")
        self.table1=QtGui.QTableWidget()
        self.setWindowTitle(u'追加读者')
        self.table1.setColumnCount(6)
        self.table1.setRowCount(10)
        self.table1.setHorizontalHeaderLabels([u'读者号',u'学号' ,u'姓名' ,u'年级', u'院系',u'身份' ])
        vbox =QtGui.QVBoxLayout()
        hbox =QtGui.QHBoxLayout()
        tanhuang=QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        
        hbox.addStretch(1)
        hbox.addItem(tanhuang)
        hbox.addWidget(okButton)
        #vbox.addStretch(1)
        vbox.addWidget(self.table1)
        vbox.addLayout(hbox)
        
        self.setLayout(vbox)
        self.show()
        
        self.connect(okButton, QtCore.SIGNAL('clicked()'),self.buttonClicked)
        
     
        
    def addbook(self):
        self.erro=0
        self.db=mysql.connector.connect(user='root',password='1111yyyy',database='library',use_unicode=True,charset="utf8")
        self.stcur=self.db.cursor()
        for i in range(10):
            if  ((self.table1.item(i, 0))and(self.table1.item(i, 1))and(self.table1.item(i, 2))and(self.table1.item(i, 3))and(self.table1.item(i, 4))):
                for j in range(6):
                    self.temp= QtGui.QTableWidgetItem
                    self.temp=self.table1.item(i, j)
                    if (self.temp):
                        self.a[j]=self.temp.text()
                        if (j!=0):
                            self.a[j]=',"%s"' %(unicode(self.a[j].toUtf8(), 'utf-8', 'ignore'))
                        else:
                            self.a[j]='"%s"' %(unicode(self.a[j].toUtf8(), 'utf-8', 'ignore'))
                    else:
                            self.a[j]=',""'
                self.s='insert into reader values(%s%s%s%s%s%s)' %(self.a[0], self.a[1], self.a[2], self.a[3], self.a[4], self.a[5])
                print self.s
                try:
                    self.stcur.execute(self.s)
                    self.db.commit()
                    print self.s    
                except:
                    self.ouch=QtGui.QMessageBox.about( self,  u"呃..", u"第%s 位读者添加失败~"%(str(i+1)) )
                    self.erro=self.erro+1
                print self.s
                
        self.db.close()
    
    def buttonClicked(self):

        #sender = self.sender()
        print 'haah'
        self.addbook()
        if(self.erro==0):
            self.ouch=QtGui.QMessageBox.about( self,  u"嗯..", u"添加大成功!" )
            self.table1.clearContents()
        #self.close()

class addblog(QtGui.QDialog):
    def __init__(self, db):
        self.db=db
        super(addblog, self).__init__()
        #Dialog.setObjectName(_fromUtf8("Dialog"))
        #Dialog.setWindowModality(QtCore.Qt.NonModal)
        #self.setEnabled(True)
        self.resize(398, 276)
        self.setWindowIcon(QtGui.QIcon('icon72.png'))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(398, 276))
        self.setMaximumSize(QtCore.QSize(398, 276))
        self.buttonBox = QtGui.QDialogButtonBox(self)
        self.buttonBox.setEnabled(True)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.widget = QtGui.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(20, 70, 337, 31))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.textEdit = QtGui.QTextEdit(self.widget)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.horizontalLayout.addWidget(self.textEdit)
        self.widget1 = QtGui.QWidget(self)
        self.widget1.setGeometry(QtCore.QRect(20, 110, 337, 31))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.widget1)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.textEdit_2 = QtGui.QTextEdit(self.widget1)
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.horizontalLayout_2.addWidget(self.textEdit_2)

        self.retranslateUi()
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.ok)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.show()

    def retranslateUi(self):
        self.setWindowTitle(_translate("Dialog", "图书借阅", None))
        self.label.setText(_translate("Dialog", "读者号", None))
        self.label_2.setText(_translate("Dialog", "藏书号", None))
        
    def ok(self):
        self.db=mysql.connector.connect(user='root',password='1111yyyy',database='library',use_unicode=True,charset="utf8")
        self.stcur=self.db.cursor()
        self.a1=self.textEdit.toPlainText()
        #print unicode(self.a1, 'utf-8', 'ignore')
        self.a2=self.textEdit_2.toPlainText()
        #print unicode(self.a2, 'utf-8', 'ignore')
        if((self.a1!='')and(self.a2!='')):

            self.a3=time.strftime('%Y-%m-%d')
            self.a4=datetime.today()
            Mon = timedelta(days=30)
            self.a4=self.a4+Mon
            self.a4=self.a4.strftime('%Y-%m-%d')
        
            self.qua='insert into blog values("%s","%s","%s","%s")' %(self.a1, self.a2, self.a3, self.a4)
            self.db=mysql.connector.connect(user='root',password='1111yyyy',database='library',use_unicode=True,charset="utf8")
            self.stcur=self.db.cursor()
            try:
                self.stcur.execute(self.qua)
                self.ouch=QtGui.QMessageBox.about( self,  u"嗯", u"借阅成功~" ) 
                self.db.commit()
                self.db.close()
                self.close()
            except:
                self.ouch=QtGui.QMessageBox.about( self,  u"Sorry..", u"借阅失败，请检查读者号和藏书号！")
                self.db.close()
                #self.close()
            
        #self.db.close()
        #self.close()
    
class adddialog(QtGui.QDialog):
    def __init__(self, db):
        super(adddialog, self).__init__()
        self.db=db
        self.initUI()
        self.a=['', '', '', '', '', '', '']
    
    def initUI(self):
        self.resize(785, 371)
        self.setWindowIcon(QtGui.QIcon('icon72.png'))
        self.setWindowTitle(u'追加书籍')
        okButton = QtGui.QPushButton("OK")
        self.table1=QtGui.QTableWidget()
        self.table1.setColumnCount(7)
        self.table1.setRowCount(10)
        self.table1.setHorizontalHeaderLabels([u'书号',u'书名' ,u'isbn' ,u'作者', u'分类',u'出版社',u'备注' ])
        vbox =QtGui.QVBoxLayout()
        hbox =QtGui.QHBoxLayout()
        tanhuang=QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        
        hbox.addStretch(1)
        hbox.addItem(tanhuang)
        hbox.addWidget(okButton)
        #vbox.addStretch(1)
        vbox.addWidget(self.table1)
        vbox.addLayout(hbox)
        
        self.setLayout(vbox)
        self.show()
        
        self.connect(okButton, QtCore.SIGNAL('clicked()'),self.buttonClicked)
        
     
        
    def addbook(self):
        self.db=mysql.connector.connect(user='root',password='1111yyyy',database='library',use_unicode=True,charset="utf8")
        self.stcur=self.db.cursor()
        self.erro=0
        for i in range(10):
            if  ((self.table1.item(i, 0))):
                if(self.table1.item(i, 1)):
                    if(self.table1.item(i, 2)):
                        for j in range(7):
                            self.temp= QtGui.QTableWidgetItem
                            self.temp=self.table1.item(i, j)
                            if (self.temp):
                                self.a[j]=self.temp.text()
                                if (j!=0):
                                    self.a[j]=',"%s"' %(unicode(self.a[j].toUtf8(), 'utf-8', 'ignore'))
                                else:
                                    self.a[j]='"%s"' %(unicode(self.a[j].toUtf8(), 'utf-8', 'ignore'))
                            else:
                                self.a[j]=',""'
                        self.s='insert into collection values(%s%s%s%s%s%s%s)' %(self.a[0], self.a[1], self.a[2], self.a[3], self.a[4], self.a[5], self.a[6])
                        print self.s
                        try:
                            self.stcur.execute(self.s)
                            self.db.commit()
                            print self.s    
                        except:
                            self.ouch=QtGui.QMessageBox.about( self,  u"呃..", u"第%s本书添加失败~"%(str(i+1)) )
                            self.erro=self.erro+1
        self.db.close()
        
    
    def buttonClicked(self):

        #sender = .sender()
        print 'haah'
        self.addbook()
        if(self.erro==0):
            self.ouch=QtGui.QMessageBox.about( self,  u"嗯..", u"添加大成功！")
            self.table1.clearContents()
           
    
class Ui_MainWindow(object):
    ca=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    cb=[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    def getblog(self):
        self.qts=''
        self.qts2=''
        
        self.qts=self.textEdit_8.toPlainText()
        if (self.qts):
            self.qts2='select * from blog where readerno like "%s"' %(unicode(self.qts, 'utf-8', 'ignore'))
        else:
            self.qts2='select * from blog where readerno like "%%"'
        
        if(self.checkBox_37.isChecked()):
            self.dmin= self.dateEdit.date().toString('yyyy-MM-dd')
            self.dmax= self.dateEdit_2.date().toString('yyyy-MM-dd')
            self.qts2='%s and bdate>="%s" and otgbdate<="%s"' %(self.qts2, self.dmin, self.dmax)
        
        if(self.checkBox_41.isChecked()):
            self.dtemp=time.strftime('%Y-%m-%d')
            self.qts2='%s and otgbdate<="%s"' %(self.qts2, self.dtemp)
        
        self.qts=''
        self.qts=self.textEdit_9.toPlainText()
        #print self.qts
        if (self.qts):
            self.qts='and bookno in(select bookno from collection where bookname like "%s")' %(unicode(self.qts, 'utf-8', 'ignore'))
        else:
            self.qts=''
        #self.qts = u'%s' %(self.qts)
        self.qts2='%s %s' %(self.qts2, self.qts)
        print self.qts2

        self.tableWidget_3.clearContents()

        self.createconnection()
        self.stcur.execute(self.qts2)
        self.blog=self.stcur.fetchall()
        for i in range(len(self.blog)):
            print self.blog[i]
            self.temp= QtGui.QTableWidgetItem (self.blog[i][0])
            self.tableWidget_3.setItem(i, 0, self.temp)
            self.stcur.execute('select rname from reader where readerno like "%s"'%(self.blog[i][0]))
            self.tt=self.stcur.fetchall()
            self.temp= QtGui.QTableWidgetItem (self.tt[0][0])
            self.tableWidget_3.setItem(i, 2, self.temp)
            
            self.temp= QtGui.QTableWidgetItem (self.blog[i][1])
            self.tableWidget_3.setItem(i, 1, self.temp)
            self.stcur.execute('select bookname from collection where bookno like "%s"'%(self.blog[i][1]))
            self.tt=self.stcur.fetchall()
            print self.tt[0][0]
            self.temp= QtGui.QTableWidgetItem (self.tt[0][0])
            self.tableWidget_3.setItem(i, 3, self.temp)
            
            self.temp= QtGui.QTableWidgetItem (str(self.blog[i][2].strftime("%Y-%m-%d")))
            self.tableWidget_3.setItem(i, 4, self.temp)
            
            self.temp= QtGui.QTableWidgetItem (str(self.blog[i][3].strftime("%Y-%m-%d")))
            self.tableWidget_3.setItem(i, 5, self.temp)
        #print self.blog
        self.dropconnection()
        
        
    def getreader(self):
        self.cbs=['','','','','','','','','','','','']
        self.qts=''
        self.qts=self.textEdit.toPlainText()
        self.qts2=''
        #print self.qts
        if (self.qts):
            self.qts2='rname like "%s"' %(unicode(self.qts, 'utf-8', 'ignore'))
        else:
            self.qts2='rname like "%"'
        
        self.qts=''
        self.qts=self.textEdit_2.toPlainText()
        #print self.qts
        if (self.qts):
            self.qts='and readerno like "%s"' %(unicode(self.qts, 'utf-8', 'ignore'))
        else:
            self.qts='and readerno like "%"'
        #self.qts = u'%s' %(self.qts)
        self.qts2='%s %s' %(self.qts2, self.qts)
        
        self.qts=''
        self.qts=self.textEdit_3.toPlainText()
        #print self.qts
        if (self.qts):
            self.qts='and sno like "%s"' %(unicode(self.qts, 'utf-8', 'ignore'))
        else:
            self.qts='and sno like "%"'
        #self.qts = u'%s' %(self.qts)
        self.qts2='%s %s' %(self.qts2, self.qts)
        
        self.cb[0]=self.checkBox.isChecked()
        self.cb[1]=self.checkBox_2.isChecked()
        self.cb[2]=self.checkBox_3.isChecked()
        
        
        self.cb[3]=self.checkBox_4.isChecked()
        self.cb[4]=self.checkBox_5.isChecked()
        self.cb[5]=self.checkBox_6.isChecked()
        self.cb[6]=self.checkBox_7.isChecked()
        
        self.cb[7]=self.checkBox_8.isChecked()
        self.cb[8]=self.checkBox_9.isChecked()
        self.cb[9]=self.checkBox_10.isChecked()
        self.cb[10]=self.checkBox_11.isChecked()
        
        self.sumcb=0;
        
        if (self.cb[0]):
            self.sumcb=self.sumcb+1;
            if(self.sumcb==1):
                self.cbs[0]=' and (sk="%s"'%(u'本科生')
            else:
                self.cbs[0]=' or sk="%s"'%(u'本科生')
        else:
            self.cbs[0]=''
        
        if (self.cb[1]):
            self.sumcb=self.sumcb+1;
            if(self.sumcb==1):
                self.cbs[1]=' and (sk="%s"'%(u'研究生')
            else:
                self.cbs[1]=' or sk="%s"'%(u'研究生')
        else:
            self.cbs[1]=''
        
        if (self.cb[2]):
            self.sumcb=self.sumcb+1;
            if(self.sumcb==1):
                self.cbs[2]=' and ((sk!="%s" and sk!="%s")'%(u'本科生',u'研究生')
            else:
                self.cbs[2]=' or (sk!="%s" and sk!="%s")'%(u'本科生',u'研究生')
        else:
            self.cbs[2]=''
        
        if (self.sumcb):
            self.ss1='%s%s%s)'%(self.cbs[0], self.cbs[1], self.cbs[2])
        else:
            self.ss1=''
        #print self.ss1
        
        self.sumcb=0;
        if (self.cb[3]):
            self.sumcb=self.sumcb+1;
            if(self.sumcb==1):
                self.cbs[3]=' and (dept="%s"'%(u'计算机学院')
            else:
                self.cbs[3]=' or dept="%s"'%(u'计算机学院')
        else:
            self.cbs[3]=''
        
        if (self.cb[4]):
            self.sumcb=self.sumcb+1;
            if(self.sumcb==1):
                self.cbs[4]=' and (dept="%s"'%(u'电子信息学院')
            else:
                self.cbs[4]=' or dept="%s"'%(u'电子信息学院')
        else:
            self.cbs[4]=''
        
        if (self.cb[5]):
            self.sumcb=self.sumcb+1;
            if(self.sumcb==1):
                self.cbs[5]=' and (dept="%s"'%(u'理学院')
            else:
                self.cbs[5]=' or dept="%s"'%(u'理学院')
        else:
            self.cbs[5]=''
        
        if (self.cb[6]):
            self.sumcb=self.sumcb+1;
            if(self.sumcb==1):
                self.cbs[6]=' and ((dept!="%s" and dept!="%s" and dept!="%s")'%(u'计算机学院', u'电子信息学院', u'理学院')
            else:
                self.cbs[6]=' or (dept!="%s" and dept!="%s" and dept!="%s")'%(u'计算机学院', u'电子信息学院', u'理学院')
        else:
            self.cbs[6]=''
        
        if (self.sumcb):
            self.ss2='%s%s%s%s)'%(self.cbs[3], self.cbs[4], self.cbs[5], self.cbs[6])
        else:
            self.ss2=''
        #print self.ss2
        
        self.sumcb=0;
        if (self.cb[7]):
            self.sumcb=self.sumcb+1;
            if(self.sumcb==1):
                self.cbs[7]=' and (grade="1"'
            else:
                self.cbs[7]=' or grade="1"'
        else:
            self.cbs[7]=''
        
        if (self.cb[8]):
            self.sumcb=self.sumcb+1;
            if(self.sumcb==1):
                self.cbs[8]=' and (grade="2"'
            else:
                self.cbs[8]=' or grade="2"'
        else:
            self.cbs[8]=''
        
        if (self.cb[9]):
            self.sumcb=self.sumcb+1;
            if(self.sumcb==1):
                self.cbs[9]=' and (grade="3"'
            else:
                self.cbs[9]=' or grade="3"'
        else:
            self.cbs[9]=''
            
        if (self.cb[10]):
            self.sumcb=self.sumcb+1;
            if(self.sumcb==1):
                self.cbs[10]=' and (grade="4"'
            else:
                self.cbs[10]=' or grade="4"'
        else:
            self.cbs[10]=''
        
        if (self.sumcb):
            self.ss3='%s%s%s%s)'%(self.cbs[7], self.cbs[8], self.cbs[9], self.cbs[10])
        else:
            self.ss3=' '
        #print self.ss3
        
        self.cbss="select* from reader where %s%s%s%s"%(self.qts2, self.ss1,self.ss2,self.ss3 )
        print self.cbss
        
        self.createconnection()
        self.stcur.execute(self.cbss)
        self.reader=self.stcur.fetchall()
        self.tableWidget_2.clearContents()
        for i in range(len(self.reader)):
            for j in range(6):
                self.temp= QtGui.QTableWidgetItem (self.reader[i][j])
                self.tableWidget_2.setItem(i, j, self.temp)
        #print self.reader
        self.dropconnection()
        
        
    def getcollection(self):
        #self.ca[22]=[0]
        self.cass=''
        self.cas=['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
        self.ca[0]=self.checkBox_13.isChecked()
        self.ca[1]=self.checkBox_14.isChecked()
        self.ca[2]=self.checkBox_15.isChecked()
        self.ca[3]=self.checkBox_16.isChecked()
        self.ca[4]=self.checkBox_17.isChecked()
        self.ca[5]=self.checkBox_18.isChecked()
        self.ca[6]=self.checkBox_19.isChecked()
        self.ca[7]=self.checkBox_20.isChecked()
        self.ca[8]=self.checkBox_21.isChecked()
        self.ca[9]=self.checkBox_23.isChecked()
        self.ca[10]=self.checkBox_22.isChecked()
        self.ca[11]=self.checkBox_24.isChecked()
        self.ca[12]=self.checkBox_25.isChecked()
        self.ca[13]=self.checkBox_26.isChecked()
        self.ca[14]=self.checkBox_27.isChecked()
        self.ca[15]=self.checkBox_28.isChecked()
        self.ca[16]=self.checkBox_29.isChecked()
        self.ca[17]=self.checkBox_30.isChecked()
        self.ca[18]=self.checkBox_31.isChecked()
        self.ca[19]=self.checkBox_32.isChecked()
        self.ca[20]=self.checkBox_33.isChecked()
        self.ca[21]=self.checkBox_34.isChecked()
        self.sumca=0;
        
        self.qts=''
        self.qts=self.textEdit_4.toPlainText()
        self.qts2=''
        #print self.qts
        if (self.qts):
            self.qts2='collection.bookno like "%s"' %(unicode(self.qts, 'utf-8', 'ignore'))
        else:
            self.qts2='collection.bookno like "%"'
        #self.qts = u'%s' %(self.qts)
        
        self.qts=''
        self.qts=self.textEdit_5.toPlainText()
        #print self.qts
        if (self.qts):
            self.qts='and bookname like "%s"' %(unicode(self.qts, 'utf-8', 'ignore'))
        else:
            self.qts='and bookname like "%"'
        #self.qts = u'%s' %(self.qts)
        self.qts2='%s %s' %(self.qts2, self.qts)
        
        self.qts=''
        self.qts=self.textEdit_6.toPlainText()
        #print self.qts
        if (self.qts):
            self.qts='and aurthor like "%s"' %(unicode(self.qts, 'utf-8', 'ignore'))
        else:
            self.qts='and aurthor like "%"'
        #self.qts = u'%s' %(self.qts)
        self.qts2='%s %s' %(self.qts2, self.qts)
        
        self.qts=''
        self.qts=self.textEdit_7.toPlainText()
        #print self.qts
        if (self.qts):
            self.qts='and ISBN like "%s"' %(unicode(self.qts, 'utf-8', 'ignore'))
        else:
            self.qts='and ISBN like "%"'
        #self.qts = u'%s' %(self.qts)
        self.qts2='%s %s' %(self.qts2, self.qts)
        
       
        
        #print self.qts2
        
        if (self.ca[0]):
            self.sumca=self.sumca+1;
            if(self.sumca==1):
                self.cas[0]=' and (kind="A"'
            else:
                self.cas[0]='or kind="A"'
        else:
            self.cas[0]=''
            
        if (self.ca[1]):
            self.sumca=self.sumca+1;
            if(self.sumca==1):
                self.cas[1]=' and (kind="B"'
            else:
                self.cas[1]='or kind="B"'
        else:
            self.cas[1]=''
        
        if (self.ca[2]):
            self.sumca=self.sumca+1;
            if(self.sumca==1):
                self.cas[2]=' and (kind="C"'
            else:
                self.cas[2]='or kind="C"'
        else:
            self.cas[2]=''
            
        if (self.ca[3]):
            self.sumca=self.sumca+1;
            if(self.sumca==1):
                self.cas[3]=' and (kind="D"'
            else:
                self.cas[3]='or kind="D"'
        else:
            self.cas[3]=''
            
        if (self.ca[4]):
            self.sumca=self.sumca+1;
            if(self.sumca==1):
                self.cas[4]=' and (kind="E"'
            else:
                self.cas[4]='or kind="E"'
        else:
            self.cas[4]=''
        
            
        if (self.ca[5]):
            self.sumca=self.sumca+1;
            if(self.sumca==1):
                self.cas[5]=' and (kind="F"'
            else:
                self.cas[5]='or kind="F"'
        else:
            self.cas[5]=''
        
        if (self.ca[6]):
            self.sumca=self.sumca+1;
            if(self.sumca==1):
                self.cas[6]=' and (kind="G"'
            else:
                self.cas[6]='or kind="G"'
        else:
            self.cas[6]=''
        
        if (self.ca[7]):
            self.sumca=self.sumca+1;
            if(self.sumca==1):
                self.cas[7]=' and (kind="H"'
            else:
                self.cas[7]='or kind="H"'
        else:
            self.cas[7]=''
        
        if (self.ca[8]):
            self.sumca=self.sumca+1;
            if(self.sumca==1):
                self.cas[8]=' and (kind="I"'
            else:
                self.cas[8]='or kind="I"'
        else:
            self.cas[8]=''
        
        if (self.ca[9]):
            self.sumca=self.sumca+1;
            if(self.sumca==1):
                self.cas[9]=' and (kind="J"'
            else:
                self.cas[9]='or kind="J"'
        else:
            self.cas[9]=''
        
        if (self.ca[10]):
            self.sumca=self.sumca+1;
            if(self.sumca==1):
                self.cas[10]=' and (kind="K"'
            else:
                self.cas[10]='or kind="K"'
        else:
            self.cas[10]=''
        
        if (self.ca[11]):
            self.sumca=self.sumca+1;
            if(self.sumca==1):
                self.cas[11]=' and (kind="N"'
            else:
                self.cas[11]='or kind="N"'
        else:
            self.cas[11]=''
        
        if (self.ca[12]):
            self.sumca=self.sumca+1;
            if(self.sumca==1):
                self.cas[12]=' and (kind="O"'
            else:
                self.cas[12]='or kind="O"'
        else:
            self.cas[12]=''
            
        if (self.ca[13]):
            self.sumca=self.sumca+1;
            if(self.sumca==1):
                self.cas[13]=' and (kind="P"'
            else:
                self.cas[13]='or kind="P"'
        else:
            self.cas[13]=''
            
        if (self.ca[14]):
            self.sumca=self.sumca+1;
            if(self.sumca==1):
                self.cas[14]=' and (kind="Q"'
            else:
                self.cas[14]='or kind="Q"'
        else:
            self.cas[14]=''
        
        if (self.ca[15]):
            self.sumca=self.sumca+1;
            if(self.sumca==1):
                self.cas[15]=' and (kind="R"'
            else:
                self.cas[15]='or kind="R"'
        else:
            self.cas[15]=''
        
        if (self.ca[16]):
            self.sumca=self.sumca+1;
            if(self.sumca==1):
                self.cas[16]=' and (kind="S"'
            else:
                self.cas[16]='or kind="S"'
        else:
            self.cas[16]=''
        
        if (self.ca[17]):
            self.sumca=self.sumca+1;
            if(self.sumca==1):
                self.cas[17]=' and (kind="T"'
            else:
                self.cas[17]='or kind="T"'
        else:
            self.cas[17]=''
        
        if (self.ca[18]):
            self.sumca=self.sumca+1;
            if(self.sumca==1):
                self.cas[18]=' and (kind="U"'
            else:
                self.cas[18]='or kind="U"'
        else:
            self.cas[18]=''
        
        if (self.ca[19]):
            self.sumca=self.sumca+1;
            if(self.sumca==1):
                self.cas[19]=' and (kind="V"'
            else:
                self.cas[19]='or kind="V"'
        else:
            self.cas[19]=''
        
        if (self.ca[20]):
            self.sumca=self.sumca+1;
            if(self.sumca==1):
                self.cas[20]=' and (kind="X"'
            else:
                self.cas[20]='or kind="X"'
        else:
            self.cas[20]=''
        
        if (self.ca[21]):
            self.sumca=self.sumca+1;
            if(self.sumca==1):
                self.cas[21]=' and (kind="Z"'
            else:
                self.cas[21]='or kind="Z"'
        else:
            self.cas[21]=''
            
        if (self.sumca==0):
            self.cass=''
        else:
            self.cass='%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s)' %(self.cas[0], self.cas[1], self.cas[2], self.cas[3], self.cas[4], self.cas[5], self.cas[6], self.cas[7], self.cas[8], self.cas[9], self.cas[10], self.cas[11], self.cas[12], self.cas[13], self.cas[14], self.cas[15], self.cas[16], self.cas[17], self.cas[18], self.cas[19], self.cas[20], self.cas[21])
        #print self.sumca
        self.cass='select * \
        from collection \
        where %s%s' %(self.qts2, self.cass)
            
        if(self.checkBox_36.isChecked()):
            self.cass='%s and bookno not in(select bookno from blog)' %(self.cass)
        
        self.createconnection()
        self.stcur.execute(self.cass)
        self.collection=self.stcur.fetchall()
        self.tableWidget.clearContents()
        for i in range(len(self.collection)):
            for j in range(7):
                self.temp= QtGui.QTableWidgetItem (self.collection[i][j])
                self.tableWidget.setItem(i, j, self.temp)
        print self.collection
        self.dropconnection()
        print self.cass
        #print self.ca
        
    def createconnection(self):
        try:
            self.db=mysql.connector.connect(user='root',password='1111yyyy',database='library',use_unicode=True,charset="utf8")
            self.stcur=self.db.cursor()
        except :
            self.warn=QtGui.QMessageBox.about( MainWindow,  u"Sorry..", u"数据库连接异常，请检查数据库设置！" ) 
    def dropconnection(self):
        self.db.commit()
        self.db.close()
    
    def showtable(self):
        self.index=self.tabWidget.currentIndex ()
        if (self.index==0):
            self.showcollection()
        elif(self.index==1):
            self.showreader()
        elif(self.index==2):
            self.showblog()
            
    def gettable(self):
        self.index=self.tabWidget.currentIndex ()
        if(self.index==0):
            self.getcollection()
        elif(self.index==1):
            self.getreader()
        elif(self.index==2):
            self.getblog()
    
    def showcollection(self):
        #self.getcollectionkind()
        self.createconnection()
        self.tableWidget.clearContents()
        self.stcur.execute("select *\
        from collection")
        self.collection=self.stcur.fetchall()
        for i in range(len(self.collection)):
            for j in range(7):
                self.temp= QtGui.QTableWidgetItem (self.collection[i][j])
                self.tableWidget.setItem(i, j, self.temp)
        self.dropconnection()
        
    def showreader(self):
        #self.getcollectionkind()
        self.createconnection()
        self.stcur.execute("select *\
        from reader")
        self.tableWidget_2.clearContents()
        self.reader=self.stcur.fetchall()
        for i in range(len(self.reader)):
            for j in range(6):
                self.temp= QtGui.QTableWidgetItem (self.reader[i][j])
                self.tableWidget_2.setItem(i, j, self.temp)
        self.dropconnection()
        
    def showblog(self):
        #self.getcollectionkind()
        self.createconnection()
        self.stcur.execute('select blog.readerno,blog.bookno,reader.rname,collection.bookname,blog.bdate,blog.otgbdate from reader,blog,collection where blog.bookno=collection.bookno and reader.readerno=.blog.readerno')
        self.blog=self.stcur.fetchall()
        self.tableWidget_3.clearContents()
        for i in range(len(self.blog)):
            for j in range(6):
                if ((j==4)|(j==5)) :
                    self.dtemp=str(self.blog[i][j].strftime("%Y-%m-%d"))
                    self.temp= QtGui.QTableWidgetItem (self.dtemp)
                    self.tableWidget_3.setItem(i, j, self.temp)
                else:
                    self.temp= QtGui.QTableWidgetItem (self.blog[i][j])
                    self.tableWidget_3.setItem(i, j, self.temp)
        self.dropconnection()
    def sorry(self):
        self.ouch=QtGui.QMessageBox.about( MainWindow,  u"Sorry..", u"其实这个功能被弃置了" )    
    def about(self):
        self.about=QtGui.QMessageBox.about( MainWindow,  u"关于..", u"\n糟糕的图书馆管理系统 v0.2\n\n这个案例展示了一个糟糕的图书馆管理系统\n向世人展示了顶层设计的重要性\n所以，好孩子请勿模仿!\n\n\t——写在还没处理完bug的2015-6-15\n\n本软件及源码遵循万恶的GPL协议，所以你懂的" )
    def help(self):
        self.help=QtGui.QMessageBox.about( MainWindow,  u"帮助..", u"\n   实在抱歉还没想好   \n" )
    def newdelblog(self):
        self._eu = delblog(self.db)
    def newdelreader(self):
        self._ev = delreader(self.db)
    def newdelcollection(self):
        self._ew = delcollection(self.db)
    def newaddcollection(self):
        self._ex = adddialog(self.db)
    def newaddreader(self):
        self._ez = addreader(self.db)
    
    def newaddblog(self):
        self._ey = addblog(self.db)
        
    def freshtable1(self):
        pass

    def setupUi(self, MainWindow):
        
        MainWindow.setWindowIcon(QtGui.QIcon('icon72.png'))
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1053, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setContentsMargins(-1, 2, -1, 2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setKerning(False)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setContentsMargins(-1, 5, -1, 2)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(2)
        self.horizontalLayout_5.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_8 = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_5.addWidget(self.label_8)
        self.textEdit_4 = QtGui.QTextEdit(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_4.sizePolicy().hasHeightForWidth())
        self.textEdit_4.setSizePolicy(sizePolicy)
        self.textEdit_4.setMaximumSize(QtCore.QSize(120, 27))
        self.textEdit_4.setObjectName(_fromUtf8("textEdit_4"))
        self.horizontalLayout_5.addWidget(self.textEdit_4)
        self.label_9 = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_5.addWidget(self.label_9)
        self.textEdit_5 = QtGui.QTextEdit(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_5.sizePolicy().hasHeightForWidth())
        self.textEdit_5.setSizePolicy(sizePolicy)
        self.textEdit_5.setMaximumSize(QtCore.QSize(150, 27))
        self.textEdit_5.setObjectName(_fromUtf8("textEdit_5"))
        self.horizontalLayout_5.addWidget(self.textEdit_5)
        self.label_10 = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_5.addWidget(self.label_10)
        self.textEdit_6 = QtGui.QTextEdit(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_6.sizePolicy().hasHeightForWidth())
        self.textEdit_6.setSizePolicy(sizePolicy)
        self.textEdit_6.setMaximumSize(QtCore.QSize(150, 27))
        self.textEdit_6.setObjectName(_fromUtf8("textEdit_6"))
        self.horizontalLayout_5.addWidget(self.textEdit_6)
        self.label_11 = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_5.addWidget(self.label_11)
        self.textEdit_7 = QtGui.QTextEdit(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_7.sizePolicy().hasHeightForWidth())
        self.textEdit_7.setSizePolicy(sizePolicy)
        self.textEdit_7.setMaximumSize(QtCore.QSize(150, 27))
        self.textEdit_7.setObjectName(_fromUtf8("textEdit_7"))
        self.horizontalLayout_5.addWidget(self.textEdit_7)
        self.checkBox_36 = QtGui.QCheckBox(self.tab)
        self.checkBox_36.setObjectName(_fromUtf8("checkBox_36"))
        self.horizontalLayout_5.addWidget(self.checkBox_36)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.checkBox_24 = QtGui.QCheckBox(self.tab)
        self.checkBox_24.setObjectName(_fromUtf8("checkBox_24"))
        self.gridLayout.addWidget(self.checkBox_24, 1, 2, 1, 1)
        self.checkBox_21 = QtGui.QCheckBox(self.tab)
        self.checkBox_21.setObjectName(_fromUtf8("checkBox_21"))
        self.gridLayout.addWidget(self.checkBox_21, 0, 9, 1, 1)
        self.checkBox_31 = QtGui.QCheckBox(self.tab)
        self.checkBox_31.setObjectName(_fromUtf8("checkBox_31"))
        self.gridLayout.addWidget(self.checkBox_31, 1, 9, 1, 1)
        self.checkBox_15 = QtGui.QCheckBox(self.tab)
        self.checkBox_15.setObjectName(_fromUtf8("checkBox_15"))
        self.gridLayout.addWidget(self.checkBox_15, 0, 3, 1, 1)
        self.checkBox_17 = QtGui.QCheckBox(self.tab)
        self.checkBox_17.setObjectName(_fromUtf8("checkBox_17"))
        self.gridLayout.addWidget(self.checkBox_17, 0, 5, 1, 1)
        self.checkBox_19 = QtGui.QCheckBox(self.tab)
        self.checkBox_19.setObjectName(_fromUtf8("checkBox_19"))
        self.gridLayout.addWidget(self.checkBox_19, 0, 7, 1, 1)
        self.checkBox_20 = QtGui.QCheckBox(self.tab)
        self.checkBox_20.setObjectName(_fromUtf8("checkBox_20"))
        self.gridLayout.addWidget(self.checkBox_20, 0, 8, 1, 1)
        self.label_12 = QtGui.QLabel(self.tab)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout.addWidget(self.label_12, 0, 0, 1, 1)
        self.checkBox_18 = QtGui.QCheckBox(self.tab)
        self.checkBox_18.setObjectName(_fromUtf8("checkBox_18"))
        self.gridLayout.addWidget(self.checkBox_18, 0, 6, 1, 1)
        self.checkBox_13 = QtGui.QCheckBox(self.tab)
        self.checkBox_13.setObjectName(_fromUtf8("checkBox_13"))
        self.gridLayout.addWidget(self.checkBox_13, 0, 1, 1, 1)
        self.checkBox_14 = QtGui.QCheckBox(self.tab)
        self.checkBox_14.setObjectName(_fromUtf8("checkBox_14"))
        self.gridLayout.addWidget(self.checkBox_14, 0, 2, 1, 1)
        self.checkBox_16 = QtGui.QCheckBox(self.tab)
        self.checkBox_16.setObjectName(_fromUtf8("checkBox_16"))
        self.gridLayout.addWidget(self.checkBox_16, 0, 4, 1, 1)
        self.checkBox_29 = QtGui.QCheckBox(self.tab)
        self.checkBox_29.setObjectName(_fromUtf8("checkBox_29"))
        self.gridLayout.addWidget(self.checkBox_29, 1, 7, 1, 1)
        self.checkBox_30 = QtGui.QCheckBox(self.tab)
        self.checkBox_30.setObjectName(_fromUtf8("checkBox_30"))
        self.gridLayout.addWidget(self.checkBox_30, 1, 8, 1, 1)
        self.checkBox_23 = QtGui.QCheckBox(self.tab)
        self.checkBox_23.setObjectName(_fromUtf8("checkBox_23"))
        self.gridLayout.addWidget(self.checkBox_23, 1, 0, 1, 1)
        self.checkBox_22 = QtGui.QCheckBox(self.tab)
        self.checkBox_22.setObjectName(_fromUtf8("checkBox_22"))
        self.gridLayout.addWidget(self.checkBox_22, 1, 1, 1, 1)
        self.checkBox_26 = QtGui.QCheckBox(self.tab)
        self.checkBox_26.setObjectName(_fromUtf8("checkBox_26"))
        self.gridLayout.addWidget(self.checkBox_26, 1, 4, 1, 1)
        self.checkBox_25 = QtGui.QCheckBox(self.tab)
        self.checkBox_25.setObjectName(_fromUtf8("checkBox_25"))
        self.gridLayout.addWidget(self.checkBox_25, 1, 3, 1, 1)
        self.checkBox_27 = QtGui.QCheckBox(self.tab)
        self.checkBox_27.setObjectName(_fromUtf8("checkBox_27"))
        self.gridLayout.addWidget(self.checkBox_27, 1, 5, 1, 1)
        self.checkBox_28 = QtGui.QCheckBox(self.tab)
        self.checkBox_28.setObjectName(_fromUtf8("checkBox_28"))
        self.gridLayout.addWidget(self.checkBox_28, 1, 6, 1, 1)
        self.checkBox_32 = QtGui.QCheckBox(self.tab)
        self.checkBox_32.setObjectName(_fromUtf8("checkBox_32"))
        self.gridLayout.addWidget(self.checkBox_32, 2, 0, 1, 1)
        self.checkBox_33 = QtGui.QCheckBox(self.tab)
        self.checkBox_33.setObjectName(_fromUtf8("checkBox_33"))
        self.gridLayout.addWidget(self.checkBox_33, 2, 1, 1, 2)
        self.checkBox_34 = QtGui.QCheckBox(self.tab)
        self.checkBox_34.setObjectName(_fromUtf8("checkBox_34"))
        self.gridLayout.addWidget(self.checkBox_34, 2, 3, 1, 2)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.tableWidget = QtGui.QTableWidget(self.tab)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(200)
        self.tableWidget.setSortingEnabled(1)
        self.tableWidget.setHorizontalHeaderLabels([u'书号',u'书名' ,u'isbn' ,u'作者', u'分类',u'出版社',u'备注' ])
        self.verticalLayout_4.addWidget(self.tableWidget)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setContentsMargins(-1, 5, -1, 2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.textEdit = QtGui.QTextEdit(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.horizontalLayout_2.addWidget(self.textEdit)
        self.label_2 = QtGui.QLabel(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.textEdit_2 = QtGui.QTextEdit(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_2.sizePolicy().hasHeightForWidth())
        self.textEdit_2.setSizePolicy(sizePolicy)
        self.textEdit_2.setMinimumSize(QtCore.QSize(100, 0))
        self.textEdit_2.setMaximumSize(QtCore.QSize(120, 16777215))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.horizontalLayout_2.addWidget(self.textEdit_2)
        self.label_6 = QtGui.QLabel(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_2.addWidget(self.label_6)
        self.textEdit_3 = QtGui.QTextEdit(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_3.sizePolicy().hasHeightForWidth())
        self.textEdit_3.setSizePolicy(sizePolicy)
        self.textEdit_3.setMinimumSize(QtCore.QSize(40, 27))
        self.textEdit_3.setMaximumSize(QtCore.QSize(120, 16777215))
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.horizontalLayout_2.addWidget(self.textEdit_3)
        self.label_3 = QtGui.QLabel(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.checkBox = QtGui.QCheckBox(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.horizontalLayout_2.addWidget(self.checkBox)
        self.checkBox_2 = QtGui.QCheckBox(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_2.sizePolicy().hasHeightForWidth())
        self.checkBox_2.setSizePolicy(sizePolicy)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.horizontalLayout_2.addWidget(self.checkBox_2)
        self.checkBox_3 = QtGui.QCheckBox(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_3.sizePolicy().hasHeightForWidth())
        self.checkBox_3.setSizePolicy(sizePolicy)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.horizontalLayout_2.addWidget(self.checkBox_3)
        self.label_7 = QtGui.QLabel(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setText(_fromUtf8(""))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_2.addWidget(self.label_7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_5 = QtGui.QLabel(self.tab_2)
        self.label_5.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_4.addWidget(self.label_5)
        self.checkBox_8 = QtGui.QCheckBox(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_8.sizePolicy().hasHeightForWidth())
        self.checkBox_8.setSizePolicy(sizePolicy)
        self.checkBox_8.setObjectName(_fromUtf8("checkBox_8"))
        self.horizontalLayout_4.addWidget(self.checkBox_8)
        self.checkBox_9 = QtGui.QCheckBox(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_9.sizePolicy().hasHeightForWidth())
        self.checkBox_9.setSizePolicy(sizePolicy)
        self.checkBox_9.setObjectName(_fromUtf8("checkBox_9"))
        self.horizontalLayout_4.addWidget(self.checkBox_9)
        self.checkBox_10 = QtGui.QCheckBox(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_10.sizePolicy().hasHeightForWidth())
        self.checkBox_10.setSizePolicy(sizePolicy)
        self.checkBox_10.setObjectName(_fromUtf8("checkBox_10"))
        self.horizontalLayout_4.addWidget(self.checkBox_10)
        self.checkBox_11 = QtGui.QCheckBox(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_11.sizePolicy().hasHeightForWidth())
        self.checkBox_11.setSizePolicy(sizePolicy)
        self.checkBox_11.setObjectName(_fromUtf8("checkBox_11"))
        self.horizontalLayout_4.addWidget(self.checkBox_11)
        #self.checkBox_12 = QtGui.QCheckBox(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.checkBox_12.sizePolicy().hasHeightForWidth())
        #self.checkBox_12.setSizePolicy(sizePolicy)
        #self.checkBox_12.setObjectName(_fromUtf8("checkBox_12"))
        #self.horizontalLayout_4.addWidget(self.checkBox_12)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_4 = QtGui.QLabel(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        self.checkBox_4 = QtGui.QCheckBox(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_4.sizePolicy().hasHeightForWidth())
        self.checkBox_4.setSizePolicy(sizePolicy)
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.horizontalLayout_3.addWidget(self.checkBox_4)
        self.checkBox_5 = QtGui.QCheckBox(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_5.sizePolicy().hasHeightForWidth())
        self.checkBox_5.setSizePolicy(sizePolicy)
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.horizontalLayout_3.addWidget(self.checkBox_5)
        self.checkBox_6 = QtGui.QCheckBox(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_6.sizePolicy().hasHeightForWidth())
        self.checkBox_6.setSizePolicy(sizePolicy)
        self.checkBox_6.setObjectName(_fromUtf8("checkBox_6"))
        self.horizontalLayout_3.addWidget(self.checkBox_6)
        self.checkBox_7 = QtGui.QCheckBox(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_7.sizePolicy().hasHeightForWidth())
        self.checkBox_7.setSizePolicy(sizePolicy)
        self.checkBox_7.setObjectName(_fromUtf8("checkBox_7"))
        self.horizontalLayout_3.addWidget(self.checkBox_7)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.tableWidget_2 = QtGui.QTableWidget(self.tab_2)
        self.tableWidget_2.setObjectName(_fromUtf8("tableWidget_2"))
        self.tableWidget_2.setColumnCount(6)
        self.tableWidget_2.setRowCount(200)
        self.tableWidget_2.setHorizontalHeaderLabels([u'读者号',u'学号' ,u'姓名' ,u'年级', u'院系',u'身份' ])
        self.tableWidget_2.setSortingEnabled(1)
        self.verticalLayout_3.addWidget(self.tableWidget_2)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_13 = QtGui.QLabel(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_7.addWidget(self.label_13)
        self.textEdit_8 = QtGui.QTextEdit(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_8.sizePolicy().hasHeightForWidth())
        self.textEdit_8.setSizePolicy(sizePolicy)
        self.textEdit_8.setMinimumSize(QtCore.QSize(100, 0))
        self.textEdit_8.setMaximumSize(QtCore.QSize(120, 16777215))
        self.textEdit_8.setObjectName(_fromUtf8("textEdit_8"))
        self.horizontalLayout_7.addWidget(self.textEdit_8)
        self.label_15 = QtGui.QLabel(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_7.addWidget(self.label_15)
        self.textEdit_9 = QtGui.QTextEdit(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_9.sizePolicy().hasHeightForWidth())
        self.textEdit_9.setSizePolicy(sizePolicy)
        self.textEdit_9.setMaximumSize(QtCore.QSize(150, 27))
        self.textEdit_9.setObjectName(_fromUtf8("textEdit_9"))
        self.horizontalLayout_7.addWidget(self.textEdit_9)
        #self.label_16 = QtGui.QLabel(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        #self.label_16.setSizePolicy(sizePolicy)
        #self.label_16.setObjectName(_fromUtf8("label_16"))
        #self.horizontalLayout_7.addWidget(self.label_16)
        #self.checkBox_38 = QtGui.QCheckBox(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.checkBox_38.sizePolicy().hasHeightForWidth())
        #self.checkBox_38.setSizePolicy(sizePolicy)
        #self.checkBox_38.setChecked(True)
        #self.checkBox_38.setObjectName(_fromUtf8("checkBox_38"))
        #self.horizontalLayout_7.addWidget(self.checkBox_38)
        #self.checkBox_40 = QtGui.QCheckBox(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.checkBox_40.sizePolicy().hasHeightForWidth())
        #self.checkBox_40.setSizePolicy(sizePolicy)
        #self.checkBox_40.setObjectName(_fromUtf8("checkBox_40"))
        #self.horizontalLayout_7.addWidget(self.checkBox_40)
        #self.checkBox_39 = QtGui.QCheckBox(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.checkBox_39.sizePolicy().hasHeightForWidth())
        #self.checkBox_39.setSizePolicy(sizePolicy)
        #self.checkBox_39.setObjectName(_fromUtf8("checkBox_39"))
        #self.horizontalLayout_7.addWidget(self.checkBox_39)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.checkBox_37 = QtGui.QCheckBox(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_37.sizePolicy().hasHeightForWidth())
        self.checkBox_37.setSizePolicy(sizePolicy)
        self.checkBox_37.setObjectName(_fromUtf8("checkBox_37"))
        self.horizontalLayout_6.addWidget(self.checkBox_37)
        self.dateEdit = QtGui.QDateEdit(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit.sizePolicy().hasHeightForWidth())
        self.dateEdit.setSizePolicy(sizePolicy)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.horizontalLayout_6.addWidget(self.dateEdit)
        self.label_14 = QtGui.QLabel(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_6.addWidget(self.label_14)
        self.dateEdit_2 = QtGui.QDateEdit(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit_2.sizePolicy().hasHeightForWidth())
        self.dateEdit_2.setSizePolicy(sizePolicy)
        self.dateEdit_2.setObjectName(_fromUtf8("dateEdit_2"))
        self.horizontalLayout_6.addWidget(self.dateEdit_2)
        self.checkBox_41 = QtGui.QCheckBox(self.tab_3)
        self.checkBox_41.setObjectName(_fromUtf8("checkBox_41"))
        self.horizontalLayout_6.addWidget(self.checkBox_41)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.tableWidget_3 = QtGui.QTableWidget(self.tab_3)
        self.tableWidget_3.setObjectName(_fromUtf8("tableWidget_3"))
        self.tableWidget_3.setColumnCount(6)
        self.tableWidget_3.setRowCount(200)
        self.tableWidget_3.setHorizontalHeaderLabels([u'读者号',u'藏书号',u'姓名' ,u'书名', u'借出日期',u'应还日期' ])
        self.tableWidget_3.setSortingEnabled(1)
        self.verticalLayout_5.addWidget(self.tableWidget_3)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1053, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        self.menu_2 = QtGui.QMenu(self.menubar)
        self.menu_2.setObjectName(_fromUtf8("menu_2"))
        self.menu_3 = QtGui.QMenu(self.menubar)
        self.menu_3.setObjectName(_fromUtf8("menu_3"))
        self.menuBangzhu = QtGui.QMenu(self.menubar)
        self.menuBangzhu.setObjectName(_fromUtf8("menuBangzhu"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        self.toolBar.setIconSize(QtCore.QSize(46, 46))
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/新前缀/jie.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.action.setIcon(icon)
        self.action.setObjectName(_fromUtf8("action"))
        self.action_2 = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/新前缀/huan.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.action_2.setIcon(icon1)
        self.action_2.setObjectName(_fromUtf8("action_2"))
        self.action_3 = QtGui.QAction(MainWindow)
        self.action_3.setObjectName(_fromUtf8("action_3"))
        self.action_4 = QtGui.QAction(MainWindow)
        self.action_4.setObjectName(_fromUtf8("action_4"))
        self.action_5 = QtGui.QAction(MainWindow)
        self.action_5.setObjectName(_fromUtf8("action_5"))
        self.action_6 = QtGui.QAction(MainWindow)
        self.action_6.setObjectName(_fromUtf8("action_6"))
        self.action_7 = QtGui.QAction(MainWindow)
        self.action_7.setObjectName(_fromUtf8("action_7"))
        self.action_8 = QtGui.QAction(MainWindow)
        self.action_8.setObjectName(_fromUtf8("action_8"))
        self.action_9 = QtGui.QAction(MainWindow)
        self.action_9.setObjectName(_fromUtf8("action_9"))
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu_2.addAction(self.action_3)
        self.menu_2.addAction(self.action_4)
        self.menu_3.addAction(self.action_5)
        self.menu_3.addAction(self.action_7)
        self.menu_3.addAction(self.action_6)
        self.menuBangzhu.addAction(self.action_8)
        self.menuBangzhu.addAction(self.action_9)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menuBangzhu.menuAction())
        self.toolBar.addAction(self.action)
        self.toolBar.addAction(self.action_2)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL("clicked()"), self.showtable)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.gettable)
        
        QtCore.QObject.connect(self.action, QtCore.SIGNAL("triggered()"), self.newaddblog)
        QtCore.QObject.connect(self.action_3, QtCore.SIGNAL("triggered()"), self.newaddcollection)
        QtCore.QObject.connect(self.action_5, QtCore.SIGNAL("triggered()"), self.newaddreader)

        QtCore.QObject.connect(self.action_2, QtCore.SIGNAL("triggered()"), self.newdelblog)
        QtCore.QObject.connect(self.action_4, QtCore.SIGNAL("triggered()"), self.newdelcollection)
        QtCore.QObject.connect(self.action_6, QtCore.SIGNAL("triggered()"), self.newdelreader)        
        
        QtCore.QObject.connect(self.action_7, QtCore.SIGNAL("triggered()"), self.sorry)
        QtCore.QObject.connect(self.action_8, QtCore.SIGNAL("triggered()"), self.help)        
        QtCore.QObject.connect(self.action_9, QtCore.SIGNAL("triggered()"), self.about)        

        
        
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "糟糕的图书馆管理系统", None))
        self.label_8.setText(_translate("MainWindow", "藏书号", None))
        self.label_9.setText(_translate("MainWindow", "书名", None))
        self.label_10.setText(_translate("MainWindow", "作者", None))
        self.label_11.setText(_translate("MainWindow", "ISBN", None))
        self.checkBox_36.setText(_translate("MainWindow", "只显示未借", None))
        self.checkBox_24.setText(_translate("MainWindow", "N自科总论", None))
        self.checkBox_21.setText(_translate("MainWindow", "I 文学", None))
        self.checkBox_31.setText(_translate("MainWindow", "U交通运输", None))
        self.checkBox_15.setText(_translate("MainWindow", "C社科总论", None))
        self.checkBox_17.setText(_translate("MainWindow", "E军事", None))
        self.checkBox_19.setText(_translate("MainWindow", "G文体科教", None))
        self.checkBox_20.setText(_translate("MainWindow", "H语言文字", None))
        self.label_12.setText(_translate("MainWindow", "类别", None))
        self.checkBox_18.setText(_translate("MainWindow", "F经济", None))
        self.checkBox_13.setText(_translate("MainWindow", "A马毛邓", None))
        self.checkBox_14.setText(_translate("MainWindow", "B哲学宗教", None))
        self.checkBox_16.setText(_translate("MainWindow", "D政法", None))
        self.checkBox_29.setText(_translate("MainWindow", "S农业科学", None))
        self.checkBox_30.setText(_translate("MainWindow", "T工业技术", None))
        self.checkBox_23.setText(_translate("MainWindow", "J艺术", None))
        self.checkBox_22.setText(_translate("MainWindow", "K历史地理", None))
        self.checkBox_26.setText(_translate("MainWindow", "P天文学", None))
        self.checkBox_25.setText(_translate("MainWindow", "O数理化", None))
        self.checkBox_27.setText(_translate("MainWindow", "Q生物科学", None))
        self.checkBox_28.setText(_translate("MainWindow", "R医药卫生", None))
        self.checkBox_32.setText(_translate("MainWindow", "V航空航天", None))
        self.checkBox_33.setText(_translate("MainWindow", "X环境科学、劳动保护科学", None))
        self.checkBox_34.setText(_translate("MainWindow", "Z综合性图书", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "书籍", None))
        self.label.setText(_translate("MainWindow", "姓名", None))
        self.label_2.setText(_translate("MainWindow", "读者号", None))
        self.label_6.setText(_translate("MainWindow", "学号", None))
        self.label_3.setText(_translate("MainWindow", " 读者身份", None))
        self.checkBox.setText(_translate("MainWindow", "本科生", None))
        self.checkBox_2.setText(_translate("MainWindow", "研究生", None))
        self.checkBox_3.setText(_translate("MainWindow", "其他", None))
        self.label_5.setText(_translate("MainWindow", "年级", None))
        self.checkBox_8.setText(_translate("MainWindow", "1", None))
        self.checkBox_9.setText(_translate("MainWindow", "2", None))
        self.checkBox_10.setText(_translate("MainWindow", "3", None))
        self.checkBox_11.setText(_translate("MainWindow", "4", None))
        #self.checkBox_12.setText(_translate("MainWindow", "其他", None))
        self.label_4.setText(_translate("MainWindow", "部门院系", None))
        self.checkBox_4.setText(_translate("MainWindow", "计算机学院", None))
        self.checkBox_5.setText(_translate("MainWindow", "电子信息学院", None))
        self.checkBox_6.setText(_translate("MainWindow", "理学院", None))
        self.checkBox_7.setText(_translate("MainWindow", "其他", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "读者", None))
        self.label_13.setText(_translate("MainWindow", "读者号", None))
        self.label_15.setText(_translate("MainWindow", "书名", None))
        #self.label_16.setText(_translate("MainWindow", "读者身份", None))
        #self.checkBox_38.setText(_translate("MainWindow", "本科生", None))
        #self.checkBox_40.setText(_translate("MainWindow", "研究生", None))
        #self.checkBox_39.setText(_translate("MainWindow", "其他", None))
        self.checkBox_37.setText(_translate("MainWindow", "日期范围", None))
        self.label_14.setText(_translate("MainWindow", "——", None))
        self.checkBox_41.setText(_translate("MainWindow", "只显示超期借阅", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "借阅查询", None))
        self.pushButton.setText(_translate("MainWindow", "查询", None))
        self.pushButton_2.setText(_translate("MainWindow", "刷新", None))
        self.menu.setTitle(_translate("MainWindow", "图书借还", None))
        self.menu_2.setTitle(_translate("MainWindow", "藏书管理", None))
        self.menu_3.setTitle(_translate("MainWindow", "读者管理", None))
        self.menuBangzhu.setTitle(_translate("MainWindow", "帮助", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.action.setText(_translate("MainWindow", "图书借阅", None))
        self.action_2.setText(_translate("MainWindow", "图书归还", None))
        self.action_3.setText(_translate("MainWindow", "增加书目", None))
        self.action_4.setText(_translate("MainWindow", "删除书目", None))
        self.action_5.setText(_translate("MainWindow", "增加读者", None))
        self.action_6.setText(_translate("MainWindow", "删除读者", None))
        self.action_7.setText(_translate("MainWindow", "修改读者信息", None))
        self.action_8.setText(_translate("MainWindow", "帮助", None))
        self.action_9.setText(_translate("MainWindow", "关于", None))

import way

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    ui.showcollection()
    ui.showreader()
    ui.showblog()
    MainWindow.show()
    sys.exit(app.exec_())    

