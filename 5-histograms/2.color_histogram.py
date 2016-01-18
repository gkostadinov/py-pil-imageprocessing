# Visualise image's color histogram
from PIL import Image
import matplotlib.pyplot as plt


def main():
    image = Image.open('../lenna.png')
    image.show('Image')

    plt.figure()
    plt.title('Color Histogram')
    plt.xlabel('Bins')
    plt.ylabel('# of Pixels')
    plt.xlim([0, 256])

    channels = image.split()
    colors = ['r', 'g', 'b']
    for channel, color in zip(channels, colors):
        # Get the histogram for each channel
        histogram = channel.histogram()
        plt.plot(histogram, color=color)

    plt.show()
    plt.close()


if __name__ == '__main__':
    main()
