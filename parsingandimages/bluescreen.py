"""
This program creates pictures using green screens or blue screens.
The program will output a new image that has the green/blue background
replaced with the desired background.
Limitations: The background picture must be bigger than the foreground image.
"""

"""
This line imports SimpleImage for use here
This line depends on the Pillow package being installed
"""
from simpleimage import SimpleImage

def photoshop(foreground, background):
    """
    Implement the photoshop assignment where the green screen
    background will be replaced with a background image. Green
    pixels will be detected around the foreground image and
    replace green pixels with pixels from corresponding x,y
    from background image.
    Pre-Cond.: green screen image with existing foreground figure
    and background is green.
    Post-Cond.: Photoshopped image with the original foreground but
    with a separate background picture that replaces the green background.
    """
    HURDLE_FACTOR = 1.45
    original_image = SimpleImage(foreground)
    background_image = SimpleImage(background)
    for pixel in original_image:
        average = (pixel.red + pixel.green + pixel.blue) // 3
        if pixel.green > average * HURDLE_FACTOR or pixel.blue > average * HURDLE_FACTOR:
            pixel_background = background_image.get_pixel(pixel.x, pixel.y)
            pixel.red = pixel_background.red
            pixel.green = pixel_background.green
            pixel.blue = pixel_background.blue
    return original_image
def main():
    """
    This program is used to generate a bluescreen and green screen image
    made by the non-blue or the none-green parts of a foreground image
    onto a background image.
    This function runs the program and using the show() method, opens the
    processed image so viewers can see the result.
    """

    photoshopped_myself = photoshop('images/myself.jpg', 'images/piano.jpg')
    photoshopped_myself.show()
    photoshopped_jellyfish = photoshop('images/jellyfish.jpg', 'images/garden.jpg')
    photoshopped_jellyfish.show()

if __name__ == '__main__':
    main()
