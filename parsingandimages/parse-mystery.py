"""
This program takes in a text file with encrypted data and parses
it to produce RGB codes. These RGB codes are then run through a
solve_mystery() function to attribute colors to the pixels of the
new image. Hence, the corrupted file will return a mystery image.
"""

import sys

"""
This line imports SimpleImage for use here
This line depends on the Pillow package being installed
"""
from simpleimage import SimpleImage


def decorrupt_red(s):
    """
    Given a string, remove non-numeric characters and return the
    resulting int.

    Input:
        s (string): string to be processed
    Returns:
        red (int): red value extracted from string
    >>> decorrupt_red('ake&1js4ls5')
    145
    >>> decorrupt_red('111')
    111
    >>> decorrupt_red('f9s')
    9
    >>> decorrupt_red(',;[9olk2')
    92
    >>> decorrupt_red('102')
    102
    >>> decorrupt_red('ovk;0q]')
    0
    """
    numbers = ''
    for i in range(len(s)):
        if s[i].isdigit():
            numbers += s[i]
    return int(numbers)

def decorrupt_green(s):
    """
    Given a string, change 'a's to 1's, reverse the string and return
    the resulting int.

    Input:
        s (string): string to be processed
    Returns:
        green (int): green value extracted from string
    >>> decorrupt_green('602')
    206
    >>> decorrupt_green('7')
    7
    >>> decorrupt_green('78a')
    187
    >>> decorrupt_green('qwe12a')
    121
    >>> decorrupt_green('#$0a')
    10
    >>> decorrupt_green('.,pl;a02')
    201
    """
    numbers = ''
    new_str = s[::-1]
    for i in range(len(new_str)):
        if new_str[i].isdigit():
            numbers += new_str[i]
        elif new_str[i] == 'a':
            numbers += '1'
    return int(numbers)

def decorrupt_blue(s):
    """
    Given a string, retrieve the string between the two ^'s and return
    the resulting int.

    Input:
        s (string): string to be processed
    Returns:
        blue (int): blue value extracted from string

    >>> decorrupt_blue('asd^6^n')
    6
    >>> decorrupt_blue('^213^')
    213
    >>> decorrupt_blue('2349^67^')
    67
    >>> decorrupt_blue('^10^')
    10
    >>> decorrupt_blue('^79^')
    79
    >>> decorrupt_blue('^0^')
    0
    """
    numbers = ''
    start_char = s.find('^')
    end_char = s.find('^', start_char + 2)

    for i in range(start_char, end_char):
        if s[i].isdigit():
            numbers += s[i]

    return int(numbers)

def parse_line(line):
    """
    Given a string, parse the RGB values out of it and return them as a
    list of int values. You can assume that the number of RGB values
    in a line is always a multiple of 3 and the order is always
    red, green, blue.

    Input:
        line (string): string to be processed containing corrupted RGB values
    Returns:
        rgb_values (List[int]): red, green, and blue values from string

    >>> parse_line('asd56as&* 93a sdffbsdf^200^asd')
    [56, 139, 200]
    >>> parse_line('45 54 *(&^45^')
    [45, 45, 45]
    >>> parse_line('j78 32 *$^240^8 k79 32a asd^32^hg')
    [78, 23, 240, 79, 123, 32]
    >>> parse_line('al11 pl1a ool?^20^8')
    [11, 11, 20]
    >>> parse_line('lk98m kfi9omaa ^98^')
    [98, 119, 98]
    >>> parse_line('icfj3jvmloaoq2 poa #$$%^108^f]')
    [32, 1, 108]
    """
    list = []
    splitted_str = line.split(' ')
    for i in range(len(splitted_str) // 3):
        count_list = [3 * i, 3 * i + 1, 3 * i + 2]
        red = decorrupt_red(splitted_str[count_list[0]])
        list.append(red)
        green = decorrupt_green(splitted_str[count_list[1]])
        list.append(green)
        blue = decorrupt_blue(splitted_str[count_list[2]])
        list.append(blue)

    """ why doesnt this work? Because the index() method
    returns the first time that element appears in the list.
    for i in range(len(splitted_str) // 3):
        if splitted_str.index(splitted_str[i * 3]) == 3 * i:
            red = decorrupt_red(splitted_str[i * 3])
            list.append(red)
        if splitted_str.index(splitted_str[i * 3 + 1]) == i * 3 + 1:
            green = decorrupt_green(splitted_str[i * 3 + 1])
            list.append(green)
        if splitted_str.index(splitted_str[i * 3 + 2]) == i * 3 + 2:
            blue = decorrupt_blue(splitted_str[i * 3 + 2])
            list.append(blue)
    """
    return list

def parse_file(filename):
    """
    Given a filename, parse out and return a list containing
    the width and the height of the image followed by all of the RGB
    values contained in the file.

    Input:
        filename (string): file containing corrupted RGB values
    Returns:
        rgb_values (List[int]): list where the first two values are
        width and height of image, followed by list of red, green,
        and blue values
    """
    list = []
    with open(filename, 'r') as f:
        for line in f:
            splitted_line = line.strip().split(' ')
            if len(splitted_line) == 2:
                list.append(int(splitted_line[0]))
                list.append(int(splitted_line[1]))
            else:
                list += parse_line(line)
    return list

def solve_mystery(filename):
    """
    Solve the mystery as described in the handout.
    Display image hidden in corrupted text file.
    """

    # SimpleImage boilerplate provided as a starting point
    rgb_values = parse_file(filename)

    width = rgb_values[0]
    height = rgb_values[1]

    rgb_only_values = rgb_values[2:]

    image = SimpleImage.blank(width, height)
    count = 0
    for y in range(image.height):
        for x in range(image.width):
            list = [count, count + 1, count + 2]
            pixel = image.get_pixel(x, y)
            pixel.red = rgb_only_values[list[0]]
            pixel.green = rgb_only_values[list[1]]
            pixel.blue = rgb_only_values[list[2]]
            count += 3

    # This displays image on screen
    image.show()


def main():

    # (provided code, DO NOT MODIFY)
    # Command lines:
    # 1. -nums file.txt -> prints numbers
    # 2. file.txt -> shows image solution
    args = sys.argv[1:]
    if len(args) == 2 and args[0] == '-nums':
        nums = parse_file(args[1])
        print(nums)
    if len(args) == 1:
        solve_mystery(args[0])



if __name__ == '__main__':
    main()
