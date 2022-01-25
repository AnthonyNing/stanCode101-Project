"""
File: babygraphics.py
Name: Anthony Ning
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
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
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
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
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    unit = width // len(YEARS)
    return GRAPH_MARGIN_SIZE+unit*year_index


def get_y_coordinate(height, rank):
    """
    Given the height of the canvas and the rank of the current year
    returns the y coordinate where the rank should be drawn.

    Input:
        height (int): The height of the canvas
        rank (str): The rank number
    Returns:
        y_coordinate (int): The y coordinate of the rank.
    """
    unit = height / 1000
    if rank is None:
        return int(GRAPH_MARGIN_SIZE+height)
    else:
        return int(GRAPH_MARGIN_SIZE+unit*int(rank))


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    # boundary
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    # each line with year beside it
    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH-2*GRAPH_MARGIN_SIZE, i)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT, width=LINE_WIDTH)
        canvas.create_text(x+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW, font='times 20')


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

    # ----- Write your code below this line ----- #
    # number we use to assign colors
    color_num = 0
    # coordinates we use to record the previous spot
    draw_x = 0
    draw_y = 0
    # Use look-up names as keys to find values in name_data.
    for name in lookup_names:
        target_year = []
        for key in name_data:
            # case-insensitive
            if name.upper() == key.upper():
                # After finding the values in name_data, we put the keys of the values,
                # which are dictionary, into a list.
                for year in name_data[key]:
                    target_year.append(year)
                # For each year in the list, YEARS, we find if it is contained in the list that we just created.
                for i in range(len(YEARS)):
                    # Get x-coordinate for every year-index in YEARS.
                    x = get_x_coordinate(CANVAS_WIDTH - 2 * GRAPH_MARGIN_SIZE, i)
                    # If the year is not contained in the list that we just created, we assign rank as None,
                    # and we get y-coordinate.
                    # We create texts at the according coordinates.
                    if str(YEARS[i]) not in target_year:
                        rank = None
                        y = get_y_coordinate(CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE, rank)
                        canvas.create_text(x + TEXT_DX, y, text='*', anchor=tkinter.NW,
                                           fill=COLORS[color_num % 3], font='times 15')
                    # If the year is contained in the list that we just created,
                    # we get the according rank value, and we get y-coordinate.
                    # We create texts containing names and ranks at the according coordinates.
                    else:
                        rank = name_data[key][str(YEARS[i])]
                        y = get_y_coordinate(CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE, rank)
                        canvas.create_text(x + TEXT_DX, y, text=name+' '+rank, anchor=tkinter.NW,
                                           fill=COLORS[color_num % 3], font='times 15')
                    # Lastly, we draw lines from point to point.
                    if i >= 1:
                        canvas.create_line(draw_x, draw_y, x, y, width=LINE_WIDTH, fill=COLORS[color_num % 3])
                    draw_x = x
                    draw_y = y
        color_num += 1


# main() code is provided, feel free to read through it but DO NOT MODIFY
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
