from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect
from campy.gui.events.timer import pause


WIDTH = 600
HEIGHT = 400

SUN_DIAMETER = 75
HORIZON_HEIGHT = 100
SUNSET_VELOCITY = 1.0
PAUSE_TIME = 40  # MS pause b/w frames

def make_sun(window):
    sun = GOval(width=SUN_DIAMETER, height=SUN_DIAMETER, x=(window.width - SUN_DIAMETER) / 2, y=(window.height - SUN_DIAMETER) / 2)
    sun.filled = True
    sun.fill_color = 'Yellow'
    return sun


def make_horizon(window):
    horizon = GRect(width=window.width, height=HORIZON_HEIGHT, x=0, y=window.height - HORIZON_HEIGHT)
    horizon.filled = True
    horizon.fill_color = 'Green'
    return horizon


def move_sun(window, sun):
    while sun.y < window.height - HORIZON_HEIGHT:
        sun.move(0, SUNSET_VELOCITY)
        pause(PAUSE_TIME)
    return move_sun


def main():
    """
    This program makes a simple sunset animation.
    """
    window = GWindow(width=WIDTH, height=HEIGHT,title='Sunset')
    sun = make_sun(window)
    horizon = make_horizon(window)
    window.add(sun)
    window.add(horizon)
    move_sun(window, sun)

if __name__ == '__main__':
    main()