# Iterates through image's pixels and prints the RGB values
from PIL import Image


def main():
    # Load an image
    image = Image.open('../lenna.png')

    width, height = image.size

    # Iterate the pixels
    for x in range(width):
        for y in range(height):
            # Get pixel at coords (x, y)
            coords = (x, y)
            pixel = image.getpixel(coords)

            r, g, b = pixel
            print('image[%s, %s] = rgb(%s, %s, %s)' % (x, y, r, g, b))


if __name__ == '__main__':
    main()
