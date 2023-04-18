# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UtilitiesBoxMainWindowaicbBO.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(894, 739)
        self.menu_settings = QAction(MainWindow)
        self.menu_settings.setObjectName(u"menu_settings")
        self.menu_exit = QAction(MainWindow)
        self.menu_exit.setObjectName(u"menu_exit")
        self.menu_manual = QAction(MainWindow)
        self.menu_manual.setObjectName(u"menu_manual")
        self.menu_about = QAction(MainWindow)
        self.menu_about.setObjectName(u"menu_about")
        self.menu_plugins = QAction(MainWindow)
        self.menu_plugins.setObjectName(u"menu_plugins")
        self.menu_logs = QAction(MainWindow)
        self.menu_logs.setObjectName(u"menu_logs")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        self.widgets_page = QWidget()
        self.widgets_page.setObjectName(u"widgets_page")
        self.verticalLayout = QVBoxLayout(self.widgets_page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidgetPlugins = QTabWidget(self.widgets_page)
        self.tabWidgetPlugins.setObjectName(u"tabWidgetPlugins")
        self.tabWidgetPlugins.setDocumentMode(False)
        self.tabWidgetPlugins.setTabsClosable(False)
        self.tabWidgetPlugins.setMovable(True)
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidgetPlugins.addTab(self.tab_2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidgetPlugins.addTab(self.tab, "")

        self.verticalLayout.addWidget(self.tabWidgetPlugins)

        self.stackedWidget.addWidget(self.widgets_page)
        self.plugins_list = QWidget()
        self.plugins_list.setObjectName(u"plugins_list")
        self.verticalLayout_2 = QVBoxLayout(self.plugins_list)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButtonClosePluginPage = QPushButton(self.plugins_list)
        self.pushButtonClosePluginPage.setObjectName(u"pushButtonClosePluginPage")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonClosePluginPage.setFont(font)
        self.pushButtonClosePluginPage.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(251, 55, 30);")
        self.pushButtonClosePluginPage.setFlat(False)

        self.horizontalLayout_2.addWidget(self.pushButtonClosePluginPage)

        self.horizontalSpacer_6 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.btnReloadPlugins = QPushButton(self.plugins_list)
        self.btnReloadPlugins.setObjectName(u"btnReloadPlugins")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnReloadPlugins.sizePolicy().hasHeightForWidth())
        self.btnReloadPlugins.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamily(u"MS Shell Dlg 2")
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setWeight(75)
        self.btnReloadPlugins.setFont(font1)
        self.btnReloadPlugins.setStyleSheet(u"")
        self.btnReloadPlugins.setFlat(False)

        self.horizontalLayout_2.addWidget(self.btnReloadPlugins)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.labelPluginsPageTitle = QLabel(self.plugins_list)
        self.labelPluginsPageTitle.setObjectName(u"labelPluginsPageTitle")
        font2 = QFont()
        font2.setFamily(u"Arial Black")
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setWeight(75)
        self.labelPluginsPageTitle.setFont(font2)

        self.horizontalLayout_2.addWidget(self.labelPluginsPageTitle)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.line_2 = QFrame(self.plugins_list)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.scrollAreaPlugins = QScrollArea(self.plugins_list)
        self.scrollAreaPlugins.setObjectName(u"scrollAreaPlugins")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollAreaPlugins.sizePolicy().hasHeightForWidth())
        self.scrollAreaPlugins.setSizePolicy(sizePolicy1)
        self.scrollAreaPlugins.setFrameShape(QFrame.Box)
        self.scrollAreaPlugins.setLineWidth(1)
        self.scrollAreaPlugins.setMidLineWidth(0)
        self.scrollAreaPlugins.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollAreaPlugins.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 854, 604))
        self.scrollAreaPlugins.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollAreaPlugins)

        self.stackedWidget.addWidget(self.plugins_list)
        self.settings = QWidget()
        self.settings.setObjectName(u"settings")
        self.verticalLayout_3 = QVBoxLayout(self.settings)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButtonCloseSettingsPage = QPushButton(self.settings)
        self.pushButtonCloseSettingsPage.setObjectName(u"pushButtonCloseSettingsPage")
        self.pushButtonCloseSettingsPage.setFont(font1)
        self.pushButtonCloseSettingsPage.setToolTipDuration(-1)
        self.pushButtonCloseSettingsPage.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(251, 55, 30);")
        self.pushButtonCloseSettingsPage.setFlat(False)

        self.horizontalLayout_3.addWidget(self.pushButtonCloseSettingsPage)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.labelSettingsPageTitle = QLabel(self.settings)
        self.labelSettingsPageTitle.setObjectName(u"labelSettingsPageTitle")
        self.labelSettingsPageTitle.setFont(font2)

        self.horizontalLayout_3.addWidget(self.labelSettingsPageTitle)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.line = QFrame(self.settings)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.frameLanguageBlock = QFrame(self.settings)
        self.frameLanguageBlock.setObjectName(u"frameLanguageBlock")
        self.frameLanguageBlock.setFrameShape(QFrame.NoFrame)
        self.frameLanguageBlock.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frameLanguageBlock)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_language = QLabel(self.frameLanguageBlock)
        self.label_language.setObjectName(u"label_language")

        self.horizontalLayout.addWidget(self.label_language)

        self.comboBoxLangList = QComboBox(self.frameLanguageBlock)
        self.comboBoxLangList.setObjectName(u"comboBoxLangList")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.comboBoxLangList.sizePolicy().hasHeightForWidth())
        self.comboBoxLangList.setSizePolicy(sizePolicy2)
        self.comboBoxLangList.setCurrentText(u"")

        self.horizontalLayout.addWidget(self.comboBoxLangList)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)


        self.verticalLayout_3.addWidget(self.frameLanguageBlock)

        self.widget = QWidget(self.settings)
        self.widget.setObjectName(u"widget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy3)
        self.widget_place = QVBoxLayout(self.widget)
        self.widget_place.setSpacing(0)
        self.widget_place.setObjectName(u"widget_place")
        self.widget_place.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.widget)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButtonDeleteInvalidData = QPushButton(self.settings)
        self.pushButtonDeleteInvalidData.setObjectName(u"pushButtonDeleteInvalidData")
        self.pushButtonDeleteInvalidData.setStyleSheet(u"padding: 5px 20px 5px 20px")

        self.horizontalLayout_4.addWidget(self.pushButtonDeleteInvalidData)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.pushButtonAplySettings = QPushButton(self.settings)
        self.pushButtonAplySettings.setObjectName(u"pushButtonAplySettings")
        self.pushButtonAplySettings.setStyleSheet(u"padding: 5px 20px 5px 20px")

        self.horizontalLayout_4.addWidget(self.pushButtonAplySettings)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.stackedWidget.addWidget(self.settings)
        self.logs = QWidget()
        self.logs.setObjectName(u"logs")
        self.verticalLayout_5 = QVBoxLayout(self.logs)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButtonCloseLogs = QPushButton(self.logs)
        self.pushButtonCloseLogs.setObjectName(u"pushButtonCloseLogs")
        self.pushButtonCloseLogs.setFont(font1)
        self.pushButtonCloseLogs.setToolTipDuration(-1)
        self.pushButtonCloseLogs.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(251, 55, 30);")
        self.pushButtonCloseLogs.setFlat(False)

        self.horizontalLayout_6.addWidget(self.pushButtonCloseLogs)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_8)

        self.labelLogsPageTitle = QLabel(self.logs)
        self.labelLogsPageTitle.setObjectName(u"labelLogsPageTitle")
        self.labelLogsPageTitle.setFont(font2)

        self.horizontalLayout_6.addWidget(self.labelLogsPageTitle)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_9)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.listViewLogs = QListView(self.logs)
        self.listViewLogs.setObjectName(u"listViewLogs")

        self.verticalLayout_5.addWidget(self.listViewLogs)

        self.pushButtonClearLogs = QPushButton(self.logs)
        self.pushButtonClearLogs.setObjectName(u"pushButtonClearLogs")

        self.verticalLayout_5.addWidget(self.pushButtonClearLogs)

        self.stackedWidget.addWidget(self.logs)

        self.verticalLayout_4.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 894, 21))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.menu_plugins)
        self.menu.addAction(self.menu_settings)
        self.menu.addAction(self.menu_logs)
        self.menu.addSeparator()
        self.menu.addAction(self.menu_exit)
        self.menu_2.addAction(self.menu_manual)
        self.menu_2.addAction(self.menu_about)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.tabWidgetPlugins.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menu_settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
#if QT_CONFIG(shortcut)
        self.menu_settings.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Alt+S", None))
#endif // QT_CONFIG(shortcut)
        self.menu_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.menu_manual.setText(QCoreApplication.translate("MainWindow", u"User Manual", None))
#if QT_CONFIG(shortcut)
        self.menu_manual.setShortcut(QCoreApplication.translate("MainWindow", u"F1", None))
#endif // QT_CONFIG(shortcut)
        self.menu_about.setText(QCoreApplication.translate("MainWindow", u"About Utilities Box", None))
        self.menu_plugins.setText(QCoreApplication.translate("MainWindow", u"Plugins", None))
#if QT_CONFIG(shortcut)
        self.menu_plugins.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Alt+P", None))
#endif // QT_CONFIG(shortcut)
        self.menu_logs.setText(QCoreApplication.translate("MainWindow", u"Logs", None))
#if QT_CONFIG(shortcut)
        self.menu_logs.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Alt+L", None))
#endif // QT_CONFIG(shortcut)
        self.tabWidgetPlugins.setTabText(self.tabWidgetPlugins.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.tabWidgetPlugins.setTabText(self.tabWidgetPlugins.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
#if QT_CONFIG(tooltip)
        self.pushButtonClosePluginPage.setToolTip(QCoreApplication.translate("MainWindow", u"Back to Main page", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonClosePluginPage.setText(QCoreApplication.translate("MainWindow", u"\u00ab", None))
#if QT_CONFIG(tooltip)
        self.btnReloadPlugins.setToolTip(QCoreApplication.translate("MainWindow", u"Reload all plugins from plugins directory", None))
#endif // QT_CONFIG(tooltip)
        self.btnReloadPlugins.setText(QCoreApplication.translate("MainWindow", u"\u21ba", None))
        self.labelPluginsPageTitle.setText(QCoreApplication.translate("MainWindow", u"Plugins", None))
#if QT_CONFIG(tooltip)
        self.pushButtonCloseSettingsPage.setToolTip(QCoreApplication.translate("MainWindow", u"Back to Main page", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonCloseSettingsPage.setText(QCoreApplication.translate("MainWindow", u"\u00ab", None))
        self.labelSettingsPageTitle.setText(QCoreApplication.translate("MainWindow", u"Application Settings", None))
        self.label_language.setText(QCoreApplication.translate("MainWindow", u"Language", None))
#if QT_CONFIG(tooltip)
        self.pushButtonDeleteInvalidData.setToolTip(QCoreApplication.translate("MainWindow", u"Check the database for outdated plug-in data", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonDeleteInvalidData.setText(QCoreApplication.translate("MainWindow", u"Delete Invalid Data", None))
#if QT_CONFIG(tooltip)
        self.pushButtonAplySettings.setToolTip(QCoreApplication.translate("MainWindow", u"Apply and save current settings", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonAplySettings.setText(QCoreApplication.translate("MainWindow", u"Apply Settings", None))
#if QT_CONFIG(tooltip)
        self.pushButtonCloseLogs.setToolTip(QCoreApplication.translate("MainWindow", u"Back to Main page", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonCloseLogs.setText(QCoreApplication.translate("MainWindow", u"\u00ab", None))
        self.labelLogsPageTitle.setText(QCoreApplication.translate("MainWindow", u"Logs", None))
        self.pushButtonClearLogs.setText(QCoreApplication.translate("MainWindow", u"Clear logs", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"App", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

