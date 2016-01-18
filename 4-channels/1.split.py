# Split image's channels
from PIL import Image


def main():
    image = Image.open('../lenna.png')
    image.show('Original')

    # Image.split splits image's channels and returns a tuple of channels
    # or the same image if the mode is L or 1
    r, g, b = image.split()

    r.show('R channel')
    g.show('G channel')
    b.show('B channel')

if __name__ == '__main__':
    main()
