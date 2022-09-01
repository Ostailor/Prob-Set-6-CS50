import sys
from PIL import Image, ImageOps

accept = ['.jpg', 'jpeg', '.png']

try:
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too many command-line arguments")
    if sys.argv[1][-4:].lower() not in accept:
        sys.exit("Invalid output")
    elif sys.argv[2][-4:].lower() not in accept:
        sys.exit("Invalid output")
    elif sys.argv[1][-4:].lower() != sys.argv[2][-4:].lower():
        sys.exit("Input and output have different extensions")

    person = Image.open(sys.argv[1])
    shirt = Image.open('shirt.png')
except FileNotFoundError:
    sys.exit("Input does not exit")
else:
    final = ImageOps.fit(person, [600, 600])
    final.paste(shirt, shirt)
    final.save(sys.argv[2])
