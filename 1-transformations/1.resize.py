# Resizing images using Image.resize
from PIL import Image


def main():
    image = Image.open('../lenna.png')
    image.show('Original')

    width, height = image.size
    new_width, new_height = (150, 100)

    # Resize image without preserving aspect ratio
    resized_image = image.resize((new_width, new_height))
    resized_image.show('Resize without preserving aspect')

    # Resize by preserving aspect ratio
    # Float casting the height so that the ratio is a float number
    ratio = width / float(height)

    # Casting to integer because we are working with pixels
    new_height = int(new_width / ratio)
    # or new_width = int(new_height * ratio)
    resized_image = image.resize((new_width, new_height))
    resized_image.show('Resize by preserving aspect')

if __name__ == '__main__':
    main()
