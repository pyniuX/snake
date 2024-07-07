# Copyright (c) 2024 pyniu entertainment - No Rights Reserved. 
from ursina import *

app = Ursina()

arena = Entity(model="cube", color=color.green, scale=(2,1,3))
snake = Entity(model='cube', color=color.red, scale_y=1, collider='box')
# point = Entity(model='sphere', color=color.red, scale=0.3)

speed_x=speed_y=0.1

def update():
    snake.x += held_keys['d'] * time.dt
    snake.x -= held_keys['a'] * time.dt
    snake.y += held_keys['w'] * time.dt
    snake.y -= held_keys['s'] * time.dt


# def input(key):
    # if key == "space":
        # player.y += 1
        # invoke(setattr, player, 'y', player.y-1, delay=.25)

app.run()