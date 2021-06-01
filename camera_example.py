import sys

import pygame as pg

import point_transformations.camera


"""Example use of linear transformations to generate pseudo 3D graphics."""

# construct camera instance
isometric_camera = point_transformations.camera.IsometricCamera((0, 0, 0), 1)
print(f"Construct Camera: \n {isometric_camera}")

# update camera position
isometric_camera.translate(1, 20, 3)
print(f"Translate Camera: \n {isometric_camera}")

# update projection scale
isometric_camera.scale(10)
print(f"Scale Camera: \n {isometric_camera}")

# apply camera to list of 3D points
points = [(50, 50, 50), (50, 50, 100), (100, 50, 100), (100, 100, 100)] # random 3D plane
projected_points = isometric_camera.apply(points) # projection of the shape on a 2D plane
print(f"3D points: \n {points}")
print(f"2D points: \n {projected_points}")

pg.init()
screen = pg.display.set_mode((400, 400))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT: 
            sys.exit()

    screen.fill((0, 0, 0))
    pg.draw.polygon(screen, (255, 0, 0), projected_points)
    pg.display.flip()
