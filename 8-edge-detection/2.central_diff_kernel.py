# Using the same method as in 1.gradient but this time
# the edge detection is done with ImageFilter.Kernel
from PIL import Image, ImageFilter, ImageChops


def apply_edge_detector(input_image):
    # Apply median filter with 3x3 window
    median_image = input_image.filter(
        ImageFilter.MedianFilter(3))

    # Apply 3x3 center difference filters
    # Apply for X
    kernel_x = (0, 0, 0,
                -1, 0, 1,
                0, 0, 0)
    kernelx_image = median_image.filter(
        ImageFilter.Kernel((3, 3), kernel_x, scale=2))

    # Apply for Y
    kernel_y = (0, -1, 0,
                0, 0, 0,
                0, 1, 0)
    kernely_image = median_image.filter(
        ImageFilter.Kernel((3, 3), kernel_y, scale=2))

    # Sum the pixels of X and Y
    merged = ImageChops.add(
        kernelx_image, kernely_image)

    # Thresholding
    merged = merged.point(lambda x: 0 if x < 10 else 255)

    return merged


def main():
    # Edge detection works with grayscale images so we convert it to luminosity
    input_image = Image.open('../lenna.png').convert('L')
    output_image = apply_edge_detector(input_image)
    output_image.show('Edge detection')

if __name__ == '__main__':
    main()
