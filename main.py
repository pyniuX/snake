# Copyright (c) 2024 pyniu entertainment - No Rights Reserved. 
from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

app = Ursina(borderless=False, forced_aspect_ratio=16/9, fullscreen=True)
window.color=color.gray
camera.orthographic=True
camera.fov=10

floor = Entity(model='quad', y=-5/window.aspect_ratio, scale=(10*window.aspect_ratio,0.1), collider='box', visible=True)
ceiling = duplicate(floor, y=5/window.aspect_ratio)
left_wall = Entity(model='quad', x=-5*window.aspect_ratio, y=0, scale=(0.1,10/window.aspect_ratio), collider='box', visible=True)
right_wall = duplicate(left_wall, x=5*window.aspect_ratio)



col_cooldown = .15
rot_cooldown = .25
snake = Entity(model='cube', scale=0.5, collider='box', color=color.red, collision_cooldown=col_cooldown, rotation_cooldown=rot_cooldown)


# point = Entity(model='sphere', color=color.red, scale=0.3)


def update():
    snake.position += snake.up * time.dt * 2
    snake.rotation_cooldown -= time.dt
    snake.collision_cooldown -= time.dt

    if snake.collision_cooldown<=0:
        #TODO: position change not working, vec2 or without?
        hit_info = snake.intersects()
        if hit_info.hit:
            snake.collision_cooldown = col_cooldown
            if hit_info.entity == ceiling or floor:
                print(snake.position)
                snake.position = (snake.x, -snake.y)    
                # floor.collision = False        
                print(snake.position)
            if hit_info.entity == left_wall or right_wall:
                print(snake.position)
                snake.position = Vec2(-snake.x, snake.y)    
                print(snake.position)

    if snake.rotation_cooldown<=0:
        if held_keys['a']:
            snake.rotation_z=-90
            snake.rotation_cooldown = rot_cooldown 
        elif held_keys['d']:
            snake.rotation_z=90
            snake.rotation_cooldown = rot_cooldown
        elif held_keys['w']:
            snake.rotation_z=0
            snake.rotation_cooldown = rot_cooldown
        elif held_keys['s']:
            snake.rotation_z=180
            snake.rotation_cooldown = rot_cooldown

    

app.run()