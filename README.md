# CyberCV
Repository for Python desktop application for cybersportsmen reaction testing

## Features
Provides 6 different reaction tests for cybersportsmen with estimation of their reaction speed as a primary goal.
Here is the list of tests (we keep the names, provided by program requestors):
- Reaction Test
- Color Reaction Test
- Action Reaction Test
- Choice Reaction Test
- Tapping Test
- Noisy Test

For more info about each specific test check out docstring for corresponding class in .py file.

## Requirements
Testing is implemented using the following Python CV (Computer Vision) libraries:
- opencv-python (cv2)
- mediapipe

Supplementary libraries:
- numpy
- requests

Libraries for building .exe file:
- pyinstaller

## Installation
```bash
git clone https://github.com/Ausar686/CyberCV
cd CyberCV
pip install requirements.txt
```

## Running
### Windows
```bash
python main.py
```

### Linux
```bash
python3 main.py
```

## Building an .exe file (Windows only)
Run inside "CyberCV" directory: 
```bash
pyinstaller main.py
```

> **Note:** Don't forget to copy video files into created directory.
**DO NOT** rename video files.
**DO NOT** create individual dirctory for .mp4 files inside your directory with .exe file
