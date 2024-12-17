# Copyright (c) 2024 Krzysztof Puk
# All rights reserved
# https://github.com/pyniuX

from ursina import (Entity, color, time, window)
from random import randint
import logging

# point_cd = 2

class Point(Entity):
    cooldown = 2

    def __init__(self, **kwargs):
        super().__init__(
            model = 'sphere',
            color = color.red,
            scale = 0.5,
            collider = None,
            visible = False,
            **kwargs,)


    def update(self,):
        self.cooldown -= time.dt

        if self.cooldown <= 0:
            if not self.visible:
                self.x = randint(-810, 810)/100
                self.y = randint(-260, 260)/100
                logging.debug(f"Point appeared at ({self.x}, {self.y}).")
                self.visible = True
                self.collider = 'box'

            hit_info = self.intersects()
            if hit_info:
                logging.debug(f"Point collided at ({self.x}, {self.y}).")
                self.collider = None
                self.cooldown = Point.cooldown
                self.visible = False
