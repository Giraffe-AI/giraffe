import pygame
import pymunk
import pymunk.pygame_util

# Initialize Pygame and Pymunk
pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

space = pymunk.Space()


# Initialize a space for the physics simulation
space = pymunk.Space()
space.gravity = (0, 0)  # No gravity

draw_options = pymunk.pygame_util.DrawOptions(screen)

# Create the cue ball
cue_mass = 1
cue_radius = 10
moment = pymunk.moment_for_circle(cue_mass, 0, cue_radius)
cue_body = pymunk.Body(cue_mass, moment)
cue_body.position = 50, 50
cue_shape = pymunk.Circle(cue_body, cue_radius)
cue_shape.elasticity = 1.0  # Perfectly elastic collisions
cue_shape.collision_type = 1
space.add(cue_body, cue_shape)

# Create a planet
planet_mass = 1
planet_radius = 15
moment = pymunk.moment_for_circle(planet_mass, 0, planet_radius)
planet_body = pymunk.Body(planet_mass, moment)
planet_body.position = 300, 200
planet_shape = pymunk.Circle(planet_body, planet_radius)
planet_shape.elasticity = 1.0  # Perfectly elastic collisions
planet_shape.collision_type = 2
space.add(planet_body, planet_shape)

# Existing cue ball and first planet code goes here...

# Additional planets
planet_positions = [(400, 200), (500, 300), (600, 400)]  # Specify desired positions for new planets
planet_radii = [20, 25, 30]  # Specify desired sizes for new planets
for position, radius in zip(planet_positions, planet_radii):
    planet_mass = 1
    moment = pymunk.moment_for_circle(planet_mass, 0, radius)  # Use radius from the list
    planet_body = pymunk.Body(planet_mass, moment)
    planet_body.position = position  # Use position from the list
    planet_shape = pymunk.Circle(planet_body, radius)  # Use radius from the list
    planet_shape.elasticity = 1.0  # Perfectly elastic collisions
    planet_shape.collision_type = 2
    space.add(planet_body, planet_shape)


# Create a black hole
black_hole_mass = 1
black_hole_radius = 20
moment = pymunk.moment_for_circle(black_hole_mass, 0, black_hole_radius)
black_hole_body = pymunk.Body(black_hole_mass, moment, body_type=pymunk.Body.STATIC)
black_hole_body.position = 500, 200
black_hole_shape = pymunk.Circle(black_hole_body, black_hole_radius)
black_hole_shape.collision_type = 3
space.add(black_hole_body, black_hole_shape)

# Create walls
wall_thickness = 10
walls = [
    pymunk.Segment(space.static_body, (0, 0), (0, 400), wall_thickness),  # Left
    pymunk.Segment(space.static_body, (0, 0), (600, 0), wall_thickness),  # Top
    pymunk.Segment(space.static_body, (600, 0), (600, 400), wall_thickness),  # Right
    pymunk.Segment(space.static_body, (0, 400), (600, 400), wall_thickness),  # Bottom
]
for wall in walls:
    wall.elasticity = 1.0  # Makes the cue ball bounce off the walls
    wall.friction = 0.1
    space.add(wall)  # Add each wall to the space individually

def check_collision(arbiter, space, data):
    shape1, shape2 = arbiter.shapes
    black_hole_shape = data['black_hole_shape']

    if shape1 == black_hole_shape:
        planet_shape = shape2
    else:
        planet_shape = shape1

    # Calculate the distance between the centers of the black hole and the planet
    distance = black_hole_shape.body.position.get_distance(planet_shape.body.position)

    # If the distance is less than the sum of the radii, remove the planet
    if distance < black_hole_shape.radius + planet_shape.radius:
        space.remove(planet_shape, planet_shape.body)  # remove the planet
        return False  # Ignore the collision

    return True  # Otherwise, process the collision

# Set collision types
cue_shape.collision_type = 1
planet_shape.collision_type = 2
black_hole_shape.collision_type = 3

# Set up collision handler
handler = space.add_collision_handler(2, 3)  # Handle collisions between planets and black hole
handler.begin = check_collision
handler.data["black_hole_shape"] = black_hole_shape


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Apply an impulse to the cue ball when the mouse is clicked
            mouse_position = pygame.mouse.get_pos()
            direction = pymunk.Vec2d(*mouse_position) - cue_body.position
            impulse = direction.normalized() * 100
            cue_body.apply_impulse_at_world_point(impulse, cue_body.position)

    # Clear the screen
    screen.fill((50, 50, 50))

    # Step the simulation
    space.step(1/60.0)

    # Draw everything
    space.debug_draw(draw_options)

    # Flip the display
    pygame.display.flip()

    # Delay between frames
    clock.tick(60)

pygame.quit()
