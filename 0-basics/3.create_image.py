# Creates a new image with random RGB values
import random
from PIL import Image


def random_color_intensity():
    return random.randint(0, 255)


def random_rgb_color():
    r = random_color_intensity()
    g = random_color_intensity()
    b = random_color_intensity()

    return (r, g, b)


def main():
    # Load an image
    width = 200
    height = 200
    image = Image.new('RGB', (width, height))

    width, height = image.size

    # Iterate the pixels
    for x in range(width):
        for y in range(height):
            pixel = random_rgb_color()

            # Put random color pixel at coords (x, y)
            coords = (x, y)
            image.putpixel(coords, pixel)

    # Show and save the image
    image.show()
    image.save('noise.jpg', 'JPEG')

if __name__ == '__main__':
    main()
