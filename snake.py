# Copyright (c) 2024 Krzysztof Puk
# All rights reserved
# https://github.com/pyniuX

from ursina import (Entity, color)

class Snake(Entity):
    rotation_cooldown = .15
    collision_cooldown = .25

    def __init__(self, **kwargs):
        super().__init__(
            model = 'cube',
            scale = 0.5,
            collider = 'box',
            color = color.red,
            **kwargs,)

    def rotate_z(self, degrees: int):
        self.rotation_z = degrees
        self.rotation_cooldown = Snake.rotation_cooldown


    def move(self, x: int, y: int):
        self.position = (x, y)
        self.collision_cooldown = Snake.collision_cooldown