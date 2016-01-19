# Edge detection using sobel operator
from PIL import Image, ImageFilter, ImageChops


def apply_edge_detector(input_image):
    # Apply median filter with 3x3 window
    median_image = input_image.filter(
        ImageFilter.MedianFilter(3))

    # Apply 3x3 Sobel filters
    # Apply for X
    kernel_x = (-1, 0, 1,
                -2, 0, 2,
                -1, 0, 1)
    kernelx_image = median_image.filter(
        ImageFilter.Kernel((3, 3), kernel_x, scale=1))

    # Apply for Y
    kernel_y = (1, 2, 1,
                0, 0, 0,
                -1, -2, -1)
    kernely_image = median_image.filter(
        ImageFilter.Kernel((3, 3), kernel_y, scale=1))

    # Sum the pixels of the X and Y sobel images
    merged = ImageChops.add(
        kernelx_image, kernely_image)

    # Thresholding
    merged = merged.point(lambda x: 0 if x < 60 else 255)

    return merged


def main():
    # Edge detection works with grayscale images so we convert it to luminosity
    input_image = Image.open('../lenna.png').convert('L')
    output_image = apply_edge_detector(input_image)
    output_image.show('Edge detection using sobel operators')

if __name__ == '__main__':
    main()
