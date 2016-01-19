# Rank filtering - the rank filter sorts all pixels in a region and
# sets the value of the rank-th pixel.
import time
from PIL import Image, ImageFilter


def main():
    image = Image.open('../lenna.png')

    # Create a grayscale 3x3 sample image with values (0-9) * 28
    sample_image = Image.new('L', (3, 3))
    sample_image.putdata(list(map(lambda x: x * 28, range(9))))
    sample_image.resize((600, 600)).show('Sample image before ranking')

    # Apply 3x3 rank filters with ranks ranging 0-9
    for i in range(9):
        time.sleep(0.5)
        rank_filter = ImageFilter.RankFilter(3, rank=i)
        ranked_image = sample_image.filter(rank_filter)
        ranked_image.resize((600, 600)).show('Rank: %s, size 3x3' % i)

    # Now apply rank-based filters to the original image
    image.show('Original')

    for size in range(3, 9, 2):
        time.sleep(0.5)
        # Median filter, rank = (size * size) / 2 (the median value of
        # the sorted window). The median filter is used largely for
        # noise reduction.
        median_filter = ImageFilter.MedianFilter(size)
        median_filter_image = image.filter(median_filter)
        median_filter_image.show('Median filter, size: %sx%s' % (size, size))

        # Min filter, rank = 0 or the smallest pixel value in the sorted
        # window. Used in astrophotography. Dilates dark objects.
        min_filter = ImageFilter.MinFilter(size)
        min_filter_image = image.filter(min_filter)
        min_filter_image.show('Minimum filter, size: %sx%s' % (size, size))

        # Max filter, rank = size * size - 1 or the biggest pixel value
        # in the sorted window.
        max_filter = ImageFilter.MaxFilter(size)
        max_filter_image = image.filter(max_filter)
        max_filter_image.show('Maximum filter, size: %sx%s' % (size, size))


if __name__ == '__main__':
    main()
