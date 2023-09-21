# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formqOeeFF.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(938, 686)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(True)
        self.lineEdit.setMaximumSize(QSize(300, 16777215))
        self.lineEdit.setStyleSheet(u"")
        self.lineEdit.setClearButtonEnabled(False)

        self.horizontalLayout.addWidget(self.lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 2, 1, 1)

        self.pushButton_13 = QPushButton(Form)
        self.pushButton_13.setObjectName(u"pushButton_13")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_13, 1, 2, 1, 1)

        self.pushButton_15 = QPushButton(Form)
        self.pushButton_15.setObjectName(u"pushButton_15")
        sizePolicy.setHeightForWidth(self.pushButton_15.sizePolicy().hasHeightForWidth())
        self.pushButton_15.setSizePolicy(sizePolicy)
        self.pushButton_15.setMinimumSize(QSize(0, 60))

        self.gridLayout.addWidget(self.pushButton_15, 2, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.pushButton_14 = QPushButton(Form)
        self.pushButton_14.setObjectName(u"pushButton_14")
        sizePolicy.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy)
        self.pushButton_14.setMinimumSize(QSize(0, 60))

        self.gridLayout.addWidget(self.pushButton_14, 1, 1, 1, 1)

        self.pushButton_18 = QPushButton(Form)
        self.pushButton_18.setObjectName(u"pushButton_18")
        sizePolicy.setHeightForWidth(self.pushButton_18.sizePolicy().hasHeightForWidth())
        self.pushButton_18.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_18, 0, 2, 1, 1)

        self.pushButton_19 = QPushButton(Form)
        self.pushButton_19.setObjectName(u"pushButton_19")
        sizePolicy.setHeightForWidth(self.pushButton_19.sizePolicy().hasHeightForWidth())
        self.pushButton_19.setSizePolicy(sizePolicy)
        self.pushButton_19.setMinimumSize(QSize(0, 60))

        self.gridLayout.addWidget(self.pushButton_19, 0, 3, 1, 1)

        self.pushButton_20 = QPushButton(Form)
        self.pushButton_20.setObjectName(u"pushButton_20")
        sizePolicy.setHeightForWidth(self.pushButton_20.sizePolicy().hasHeightForWidth())
        self.pushButton_20.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_20, 0, 1, 1, 1)

        self.pushButton_11 = QPushButton(Form)
        self.pushButton_11.setObjectName(u"pushButton_11")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy1)
        self.pushButton_11.setMinimumSize(QSize(0, 60))

        self.gridLayout.addWidget(self.pushButton_11, 3, 2, 1, 1)

        self.pushButton_16 = QPushButton(Form)
        self.pushButton_16.setObjectName(u"pushButton_16")
        sizePolicy.setHeightForWidth(self.pushButton_16.sizePolicy().hasHeightForWidth())
        self.pushButton_16.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_16, 2, 3, 1, 1)

        self.pushButton_17 = QPushButton(Form)
        self.pushButton_17.setObjectName(u"pushButton_17")
        sizePolicy.setHeightForWidth(self.pushButton_17.sizePolicy().hasHeightForWidth())
        self.pushButton_17.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_17, 1, 3, 1, 1)

        self.pushButton_12 = QPushButton(Form)
        self.pushButton_12.setObjectName(u"pushButton_12")
        sizePolicy.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_12, 2, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 4, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        QWidget.setTabOrder(self.lineEdit, self.pushButton_20)
        QWidget.setTabOrder(self.pushButton_20, self.pushButton_18)
        QWidget.setTabOrder(self.pushButton_18, self.pushButton_19)
        QWidget.setTabOrder(self.pushButton_19, self.pushButton_14)
        QWidget.setTabOrder(self.pushButton_14, self.pushButton_13)
        QWidget.setTabOrder(self.pushButton_13, self.pushButton_17)
        QWidget.setTabOrder(self.pushButton_17, self.pushButton_15)
        QWidget.setTabOrder(self.pushButton_15, self.pushButton_12)
        QWidget.setTabOrder(self.pushButton_12, self.pushButton_16)
        QWidget.setTabOrder(self.pushButton_16, self.pushButton_11)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438 \u043a\u043e\u0434 \u0437\u0430\u043c\u043a\u0430", None))
        self.pushButton_13.setText(QCoreApplication.translate("Form", u"5", None))
        self.pushButton_15.setText(QCoreApplication.translate("Form", u"8", None))
        self.pushButton_14.setText(QCoreApplication.translate("Form", u"4", None))
        self.pushButton_18.setText(QCoreApplication.translate("Form", u"2", None))
        self.pushButton_19.setText(QCoreApplication.translate("Form", u"3", None))
        self.pushButton_20.setText(QCoreApplication.translate("Form", u"1", None))
        self.pushButton_11.setText(QCoreApplication.translate("Form", u"0", None))
        self.pushButton_16.setText(QCoreApplication.translate("Form", u"7", None))
        self.pushButton_17.setText(QCoreApplication.translate("Form", u"6", None))
        self.pushButton_12.setText(QCoreApplication.translate("Form", u"9", None))
    # retranslateUi

