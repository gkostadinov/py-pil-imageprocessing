# Visualise image's grayscale histogram
from PIL import Image
import matplotlib.pyplot as plt


def main():
    image = Image.open('../lenna.png')
    image.show('Image')

    # Get the grayscale histogram using Image.histogram
    grayscale_histogram = image.convert('L').histogram()
    plt.figure()
    plt.title('Grayscale Histogram')
    plt.xlabel('Bins')
    plt.ylabel('# of Pixels')
    plt.plot(grayscale_histogram)
    plt.xlim([0, 256])
    plt.show()
    plt.close()


if __name__ == '__main__':
    main()
