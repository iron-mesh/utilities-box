# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DialogAboutpebXnW.ui'
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
    QFrame, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import pussy_ressources_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(687, 598)
        icon = QIcon()
        icon.addFile(u":/imgs/imgs/PUSSY_Logo_min.svg", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(False)
        self.verticalLayout_4 = QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer_5 = QSpacerItem(32, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, -1)
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_7)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.label_app_logo = QLabel(Dialog)
        self.label_app_logo.setObjectName(u"label_app_logo")
        self.label_app_logo.setMaximumSize(QSize(200, 200))
        self.label_app_logo.setPixmap(QPixmap(u":/imgs/imgs/PUSSY_Logo.svg"))
        self.label_app_logo.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label_app_logo)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.version_label = QLabel(Dialog)
        self.version_label.setObjectName(u"version_label")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.version_label.sizePolicy().hasHeightForWidth())
        self.version_label.setSizePolicy(sizePolicy)
        self.version_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.version_label)

        self.version_label_edit = QLabel(Dialog)
        self.version_label_edit.setObjectName(u"version_label_edit")
        sizePolicy.setHeightForWidth(self.version_label_edit.sizePolicy().hasHeightForWidth())
        self.version_label_edit.setSizePolicy(sizePolicy)
        self.version_label_edit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.version_label_edit)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_6)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.line_6 = QFrame(Dialog)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_6)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.label_title = QLabel(Dialog)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setStyleSheet(u"font: 900 32px \"Segoe UI\";\n"
"")
        self.label_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_title)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(12, 12, 12, 12)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.label_app_desc = QLabel(Dialog)
        self.label_app_desc.setObjectName(u"label_app_desc")
        self.label_app_desc.setWordWrap(True)

        self.horizontalLayout_4.addWidget(self.label_app_desc)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.btn_python3 = QPushButton(Dialog)
        self.btn_python3.setObjectName(u"btn_python3")
        self.btn_python3.setMaximumSize(QSize(16777215, 16777213))
        self.btn_python3.setSizeIncrement(QSize(0, 0))
        self.btn_python3.setBaseSize(QSize(0, 0))
        self.btn_python3.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_python3.setStyleSheet(u"padding: 8px")
        self.btn_python3.setText(u"Python 3")
        icon1 = QIcon()
        icon1.addFile(u":/imgs/imgs/pngwing.com.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_python3.setIcon(icon1)
        self.btn_python3.setIconSize(QSize(32, 32))
        self.btn_python3.setCheckable(False)

        self.horizontalLayout_2.addWidget(self.btn_python3)

        self.btn_pyside6 = QPushButton(Dialog)
        self.btn_pyside6.setObjectName(u"btn_pyside6")
        self.btn_pyside6.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pyside6.setStyleSheet(u"padding: 8px")
        self.btn_pyside6.setText(u"PySide6")
        icon2 = QIcon()
        icon2.addFile(u":/imgs/imgs/Pyside.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pyside6.setIcon(icon2)
        self.btn_pyside6.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btn_pyside6)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(6, 6, 6, 6)
        self.btn_developerwebsite = QPushButton(Dialog)
        self.btn_developerwebsite.setObjectName(u"btn_developerwebsite")
        self.btn_developerwebsite.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_developerwebsite.setStyleSheet(u"padding: 8px")
        icon3 = QIcon()
        icon3.addFile(u":/imgs/imgs/logo_vector.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_developerwebsite.setIcon(icon3)
        self.btn_developerwebsite.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.btn_developerwebsite)

        self.btn_support_author = QPushButton(Dialog)
        self.btn_support_author.setObjectName(u"btn_support_author")
        self.btn_support_author.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_support_author.setStyleSheet(u"padding: 8px")
        icon4 = QIcon()
        icon4.addFile(u":/imgs/imgs/Like-Button-PNG.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_support_author.setIcon(icon4)
        self.btn_support_author.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.btn_support_author)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_4 = QSpacerItem(32, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.line_5 = QFrame(Dialog)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_5)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout_4.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"About PUSSY", None))
        self.label_app_logo.setText("")
        self.version_label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><span style=\" font-weight:700;\">Version: </span></body></html>", None))
        self.version_label_edit.setText("")
        self.label_title.setText(QCoreApplication.translate("Dialog", u"PUSSY", None))
        self.label_app_desc.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>PUSSY(Python Universal Script System for You) - program complex for fast development and management mini-programs with GUI on Python3 and Pyside6.  </p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Powered by:", None))
        self.btn_developerwebsite.setText(QCoreApplication.translate("Dialog", u"Developer's website", None))
        self.btn_support_author.setText(QCoreApplication.translate("Dialog", u"Support the author", None))
    # retranslateUi

