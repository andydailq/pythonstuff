from simpleimage import SimpleImage
# triple image width. Vertical flip first, keep second as original, and reflect about y-axis for third
def triplicate(filename):
    image = SimpleImage(filename)
    new = SimpleImage.blank(image.width * 3, image.height)
    for y in range(image.height):
        for x in range(image.width):
            old = image.get_pixel(x, y)

            # left image
            left = new.get_pixel(x, image.height - 1 - y)
            left.red = old.red
            left.green = old.green
            left.blue = old.blue

            # middle image
            middle = new.get_pixel(x + image.width, y)
            middle.red = old.red
            middle.green = old.green
            middle.blue = old.blue

            # right image
            right = new.get_pixel(image.width - 1 - x, y)
            right.red = old.red
            right.green = old.green
            right.blue = old.blue
    pass

def process_all_images(filename):
# processes file name and adds extension .png
    with open(filename, 'r') as f:
        for line in f:
            array = line.split()
            for each in array:
                image = triplicate(each + '.png')
                image.show()