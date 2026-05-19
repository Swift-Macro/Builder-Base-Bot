import pyautogui as py
import time
import keyboard

# Change these values for your needs
battles = 5 # Change the amount of battles you want to do before checking loot cart
searchingBaseTime = 20
starsWaitTime = 45



selectedTroop = None
armySlots = 1
hasBuilderMachine = False
threshold = 0.8
running = True

# Maximum number of slots is 6
deployTroopLocations = [(314, 510), (1370, 221), (845, 36), (542, 193), (777, 843), (1208, 670)]
slotsLocations = [(463, 975), (586, 978), (710, 978), (850, 987), (971, 974), (1096, 981)]

def StartBot():
    global running
    running = True
    keyboard.wait("enter")

    while running:
        for attacks in range(battles):
            FindAndClickImage(attackButtonImage)
            time.sleep(1)
            if FindAndClickImage(findNowButtonImage):
                # Proceed to attack the base
                AttackingBase()

            if not running:
                return

        if FindAndClickImage(elixirCartImage, 1) or FindAndClickImage(elixirCartImage2, 1):
            time.sleep(1)
            if not running:
                return
            py.click(1403, 917)
            py.click(1610, 115)

def AttackingBase():
    if FindAndClickImage(battleStartsImage, searchingBaseTime):
        time.sleep(2)

        if not running:
            return

        py.moveTo(960, 540)
        time.sleep(1)
        for i in range(10):  # Zoom out to see the whole base
            py.scroll(-1000)

        if not running:
            return

        if hasBuilderMachine:
            py.click(325, 972)
            py.click(deployTroopLocations[1])

        time.sleep(1)
        DeployTroops()

        if not running:
            return

        if FindAndClickImage(twoStarsImage, starsWaitTime):
            py.click(113, 805)
            FindAndClickImage(okayButtonImage)
        if not FindAndClickImage(returnHomeButton, 1):
            py.click(113, 805)
            FindAndClickImage(okayButtonImage)
            time.sleep(2)
            FindAndClickImage(returnHomeButton)
    else:
        # Stop searching
        py.click(958, 872)
        time.sleep(1)

def DeployTroops():
    if selectedTroop == "Baby Dragon" or selectedTroop == "Pekka" or selectedTroop == "Bomber":
        # Clicking on slots and deploying them
        for w in range(armySlots):
            py.click(slotsLocations[w])
            py.click(deployTroopLocations[w])
            if not running:
                return

        # This is for clan game challenge
        if selectedTroop == "Bomber":
            for position in range(armySlots):
                # Clicking abilities
                py.click(slotsLocations[position])

def FindAndClickImage(imageName: str, timer: int = None):
    start = time.perf_counter()
    imageFound = False

    if timer is not None:
        duration = timer
    else:
        duration = 5

    while True:
        # Timer Countdown started
        if time.perf_counter() - start >= duration:
            break
        try:
            if not running:
                return
            imageLocation = py.locateOnScreen(imageName, confidence=threshold)
        except py.ImageNotFoundException:
            pass
        else:
            imageFound = True
            break
    if imageFound:
        py.click(py.center(imageLocation))
        return True
    else:
        print(f"Couldn't find image: {imageName}")
        return False

attackButtonImage = r"Images\BuilderBaseImages\attackButton.png"
findNowButtonImage = r"Images\BuilderBaseImages\findNowButton.png"
battleStartsImage = r"Images\BuilderBaseImages\battleStartsImage.png"
twoStarsImage = r"Images\BuilderBaseImages\twoStarsImage.png"
returnHomeButton = r"Images\BuilderBaseImages\returnHomeButton.png"
okayButtonImage = r"Images\BuilderBaseImages\okayButton.png"
elixirCartImage = r"Images\BuilderBaseImages\elixirCartImage.png"
elixirCartImage2 = r"Images\BuilderBaseImages\elixirCartImage2.png"
