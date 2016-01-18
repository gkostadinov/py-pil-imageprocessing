# Contrast enhancements
import time
from PIL import Image, ImageEnhance


def main():
    image = Image.open('../lenna.png')
    image.show('Original')

    color_enhancer = ImageEnhance.Contrast(image)
    # Enhancement factor of 0 gives solid grey image
    color_enhancer.enhance(0).show('Contrast factor: 0')
    # Enhancement factor of 1 gives the original image
    color_enhancer.enhance(1).show('Contrast factor: 1')

    # Increase the contrast of the image by increasing the factor
    # above 1 (up to 2)
    for i in range(10):
        factor = 1 + i / 10.0
        time.sleep(0.2)
        color_enhancer.enhance(factor).show('Contrast factor: %s' % factor)

if __name__ == '__main__':
    main()
