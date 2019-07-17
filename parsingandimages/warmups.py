
"""
This line imports SimpleImage for use here
This line depends on the Pillow package being installed
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    Saturates the "red" pixels and grayscales all other pixels in the
    image in order to highlight areas of wildfires.

    Input:
        filename (string): name of image file to be read in

    Returns:
        highlighted (SimpleImage): image with reddish pixels highlighted
    """
    image = SimpleImage(filename)
    for pixel in image:
        average = (pixel.red + pixel.blue + pixel.green) // 3
        if pixel.red > average * HURDLE_FACTOR:
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        else:
            pixel.red = average
            pixel.green = average
            pixel.blue = average
    return image


def reflect(filename):
    """
    Vertically "reflects" an image over the bottom horizontal axis and
    returns an image of twice the original height.

    Input:
        filename (string): name of image file to be read in

    Returns:
        reflected (SimpleImage): reflected image, twice original height
    """
    image = SimpleImage(filename)
    reflected = SimpleImage.blank(width=image.width, height=2*image.height)
    for y in range(image.height):
        for x in range(image.width):
            old_pixel = image.get_pixel(x, y)
            # top image
            top_image = reflected.get_pixel(x, y)
            top_image.red = old_pixel.red
            top_image.green = old_pixel.green
            top_image.blue = old_pixel.blue
            # bottom image
            bottom_image = reflected.get_pixel(x, 2 * image.height - 1 - y)
            bottom_image.red = old_pixel.red
            bottom_image.green = old_pixel.green
            bottom_image.blue = old_pixel.blue
    return reflected


def main():

    # Comment/uncomment these out as you implement them!
    # When you submit this file, make sure all lines in main are uncommented

    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()

    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
