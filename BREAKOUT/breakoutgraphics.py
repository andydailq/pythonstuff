"""
Breakout
run from cmd line or main()
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

# Color names to cycle through for brick rows.
COLORS = ['RED', 'ORANGE', 'YELLOW', 'GREEN', 'BLUE']

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 5.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 3.5      # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle.
        self.paddle = GRect(width=paddle_width, height=paddle_height, x=(self.window.width - paddle_width) / 2,
                            y=self.window.height - paddle_offset)
        self.paddle_fill_add()

        # Center a filled ball in the graphical window.
        self.ball = GOval(width=BALL_RADIUS * 2, height=BALL_RADIUS * 2, x=self.window.width / 2 - BALL_RADIUS,
                          y=self.window.height / 2 - BALL_RADIUS)
        self.ball_fill_add()

        # Default initial velocity for the ball.
        self.vx = 0
        self.vy = 0

        # Initialize our mouse listeners.
        onmouseclicked(self.click_handler)
        onmousemoved(self.move_paddle_handler)

        # Draw bricks.
        self.draw_bricks()

        # Default number of bricks
        self.brick_nums = BRICK_COLS * BRICK_ROWS

    def draw_bricks(self):
        count = 0
        color = COLORS[count]
        for i in range(BRICK_ROWS):
            for j in range(BRICK_COLS):
                if count == 2:
                    color = COLORS[i // 2]
                    count = 0
                brick = GRect(width=BRICK_WIDTH, height=BRICK_HEIGHT, x=j * (BRICK_WIDTH + BRICK_SPACING),
                              y=BRICK_OFFSET + i * (BRICK_HEIGHT + BRICK_SPACING))
                brick.filled = True
                brick.fill_color = color
                self.window.add(brick)
                count += 1

    def paddle_fill_add(self):
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle)

    def ball_fill_add(self):
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.window.add(self.ball)

    def move_paddle_handler(self, event):
        x = event.x
        if self.paddle is not None:
            self.window.remove(self.paddle)

        if x + PADDLE_WIDTH / 2 <= self.window.width and x - PADDLE_WIDTH / 2 >= 0:
            self.paddle = GRect(width=PADDLE_WIDTH, height=PADDLE_HEIGHT, x=x - PADDLE_WIDTH / 2,
                                y=self.window.height - PADDLE_OFFSET)
            self.paddle_fill_add()
        elif x - PADDLE_WIDTH / 2 < 0:
            self.paddle = GRect(width=PADDLE_WIDTH, height=PADDLE_HEIGHT, x=0,
                                y=self.window.height - PADDLE_OFFSET)
            self.paddle_fill_add()
        elif x + PADDLE_WIDTH / 2 > self.window.width:
            self.paddle = GRect(width=PADDLE_WIDTH, height=PADDLE_HEIGHT, x=self.window.width - PADDLE_WIDTH,
                                y=self.window.height - PADDLE_OFFSET)
            self.paddle_fill_add()

    def move_ball(self):
        self.ball.move(self.vx, self.vy)

    def handle_wall_collisions(self):
        if self.ball.x <= 0 or self.ball.x >= self.window.width - self.ball.width:
            self.vx = -self.vx
        if self.ball.y <= 0:
            self.vy = -self.vy

    def click_handler(self, event):
        if self.vy == 0:
            self.vx = random.uniform(-MAX_X_SPEED, MAX_X_SPEED)
            self.vy = INITIAL_Y_SPEED

    def check_obj_collision(self):
        obj_one = self.window.get_object_at(self.ball.x, self.ball.y)
        obj_two = self.window.get_object_at(self.ball.x + 2 * BALL_RADIUS, self.ball.y)
        obj_three = self.window.get_object_at(self.ball.x, self.ball.y + 2 * BALL_RADIUS)
        obj_four = self.window.get_object_at(self.ball.x + 2 * BALL_RADIUS, self.ball.y + 2 * BALL_RADIUS)

        if obj_one is not None:
            return obj_one
        elif obj_two is not None:
            return obj_two
        elif obj_three is not None:
            return obj_three
        elif obj_four is not None:
            return obj_four
        else:
            return None

    def handle_obj_collisions(self):
        obj = self.check_obj_collision()
        if obj is not None:
            if obj != self.paddle:
                self.window.remove(obj)
                self.brick_nums -= 1
                self.vy = -self.vy
            else:
                self.vy = -abs(self.vy)

    def out_of_zone(self):
        if self.window.height <= self.ball.y:
            return True
        else:
            return False

    def remove_ball(self):
        self.window.remove(self.ball)

    def reset_ball_position(self):
        self.ball.x = (self.window.width - self.ball.width) / 2
        self.ball.y = (self.window.height - self.ball.height) / 2

    def reset_ball_velocity(self):
        self.vx = 0
        self.vy = 0

    def reset_ball(self):
        self.remove_ball()
        self.reset_ball_position()
        while self.out_of_zone():
            self.reset_ball_position()
        self.reset_ball_velocity()
        self.ball_fill_add()

    def win_or_lose(self, won):
        if won:
            label = GLabel('You beat the game!')
        else:
            label = GLabel('You lost the game!')
        label_x = self.window.width/ 2 - label.width / 2
        label_y = self.window.height / 2 - label.height / 2
        self.window.remove(self.ball)
        self.window.add(label, label_x, label_y)

