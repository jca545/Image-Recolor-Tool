from PIL import Image

INPUT = "1677893104127.png"
OUTPUT = "blue.png"
# Example replacement color (yellow)
OLD_COLOR = (210, 166, 215)
NEW_COLOR = (191, 221, 255)


# https://rgbcolorpicker.com/

def isRed(pixel):
    r = pixel[0]
    g = pixel[1]
    b = pixel[2]
    if r > 100 and g < 100 and b < 100:
        return True
    return False

def isGreen(pixel): 
    r = pixel[0]
    g = pixel[1]
    b = pixel[2]
    if r < 100 and g > 100 and b < 100:
        return True
    return False

def isBlue(pixel):
    r = pixel[0]
    g = pixel[1]
    b = pixel[2]
    if r < 100 and g < 100 and b > 100:
        return True
    return False

def isYellow(pixel):
    r = pixel[0]
    g = pixel[1]
    b = pixel[2]
    if r > 100 and g > 100 and b < 100:
        return True
    return False

def isPurple(pixel):
    r = pixel[0]
    g = pixel[1]
    b = pixel[2]
    if r > 200 and g > 150 and b > 200:
        return True
    return False

def match(pixel):
    if pixel == OLD_COLOR:
        return True
    return False


# ---- main program ----
img = Image.open(INPUT).convert("RGBA")
pixels = img.load()

width, height = img.size


for row in range(height):
    for col in range(width):
        r, g, b, a = pixels[col, row]

        # Skip transparent pixels
        if a == 0:
            continue

        # replacing
        if isPurple([r, g, b]):
            pixels[col, row] = (*NEW_COLOR, a)   # same alpha

img.save(OUTPUT)
print("Saved:", OUTPUT)
