# Copyright (c) 2024 Krzysztof Puk
# All rights reserved
# https://github.com/pyniuX

import logging

logging.basicConfig(
    filename="logs.txt",
    encoding="utf-8",
    filemode="w",
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
    level=logging.DEBUG,
)

from ursina import *
from point import *
from snake import *

app = Ursina(borderless=False, forced_aspect_ratio=16/9, fullscreen=True)
window.color = color.gray
camera.orthographic = True
camera.fov = 10

floor = Entity(model='quad', y=-5/window.aspect_ratio, scale=(10*window.aspect_ratio,0.1), collider='box', visible=True)
ceiling = duplicate(floor, y=-floor.y)
left_wall = Entity(model='quad', x=-5*window.aspect_ratio, y=0, scale=(0.1,10/window.aspect_ratio), collider='box', visible=True)
right_wall = duplicate(left_wall, x=-left_wall.x)

logging.debug(f"ARENA DIMENSIONS: ({right_wall.x *2}, {ceiling.y * 2}). ")

snake = Snake()
point = Point()

def update():
    snake.position += snake.up * time.dt * 2
    snake.rotation_cooldown -= time.dt
    snake.collision_cooldown -= time.dt

    if snake.collision_cooldown <= 0:
        hit_info = snake.intersects()
        if hit_info.hit:
            logging.debug(f"Snake collided at: ({snake.x}, {snake.y}).")
            if hit_info.entity in [ceiling, floor]:
                snake.move(snake.x, -snake.y)
            elif hit_info.entity in [left_wall, right_wall]:
                snake.move(-snake.x, snake.y)

    if snake.rotation_cooldown <= 0:
        if held_keys['a']:
            snake.rotate_z(-90)
        elif held_keys['d']:
            snake.rotate_z(90)
        elif held_keys['w']:
            snake.rotate_z(0)
        elif held_keys['s']:
            snake.rotate_z(180)


logging.info("App started.")
app.run()