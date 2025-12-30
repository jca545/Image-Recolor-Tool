# Image-Recolor-Tool

This tool replace a specified color to a new color specified by rgb.

## Installation
This tool requires using Python and the *PIL* library. 

Use the following command to install if haven't.
```bash
pip install pillow
```


## Getting Started


Follow the instructions to run the main script _main.py_:

#### 3.1. Clone and Navigate
```bash
# 1. Clone this repo to your local machine
git clone $THISREPO
# 2. Navigate into the repository directory
cd $THISREPO
```

#### 3.2. modify the code’s global variables
* **INPUT**: Path to the input image file for replacing color.
* **OUTPUT**: Path for the output image to save to.

For replacing a color (e.g. all Blue)
* replace line 77's function to the desire color's function.

For replacing specific rgb color
* **OLD_COLOR**: The rgb color to replace.
* **NEW_COLOR**: The rgb color to replace to.

#### 3.3. Run main.py
```bash
python3 main.py
```
You should see a "Saved: ..." in the terminal when done.