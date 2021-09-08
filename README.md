# ImageSee

A simple and fast Image Viewer written in PyQt5/Qt

# WARNING:

This program is in beta. Until v1.0.0 (or the whatever stable version), there will not be a guided installer. For all beta versions (any version that has v0 at the start), you can download the zip files. Otherwise, you can wait until I make the installer. Plus, v1.0.0 (and above) will be the finished program.

# Installation

**Note:** Mac/Linux zipped versions in the releases won't come anytime soon, due to PyInstaller requiring a machine for each OS. While virtual machines are a thing, it's a hassle to do it every time, and so I won't do it, atleast when I can figure out an automated solution.

## For Windows users:

1. Go to the Releases and find the latest release.
2. Download the zip file.
3. Unzip it.
4. Run the exe file.

## For Mac/Linux users:

You **_can_** actually use it on Mac/Linux! However, you have to build it manually.

If you wanted to build it and package it into a distributable, then:

1. Download the source code (by: `git clone https://github.com/0xBooper/ImageSee.git`)
2. Download Python 3
3. Install all dependencies. The project requires only PyQt5, so you can do `pip install pyqt5`
4. Install PyInstaller, for the build process (by: `pip install pyinstaller`)
5. Run `pyinstaller ImageSee.spec`

---
