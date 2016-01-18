# Equialize image's histogram
from PIL import Image, ImageOps
import matplotlib.pyplot as plt


def plot_histogram(title, image):
    plt.figure()
    plt.title(title)
    plt.xlabel('Bins')
    plt.ylabel('# of Pixels')
    plt.xlim([0, 256])

    histogram = image.histogram()
    plt.plot(histogram)

    plt.show()
    plt.close()


def main():
    image = Image.open('../lenna.png').convert('L')
    image.show('Original')
    plot_histogram('Original Histogram', image)

    equalized_image = ImageOps.equalize(image)
    equalized_image.show('Equalized image')
    plot_histogram('Equalized Histogram', equalized_image)


if __name__ == '__main__':
    main()
