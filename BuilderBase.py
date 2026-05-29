import pyautogui as py
import time
import keyboard
import random
import cv2 as cv
import numpy as np
import torch
import re
import easyocr

# Change these values for your needs
battles = 5 # Change the amount of battles you want to do before checking loot cart
searchingBaseTime = 20 # Change the amount of time you search for a base before canceling
starsWaitTime = 45 # Change the amount of time before you end the battle if you have not collected two stars
maxStorageGold = 0 # Gold storage capacity
maxStorageElixir = 0 # Elixir storage capacity
maxWalls = None # Attack option, whether you want to fill storages or max walls
allWallLevelsAboveFive = False # If true can upgrade your walls with elixir otherwise only gold


selectedTroop = None
armySlots = 1
hasBuilderMachine = False
builderMachineOffSetPos = 0
running = True

# Maximum number of slots is 6
deployTroopLocations = [(314, 510), (1370, 221), (845, 36), (542, 193), (777, 843), (1208, 670)]
slotsLocations = [(418, 963), (544, 963), (670, 963), (796, 963), (922, 963), (1048, 963)]

reader = easyocr.Reader(["en"], gpu=False)
model = torch.jit.load("digits_model_New_Model.pt")
CHARS = "0123456789 "

def StartBot():
    global running
    global builderMachineOffSetPos

    running = True
    if hasBuilderMachine:
        builderMachineOffSetPos = 0
    else:
        builderMachineOffSetPos = 130

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

        # Checking if out of battle then moving up and collecting elixir cart
        FindAndClickImage(goldStorageImage, clickImage= False)
        py.moveTo(960, 540)
        py.dragRel(-50, 200, 0.2)
        time.sleep(1)

        if FindAndClickImage(elixirCartImage2, 2) or FindAndClickImage(elixirCartImage, threshold = 0.9):
            time.sleep(1)
            if not running:
                return
            py.click(1403, 917)
            py.click(1610, 115)

        time.sleep(3)

        if maxWalls:
            # Upgrade Walls
            isFullGold = CheckStorages("GoldStorage")
            if allWallLevelsAboveFive:
                isFullElixir = CheckStorages("ElixirStorage")
            else:
                isFullElixir = False
            if isFullGold or isFullElixir:
                # Upgrade Walls
                UpgradeWalls(isFullGold, isFullElixir)
            else:
                # Keep Attacking
                pass
        else:
            # Fill Storages
            isFullGold = CheckStorages("GoldStorage")
            isFullElixir = CheckStorages("ElixirStorage")

            if isFullGold and isFullElixir:
                print("Storages are Full")
                return


def UpgradeWalls(isFullGold, isFullElixir):
    ifiniteLoop = True
    py.click(1040, 50) # Clicking builder position
    time.sleep(1)
    x , y = (1040, 140)
    py.moveTo(x, y)

    while ifiniteLoop:
        # region for the screenshot takes (left,top,width,height) the top is the y coordinate of the top left coordinate
        screenshot = py.screenshot(region=(x - 250, y, 300, 560))
        screenshot = np.array(screenshot)
        screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2GRAY)

        # cv.imshow("Window", screenshot)

        # cv.waitKey(0)

        # Loop over the screenshot of the text
        # Check if the screenshot has text in the current section and if so click on the bounding box
        # Converting the screenshot to text then using regex to find the text "Wall"
        global reader
        result = reader.readtext(screenshot)
        regexText = re.compile(r"Wall x[\w?][\w?][\w?]|Wall x[\w?][\w?]")
        for i in range(len(result)):
            print(result[i][1])
            # Checks to see if the match has triple digit walls or double digits, if its single it just ignores it
            match = regexText.search(str(result[i][1]))
            if match != None:
                # Clicking on the bounding box location of the text
                point = result[i][0][0]
                boundingX, boundingY = map(int, point)
                py.click(x + boundingX + 10, y + boundingY + 10)
                ifiniteLoop = False
                break

        if not running:
            return

        time.sleep(0.3)

        # scroll 300x3 units down for one section
        for i in range(3):
            py.scroll(-300)
            print("scroll")
        # Wait for the section to stop moving and take a screenshot
        time.sleep(2.5)

    if not running:
        return

    # Clicking the buttons for upgrading the walls
    FindAndClickImage(upgradeMoreButtonImage)

    x, y = (963, 908)

    time.sleep(RandomFloatNumber(1, 2))

    # Checking if it can upgrade 10 walls until it cant on walls below level 6
    if allWallLevelsAboveFive:
        elixirOffSet = -80
    else:
        elixirOffSet = 0
    if FindAndClickImage(tenMoreWallsImage, 1, clickImage=False, moveToImage=True):
        while True:
            color = py.pixel(x - 143 + elixirOffSet, y)
            if color[2] in range(200, 256):
                py.click(x - 143 + elixirOffSet, y)
            else:
                break

    if isFullGold:
        if FindAndClickImage(tenMoreWallsImage, 1, clickImage=False, moveToImage=False):
            # Has more than 10 walls
            upgradeLootPos = 150 + elixirOffSet
            screenXpos = 95 + elixirOffSet
            buttonOffSet = 7 + elixirOffSet
        else:
            # Has less than 10 walls so it wont show the upgrade with 10 walls button
            upgradeLootPos = 80 + elixirOffSet
            screenXpos = 25 + elixirOffSet
            buttonOffSet = -73 + elixirOffSet
        lootNumber = maxStorageGold

    elif isFullElixir:
        if FindAndClickImage(tenMoreWallsImage, 1, clickImage=False, moveToImage=False):
            # Has more than 10 walls
            upgradeLootPos = 235
            screenXpos = 173
            buttonOffSet = -73
        else:
            # Has less than 10 walls so it wont show the upgrade with 10 walls button
            upgradeLootPos = 150
            screenXpos = 95
            buttonOffSet = -153
        lootNumber = maxStorageElixir

    if not running:
        return

    # Checking if it can upgrade 1 wall until it cant
    while True:
        screenshot = py.screenshot(region=(x + screenXpos, y - 100, 102, 25))
        screenshot = np.array(screenshot)

        # Converting color to not get mismatched color then to grayscale and add blur and sharpen the image to improve image quality
        screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)
        gray = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
        blur = cv.GaussianBlur(gray, (3, 3), 0)
        kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
        sharp = cv.filter2D(blur, -1, kernel)

        # Turning all pixels to either black or white and then resizing it to compare it into the trained model
        _, final = cv.threshold(sharp, 200, 255, cv.THRESH_BINARY)
        final = cv.resize(final, (180, 32))
        number = PredictNumber(final)

        wallLoot = int(number.replace(" ", ""))
        print(wallLoot)

        color = py.pixel(x + buttonOffSet, y)

        if color[2] in range(200, 256) and wallLoot < lootNumber:
            py.click(x + buttonOffSet, y)
        else:
            break

    if not running:
        return

    # Click the upgrade button
    py.click(x + upgradeLootPos, y)

    time.sleep(1)

    if not running:
        return

    # Click the okay button
    FindAndClickImage(okayButtonImage)

    time.sleep(1)

def PredictNumber(img):

    img = img.astype("float32") / 255.0
    img = torch.tensor(img)

    # Fixing the image values
    img = img.unsqueeze(0).unsqueeze(0)

    with torch.no_grad():
        preds = model(img)

    preds = torch.argmax(preds, dim=2)
    result = []
    prev = 0

    for p in preds[0]:
        p = int(p)

        if p != 0 and p != prev:
            result.append(CHARS[p-1])

        prev = p

    return "".join(result)

def CheckStorages(storageType):
    if storageType == "GoldStorage":
        FindAndClickImage(goldStorageImage, clickImage = False)
    else:
        FindAndClickImage(elixirStorageImage, clickImage = False)
    x, y = py.position()

    # Top left point, bottom right point, width, height
    screenshot = py.screenshot(region=(x - 215, y - 15, 180, 32))
    screenshot = np.array(screenshot)

    # Converting color to not get mismatched color then to grayscale and add blur and sharpen the image to improve image quality
    screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)
    gray = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (3, 3), 0)
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    sharp = cv.filter2D(blur, -1, kernel)

    # Turning all pixels to either black or white and then resizing it to compare it into the trained model
    _, final = cv.threshold(sharp, 200, 255, cv.THRESH_BINARY)
    final = cv.resize(final, (180, 32))
    number = PredictNumber(final)

    currentStorageLoot = int(number.replace(" ", ""))

    print(currentStorageLoot)

    if currentStorageLoot < maxStorageGold:
        # Storage is not full
        return False
    else:
        # Storage is full
        return True

def AttackingBase():
    if FindAndClickImage(battleStartsImage, searchingBaseTime):
        time.sleep(RandomFloatNumber(2, 3))

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
            if not FindAndClickImage(returnHomeButton):
                time.sleep(4)
                py.click(113, 805)
                FindAndClickImage(okayButtonImage)
                FindAndClickImage(returnHomeButton)
    else:
        # Stop searching
        py.click(958, 872)
        time.sleep(RandomFloatNumber(1, 2))

def DeployTroops():
    # Checks if all the troops have been deployed if not check the positions color and deploy
    while True:
        allDropped = False

        allDropped, delay = DeploymentSequence(allDropped)
        if not allDropped:
            break
        time.sleep(delay)

    # This is for clan game challenge
    if selectedTroop == "Bomber":
        for position in range(armySlots):
            # Clicking abilities
            py.click(slotsLocations[position])

def DeploymentSequence(allDropped):
    tempDeployTroopLocations = deployTroopLocations.copy()

    if selectedTroop == "Night Witch":
        delay = RandomFloatNumber(0, 2)
        a, b = slotsLocations[0][0] - builderMachineOffSetPos, slotsLocations[0][1]
        color = py.pixel(a, b)
        if color[0] in range(50, 80):
            allDropped = True
            py.click(a, b) # Click slot
            x, y, removeTemp = RandomPosition(tempDeployTroopLocations)
            tempDeployTroopLocations.remove(removeTemp)

            py.mouseDown(x, y)
            time.sleep(3)
            py.mouseUp()

            # Activating abilities
            for troops in range(armySlots):
                py.click(slotsLocations[troops][0] - builderMachineOffSetPos, slotsLocations[troops][1])

                time.sleep(RandomFloatNumber(0.5, 1))

            color = py.pixel(a, b)
            if color[0] in range(50, 80):
                return allDropped, delay
            else:
                allDropped = False
                return allDropped, delay
        else:
            return allDropped, delay

    elif selectedTroop == "Baby Dragon" or selectedTroop == "Pekka":
        delay = RandomFloatNumber(3, 6)
        # Used for range so we cant put the troop on different spots that are not used in the slotsLocation copy
        for location in range(armySlots):
            # Moves to the slot location to get the pixel value of it to see if the troop is not dropped
            if selectedTroop == "Pekka":
                py.moveTo(slotsLocations[location][0] - builderMachineOffSetPos, slotsLocations[location][1] - 3)
            else:
                py.moveTo(slotsLocations[location][0] - builderMachineOffSetPos, slotsLocations[location][1])

            x, y = py.position()
            color = py.pixel(x, y)

            if not running:
                return

            if color[0] in range(50, 80):
                time.sleep(RandomFloatNumber(0, 0.7))
                py.click()
                allDropped = True

                x, y, removeTemp = RandomPosition(tempDeployTroopLocations)
                tempDeployTroopLocations.remove(removeTemp)
                py.click(x, y)

        return allDropped, delay

def RandomPosition(tempDeployTroopLocations):
    # Randomizes the points/coordinate it chooses each time from the tempDeployTroopLocations list
    randomPoint = random.randrange(len(tempDeployTroopLocations))

    # Randomizes the amount it moves on the x axis from -100 to the maximum 200
    xRange = random.randint(tempDeployTroopLocations[randomPoint][0] - 100, tempDeployTroopLocations[randomPoint][0] + 200)

    if (tempDeployTroopLocations[randomPoint][0], tempDeployTroopLocations[randomPoint][1]) == (777, 843) or (tempDeployTroopLocations[randomPoint][0], tempDeployTroopLocations[randomPoint][1]) == (845, 36):
        yRange = 50
    else:
        yRange = 200

    # This gets the lower and higher x values to allow the full range of the x axis (-100)
    lowPoint = min(xRange, tempDeployTroopLocations[randomPoint][0])
    highPoint = max(xRange, tempDeployTroopLocations[randomPoint][0])

    # Chooses a point to set between values of low to high
    x = random.triangular(lowPoint, highPoint)
    y = random.triangular(tempDeployTroopLocations[randomPoint][1],tempDeployTroopLocations[randomPoint][1] + yRange)
    if (tempDeployTroopLocations[randomPoint][0], tempDeployTroopLocations[randomPoint][1]) == (777, 843):
        print(x, y)
    # Removes the point from the list to prevent dropping the same troop on each other
    removeTemp = tempDeployTroopLocations[randomPoint]
    return x, y, removeTemp

def FindAndClickImage(imageName: str, timer: int = None, threshold : float = 0.8, clickImage : bool = True, moveToImage : bool = True):
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
    if imageFound and clickImage:
        py.click(py.center(imageLocation))
        return True
    elif imageFound and moveToImage: # Move to image
        py.moveTo(py.center(imageLocation))
        return True
    elif imageFound: # Dont move to image or click
        return True
    else:
        print(f"Couldn't find image: {imageName}")
        return False

def CheckWallLevel():
    # region for the screenshot takes (left,top,width,height) the top is the y coordinate of the top left coordinate
    screenshot = py.screenshot(region=(1060, 749, 35 , 40))
    screenshot = np.array(screenshot)

    # Converting color to not get mismatched color then to grayscale and add blur and sharpen the image to improve image quality
    screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)
    gray = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (3, 3), 0)
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    sharp = cv.filter2D(blur, -1, kernel)

    # Turning all pixels to either black or white
    _, final = cv.threshold(sharp, 200, 255, cv.THRESH_BINARY)
    number = PredictNumber(final)

    wallLoot = int(number.replace(" ", ""))
    if wallLoot == 0:
        wallLoot = 9

    return wallLoot

def RandomFloatNumber(lowestNumber, highestNumber):
    number = random.uniform(lowestNumber, highestNumber)
    return number


attackButtonImage = r"Images\BuilderBaseImages\attackButton.png"
findNowButtonImage = r"Images\BuilderBaseImages\findNowButton.png"
battleStartsImage = r"Images\BuilderBaseImages\battleStartsImage.png"
twoStarsImage = r"Images\BuilderBaseImages\twoStarsImage.png"
returnHomeButton = r"Images\BuilderBaseImages\returnHomeButton.png"
okayButtonImage = r"Images\BuilderBaseImages\okayButton.png"
elixirCartImage = r"Images\BuilderBaseImages\elixirCartImage.png"
elixirCartImage2 = r"Images\BuilderBaseImages\elixirCartImage2.png"
goldStorageImage = r"Images\BuilderBaseImages\goldStorageImage.png"
elixirStorageImage = r"Images\BuilderBaseImages\elixirStorageImage.png"
upgradeMoreButtonImage = r"Images\BuilderBaseImages\upgradeMoreButton.png"
tenMoreWallsImage = r"Images\BuilderBaseImages\tenMoreWallsImage.png"

