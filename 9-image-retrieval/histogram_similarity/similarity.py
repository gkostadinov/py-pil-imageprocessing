# A rather simple approach for image retrieval using image histograms and
# sobel edge detection, the output is saved in a HTML page
import os
import math
import numpy as np
import matplotlib.pylab as plt
from PIL import Image, ImageFilter

IMAGES_DIR = 'images'
HISTOGRAMS_DIR = 'histograms'


def save_histogram(histogram, output_file):
    plt.figure()
    plt.title('Histogram')
    plt.xlabel('Bins')
    plt.ylabel('# pixels')
    plt.xlim([0, len(histogram)])
    plt.plot(histogram)
    output_path = os.path.join(HISTOGRAMS_DIR, output_file)
    plt.savefig(output_path)
    plt.close()

    return output_path


def normalize_histogram(histogram):
    # Normalizes a given histogram making it with vector distance 1
    np_histogram = np.array(histogram)
    normalized_histogram = np_histogram / np.linalg.norm(np_histogram)

    return normalized_histogram.tolist()


def get_image_histogram(image):
    # Get the histogram and normalize it
    # so that the histogram vector length is 1
    # (making it much better for similarity comparison)
    histogram = normalize_histogram(image.histogram())
    histogram_path = save_histogram(
        histogram, os.path.basename(image.filename))

    return histogram, histogram_path


def get_sobel_histogram(image):
    # See 8-edge-detection/3.sobel
    grayscale_image = image.convert('L')

    median_filter = ImageFilter.MedianFilter(size=3)
    median_image = grayscale_image.filter(median_filter)

    sobel_x = (-1, 0, 1,
               -2, 0, 2,
               -1, 0, 1)
    sobel_kernel_x = ImageFilter.Kernel((3, 3), sobel_x, scale=1)
    sobel_image_x = median_image.filter(sobel_kernel_x)

    sobel_y = (1, 2, 1,
               0, 0, 0,
               -1, -2, -1)
    sobel_kernel_y = ImageFilter.Kernel((3, 3), sobel_y, scale=1)
    sobel_image_y = median_image.filter(sobel_kernel_y)

    # Generate histograms for X and Y and normalize them
    sobel_histogram_x = normalize_histogram(sobel_image_x.histogram())
    sobel_histogram_y = normalize_histogram(sobel_image_y.histogram())

    # Concatenate into a single histogram
    sobel_histogram = sobel_histogram_x
    sobel_histogram.extend(sobel_histogram_y)

    sobel_histogram_path = save_histogram(
        sobel_histogram, 'sobel_' + os.path.basename(image.filename))

    return sobel_histogram, sobel_histogram_path


def load_images():
    # Get all image filenames in the images directory
    image_filenames = os.listdir(IMAGES_DIR)

    images = {}
    for image_filename in image_filenames:
        if image_filename.endswith('jpeg') or image_filename.endswith('jpg'):
            image_filepath = os.path.join(IMAGES_DIR, image_filename)

            # Load the image and get histograms
            image = Image.open(image_filepath)
            histogram, histogram_path = get_image_histogram(image)
            sobel_histogram, sobel_histogram_path = get_sobel_histogram(image)

            images[image_filename] = {
                'image_path': image_filepath,
                'histogram': histogram,
                'histogram_path': histogram_path,
                'sobel_histogram': sobel_histogram,
                'sobel_histogram_path': sobel_histogram_path
            }

    return images


def similarity(histogram_a, histogram_b):
    # Eucledean distance
    sum_dist = 0
    for i in range(len(histogram_a)):
        sum_dist += ((histogram_a[i] - histogram_b[i]) *
                     (histogram_a[i] - histogram_b[i]))

    return math.sqrt(sum_dist)


def find_similarities(query_imagename, images):
    query_image = images[query_imagename]

    similarities = []
    for imagename, image in images.iteritems():
        if imagename == query_imagename:
            continue

        # Calculate similarities
        histogram_dist = similarity(
            query_image['histogram'], image['histogram'])
        sobel_histogram_dist = similarity(
            query_image['sobel_histogram'], image['sobel_histogram'])

        similarity_dist = 0.5 * histogram_dist + 0.5 * sobel_histogram_dist
        similarities.append((image, similarity_dist))

    return sorted(similarities, key=lambda x: x[1])


def generate_html_page(query_image, similarities):
    with open('similarities.html', 'w') as similarities_html:
        similarities_html.write(
            '<html><head><title>Similarities</title></head><body>')

        # Show the query image
        similarities_html.write(
            ('Query image:<br><img src="%s" width="400">' +
             '<img src="%s" width="300"><img src="%s" width="300"><hr>')
            % (query_image['image_path'],
               query_image['histogram_path'],
               query_image['sobel_histogram_path']))

        for image, similarity_dist in similarities:
            similarities_html.write(
                ('Similarity: %s<br><img src="%s" width="300">' +
                 '<img src="%s" width="300"><img src="%s" width="300"><hr>')
                % (similarity_dist,
                   image['image_path'],
                   image['histogram_path'],
                   image['sobel_histogram_path']))

        similarities_html.write('</body></html>')


def main():
    images = load_images()
    query_imagename = '1.jpeg'
    similarities = find_similarities(query_imagename, images)

    generate_html_page(images[query_imagename], similarities)


if __name__ == '__main__':
    main()
