"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

The user will have 3 chances to play the game.
Once you click the mouse, the game starts, and the score starts with 0.
If the ball hits the brick, the brick will disappear, and the score will be added;
If the ball hits the paddle,the ball will bounce back.
However, if the ball falls and the user doesn't catch it, the user will lose one chance.
If the chances are used up, the user can no longer play the game.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120 # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()

    # chances
    chance = NUM_LIVES
    # starter
    starter = 0
    vx = 0
    vy = 0

    # Add animation loop here!
    while True:
        # update
        if not graphics.click:
            vx = 0
            vy = 0
        else:
            if starter == 0:
                vx = graphics.horizontal_speed
                vy = graphics.vertical_speed
                starter = 1
        graphics.ball.move(vx, vy)
        # check
        if graphics.ball.x <= 0 or graphics.ball.x+graphics.ball.width >= graphics.window.width:
            vx = -vx
        if graphics.ball.y <= 0 or graphics.ball.y+graphics.ball.height >= graphics.window.height:
            vy = -vy
        if graphics.ball.y+graphics.ball.height >= graphics.window.height:
            chance = chance - 1
            graphics.window.remove(graphics.ball)
            graphics.window.add(graphics.ball,
                                x=(graphics.window.width-graphics.ball.width)//2, y=(graphics.window.height-graphics.ball.height)//2)
            graphics.click = False
            starter = 0
            if chance == 0:
                graphics.click = True
                break

        while True:
            ball_x1 = graphics.ball.x
            ball_y1 = graphics.ball.y
            object_1 = graphics.window.get_object_at(ball_x1, ball_y1)
            if object_1 is not None:
                if object_1 is graphics.paddle:
                    vy = -vy
                    break
                elif object_1 is graphics.scoreboard:
                    break
                else:
                    vy = -vy
                    graphics.window.remove(object_1)
                    graphics.score += 1
                    graphics.scoreboard.text = 'Score: '+str(graphics.score)
                    break
            else:
                ball_x2 = graphics.ball.x + graphics.ball.width
                ball_y2 = graphics.ball.y
                object_2 = graphics.window.get_object_at(ball_x2, ball_y2)
                if object_2 is not None:
                    if object_2 is graphics.paddle:
                        vy = -vy
                        break
                    elif object_2 is graphics.scoreboard:
                        break
                    else:
                        vy = -vy
                        graphics.window.remove(object_2)
                        graphics.score += 1
                        graphics.scoreboard.text = 'Score: ' + str(graphics.score)
                        break
                else:
                    ball_x3 = graphics.ball.x
                    ball_y3 = graphics.ball.y + graphics.ball.height
                    object_3 = graphics.window.get_object_at(ball_x3, ball_y3)
                    if object_3 is not None:
                        if object_3 is graphics.paddle:
                            vy = -vy
                            break
                        elif object_3 is graphics.scoreboard:
                            break
                        else:
                            vy = -vy
                            graphics.window.remove(object_3)
                            graphics.score += 1
                            graphics.scoreboard.text = 'Score: ' + str(graphics.score)
                            break
                    else:
                        ball_x4 = graphics.ball.x
                        ball_y4 = graphics.ball.y + graphics.ball.height
                        object_4 = graphics.window.get_object_at(ball_x4, ball_y4)
                        if object_4 is not None:
                            if object_4 is graphics.paddle:
                                vy = -vy
                                break
                            elif object_4 is graphics.scoreboard:
                                break
                            else:
                                vy = -vy
                                graphics.window.remove(object_4)
                                graphics.score += 1
                                graphics.scoreboard.text = 'Score: ' + str(graphics.score)
                                break
                        else:
                            break

        # pause
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
