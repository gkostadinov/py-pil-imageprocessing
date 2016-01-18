# Merge channels (images with single channel) into one
from PIL import Image


def main():
    image = Image.open('../lenna.png')
    image.show('Original')

    # Split the channels
    red, green, blue = image.split()

    # We will now make images out of each of these channels and visualise them.
    # In order to show the actual color of the channel, we will need to create
    # a completely black image representing channel with 0 values.
    # Image.new creates a black image by default.
    black = Image.new('L', image.size)

    red_image = Image.merge('RGB', [red, black, black])
    red_image.show('Red channel')
    green_image = Image.merge('RGB', [black, green, black])
    green_image.show('Green channel')
    blue_image = Image.merge('RGB', [black, black, blue])
    blue_image.show('Blue channel')

if __name__ == '__main__':
    main()
