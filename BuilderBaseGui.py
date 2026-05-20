import BuilderBase as builderBase
from ConvertUiToPy import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel
import sys
import threading
import keyboard

# Builder Base
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.show()
        self.setupUi(self)
        self.builderBaseTroopList.itemClicked.connect(self.SelectBuilderTroop)

        self.builderBaseSpinBox.valueChanged.connect(self.SetBuilderAttackLength)
        self.builderBaseSpinBox.lineEdit().setReadOnly(True)

        self.heroMachineCheckBox.toggled.connect(self.HasBuilderMachine)

        self.lootCartSpinBox.valueChanged.connect(self.SetLootCartFrequency)
        self.lootCartSpinBox.lineEdit().setReadOnly(True)

        self.surrenderSlider.valueChanged.connect(self.SetSurrenderTime)

        self.startBuilderBotBtn.clicked.connect(self.StartBuilderBaseAttack)


    def SelectBuilderTroop(self, item):
        selectedTroop = item.text()
        if selectedTroop == "Baby Dragon":
                builderBase.selectedTroop = "Baby Dragon"
        elif selectedTroop == "Pekka":
                builderBase.selectedTroop = "Pekka"
        elif selectedTroop == "Bomber":
                builderBase.selectedTroop = "Bomber"
        else:
                builderBase.selectedTroop = None

    def SetBuilderAttackLength(self, value):
        builderBase.armySlots = value

    def HasBuilderMachine(self, checked):
        if checked:
            builderBase.hasBuilderMachine = True
        else:
            builderBase.hasBuilderMachine = False

    def SetLootCartFrequency(self, value):
        builderBase.battles = value

    def SetSurrenderTime(self, value):
        self.surrenderTimerLabel.setText(f"{value}s")
        builderBase.starsWaitTime = value

    def StartBuilderBaseAttack(self):
        if builderBase.selectedTroop is not None:
            # Able to start attack
            self.stopWindow = MiniWindow()
            self.stopWindow.show()
            self.hide()
            threading.Thread(target=builderBase.StartBot, daemon=True).start()
            keyboard.add_hotkey("Esc", lambda: self.StopAttack())

    def StopAttack(self):
        self.stopWindow.hide()
        builderBase.running = False
        window.show()

class MiniWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(300, 100)
        self.label = QLabel("Press (Enter) to Start\nPress (Escape) to Stop")
        self.label.setStyleSheet("""
            QLabel {
                background-color: rgba(90, 55, 28, 235);

                border-radius: 16px;
                border: 3px solid #2b1a0f;

                /* lighting illusion */
                border-top-color: #7a4d28;
                border-left-color: #7a4d28;
                border-bottom-color: #140c06;
                border-right-color: #140c06;

                color: white;
                font-size: 16pt;
                font-weight: bold;
                padding: 10px 18px;
                property-alignment: AlignCenter;
            }
        """)
        self.setCentralWidget(self.label)

app = QApplication(sys.argv)

window = MainWindow()

app.exec()
