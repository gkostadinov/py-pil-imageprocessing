# Cropping an image region
from PIL import Image


def main():
    image = Image.open('../lenna.png')
    image.show('Original')

    # Define the region which is going to be cropped
    # A region is defined like this: (left, upper, right, lower)
    # where (left, upper) are the coordinates of the starting point
    # and (right, lower) are the coordinates of the ending point
    region = (135, 160, 235, 260)  # 100x100 region

    image_crop = image.crop(region)
    image_crop.show('Crop')

if __name__ == '__main__':
    main()
