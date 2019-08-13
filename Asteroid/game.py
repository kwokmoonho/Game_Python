"""
File: asteroids.py
Original Author: Br. Burton
Designed to be completed by others
This program implements the asteroids game.

Modified by: Kwok Moon Ho
Class: CS241

Added features:
1. background
2. machine gun
3. game over (after ship killed)
4. you win (after you kill all the asteriods)
5. draw score
"""
from global_constants import *
from bullet import Bullet
from asteriods import BigAsteriods
from ship import Ship
import random
import arcade
import math

class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)
        self.held_keys = set()
        self.score = 0
        # TODO: declare anything here you need the game class to track
        self.ship = Ship()
        self.bullets = []
        self.asteroids = []
        self.create_asteriods()

    def draw_background(self):      ##draw the background
        img = "images/background.png"
        texture = arcade.load_texture(img)
        width = texture.width
        height = texture.height
        alpha = 1
        angle = 0
        arcade.draw_texture_rectangle(width / 2, height / 2, width, height, texture, angle, alpha)

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """
        arcade.start_render()
        # clear the screen to begin drawing
        # TODO: draw each object
        self.draw_background()

        if self.ship.alive == True:         ##only draw if the ship is still alive
            self.ship.draw()
        elif self.ship.alive == False:      ##else, draw game over
            self.draw_text()

        for bullet in self.bullets:
            bullet.draw()

        if len(self.asteroids) > 0:             ##if the list of the asteriods is 0, you win!
            for asteriods in self.asteroids:
                asteriods.draw()
        else:
            self.draw_win()

        self.draw_score()

    def draw_win(self):
        text = "YOU WIN!!!"
        start_x = 150
        start_y = SCREEN_HEIGHT / 2
        arcade.draw_text(text, start_x=start_x, start_y=start_y, font_size=100, color=arcade.color.WHITE)

    def draw_score(self):
        """
        Puts the current score on the screen
        """
        score_text = "Score: {}".format(self.score)
        start_x = 10
        start_y = SCREEN_HEIGHT - 20
        arcade.draw_text(score_text, start_x=start_x, start_y=start_y, font_size=18, color=arcade.color.WHITE)


    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_keys()

        # TODO: Tell everything to advance or move forward one step in time
        self.ship.advance()

        for bullet in self.bullets:
            bullet.advance()

        for asteriod in self.asteroids:
            asteriod.advance()

        # TODO: Check for collisions
        self.check_collisions()
        self.cleanup_zombies()

    def create_asteriods(self):         ##create 5 big rock at the beginning of the game and called by the init
        for i in range(INITIAL_ROCK_COUNT):
            x = random.randint(0, SCREEN_WIDTH)
            y = random.randint(0, SCREEN_HEIGHT)
            angle = random.randint(0, 360)
            dy = BIG_ROCK_SPEED * math.cos(math.radians(angle))
            dx = BIG_ROCK_SPEED * math.sin(math.radians(angle))
            rock = BigAsteriods(x, y, dx, dy)
            self.asteroids.append(rock)

    def draw_text(self):
        score_text = "GAME OVER"
        gun_text = "Try to hold W for machine gun on next game"
        start_x = 100
        start_y = SCREEN_HEIGHT / 2
        arcade.draw_text(score_text, start_x=start_x, start_y=start_y, font_size=100, color=arcade.color.WHITE)
        arcade.draw_text(gun_text, 50, SCREEN_HEIGHT / 2 - 50, font_size = 35, color=arcade.color.WHITE)

    def check_collisions(self):
        """
        Checks to see if bullets have hit targets.
        Updates scores and removes dead items.
        :return:
        """
        for bullet in self.bullets:         ##check the bullet and the asteriods
            for asteriod in self.asteroids:
                if bullet.alive and asteriod.alive:
                    too_close = bullet.radius + asteriod.radius

                    if (abs(bullet.center.x - asteriod.center.x) < too_close and
                            abs(bullet.center.y - asteriod.center.y) < too_close):
                        bullet.alive = False
                        self.score += 1
                        asteriod.hit(self.asteroids)


        if self.ship.alive:         ##check the asteriods and the ship
            for asteriod in self.asteroids:
                close = asteriod.radius + self.ship.radius
                if(abs(asteriod.center.x - self.ship.center.x) < close and
                        abs(asteriod.center.y - self.ship.center.y) < close):
                            self.ship.alive = False

        self.cleanup_zombies()

    def cleanup_zombies(self):      ##claen the memory of the list in bullet and the asteriod
        """
        Removes any dead bullets or targets from the list.
        :return:
        """
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)

        for asteriod in self.asteroids:
            if not asteriod.alive:
                self.asteroids.remove(asteriod)

    def check_keys(self):
        """
        This function checks for keys that are being held down.
        You will need to put your own method calls in here.
        """
        if arcade.key.LEFT in self.held_keys:
            self.ship.turn_left()

        if arcade.key.RIGHT in self.held_keys:
            self.ship.turn_right()

        if arcade.key.UP in self.held_keys:
            self.ship.move()

        if arcade.key.DOWN in self.held_keys:
            self.ship.stop()

        ##Machine gun mode...
        if arcade.key.W in self.held_keys:
            bullet = Bullet(self.ship.center.x, self.ship.center.y, self.ship.direction.angle)
            bullet.fire(self.ship.direction.angle)
            self.bullets.append(bullet)


    def on_key_press(self, key: int, modifiers: int):
        """
        Puts the current key in the set of keys that are being held.
        You will need to add things here to handle firing the bullet.
        """
        if self.ship.alive:
            self.held_keys.add(key)

            if key == arcade.key.SPACE:
                bulet = Bullet(self.ship.center.x, self.ship.center.y, self.ship.direction.angle)
                bullet.fire(self.ship.direction.angle)
                self.bullets.append(bullet)

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)


# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()