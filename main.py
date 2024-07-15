# Copyright (c) 2024 pyniu entertainment - No Rights Reserved. 
from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

app = Ursina()
# TODO: independent window size
window.borderless=False
window.color=color.gray
# window.fullscreen=True
camera.orthographic=True
camera.fov=10

floor = Entity(model='quad', y=-5.5, collider='box', scale=(20,1), visible=True)
ceiling = duplicate(floor, y=5.5, rotation_z=180, visible=True,)
left_wall = duplicate(floor, x=-8.5, rotation_z=90, visible=True)
right_wall = duplicate(floor, x=8.5,  rotation_z=-90, visible=True)
left_wall.y +=1
right_wall.y +=1

collison_cooldown = .15
rotation_cooldown = .25
snake = Entity(model='cube', scale=0.5, collider='box', color=color.red, collison_cooldown=collison_cooldown, rotation_cooldown=rotation_cooldown)


# point = Entity(model='sphere', color=color.red, scale=0.3)


def update():
    snake.position += snake.up * time.dt * 2
    snake.rotation_cooldown -= time.dt

    if held_keys['a'] and snake.rotation_cooldown <= 0:
        snake.rotation_z=-90
        snake.rotation_cooldown = .25 

    elif held_keys['d'] and snake.rotation_cooldown <= 0:
        snake.rotation_z=90
        snake.rotation_cooldown = .25 

    elif held_keys['w'] and snake.rotation_cooldown <= 0:
        snake.rotation_z=0
        snake.rotation_cooldown = .25 

    elif held_keys['s'] and snake.rotation_cooldown <= 0:
        snake.rotation_z=180
        snake.rotation_cooldown = .25 

    

app.run()