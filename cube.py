# python facelet representation
#cube = {
#    "U": ["W"] * 9,  # Up face
#   "D": ["Y"] * 9,  # Down face
#    "F": ["G"] * 9,  # Front face
#    "B": ["B"] * 9,  # Back face
#    "L": ["O"] * 9,  # Left face
#    "R": ["R"] * 9,  # Right face
#}

from ursina import *

app = Ursina()

DirectionalLight(shadows=False)
AmbientLight(color=color.rgba(255, 255, 255, 100))


OFFSET = 1.01
CUBIE_SIZE = 0.95
sticker_offset = 0.51 # to avoid z fighting
sticker_scale = (0.9, 0.9)

face_colors = {
    'U': color.white,
    'D': color.yellow,
    'F': color.green,
    'B': color.blue,
    'L': color.orange,
    'R': color.red
}

cube_parent = Entity()

# cubies (27)
for x in range(3):
    for y in range(3):
        for z in range(3):
            pos = Vec3(x - 1, y - 1, z - 1) * OFFSET
            cube = Entity(
                parent=cube_parent,
                model='cube',
                color=color.rgb(30, 30, 30),
                position=pos,
                scale=CUBIE_SIZE,
                unlit=True,
                #alpha=0.5,
                
            )

            # stickers

            if y == 2:
                Entity(parent=cube,
                       model='plane',
                       color=face_colors['U'],
                       position=(0, sticker_offset, 0),
                       rotation_x=-90,
                       scale=sticker_scale,
                       unlit=True
                )
            if y == 0:
                Entity(parent=cube,
                       model='quad',
                       color=face_colors['D'],
                       position=(0, -sticker_offset, 0),
                       rotation_x=90,
                       scale=sticker_scale,
                       unlit=True
                )
            if z == 2:
                Entity(parent=cube,
                       model='quad',
                       color=face_colors['F'],
                       position=(0, 0, sticker_offset),
                       scale=sticker_scale,
                       unlit=True
                )
            if z == 0:
                Entity(parent=cube,
                       model='quad', color=face_colors['B'],
                       position=(0, 0, -sticker_offset),
                       rotation_y=180,
                       scale=sticker_scale,
                       unlit=True
                )
            if x == 0:
                Entity(parent=cube,
                       model='quad',
                       color=face_colors['L'],
                       position=(-sticker_offset, 0, 0),
                       rotation_y=-90,
                       scale=sticker_scale,
                       unlit=True
                )
            if x == 2:
                Entity(parent=cube,
                       model='quad',
                       color=face_colors['R'],
                       position=(sticker_offset, 0, 0),
                       rotation_y=90,
                       scale=sticker_scale,
                       unlit=True
                )

# Add EditorCamera for mouse control
EditorCamera()

# Optional: Manual rotation with keys
def update():
    if held_keys['left arrow']:
        cube_parent.rotation_y += 100 * time.dt
    if held_keys['right arrow']:
        cube_parent.rotation_y -= 100 * time.dt
    if held_keys['up arrow']:
        cube_parent.rotation_x += 100 * time.dt
    if held_keys['down arrow']:
        cube_parent.rotation_x -= 100 * time.dt

cube_parent.rotation_y = 30
cube_parent.rotation_x = -20


app.run()
