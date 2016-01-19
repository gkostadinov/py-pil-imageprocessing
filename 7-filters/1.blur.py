# Blur filters
import time
from PIL import Image, ImageFilter


def main():
    image = Image.open('../lenna.png')
    image.show('Original')

    # Normal blur
    image_filter = ImageFilter.BLUR
    blurred_image = image.filter(image_filter)
    blurred_image.show('Normal Blur')

    # Gaussian blur with radius 1-10
    for i in range(10):
        radius = 1 + i
        time.sleep(0.2)

        image_filter = ImageFilter.GaussianBlur(radius=radius)
        blurred_image = image.filter(image_filter)
        blurred_image.show('Gaussian Blur (radius %s)' % radius)

if __name__ == '__main__':
    main()
