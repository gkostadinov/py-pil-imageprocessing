# Using convolution kernels
# A small matrix, 3x3 or 5x5, is convolved with 3x3 window for each pixel
# resulting in an output pixel:
# https://en.wikipedia.org/wiki/Kernel_(image_processing)
from PIL import Image, ImageFilter


def main():
    image = Image.open('../lenna.png')
    image.show('Original')

    # Using kernels for blurring
    # The size of the kernel - can be 3x3 or 5x5
    size = (3, 3)
    # The kernel itself
    kernel_matrix = (1, 1, 1,
                     1, 1, 1,
                     1, 1, 1)
    # The final convolved result for each pixel is divied by the scale argument
    # By default it is the sum of the kernel matrix weights.
    # In our case the sum is 9. Each pixel is a result of convolving
    # the neighbour pixels with the kernel matrix and then dividing it by 9.
    # In other words - it is the mean value of the 3x3 window for each pixel
    # thus resulting in a blurred image.
    kernel = ImageFilter.Kernel(size, kernel_matrix)
    blurred_image = image.filter(kernel)
    blurred_image.show('Blur')

    # Let's smooth the image
    kernel_matrix = (1, 1, 1,
                     1, 5, 1,
                     1, 1, 1)
    kernel = ImageFilter.Kernel(size, kernel_matrix)
    smooth_image = image.filter(kernel)
    smooth_image.show('Smooth')

    # Sharpening
    kernel_matrix = (-2, -2, -2,
                     -2, 32, -2,
                     -2, -2, -2)
    kernel = ImageFilter.Kernel(size, kernel_matrix, scale=16)
    sharpen_image = image.filter(kernel)
    sharpen_image.show('Sharpen')

    # Detail
    kernel_matrix = (0, -1, 0,
                     -1, 10, -1,
                     0, -1, 0)
    kernel = ImageFilter.Kernel(size, kernel_matrix, scale=6)
    detail_image = image.filter(kernel)
    detail_image.show('Detail')


if __name__ == '__main__':
    main()
