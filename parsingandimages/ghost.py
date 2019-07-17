"""
ghost.py
"""

import os
import sys

"""
This line imports SimpleImage for use here
This line depends on the Pillow package being installed
"""
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the square of the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): squared distance between red, green, and blue pixel values

    This Doctest creates a simple green image and tests against
    a pixel of RGB values (0, 255, 0)
    >>> green_im = SimpleImage.blank(20, 20, 'green')
    >>> green_pixel = green_im.get_pixel(0, 0)
    >>> get_pixel_dist(green_pixel, 0, 255, 0)
    0
    >>> get_pixel_dist(green_pixel, 0, 255, 255)
    65025
    >>> get_pixel_dist(green_pixel, 5, 255, 10)
    125
    """
    distance = (pixel.red - red) ** 2 + (pixel.green - green) ** 2 + (pixel.blue - blue) ** 2
    return distance


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels

    Assumes you are returning in the order: [red, green, blue]
    This doctest creates a red, green, and blue pixel and runs some simple tests.
    >>> green_pixel = SimpleImage.blank(20, 20, 'green').get_pixel(0, 0)
    >>> red_pixel = SimpleImage.blank(20, 20, 'red').get_pixel(0, 0)
    >>> blue_pixel = SimpleImage.blank(20, 20, 'blue').get_pixel(0, 0)
    >>> get_average([green_pixel, red_pixel, blue_pixel])
    [85, 85, 85]
    >>> get_average([green_pixel, green_pixel, green_pixel])
    [0, 255, 0]
    >>> get_average([green_pixel, green_pixel, green_pixel, blue_pixel])
    [0, 191, 63]
    """
    red_amount = 0
    green_amount = 0
    blue_amount = 0
    count = 0
    for i in range(len(pixels)):
        red_amount += pixels[i].red
        green_amount += pixels[i].green
        blue_amount += pixels[i].blue
        count += 1
    average_red = red_amount // count
    average_green = green_amount // count
    average_blue = blue_amount // count

    return [average_red, average_green, average_blue]

def get_best_pixel(pixels):
    """
    Given a list of 3 or more pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    This doctest creates a red, green, and blue pixel and runs some simple tests.
    >>> green_pixel = SimpleImage.blank(20, 20, 'green').get_pixel(0, 0)
    >>> red_pixel = SimpleImage.blank(20, 20, 'red').get_pixel(0, 0)
    >>> blue_pixel = SimpleImage.blank(20, 20, 'blue').get_pixel(0, 0)
    >>> best1 = get_best_pixel([green_pixel, blue_pixel, blue_pixel])
    >>> best1.red, best1.green, best1.blue
    (0, 0, 255)
    >>> best2 = get_best_pixel([green_pixel, green_pixel, green_pixel, blue_pixel])
    >>> best2.red, best2.green, best2.blue
    (0, 255, 0)
    >>> best3 = get_best_pixel([red_pixel, red_pixel, red_pixel])
    >>> best3.red, best3.green, best3.blue
    (255, 0, 0)
    """
    average_RGB = get_average(pixels)
    compared_shortest_dist = float('inf')
    count = 0
    for i in range(len(pixels)):
        shortest_dist = get_pixel_dist(pixels[i], average_RGB[0], average_RGB[1], average_RGB[2])
        if shortest_dist <= compared_shortest_dist:
            compared_shortest_dist = shortest_dist
            count = i
    best_pixel = pixels[count]
    return best_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)

    pixel_list = []
    for y in range(height):
        for x in range(width):
            for i in range(len(images)):
                pixel_list.append(images[i].get_pixel(x, y))

            best_pixel = get_best_pixel(pixel_list)
            result.get_pixel(x, y).red = best_pixel.red
            result.get_pixel(x, y).green = best_pixel.green
            result.get_pixel(x, y).blue = best_pixel.blue
            pixel_list.clear()

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
