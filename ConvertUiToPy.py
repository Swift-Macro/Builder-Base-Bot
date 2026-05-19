# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BuilderBaseUI.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QCheckBox,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 320)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(900, 320))
        MainWindow.setMaximumSize(QSize(900, 320))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget {\n"
"    background-image: url(Images/Background.jpg);\n"
"    background-repeat: repeat;\n"
"    background-position: center;\n"
"\n"
"}\n"
"\n"
"QListWidget:focus {\n"
"    outline: none;\n"
"}\n"
"QListWidget::item {\n"
"    border-radius: 6px;\n"
"}")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.iconOnly = QWidget(self.centralwidget)
        self.iconOnly.setObjectName(u"iconOnly")
        self.iconOnly.setEnabled(True)
        self.iconOnly.setStyleSheet(u"#iconOnly {\n"
"		background-color: #313a46;\n"
"		width:50px;\n"
"}\n"
"\n"
"#iconOnly QPushButton, QLabel {\n"
"		height:50px;\n"
"		border:none;\n"
"}\n"
"\n"
"#iconOnly QPushButton:hover {\n"
"		background-color: rgba( 86, 101, 115, 0.5);\n"
"}\n"
"\n"
"\n"
"#logoLabel {\n"
"		padding: 5px\n"
"}\n"
"")
        self.verticalLayout_47 = QVBoxLayout(self.iconOnly)
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.logoLabel = QLabel(self.iconOnly)
        self.logoLabel.setObjectName(u"logoLabel")
        self.logoLabel.setStyleSheet(u"")
        self.logoLabel.setPixmap(QPixmap(u"Images/logo.png"))
        self.logoLabel.setScaledContents(False)
        self.logoLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_26.addWidget(self.logoLabel)


        self.verticalLayout_47.addLayout(self.horizontalLayout_26)

        self.verticalLayout_43 = QVBoxLayout()
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")

        self.verticalLayout_47.addLayout(self.verticalLayout_43)

        self.verticalSpacer_35 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_47.addItem(self.verticalSpacer_35)


        self.gridLayout.addWidget(self.iconOnly, 0, 0, 2, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_25 = QHBoxLayout(self.widget)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalSpacer_15 = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_15)

        self.label_20 = QLabel(self.widget)
        self.label_20.setObjectName(u"label_20")
        font = QFont()
        font.setPointSize(10)
        self.label_20.setFont(font)

        self.horizontalLayout_24.addWidget(self.label_20)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_13)


        self.horizontalLayout_25.addLayout(self.horizontalLayout_24)


        self.gridLayout.addWidget(self.widget, 0, 1, 1, 1)

        self.section1 = QVBoxLayout()
        self.section1.setObjectName(u"section1")
        self.mainContent = QWidget(self.centralwidget)
        self.mainContent.setObjectName(u"mainContent")
        self.horizontalLayout = QHBoxLayout(self.mainContent)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.troopConfiguration = QFrame(self.mainContent)
        self.troopConfiguration.setObjectName(u"troopConfiguration")
        sizePolicy.setHeightForWidth(self.troopConfiguration.sizePolicy().hasHeightForWidth())
        self.troopConfiguration.setSizePolicy(sizePolicy)
        self.troopConfiguration.setMaximumSize(QSize(16777215, 250))
        self.troopConfiguration.setStyleSheet(u"#troopConfiguration {\n"
"    background-color: rgba(90, 55, 28, 235);\n"
"\n"
"    border-radius: 16px;\n"
"    border: 3px solid #2b1a0f;\n"
"\n"
"    /* lighting illusion */\n"
"    border-top-color: #7a4d28;\n"
"    border-left-color: #7a4d28;\n"
"    border-bottom-color: #140c06;\n"
"    border-right-color: #140c06;\n"
"}")
        self.troopConfiguration.setFrameShape(QFrame.Shape.StyledPanel)
        self.troopConfiguration.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.troopConfiguration)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.troopOptionslbl_2 = QLabel(self.troopConfiguration)
        self.troopOptionslbl_2.setObjectName(u"troopOptionslbl_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.troopOptionslbl_2.sizePolicy().hasHeightForWidth())
        self.troopOptionslbl_2.setSizePolicy(sizePolicy2)
        self.troopOptionslbl_2.setMinimumSize(QSize(0, 50))
        self.troopOptionslbl_2.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.troopOptionslbl_2.setFont(font1)
        self.troopOptionslbl_2.setStyleSheet(u"QLabel {\n"
"    background-color: rgba(90, 55, 28, 235);\n"
"\n"
"    border-radius: 16px;\n"
"    border: 3px solid #2b1a0f;\n"
"\n"
"    /* lighting illusion */\n"
"    border-top-color: #7a4d28;\n"
"    border-left-color: #7a4d28;\n"
"    border-bottom-color: #140c06;\n"
"    border-right-color: #140c06;\n"
"}")
        self.troopOptionslbl_2.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_15.addWidget(self.troopOptionslbl_2)

        self.troopOptionsLayout_2 = QVBoxLayout()
        self.troopOptionsLayout_2.setObjectName(u"troopOptionsLayout_2")
        self.labelsLayout_2 = QHBoxLayout()
        self.labelsLayout_2.setObjectName(u"labelsLayout_2")
        self.labelsLayout_2.setContentsMargins(15, -1, -1, -1)
        self.verticalSpacer_16 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.labelsLayout_2.addItem(self.verticalSpacer_16)

        self.selectTrooplbl_2 = QLabel(self.troopConfiguration)
        self.selectTrooplbl_2.setObjectName(u"selectTrooplbl_2")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.selectTrooplbl_2.setFont(font2)
        self.selectTrooplbl_2.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    padding-bottom: 4px;\n"
"\n"
"    border: none;\n"
"    border-bottom: 3px solid #E6B85C;   /* gold underline */\n"
"	max-width: 85px;\n"
"}")

        self.labelsLayout_2.addWidget(self.selectTrooplbl_2)

        self.verticalSpacer_11 = QSpacerItem(108, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.labelsLayout_2.addItem(self.verticalSpacer_11)

        self.eventTroopLabel_6 = QLabel(self.troopConfiguration)
        self.eventTroopLabel_6.setObjectName(u"eventTroopLabel_6")
        self.eventTroopLabel_6.setFont(font2)
        self.eventTroopLabel_6.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    padding-bottom: 4px;\n"
"\n"
"    border: none;\n"
"    border-bottom: 3px solid #E6B85C;   /* gold underline */\n"
"	max-width: 85px;\n"
"}")

        self.labelsLayout_2.addWidget(self.eventTroopLabel_6)

        self.verticalSpacer_12 = QSpacerItem(100, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.labelsLayout_2.addItem(self.verticalSpacer_12)

        self.eventTroopLabel_7 = QLabel(self.troopConfiguration)
        self.eventTroopLabel_7.setObjectName(u"eventTroopLabel_7")
        self.eventTroopLabel_7.setFont(font2)
        self.eventTroopLabel_7.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    padding-bottom: 4px;\n"
"\n"
"    border: none;\n"
"    border-bottom: 3px solid #E6B85C;   /* gold underline */\n"
"	max-width: 85px;\n"
"}")

        self.labelsLayout_2.addWidget(self.eventTroopLabel_7)

        self.verticalSpacer_13 = QSpacerItem(80, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.labelsLayout_2.addItem(self.verticalSpacer_13)


        self.troopOptionsLayout_2.addLayout(self.labelsLayout_2)

        self.troopLayout_2 = QHBoxLayout()
        self.troopLayout_2.setObjectName(u"troopLayout_2")
        self.troopLayout_2.setContentsMargins(15, -1, 15, 15)
        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.troopLayout_2.addItem(self.horizontalSpacer_2)

        self.builderBaseTroopList = QListWidget(self.troopConfiguration)
        QListWidgetItem(self.builderBaseTroopList)
        QListWidgetItem(self.builderBaseTroopList)
        QListWidgetItem(self.builderBaseTroopList)
        self.builderBaseTroopList.setObjectName(u"builderBaseTroopList")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.builderBaseTroopList.sizePolicy().hasHeightForWidth())
        self.builderBaseTroopList.setSizePolicy(sizePolicy3)
        self.builderBaseTroopList.setMaximumSize(QSize(150, 16777215))
        self.builderBaseTroopList.setFont(font)
        self.builderBaseTroopList.setMouseTracking(False)
        self.builderBaseTroopList.setTabletTracking(True)
        self.builderBaseTroopList.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.builderBaseTroopList.setAcceptDrops(False)
        self.builderBaseTroopList.setStyleSheet(u"QListWidget {\n"
"    background-color: rgba(90, 55, 28, 235);\n"
"    border-radius: 16px;\n"
"    border: 3px solid #2b1a0f;\n"
"\n"
"    /* lighting illusion */\n"
"    border-top-color: #7a4d28;\n"
"    border-left-color: #7a4d28;\n"
"    border-bottom-color: #140c06;\n"
"    border-right-color: #140c06;\n"
"}\n"
"\n"
"/* normal items = square-ish with rounded corners */\n"
"QListWidget::item {\n"
"    border-radius: 6px; /* small rounding for square shape */\n"
"}\n"
"\n"
"/* hover effect */\n"
"QListWidget::item:hover {\n"
"    background-color: rgba(255, 255, 255, 30); /* subtle highlight */\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"/* item pressed = looks pushed down */\n"
"QListWidget::item:pressed {\n"
"    background-color: rgba(0, 0, 0, 40);\n"
"    border-top: 2px solid #140c06;\n"
"    border-left: 2px solid #140c06;\n"
"    border-bottom: 2px solid #7a4d28;\n"
"    border-right: 2px solid #7a4d28;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"/* keep the pressed look when selected */\n"
"QListWidg"
                        "et::item:selected {\n"
"    background-color: rgba(0, 0, 0, 30);\n"
"    border-top: 2px solid #140c06;\n"
"    border-left: 2px solid #140c06;\n"
"    border-bottom: 2px solid #7a4d28;\n"
"    border-right: 2px solid #7a4d28;\n"
"    border-radius: 6px;\n"
"}")
        self.builderBaseTroopList.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerItem)
        self.builderBaseTroopList.setBatchSize(100)
        self.builderBaseTroopList.setSortingEnabled(False)

        self.troopLayout_2.addWidget(self.builderBaseTroopList)

        self.verticalSpacer_14 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.troopLayout_2.addItem(self.verticalSpacer_14)

        self.widget_3 = QWidget(self.troopConfiguration)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_16 = QVBoxLayout(self.widget_3)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.builderBaseSpinBox = QSpinBox(self.widget_3)
        self.builderBaseSpinBox.setObjectName(u"builderBaseSpinBox")
        sizePolicy1.setHeightForWidth(self.builderBaseSpinBox.sizePolicy().hasHeightForWidth())
        self.builderBaseSpinBox.setSizePolicy(sizePolicy1)
        self.builderBaseSpinBox.setStyleSheet(u"QSpinBox {\n"
"    background-color: rgba(90, 55, 28, 235);\n"
"    border-radius: 11px;\n"
"    border: 2px solid #2b1a0f;\n"
"    border-top-color: #7a4d28;\n"
"    border-left-color: #7a4d28;\n"
"    border-bottom-color: #140c06;\n"
"    border-right-color: #140c06;\n"
"    padding: 4px 8px;\n"
"	font: bold;\n"
"    font-size: 14pt; /* <- set the font size here */\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    background-color: #c28a4b;\n"
"    border-radius: 10px;\n"
"    border: 2px solid #2b1a0f;\n"
"    border-top-color: #f1b56e;\n"
"    border-left-color: #f1b56e;\n"
"    border-bottom-color: #5c381d;\n"
"    border-right-color: #5c381d;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover {\n"
"    background-color: #e0a65f;\n"
"}\n"
"\n"
"QSpinBox::up-button:pressed {\n"
"    background-color: #8f5a2d;\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-posi"
                        "tion: bottom right;\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    background-color: #c28a4b;\n"
"    border-radius: 10px;\n"
"    border: 2px solid #2b1a0f;\n"
"    border-top-color: #f1b56e;\n"
"    border-left-color: #f1b56e;\n"
"    border-bottom-color: #5c381d;\n"
"    border-right-color: #5c381d;\n"
"}\n"
"\n"
"QSpinBox::down-button:hover {\n"
"    background-color: #e0a65f;\n"
"}\n"
"\n"
"QSpinBox::down-button:pressed {\n"
"    background-color: #8f5a2d;\n"
"}")
        self.builderBaseSpinBox.setFrame(True)
        self.builderBaseSpinBox.setReadOnly(False)
        self.builderBaseSpinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.builderBaseSpinBox.setMinimum(1)
        self.builderBaseSpinBox.setMaximum(6)

        self.verticalLayout_16.addWidget(self.builderBaseSpinBox)


        self.troopLayout_2.addWidget(self.widget_3)

        self.verticalSpacer_15 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.troopLayout_2.addItem(self.verticalSpacer_15)

        self.heroMachineCheckBox = QCheckBox(self.troopConfiguration)
        self.heroMachineCheckBox.setObjectName(u"heroMachineCheckBox")
        sizePolicy.setHeightForWidth(self.heroMachineCheckBox.sizePolicy().hasHeightForWidth())
        self.heroMachineCheckBox.setSizePolicy(sizePolicy)
        self.heroMachineCheckBox.setMaximumSize(QSize(140, 100))
        self.heroMachineCheckBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.heroMachineCheckBox.setStyleSheet(u"QCheckBox {\n"
"    spacing: 6px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    border-radius: 8px;   /* half of width/height = perfect circle */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: #3b2414;\n"
"    border: 2px solid #1a0f07;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #66bb6a;\n"
"    border: 2px solid #1b5e20;\n"
"}")

        self.troopLayout_2.addWidget(self.heroMachineCheckBox)

        self.horizontalSpacer_3 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.troopLayout_2.addItem(self.horizontalSpacer_3)


        self.troopOptionsLayout_2.addLayout(self.troopLayout_2)


        self.verticalLayout_15.addLayout(self.troopOptionsLayout_2)


        self.horizontalLayout.addWidget(self.troopConfiguration)

        self.startBotFrame_2 = QFrame(self.mainContent)
        self.startBotFrame_2.setObjectName(u"startBotFrame_2")
        sizePolicy2.setHeightForWidth(self.startBotFrame_2.sizePolicy().hasHeightForWidth())
        self.startBotFrame_2.setSizePolicy(sizePolicy2)
        self.startBotFrame_2.setMinimumSize(QSize(0, 100))
        self.startBotFrame_2.setMaximumSize(QSize(16777215, 100))
        self.startBotFrame_2.setStyleSheet(u"#startBotFrame_2 {\n"
"    background-color: rgba(90, 55, 28, 235);\n"
"\n"
"    border-radius: 16px;\n"
"    border: 3px solid #2b1a0f;\n"
"\n"
"    /* lighting illusion */\n"
"    border-top-color: #7a4d28;\n"
"    border-left-color: #7a4d28;\n"
"    border-bottom-color: #140c06;\n"
"    border-right-color: #140c06;\n"
"}")
        self.startBotFrame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.startBotFrame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.startBotFrame_2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.startAttackLayout_2 = QVBoxLayout()
        self.startAttackLayout_2.setObjectName(u"startAttackLayout_2")
        self.startBuilderBotBtn = QPushButton(self.startBotFrame_2)
        self.startBuilderBotBtn.setObjectName(u"startBuilderBotBtn")
        sizePolicy1.setHeightForWidth(self.startBuilderBotBtn.sizePolicy().hasHeightForWidth())
        self.startBuilderBotBtn.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(True)
        self.startBuilderBotBtn.setFont(font3)
        self.startBuilderBotBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.startBuilderBotBtn.setStyleSheet(u"/* ======================\n"
"   ATTACK BUTTON (GREEN)\n"
"====================== */\n"
"\n"
"QPushButton {\n"
"    background-color: #4CAF50;\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    padding: 8px;\n"
"    font-weight: bold;\n"
"    border: 3px solid #2e7d32;\n"
"}\n"
"\n"
"\n"
"/* hover */\n"
"QPushButton:hover {\n"
"    background-color: #66cc66;\n"
"}\n"
"\n"
"\n"
"/* pressed (clicking) */\n"
"QPushButton:pressed {\n"
"    background-color: #2e7d32;\n"
"\n"
"    /* push-down effect */\n"
"    padding-top: 10px;\n"
"    padding-bottom: 6px;\n"
"}\n"
"\n"
"\n"
"/* stays highlighted when active */\n"
"QPushButton#attackButton:checked {\n"
"    background-color: #43a047;\n"
"    border: 3px solid #a5d6a7;\n"
"}")
        self.startBuilderBotBtn.setCheckable(False)

        self.startAttackLayout_2.addWidget(self.startBuilderBotBtn)


        self.verticalLayout_14.addLayout(self.startAttackLayout_2)


        self.horizontalLayout.addWidget(self.startBotFrame_2)


        self.section1.addWidget(self.mainContent)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.section1.addItem(self.verticalSpacer)


        self.gridLayout.addLayout(self.section1, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logoLabel.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Loot Farming Bot by Swift", None))
        self.troopOptionslbl_2.setText(QCoreApplication.translate("MainWindow", u"Troop Configuration", None))
        self.selectTrooplbl_2.setText(QCoreApplication.translate("MainWindow", u"Select Troop:", None))
        self.eventTroopLabel_6.setText(QCoreApplication.translate("MainWindow", u"Army Slots:", None))
        self.eventTroopLabel_7.setText(QCoreApplication.translate("MainWindow", u"Options:", None))

        __sortingEnabled = self.builderBaseTroopList.isSortingEnabled()
        self.builderBaseTroopList.setSortingEnabled(False)
        ___qlistwidgetitem = self.builderBaseTroopList.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Baby Dragon", None))
        ___qlistwidgetitem1 = self.builderBaseTroopList.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Pekka", None))
        ___qlistwidgetitem2 = self.builderBaseTroopList.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Bomber", None))
        self.builderBaseTroopList.setSortingEnabled(__sortingEnabled)

        self.heroMachineCheckBox.setText(QCoreApplication.translate("MainWindow", u"Has Hero Machine", None))
        self.startBuilderBotBtn.setText(QCoreApplication.translate("MainWindow", u"Start Bot", None))
    # retranslateUi

