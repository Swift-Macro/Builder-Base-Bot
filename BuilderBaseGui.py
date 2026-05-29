from PySide6.QtGui import QIntValidator
import BuilderBase as builderBase
from ConvertUiToPy import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel
import sys
import threading
import keyboard


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.show()
        self.setupUi(self)
        self.builderBaseTroopList.itemClicked.connect(self.SelectBuilderTroop)

        self.builderBaseSpinBox.valueChanged.connect(self.SetBuilderAttackLength)
        self.builderBaseSpinBox.lineEdit().setReadOnly(True)

        self.heroMachineCheckBox.toggled.connect(self.HasBuilderMachine)
        self.allWallsCheckBox.toggled.connect(self.AllWallsAboveFive)

        self.lootCartSpinBox.valueChanged.connect(self.SetLootCartFrequency)
        self.lootCartSpinBox.lineEdit().setReadOnly(True)

        self.surrenderSlider.valueChanged.connect(self.SetSurrenderTime)

        self.startBuilderBotBtn.clicked.connect(self.StartBuilderBaseAttack)

        self.goldLineEdit.setValidator(QIntValidator(0, 99999999))
        self.goldLineEdit.textChanged.connect(self.FormatNumberTyping)
        self.goldLineEdit.editingFinished.connect(self.SetGoldValue)

        self.elixerLineEdit.setValidator(QIntValidator(0, 99999999))
        self.elixerLineEdit.textChanged.connect(self.FormatNumberTyping)
        self.elixerLineEdit.editingFinished.connect(self.SetElixerValue)

        self.maxWallsBtn.clicked.connect(lambda c: self.SetAttackOption(self.maxWallsBtn.isChecked(), "maxWalls"))
        self.fillStoragesBtn.clicked.connect(lambda c: self.SetAttackOption(self.fillStoragesBtn.isChecked(), "fillStorages"))

    def SetAttackOption(self, checked, attackOption):
        if checked:
            if attackOption == "maxWalls":
                self.fillStoragesBtn.setChecked(False)
                builderBase.maxWalls = True
            elif attackOption == "fillStorages":
                self.maxWallsBtn.setChecked(False)
                builderBase.maxWalls = False
            else:
                pass
        else:
            pass

    def FormatNumberTyping(self):
        lineEdit = self.sender()
        text = lineEdit.text()

        if text == "":
            return

        cursor_pos = lineEdit.cursorPosition()

        clean = text.replace(",", "")

        if clean.isdigit():
            num = int(clean)
            formatted = f"{num:,}"

            lineEdit.blockSignals(True)
            lineEdit.setText(formatted)
            lineEdit.blockSignals(False)

            lineEdit.setCursorPosition(
                min(cursor_pos + (formatted.count(",") - text.count(",")), len(formatted))
            )

    def SetGoldValue(self):
        builderBase.maxStorageGold = int(self.goldLineEdit.text().replace(",", ""))

    def SetElixerValue(self):
        builderBase.maxStorageElixir = int(self.elixerLineEdit.text().replace(",", ""))

    def SelectBuilderTroop(self, item):
        selectedTroop = item.text()
        if selectedTroop == "Baby Dragon":
            builderBase.selectedTroop = "Baby Dragon"
        elif selectedTroop == "Pekka":
            builderBase.selectedTroop = "Pekka"
        elif selectedTroop == "Bomber":
            builderBase.selectedTroop = "Bomber"
        elif selectedTroop == "Night Witch":
            builderBase.selectedTroop = "Night Witch"
        elif selectedTroop == "Barbarian":
            builderBase.selectedTroop = "Barbarian"
        else:
            builderBase.selectedTroop = None

    def SetBuilderAttackLength(self, value):
        builderBase.armySlots = value

    def HasBuilderMachine(self, checked):
        if checked:
            builderBase.hasBuilderMachine = True
        else:
            builderBase.hasBuilderMachine = False

    def AllWallsAboveFive(self, checked):
        if checked:
            builderBase.allWallLevelsAboveFive = True
        else:
            builderBase.allWallLevelsAboveFive = False

    def SetLootCartFrequency(self, value):
        builderBase.battles = value

    def SetSurrenderTime(self, value):
        self.surrenderTimerLabel.setText(f"{value}s")
        builderBase.starsWaitTime = value

    def StartBuilderBaseAttack(self):
        if self.goldLineEdit.text() and self.elixerLineEdit.text() and builderBase.selectedTroop is not None and builderBase.maxWalls is not None:
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
