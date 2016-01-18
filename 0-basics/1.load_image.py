# Loads an image using Image.open and visualises it using Image.show
from PIL import Image


def main():
    # Load an image
    image = Image.open('../lenna.png')

    # Visualise it
    image.show()


if __name__ == '__main__':
    main()
