# Builder-Base-Bot
This is a standalone Builder Base macro made by Swift Macro. It is designed for Google Play Games on PC. It uses PyAutoGUI, so it will control your mouse.

The bot automatically stops an attack once it reaches 2 stars or after 45 seconds have passed (Time can be adjusted when running the program). It is based on the video:
https://www.youtube.com/watch?v=-YHt_uz3noI by BDLegend.

## Requirements
- The game must be in **Full Screen** to work
- Screen resolution must be set to **1920x1080**
- Must be on the **primary monitor**
- If needed, you can replace the images in the `Images/BuilderBaseImages` folder with your own screenshots for better accuracy or if you are using a different resolution

## How to use

### Option 1 (Recommended)
Download and run the `.exe` file from the latest release.

### Option 2 (Python)
If you clone the repository, install dependencies with: 

pip install -r requirements.txt

Then run: python BuilderBaseGui.py

## Download
Latest version: https://github.com/Swift-Macro/Builder-Base-Bot/releases/latest


## Known Bugs

### Walls

**Wall rings** can affect the detection of wall levels and cause the program to crash.
