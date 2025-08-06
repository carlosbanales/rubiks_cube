#To-do

# - fix bugs on the first layer so i can rotate the cube and still be able to 
#   rotate the individual sections

# - add a key press binding that rotates the cube continuosly as if im pressing
#   and holding the up and right arrow key

# - add the rest of the cube rotations after the bugs on the first layer are worked out 


from ursina import *

app = Ursina()

DirectionalLight(shadows=False)
AmbientLight(color=color.rgba(255, 255, 255, 150))

OFFSET = 1.01
CUBIE_SIZE = 0.95
STICKER_OFFSET = 0.51
STICKER_THICKNESS = 0.02
STICKER_SCALE = 0.9

face_colors = {
    'U': color.white,
    'D': color.yellow,
    'F': color.green,
    'B': color.blue,
    'L': color.orange,
    'R': color.red
}

cube_parent = Entity()

cubies = []

# cubies (3x3x3)
for x in range(3):
    for y in range(3):
        for z in range(3):
            pos = Vec3(x - 1, y - 1, z - 1) * OFFSET
            cube = Entity(
                parent=cube_parent,
                model='cube',
                color=color.black,
                position=pos,
                scale=CUBIE_SIZE,
                unlit=True
            )
            cubies.append(cube)

            # Stickers as thin colored cubes
            if y == 2:
                Entity(parent=cube,
                       model='cube',
                       color=face_colors['U'],
                       position=(0, STICKER_OFFSET, 0),
                       rotation_x=-90,
                       scale=(STICKER_SCALE, STICKER_SCALE, STICKER_THICKNESS),
                       unlit=True)
            if y == 0:
                Entity(parent=cube,
                       model='cube',
                       color=face_colors['D'],
                       position=(0, -STICKER_OFFSET, 0),
                       rotation_x=90,
                       scale=(STICKER_SCALE, STICKER_SCALE, STICKER_THICKNESS),
                       unlit=True)
            if z == 2:
                Entity(parent=cube,
                       model='cube',
                       color=face_colors['F'],
                       position=(0, 0, STICKER_OFFSET),
                       scale=(STICKER_SCALE, STICKER_SCALE, STICKER_THICKNESS),
                       unlit=True)
            if z == 0:
                Entity(parent=cube,
                       model='cube',
                       color=face_colors['B'],
                       position=(0, 0, -STICKER_OFFSET),
                       scale=(STICKER_SCALE, STICKER_SCALE, STICKER_THICKNESS),
                       unlit=True)
            if x == 0:
                Entity(parent=cube,
                       model='cube',
                       color=face_colors['L'],
                       position=(-STICKER_OFFSET, 0, 0),
                       scale=(STICKER_THICKNESS, STICKER_SCALE, STICKER_SCALE),
                       unlit=True)
            if x == 2:
                Entity(parent=cube,
                       model='cube',
                       color=face_colors['R'],
                       position=(STICKER_OFFSET, 0, 0),
                       scale=(STICKER_THICKNESS, STICKER_SCALE, STICKER_SCALE),
                       unlit=True)

def rotate_face_y(y_level=1, direction=1):
    pivot = Entity()
    pivot.parent = cube_parent  # <-- crucial!
    pivot.position = Vec3(0, (y_level - 1) * OFFSET, 0)  # Pivot is now in local cube space

    for cubie in cubies:
        if abs(cubie.world_position.y - ((y_level - 1) * OFFSET)) < 0.1:
            cubie.world_parent = pivot

    pivot.animate('rotation_y', 90 * direction, duration=0.25)

    def cleanup():
        for child in pivot.children:
            child.world_parent = cube_parent
        destroy(pivot)

    invoke(cleanup, delay=0.3)


def input(key):
    if key == 't':
        rotate_face_y(y_level=2, direction=1)
    elif key == 'g':
        rotate_face_y(y_level=2, direction=-1)

# Add camera
EditorCamera()

# Optional: Rotate with arrow keys
def update():
    if held_keys['left arrow']:
        cube_parent.rotation_y += 100 * time.dt
    if held_keys['right arrow']:
        cube_parent.rotation_y -= 100 * time.dt
    if held_keys['up arrow']:
        cube_parent.rotation_x += 100 * time.dt
    if held_keys['down arrow']:
        cube_parent.rotation_x -= 100 * time.dt

app.run()

