# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DialogWindowEditPropertiesueAyHj.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QFrame, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(564, 679)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frameLangSelect = QFrame(Dialog)
        self.frameLangSelect.setObjectName(u"frameLangSelect")
        self.frameLangSelect.setFrameShape(QFrame.StyledPanel)
        self.frameLangSelect.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frameLangSelect)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelPLuginLang = QLabel(self.frameLangSelect)
        self.labelPLuginLang.setObjectName(u"labelPLuginLang")
        self.labelPLuginLang.setEnabled(True)

        self.horizontalLayout.addWidget(self.labelPLuginLang)

        self.comboBoxLangSelect = QComboBox(self.frameLangSelect)
        self.comboBoxLangSelect.setObjectName(u"comboBoxLangSelect")

        self.horizontalLayout.addWidget(self.comboBoxLangSelect)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.frameLangSelect)

        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget_place = QVBoxLayout(self.widget)
        self.widget_place.setSpacing(0)
        self.widget_place.setObjectName(u"widget_place")
        self.widget_place.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.widget)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.labelPLuginLang.setText(QCoreApplication.translate("Dialog", u"Plugin Language", None))
    # retranslateUi

