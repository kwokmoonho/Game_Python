"""
File: skeet.py
Original Author: Br. Burton
Designed to be completed by others
This program implements an awesome version of skeet.
"""
from global_constants import *
from flyingObject import *
from rifle import Rifle
from target import *
from bullet import Bullet
from movingBird import MovingBird
import arcade
import math
import random

class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    It assumes the following classes exist:
        Rifle
        Target (and it's sub-classes)
        Point
        Velocity
        Bullet
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class, but mostly
    you shouldn't have to. There are a few sections that you
    must add code to.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)

        self.rifle = Rifle()
        self.score1 = 0
        self.score2 = 0
        self.mb = MovingBird()
        self.holding_down = False
        self.holding_left = False
        self.holding_right = False
        self.holding_up = False
        self.bullets = []
        self.targets = []


        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # draw each object
        self.rifle.draw()

        for bullet in self.bullets:
            bullet.draw()

        for target in self.targets:
            target.draw()

        self.draw_score()

        self.mb.draw_moving_bird()

    def draw_score(self):
        """
        Puts the current score on the screen
        """
        score1_text = "Score: {}".format(self.score1)
        start1_x = 10
        start1_y = SCREEN_HEIGHT - 20
        arcade.draw_text(score1_text, start_x=start1_x, start_y=start1_y, font_size=12, color=arcade.color.NAVY_BLUE)

        score2_text = "Score: {}".format(self.score2)
        start2_x = SCREEN_WIDTH - 80
        start2_y = SCREEN_HEIGHT - 20
        arcade.draw_text(score2_text, start_x=start2_x, start_y=start2_y, font_size=12, color=arcade.color.NAVY_BLUE)

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_collisions()
        self.check_off_screen()

        # decide if we should start a target
        if random.randint(1, 50) == 1:
            self.create_target()

        for bullet in self.bullets:
            bullet.advance()

        # TODO: Iterate through your targets and tell them to advance
        for target in self.targets:
            target.advance()

        self.check_keys()

    def create_target(self):
        """
        Creates a new target of a random type and adds it to the list.
        :return:
        """

        # TODO: Decide what type of target to create and append it to the list
        number = random.randint(1,3)
        if number == 1:
            target = StandardTarget()
            self.targets.append(target)
        if number == 2:
            target = StrongTarget()
            self.targets.append(target)
        if number == 3:
            target = SafeTarget()
            self.targets.append(target)

    def check_collisions(self):
        """
        Checks to see if bullets have hit targets.
        Updates scores and removes dead items.
        :return:
        """

        # NOTE: This assumes you named your targets list "targets"

        for bullet in self.bullets:
            for target in self.targets:

                # Make sure they are both alive before checking for a collision
                if bullet.alive and target.alive:
                    too_close = bullet.radius + target.radius

                    if (abs(bullet.center.x - target.center.x) < too_close and
                                abs(bullet.center.y - target.center.y) < too_close):
                        # its a hit!
                        bullet.alive = False
                        self.score1 += target.hit()

        for bullet in self.bullets:
            if bullet.alive:
                too_close = bullet.radius + TARGET_RADIUS
                if (abs(bullet.center.x - self.mb.center.x)) < too_close and \
                        abs(bullet.center.y - self.mb.center.y) < too_close:
                    bullet.alive = False
                    self.score1 += 10

                        # We will wait to remove the dead objects until after we
                        # finish going through the list

        # Now, check for anything that is dead, and remove it
        self.cleanup_zombies()

    def cleanup_zombies(self):
        """
        Removes any dead bullets or targets from the list.
        :return:
        """
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)

        for target in self.targets:
            if not target.alive:
                self.targets.remove(target)

    def check_off_screen(self):
        """
        Checks to see if bullets or targets have left the screen
        and if so, removes them from their lists.
        :return:
        """
        for bullet in self.bullets:
            if bullet.is_off_screen():
                self.bullets.remove(bullet)
                self.score2 += 1

        for target in self.targets:
            if target.is_off_screen():
                self.targets.remove(target)

    def check_keys(self):
        """
        Checks to see if the user is holding down an
        arrow key, and if so, takes appropriate action.
        """
        if self.holding_up:
            self.mb.move_up()

        if self.holding_right:
            self.mb.move_right()

        if self.holding_left:
            self.mb.move_left()

        if self.holding_down:
            self.mb.move_down()


    def on_key_press(self, key, key_modifiers):
        """
        Called when a key is pressed. Sets the state of
        holding an arrow key.
        :param key: The key that was pressed
        :param key_modifiers: Things like shift, ctrl, etc
        """
        if key == arcade.key.LEFT:
            self.holding_left = True

        if key == arcade.key.RIGHT:
            self.holding_right = True

        if key == arcade.key.UP:
            self.holding_up = True

        if key == arcade.key.DOWN:
            self.holding_down = True

    def on_key_release(self, key, key_modifiers):
        """
        Called when a key is released. Sets the state of
        the arrow key as being not held anymore.
        :param key: The key that was pressed
        :param key_modifiers: Things like shift, ctrl, etc
        """
        if key == arcade.key.LEFT:
            self.holding_left = False

        if key == arcade.key.RIGHT:
            self.holding_right = False

        if key == arcade.key.UP:
            self.holding_up = False

        if key == arcade.key.DOWN:
            self.holding_down = False


    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        # set the rifle angle in degrees
        self.rifle.angle = self._get_angle_degrees(x, y)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        # Fire!
        angle = self._get_angle_degrees(x, y)

        bullet = Bullet()
        bullet.fire(angle)

        self.bullets.append(bullet)

    def _get_angle_degrees(self, x, y):
        """
        Gets the value of an angle (in degrees) defined
        by the provided x and y.
        Note: This could be a static method, but we haven't
        discussed them yet...
        """
        # get the angle in radians
        angle_radians = math.atan2(y, x)

        # convert to degrees
        angle_degrees = math.degrees(angle_radians)

        return angle_degrees

# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()