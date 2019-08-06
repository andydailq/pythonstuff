"""
Breakout
Run from cmd line or main()
"""
from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120 # 120 frames per second.
NUM_LIVES = 3


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    bricks = 100

    while True:
        if graphics.out_of_zone():
            graphics.remove_ball()
            lives -= 1
            if lives > 0:
                graphics.reset_ball()
            elif lives == 0:
                graphics.win_or_lose(False)
                break
        if graphics.brick_nums == 0:
            graphics.win_or_lose(True)
            break
        graphics.move_ball()
        graphics.handle_wall_collisions()
        graphics.handle_obj_collisions()
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()




