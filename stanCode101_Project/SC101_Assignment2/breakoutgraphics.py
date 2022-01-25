"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

The class builds the scene of the game, and it detects the mouse-click.
Once the mouse is clicked, the program generates a random number for horizontal speed
and gives a initial speed for vertical speed.
Also, once the mouse is clicked, the user can control the paddle with their mouse.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

# CONSTANTS
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

INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.w_width = window_width
        self.w_height = window_height
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, y=window_height-paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(2*ball_radius, 2*ball_radius)
        self.ball.filled = True
        self.window.add(self.ball, x=window_width/2-ball_radius, y=window_height/2-ball_radius)

        # Create a scoreboard
        self.score = 0
        self.scoreboard = GLabel('Score: '+str(self.score))
        self.window.add(self.scoreboard, x=10, y=30)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        self.click = False
        onmouseclicked(self.drop)
        onmousemoved(self.move)

        # Draw bricks
        for i in range(BRICK_COLS):
            for j in range(BRICK_ROWS):
                brick_x = (BRICK_SPACING+BRICK_WIDTH)*i
                brick_y = BRICK_OFFSET+j*(BRICK_SPACING+BRICK_HEIGHT)
                brick = GRect(BRICK_WIDTH, BRICK_HEIGHT, x=brick_x, y=brick_y)
                brick.filled = True
                if j == 0 or j == 1:
                    brick.fill_color = 'red'
                elif j == 2 or j == 3:
                    brick.fill_color = 'coral'
                elif j == 4 or j == 5:
                    brick.fill_color = 'yellow'
                elif j == 6 or j == 7:
                    brick.fill_color = 'green'
                else:
                    brick.fill_color = 'darkblue'
                self.window.add(brick)

    def drop(self, mouse):
        if not self.click:
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            if random.random() > 0.5:
                self.__dx = - self.__dx
            self.click = True

    def move(self, mouse):
        if self.click:
            if mouse.x >= self.w_width-(PADDLE_WIDTH//2):
                mouse_x = self.w_width-(PADDLE_WIDTH//2)
            elif mouse.x <= PADDLE_WIDTH//2:
                mouse_x = PADDLE_WIDTH//2
            else:
                mouse_x = mouse.x
            self.window.add(self.paddle, x=mouse_x-(PADDLE_WIDTH//2), y=self.w_height-PADDLE_OFFSET)

    @property
    def horizontal_speed(self):
        return self.__dx

    @property
    def vertical_speed(self):
        return self.__dy
