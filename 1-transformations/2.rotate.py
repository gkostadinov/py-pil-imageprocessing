# Rotating or flipping an image
from PIL import Image


def main():
    image = Image.open('../lenna.png')
    image.show('Original')

    # Rotate 60 degrees counter clockwise
    rotated_image = image.rotate(60)
    rotated_image.show('Rotate 60')

    # Rotate using Image.transpose
    # Transpose supports these values:
    #  - Image.FLIP_LEFT_RIGHT
    #  - Image.FLIP_TOP_BOTTOM
    #  - Image.ROTATE_90
    #  - Image.ROTATE_180
    #  - Image.ROTATE_270
    rotated_image = image.transpose(Image.ROTATE_90)
    rotated_image.show('Rotate 90')

    # Flip horizontal
    flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)
    flipped_image.show('Flip horizontal')

    # Flip vertical
    flipped_image = image.transpose(Image.FLIP_TOP_BOTTOM)
    flipped_image.show('Flip vertical')


if __name__ == '__main__':
    main()
