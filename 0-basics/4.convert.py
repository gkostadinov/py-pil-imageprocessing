# Convert image to a specific mode
from PIL import Image


def main():
    image = Image.open('../lenna.png')
    image.show('Original')

    # Image.convert converts the image to a given mode
    # Convert to grayscale (L - luminosity)
    grayscale = image.convert('L')
    grayscale.show('Grayscale')

    # Convert to bicolor
    bicolor = image.convert('1')
    bicolor.show('Bicolor')

    # Visualise it
    image.show()


if __name__ == '__main__':
    main()
