# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DialogPluginInfoMCeKpc.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFormLayout, QLabel, QPushButton, QScrollArea,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(556, 530)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(Dialog)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 536, 480))
        self.formLayout = QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.formLayout.setHorizontalSpacing(8)
        self.formLayout.setVerticalSpacing(11)
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-weight: Bold")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.name_label = QLabel(self.scrollAreaWidgetContents)
        self.name_label.setObjectName(u"name_label")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.name_label)

        self.description_label = QLabel(self.scrollAreaWidgetContents)
        self.description_label.setObjectName(u"description_label")
        self.description_label.setWordWrap(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.description_label)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font-weight: Bold")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_6)

        self.author_name_label = QLabel(self.scrollAreaWidgetContents)
        self.author_name_label.setObjectName(u"author_name_label")
        self.author_name_label.setWordWrap(True)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.author_name_label)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"font-weight: Bold")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_7)

        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"font-weight: Bold")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_9)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font-weight: Bold")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.version_label = QLabel(self.scrollAreaWidgetContents)
        self.version_label.setObjectName(u"version_label")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.version_label)

        self.author_email_btn = QPushButton(self.scrollAreaWidgetContents)
        self.author_email_btn.setObjectName(u"author_email_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.author_email_btn.sizePolicy().hasHeightForWidth())
        self.author_email_btn.setSizePolicy(sizePolicy)
        self.author_email_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.author_email_btn.setStyleSheet(u"QPushButton{color:blue}\n"
"\n"
":hover{\n"
"		color:rgb(255, 149, 0);\n"
"		text-decoration: underline;\n"
"}")
        self.author_email_btn.setFlat(True)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.author_email_btn)

        self.label_11 = QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"font-weight: Bold")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_11)

        self.author_url_btn = QPushButton(self.scrollAreaWidgetContents)
        self.author_url_btn.setObjectName(u"author_url_btn")
        sizePolicy.setHeightForWidth(self.author_url_btn.sizePolicy().hasHeightForWidth())
        self.author_url_btn.setSizePolicy(sizePolicy)
        self.author_url_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.author_url_btn.setStyleSheet(u"QPushButton{color:blue}\n"
"\n"
":hover{\n"
"		color:rgb(255, 149, 0);\n"
"		text-decoration: underline;\n"
"}")
        self.author_url_btn.setFlat(True)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.author_url_btn)

        self.label_13 = QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"font-weight: Bold")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_13)

        self.wiki_url_btn = QPushButton(self.scrollAreaWidgetContents)
        self.wiki_url_btn.setObjectName(u"wiki_url_btn")
        sizePolicy.setHeightForWidth(self.wiki_url_btn.sizePolicy().hasHeightForWidth())
        self.wiki_url_btn.setSizePolicy(sizePolicy)
        self.wiki_url_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.wiki_url_btn.setStyleSheet(u"QPushButton{color:blue}\n"
"\n"
":hover{\n"
"		color:rgb(255, 149, 0);\n"
"		text-decoration: underline;\n"
"}")
        self.wiki_url_btn.setFlat(True)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.wiki_url_btn)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Plugin Info", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Name:", None))
        self.name_label.setText(QCoreApplication.translate("Dialog", u"This is name", None))
        self.description_label.setText(QCoreApplication.translate("Dialog", u"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Author:", None))
        self.author_name_label.setText(QCoreApplication.translate("Dialog", u"Ivan Balakirev", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Author's Emai:", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Version:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Description:", None))
        self.version_label.setText(QCoreApplication.translate("Dialog", u"0.0.0", None))
        self.author_email_btn.setText(QCoreApplication.translate("Dialog", u"products@ironmesh.ru", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Author's Webpage:", None))
        self.author_url_btn.setText(QCoreApplication.translate("Dialog", u"www.ironmesh.ru", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"Wiki URL:", None))
        self.wiki_url_btn.setText(QCoreApplication.translate("Dialog", u"wiki", None))
    # retranslateUi

