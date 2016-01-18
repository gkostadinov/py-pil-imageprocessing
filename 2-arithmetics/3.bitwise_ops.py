# Bitwise operations - add, or, xor
# Very useful arithmetics if used for masks
from PIL import Image, ImageChops

if __name__ == '__main__':
    # Create two white (image mode 1, so white is 1)
    # images and rotate them differently
    image1 = Image.new('1', (200, 200), color=1).rotate(60)
    image2 = Image.new('1', (200, 200), color=1).rotate(30)

    image1.show('Image 1')
    image2.show('Image 2')

    # Lets say we have this:
    # pixel1 - a pixel from image1
    # pixel2 - a pixel from image2

    # Logical AND - true if pixel1 > 0 and pixel2 > 0 else false
    # or in other words:
    # sets value 1 (white) if both pixels are greater than zero
    # 0 (black) otherwise
    logical_and = ImageChops.logical_and(image1, image2)
    logical_and.show('Logical and')

    # Logical OR - true if pixel1 > 0 or pixel2 > 0 else false
    # or in other words:
    # sets value 1 (white) if either of the two pixels are greater than zero
    # 0 (black) otherwise
    logical_or = ImageChops.logical_or(image1, image2)
    logical_or.show('Logical or')

    # Logical XOR - true if (pixel1 > 0 or pixel2 > 0) and
    # not (pixel1 > 0 and pixel2 > 0) else false
    # or in other words:
    # sets value 1 (white) if only either (but not both) of the two pixels
    # are greater than zero 0 (black) otherwise
    logical_xor = ImageChops.logical_xor(image1, image2)
    logical_xor.show('Logical xor')
