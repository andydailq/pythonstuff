"""

This program graphs the rank of baby names on any given canvas size
The x-axis represents the last century + one decade: (1900 - 2010) and
the y-axis represents the rank of baby names. If the rank is non-existent
or ranked at 1000, the returned rank is * on the graph. 

"""

import tkinter
import babynames
import babygraphicsgui as gui


FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 550


YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (float): The x coordinate of the vertical line associated
                              with the specified year.
    >>> round(get_x_coordinate(1000, 0), 1)
    20.0
    >>> round(get_x_coordinate(1000, 2), 1)
    180.0
    >>> round(get_x_coordinate(1000, 11), 1)
    900.0
    """
    delta = (width - GRAPH_MARGIN_SIZE * 2) / len(YEARS)

    x_coord = GRAPH_MARGIN_SIZE + delta * year_index
    return x_coord

def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas
    width = canvas.winfo_width()    # get the width of the canvas
    height = canvas.winfo_height() - 4  # get the height of the canvas

    canvas.create_line(GRAPH_MARGIN_SIZE - 1, GRAPH_MARGIN_SIZE - 1, width - GRAPH_MARGIN_SIZE - 1,
                       GRAPH_MARGIN_SIZE - 1)
    canvas.create_line(GRAPH_MARGIN_SIZE - 1, height - GRAPH_MARGIN_SIZE - 1, width - GRAPH_MARGIN_SIZE - 1,
                       height - GRAPH_MARGIN_SIZE - 1)

    for i in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(width, i) - 1, 0, get_x_coordinate(width, i) - 1, height - 1)
        canvas.create_text(get_x_coordinate(width, i) - 1 + TEXT_DX, height - GRAPH_MARGIN_SIZE - 1, text=YEARS[i],
                           anchor=tkinter.NW)


def scale_factor(num):
    """
    This function scales down the y values according to the canvas height
    to fit the data points proportionately between the upper and lower graph margins

    Input:
        y value (num): the rank of the data point
    Returns:
        scaled_value (float): The y value of the data point scaled down to fit the canvas

    >>> scale_factor(1000)
    530.0
    >>> scale_factor(100)
    71.0
    >>> scale_factor(0)
    20.0
    """
    useable_canvas_height = CANVAS_HEIGHT - (2 * GRAPH_MARGIN_SIZE)
    scaled_value = (num / MAX_RANK) * useable_canvas_height + GRAPH_MARGIN_SIZE
    return scaled_value


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid
    width = canvas.winfo_width()    # get the width of the canvas
    height = canvas.winfo_height() - 4 # get the height of the canvas

    
count = 0
    for name in lookup_names:
        color = ''
        if count % 4 == 0:
            color += COLORS[0]
        elif count % 4 == 1:
            color += COLORS[1]
        elif count % 4 == 2:
            color += COLORS[2]
        else:
            color += COLORS[3]
        count += 1
        for match_name in name_data:
            if name == match_name:
                year_rank = name_data[name] # list of year and rank of a name, sorted by year
                for i in range(len(YEARS) - 1):
                    if YEARS[i] in year_rank:
                        if YEARS[i + 1] in year_rank:
                            canvas.create_line(get_x_coordinate(width, i),
                                               scale_factor(year_rank[YEARS[i]]) - 1,
                                               get_x_coordinate(width, i + 1),
                                               scale_factor(year_rank[YEARS[i + 1]]) - 1, width=LINE_WIDTH, fill=color)
                            canvas.create_text(get_x_coordinate(width, i) + TEXT_DX,
                                               scale_factor(year_rank[YEARS[i]]) - 1,
                                               text=name + ' ' + str(year_rank[YEARS[i]]), anchor=tkinter.SW,
                                               fill=color)
                            canvas.create_text(get_x_coordinate(width, i + 1) + TEXT_DX,
                                               scale_factor(year_rank[YEARS[i + 1]]) - 1,
                                               text=name + ' ' + str(year_rank[YEARS[i + 1]]), anchor=tkinter.SW,
                                               fill=color)
                            continue
                        elif YEARS[i + 1] not in year_rank or year_rank[YEARS[i + 1]] == 1000:
                            canvas.create_line(get_x_coordinate(width, i), scale_factor(year_rank[YEARS[i]]) - 1,
                                               get_x_coordinate(width, i + 1),
                                               scale_factor(MAX_RANK) - 1, width=LINE_WIDTH, fill=color)
                            canvas.create_text(get_x_coordinate(width, i) + TEXT_DX,
                                               scale_factor(year_rank[YEARS[i]]) - 1,
                                               text=name + ' ' + str(year_rank[YEARS[i]]), anchor=tkinter.SW,
                                               fill=color)
                            canvas.create_text(get_x_coordinate(width, i + 1) + TEXT_DX,
                                               scale_factor(MAX_RANK) - 1,
                                               text=name + ' ' + str('*'), anchor=tkinter.SW, fill=color)
                            continue
                    else:
                        if YEARS[i] not in year_rank or year_rank[YEARS[i]] == 1000:
                            if YEARS[i + 1] not in year_rank or year_rank[YEARS[i + 1]] == 1000:
                                canvas.create_line(get_x_coordinate(width, i), scale_factor(MAX_RANK) - 1,
                                                   get_x_coordinate(width, i + 1),
                                                   scale_factor(MAX_RANK) - 1, width=LINE_WIDTH, fill=color)
                                canvas.create_text(get_x_coordinate(width, i) + TEXT_DX,
                                                   scale_factor(MAX_RANK) - 1,
                                                   text=name + str('*'), anchor=tkinter.SW, fill=color)
                                canvas.create_text(get_x_coordinate(width, i + 1) + TEXT_DX,
                                                   scale_factor(MAX_RANK) - 1,
                                                   text=name + ' ' + str('*'), anchor=tkinter.SW,
                                                   fill=color)
                                continue

                            elif YEARS[i + 1] in year_rank:
                                canvas.create_line(get_x_coordinate(width, i), scale_factor(MAX_RANK) - 1,
                                                   get_x_coordinate(width, i + 1),
                                                   scale_factor(year_rank[YEARS[i + 1]]) - 1, width=LINE_WIDTH,
                                                   fill=color)
                                canvas.create_text(get_x_coordinate(width, i) + TEXT_DX,
                                                   scale_factor(MAX_RANK) - 1,
                                                   text=name + ' ' + str('*'), anchor=tkinter.SW, fill=color)
                                canvas.create_text(get_x_coordinate(width, i + 1) + TEXT_DX,
                                                   scale_factor(year_rank[YEARS[i + 1]]) - 1,
                                                   text=name + ' ' + str(year_rank[YEARS[i + 1]]), anchor=tkinter.SW,
                                                   fill=color)
                                continue

        

        del color

def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()