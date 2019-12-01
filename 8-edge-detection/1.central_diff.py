# This is a detailed and behind the scenes example of how
# edge detection works. The method used is central differences.
# https://en.wikipedia.org/wiki/Edge_detection
import math
from PIL import Image, ImageFilter


def apply_edge_detector(input_image):
    output_image = Image.new('1', input_image.size)

    width, height = input_image.size

    for x in range(width):
        for y in range(height):
            # Iterate the image
            dx = dy = 1

            # Check if the current position is not a border one
            if x not in [0, width - 1] and y not in [0, height - 1]:
                # Calculate delta X and Y
                # dx = east pixel - west pixel
                dx = (input_image.getpixel((x + 1, y)) -
                      input_image.getpixel((x - 1, y))) / 2.0
                # dy = north pixel - south pixel
                dy = (input_image.getpixel((x, y - 1)) -
                      input_image.getpixel((x, y + 1))) / 2.0

                if dx == 0:
                    dx = 1
                if dy == 0:
                    dy = 1

            # Calculate gradient magnitude or how much the color has changed
            grad_magnitude = math.sqrt(dx * dx + dy * dy)
            # Calculate gradient orientation or angle of change
            grad_orientation = abs(math.atan2(dy, dx) * (180 / math.pi))
            grad_orientation = math.ceil(grad_orientation)

            # Thresholding
            output_pixel = grad_orientation <= 360 and grad_magnitude >= 20

            output_image.putpixel((x, y), output_pixel)

    return output_image


def main():
    # Edge detection works with grayscale images so we convert it to luminosity
    input_image = Image.open('../lenna.png').convert('L')
    size = 3
    median_filter = ImageFilter.MedianFilter(size)
    median_filter_image = input_image.filter(median_filter)
    median_filter_image.show('Median filter, size: %sx%s' % (size, size))
    output_image = apply_edge_detector(median_filter_image)
    output_image.show('Edge detection')

if __name__ == '__main__':
    main()
