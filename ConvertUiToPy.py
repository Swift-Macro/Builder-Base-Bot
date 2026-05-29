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
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1000, 500))
        MainWindow.setMaximumSize(QSize(1000, 500))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setMaximumSize(QSize(16777215, 500))
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
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
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
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy2)
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
        self.storageSettingsFrame = QFrame(self.mainContent)
        self.storageSettingsFrame.setObjectName(u"storageSettingsFrame")
        sizePolicy1.setHeightForWidth(self.storageSettingsFrame.sizePolicy().hasHeightForWidth())
        self.storageSettingsFrame.setSizePolicy(sizePolicy1)
        self.storageSettingsFrame.setMaximumSize(QSize(200, 16777215))
        self.storageSettingsFrame.setStyleSheet(u"#storageSettingsFrame {\n"
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
"}\n"
"")
        self.storageSettingsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.storageSettingsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.lootSettingsLayout = QVBoxLayout(self.storageSettingsFrame)
        self.lootSettingsLayout.setObjectName(u"lootSettingsLayout")
        self.storageSettingsLabel = QLabel(self.storageSettingsFrame)
        self.storageSettingsLabel.setObjectName(u"storageSettingsLabel")
        sizePolicy2.setHeightForWidth(self.storageSettingsLabel.sizePolicy().hasHeightForWidth())
        self.storageSettingsLabel.setSizePolicy(sizePolicy2)
        self.storageSettingsLabel.setMinimumSize(QSize(0, 50))
        self.storageSettingsLabel.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.storageSettingsLabel.setFont(font1)
        self.storageSettingsLabel.setStyleSheet(u"QLabel {\n"
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
        self.storageSettingsLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.lootSettingsLayout.addWidget(self.storageSettingsLabel)

        self.leftMarginLayout = QVBoxLayout()
        self.leftMarginLayout.setObjectName(u"leftMarginLayout")
        self.leftMarginLayout.setContentsMargins(15, -1, -1, -1)
        self.maxGoldlbl = QLabel(self.storageSettingsFrame)
        self.maxGoldlbl.setObjectName(u"maxGoldlbl")
        sizePolicy.setHeightForWidth(self.maxGoldlbl.sizePolicy().hasHeightForWidth())
        self.maxGoldlbl.setSizePolicy(sizePolicy)
        self.maxGoldlbl.setMinimumSize(QSize(0, 20))
        self.maxGoldlbl.setMaximumSize(QSize(16777215, 30))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.maxGoldlbl.setFont(font2)
        self.maxGoldlbl.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    font-weight: bold;\n"
"\n"
"	border: none;\n"
"}")
        self.maxGoldlbl.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.leftMarginLayout.addWidget(self.maxGoldlbl)

        self.goldLineEdit = QLineEdit(self.storageSettingsFrame)
        self.goldLineEdit.setObjectName(u"goldLineEdit")
        sizePolicy.setHeightForWidth(self.goldLineEdit.sizePolicy().hasHeightForWidth())
        self.goldLineEdit.setSizePolicy(sizePolicy)
        self.goldLineEdit.setMinimumSize(QSize(100, 20))
        self.goldLineEdit.setMaximumSize(QSize(100, 20))
        font3 = QFont()
        font3.setPointSize(9)
        font3.setUnderline(False)
        self.goldLineEdit.setFont(font3)
        self.goldLineEdit.setAutoFillBackground(False)
        self.goldLineEdit.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgba(0,0,0,140);\n"
"    border-radius: 8px;\n"
"    border: 2px solid #3b2414;\n"
"}")
        self.goldLineEdit.setFrame(True)

        self.leftMarginLayout.addWidget(self.goldLineEdit)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.leftMarginLayout.addItem(self.verticalSpacer)

        self.elixerlbl = QLabel(self.storageSettingsFrame)
        self.elixerlbl.setObjectName(u"elixerlbl")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.elixerlbl.sizePolicy().hasHeightForWidth())
        self.elixerlbl.setSizePolicy(sizePolicy3)
        self.elixerlbl.setMinimumSize(QSize(0, 20))
        self.elixerlbl.setMaximumSize(QSize(16777215, 30))
        self.elixerlbl.setFont(font2)
        self.elixerlbl.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    font-weight: bold;\n"
"\n"
"	border: none;\n"
"}")

        self.leftMarginLayout.addWidget(self.elixerlbl)

        self.elixerLineEdit = QLineEdit(self.storageSettingsFrame)
        self.elixerLineEdit.setObjectName(u"elixerLineEdit")
        sizePolicy.setHeightForWidth(self.elixerLineEdit.sizePolicy().hasHeightForWidth())
        self.elixerLineEdit.setSizePolicy(sizePolicy)
        self.elixerLineEdit.setMinimumSize(QSize(100, 20))
        self.elixerLineEdit.setMaximumSize(QSize(100, 20))
        self.elixerLineEdit.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgba(0,0,0,140);\n"
"    border-radius: 8px;\n"
"    border: 2px solid #3b2414;\n"
"}")

        self.leftMarginLayout.addWidget(self.elixerLineEdit)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.leftMarginLayout.addItem(self.verticalSpacer_2)


        self.lootSettingsLayout.addLayout(self.leftMarginLayout)


        self.horizontalLayout.addWidget(self.storageSettingsFrame)

        self.troopConfiguration = QFrame(self.mainContent)
        self.troopConfiguration.setObjectName(u"troopConfiguration")
        sizePolicy2.setHeightForWidth(self.troopConfiguration.sizePolicy().hasHeightForWidth())
        self.troopConfiguration.setSizePolicy(sizePolicy2)
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
        sizePolicy2.setHeightForWidth(self.troopOptionslbl_2.sizePolicy().hasHeightForWidth())
        self.troopOptionslbl_2.setSizePolicy(sizePolicy2)
        self.troopOptionslbl_2.setMinimumSize(QSize(0, 50))
        self.troopOptionslbl_2.setMaximumSize(QSize(16777215, 50))
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
        QListWidgetItem(self.builderBaseTroopList)
        self.builderBaseTroopList.setObjectName(u"builderBaseTroopList")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.builderBaseTroopList.sizePolicy().hasHeightForWidth())
        self.builderBaseTroopList.setSizePolicy(sizePolicy4)
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

        self.widget_2 = QWidget(self.troopConfiguration)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.heroMachineCheckBox = QCheckBox(self.widget_2)
        self.heroMachineCheckBox.setObjectName(u"heroMachineCheckBox")
        sizePolicy.setHeightForWidth(self.heroMachineCheckBox.sizePolicy().hasHeightForWidth())
        self.heroMachineCheckBox.setSizePolicy(sizePolicy)
        self.heroMachineCheckBox.setMaximumSize(QSize(200, 100))
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

        self.verticalLayout.addWidget(self.heroMachineCheckBox)

        self.allWallsCheckBox = QCheckBox(self.widget_2)
        self.allWallsCheckBox.setObjectName(u"allWallsCheckBox")
        sizePolicy.setHeightForWidth(self.allWallsCheckBox.sizePolicy().hasHeightForWidth())
        self.allWallsCheckBox.setSizePolicy(sizePolicy)
        self.allWallsCheckBox.setMaximumSize(QSize(200, 100))
        self.allWallsCheckBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.allWallsCheckBox.setStyleSheet(u"QCheckBox {\n"
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

        self.verticalLayout.addWidget(self.allWallsCheckBox)


        self.troopLayout_2.addWidget(self.widget_2)

        self.horizontalSpacer_3 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.troopLayout_2.addItem(self.horizontalSpacer_3)


        self.troopOptionsLayout_2.addLayout(self.troopLayout_2)


        self.verticalLayout_15.addLayout(self.troopOptionsLayout_2)


        self.horizontalLayout.addWidget(self.troopConfiguration)


        self.section1.addWidget(self.mainContent)

        self.mainContent_2 = QWidget(self.centralwidget)
        self.mainContent_2.setObjectName(u"mainContent_2")
        self.horizontalLayout_4 = QHBoxLayout(self.mainContent_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lootConfigurationFrame = QFrame(self.mainContent_2)
        self.lootConfigurationFrame.setObjectName(u"lootConfigurationFrame")
        self.lootConfigurationFrame.setStyleSheet(u"#lootConfigurationFrame{\n"
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
        self.lootConfigurationFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.lootConfigurationFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.lootSettingsLayout_2 = QVBoxLayout(self.lootConfigurationFrame)
        self.lootSettingsLayout_2.setObjectName(u"lootSettingsLayout_2")
        self.storageSettingsLabel_2 = QLabel(self.lootConfigurationFrame)
        self.storageSettingsLabel_2.setObjectName(u"storageSettingsLabel_2")
        sizePolicy2.setHeightForWidth(self.storageSettingsLabel_2.sizePolicy().hasHeightForWidth())
        self.storageSettingsLabel_2.setSizePolicy(sizePolicy2)
        self.storageSettingsLabel_2.setMinimumSize(QSize(0, 50))
        self.storageSettingsLabel_2.setMaximumSize(QSize(16777215, 50))
        self.storageSettingsLabel_2.setFont(font1)
        self.storageSettingsLabel_2.setStyleSheet(u"QLabel {\n"
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
        self.storageSettingsLabel_2.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.lootSettingsLayout_2.addWidget(self.storageSettingsLabel_2)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.eventTroopLabel_2 = QLabel(self.lootConfigurationFrame)
        self.eventTroopLabel_2.setObjectName(u"eventTroopLabel_2")
        self.eventTroopLabel_2.setFont(font2)
        self.eventTroopLabel_2.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    font-weight: bold;\n"
"\n"
"	border: none;\n"
"}")

        self.verticalLayout_10.addWidget(self.eventTroopLabel_2)

        self.lootCartSpinBox = QSpinBox(self.lootConfigurationFrame)
        self.lootCartSpinBox.setObjectName(u"lootCartSpinBox")
        sizePolicy2.setHeightForWidth(self.lootCartSpinBox.sizePolicy().hasHeightForWidth())
        self.lootCartSpinBox.setSizePolicy(sizePolicy2)
        self.lootCartSpinBox.setMaximumSize(QSize(16777215, 80))
        self.lootCartSpinBox.setStyleSheet(u"QSpinBox {\n"
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
        self.lootCartSpinBox.setFrame(True)
        self.lootCartSpinBox.setReadOnly(False)
        self.lootCartSpinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.lootCartSpinBox.setMinimum(1)
        self.lootCartSpinBox.setMaximum(50)
        self.lootCartSpinBox.setValue(5)

        self.verticalLayout_10.addWidget(self.lootCartSpinBox)


        self.horizontalLayout_8.addLayout(self.verticalLayout_10)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.attackDurationLabel = QLabel(self.lootConfigurationFrame)
        self.attackDurationLabel.setObjectName(u"attackDurationLabel")
        self.attackDurationLabel.setFont(font2)
        self.attackDurationLabel.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    font-weight: bold;\n"
"\n"
"	border: none;\n"
"}")

        self.verticalLayout_12.addWidget(self.attackDurationLabel)

        self.surrenderTimerLabel = QLabel(self.lootConfigurationFrame)
        self.surrenderTimerLabel.setObjectName(u"surrenderTimerLabel")
        sizePolicy.setHeightForWidth(self.surrenderTimerLabel.sizePolicy().hasHeightForWidth())
        self.surrenderTimerLabel.setSizePolicy(sizePolicy)
        self.surrenderTimerLabel.setMinimumSize(QSize(0, 20))
        self.surrenderTimerLabel.setMaximumSize(QSize(100, 10))
        self.surrenderTimerLabel.setFont(font1)
        self.surrenderTimerLabel.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    font-weight: bold;\n"
"\n"
"	border: none;\n"
"}")
        self.surrenderTimerLabel.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.verticalLayout_12.addWidget(self.surrenderTimerLabel)

        self.surrenderSlider = QSlider(self.lootConfigurationFrame)
        self.surrenderSlider.setObjectName(u"surrenderSlider")
        sizePolicy1.setHeightForWidth(self.surrenderSlider.sizePolicy().hasHeightForWidth())
        self.surrenderSlider.setSizePolicy(sizePolicy1)
        self.surrenderSlider.setMaximumSize(QSize(200, 35))
        self.surrenderSlider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    height: 12px;\n"
"\n"
"    background-color: rgba(90, 55, 28, 235);\n"
"\n"
"    border-radius: 6px;\n"
"    border: 2px solid #2b1a0f;\n"
"\n"
"    border-top-color: #7a4d28;\n"
"    border-left-color: #7a4d28;\n"
"    border-bottom-color: #140c06;\n"
"    border-right-color: #140c06;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: #c28a4b;\n"
"    border-radius: 6px;\n"
"\n"
"    border: 1px solid #2b1a0f;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: #3b2413;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: #c28a4b;\n"
"\n"
"    border-radius: 11px;\n"
"    border: 2px solid #2b1a0f;\n"
"\n"
"    border-top-color: #f1b56e;\n"
"    border-left-color: #f1b56e;\n"
"    border-bottom-color: #5c381d;\n"
"    border-right-color: #5c381d;\n"
"\n"
"    width: 22px;\n"
"    height: 22px;\n"
"\n"
"    margin: -6px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: #e0"
                        "a65f;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: #8f5a2d;\n"
"}\n"
"\n"
"QSlider::tick-mark:horizontal {\n"
"    background: #2b1a0f;\n"
"    width: 2px;\n"
"    height: 6px;\n"
"}")
        self.surrenderSlider.setMinimum(0)
        self.surrenderSlider.setMaximum(60)
        self.surrenderSlider.setValue(45)
        self.surrenderSlider.setTracking(True)
        self.surrenderSlider.setOrientation(Qt.Orientation.Horizontal)
        self.surrenderSlider.setInvertedAppearance(False)
        self.surrenderSlider.setInvertedControls(False)

        self.verticalLayout_12.addWidget(self.surrenderSlider)


        self.horizontalLayout_8.addLayout(self.verticalLayout_12)


        self.lootSettingsLayout_2.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_4.addWidget(self.lootConfigurationFrame)

        self.botOptionsFrame = QFrame(self.mainContent_2)
        self.botOptionsFrame.setObjectName(u"botOptionsFrame")
        self.botOptionsFrame.setStyleSheet(u"#botOptionsFrame {\n"
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
        self.botOptionsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.botOptionsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.botOptionsFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.botOptionslbl = QLabel(self.botOptionsFrame)
        self.botOptionslbl.setObjectName(u"botOptionslbl")
        sizePolicy2.setHeightForWidth(self.botOptionslbl.sizePolicy().hasHeightForWidth())
        self.botOptionslbl.setSizePolicy(sizePolicy2)
        self.botOptionslbl.setFont(font1)
        self.botOptionslbl.setStyleSheet(u"QLabel {\n"
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
        self.botOptionslbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.botOptionslbl)

        self.maxWallsBtn = QPushButton(self.botOptionsFrame)
        self.maxWallsBtn.setObjectName(u"maxWallsBtn")
        sizePolicy1.setHeightForWidth(self.maxWallsBtn.sizePolicy().hasHeightForWidth())
        self.maxWallsBtn.setSizePolicy(sizePolicy1)
        self.maxWallsBtn.setFont(font2)
        self.maxWallsBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.maxWallsBtn.setStyleSheet(u"QPushButton {\n"
"\n"
"    /* Warm orange gradient */\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0,\n"
"        x2:0, y2:1,\n"
"        stop:0 #F7B24D,\n"
"        stop:0.5 #E98A2A,\n"
"        stop:1 #C86A1A\n"
"    );\n"
"\n"
"    color: #FFFFFF;\n"
"\n"
"    /* Thick dark brown border */\n"
"    border: 4px solid #6A3B12;\n"
"    border-radius: 16px;\n"
"\n"
"    /* Slight inner feel */\n"
"    padding: 10px 16px;\n"
"\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"\n"
"/* HOVER \u2014 brighter, more golden */\n"
"QPushButton:hover {\n"
"\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0,\n"
"        x2:0, y2:1,\n"
"        stop:0 #FFC766,\n"
"        stop:0.5 #F29A33,\n"
"        stop:1 #D9781F\n"
"    );\n"
"}\n"
"\n"
"\n"
"/* PRESSED \u2014 darker + pressed depth */\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0,\n"
"        x2:0, y2:1,\n"
"        stop:0 #C86A1A,\n"
"        stop:0.5 #A95514,\n"
"        stop:1 #7F3E0E\n"
""
                        "    );\n"
"\n"
"    /* Push-down effect */\n"
"    padding-top: 12px;\n"
"    padding-bottom: 8px;\n"
"}\n"
"\n"
"\n"
"/* CHECKED \u2014 highlighted */\n"
"QPushButton:checked {\n"
"\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0,\n"
"        x2:0, y2:1,\n"
"        stop:0 #FFD27A,\n"
"        stop:0.5 #F2A23D,\n"
"        stop:1 #C86A1A\n"
"    );\n"
"\n"
"    border: 4px solid #FFD27A;\n"
"}")
        self.maxWallsBtn.setCheckable(True)

        self.verticalLayout_4.addWidget(self.maxWallsBtn)

        self.fillStoragesBtn = QPushButton(self.botOptionsFrame)
        self.fillStoragesBtn.setObjectName(u"fillStoragesBtn")
        sizePolicy1.setHeightForWidth(self.fillStoragesBtn.sizePolicy().hasHeightForWidth())
        self.fillStoragesBtn.setSizePolicy(sizePolicy1)
        self.fillStoragesBtn.setFont(font2)
        self.fillStoragesBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.fillStoragesBtn.setStyleSheet(u"QPushButton {\n"
"\n"
"    /* Warm orange gradient */\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0,\n"
"        x2:0, y2:1,\n"
"        stop:0 #F7B24D,\n"
"        stop:0.5 #E98A2A,\n"
"        stop:1 #C86A1A\n"
"    );\n"
"\n"
"    color: #FFFFFF;\n"
"\n"
"    /* Thick dark brown border */\n"
"    border: 4px solid #6A3B12;\n"
"    border-radius: 16px;\n"
"\n"
"    /* Slight inner feel */\n"
"    padding: 10px 16px;\n"
"\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"\n"
"/* HOVER \u2014 brighter, more golden */\n"
"QPushButton:hover {\n"
"\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0,\n"
"        x2:0, y2:1,\n"
"        stop:0 #FFC766,\n"
"        stop:0.5 #F29A33,\n"
"        stop:1 #D9781F\n"
"    );\n"
"}\n"
"\n"
"\n"
"/* PRESSED \u2014 darker + pressed depth */\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0,\n"
"        x2:0, y2:1,\n"
"        stop:0 #C86A1A,\n"
"        stop:0.5 #A95514,\n"
"        stop:1 #7F3E0E\n"
""
                        "    );\n"
"\n"
"    /* Push-down effect */\n"
"    padding-top: 12px;\n"
"    padding-bottom: 8px;\n"
"}\n"
"\n"
"\n"
"/* CHECKED \u2014 highlighted */\n"
"QPushButton:checked {\n"
"\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0,\n"
"        x2:0, y2:1,\n"
"        stop:0 #FFD27A,\n"
"        stop:0.5 #F2A23D,\n"
"        stop:1 #C86A1A\n"
"    );\n"
"\n"
"    border: 4px solid #FFD27A;\n"
"}")
        self.fillStoragesBtn.setCheckable(True)

        self.verticalLayout_4.addWidget(self.fillStoragesBtn)


        self.horizontalLayout_4.addWidget(self.botOptionsFrame)

        self.startBotFrame_2 = QFrame(self.mainContent_2)
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
        font4 = QFont()
        font4.setPointSize(16)
        font4.setBold(True)
        self.startBuilderBotBtn.setFont(font4)
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


        self.horizontalLayout_4.addWidget(self.startBotFrame_2)


        self.section1.addWidget(self.mainContent_2)


        self.gridLayout.addLayout(self.section1, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logoLabel.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Loot Farming Bot by Swift", None))
        self.storageSettingsLabel.setText(QCoreApplication.translate("MainWindow", u"Storage Capacity", None))
        self.maxGoldlbl.setText(QCoreApplication.translate("MainWindow", u"Max Gold:", None))
        self.goldLineEdit.setText("")
        self.elixerlbl.setText(QCoreApplication.translate("MainWindow", u"Max Elixer:", None))
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
        ___qlistwidgetitem3 = self.builderBaseTroopList.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Night Witch", None))
        self.builderBaseTroopList.setSortingEnabled(__sortingEnabled)

        self.heroMachineCheckBox.setText(QCoreApplication.translate("MainWindow", u"Has Hero Machine", None))
        self.allWallsCheckBox.setText(QCoreApplication.translate("MainWindow", u"All Walls Above Level 5", None))
        self.storageSettingsLabel_2.setText(QCoreApplication.translate("MainWindow", u"Loot Configuration", None))
        self.eventTroopLabel_2.setText(QCoreApplication.translate("MainWindow", u"Collect Elixir Cart Frequency", None))
        self.attackDurationLabel.setText(QCoreApplication.translate("MainWindow", u"Auto Surrender Timer", None))
        self.surrenderTimerLabel.setText(QCoreApplication.translate("MainWindow", u"45s", None))
        self.botOptionslbl.setText(QCoreApplication.translate("MainWindow", u"Bot Options", None))
        self.maxWallsBtn.setText(QCoreApplication.translate("MainWindow", u"Max Walls", None))
        self.fillStoragesBtn.setText(QCoreApplication.translate("MainWindow", u"Fill Storages", None))
        self.startBuilderBotBtn.setText(QCoreApplication.translate("MainWindow", u"Start Bot", None))
    # retranslateUi
