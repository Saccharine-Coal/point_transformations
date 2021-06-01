import math

import point_transformations.linear_transformations


class IsometricProjection(point_transformations.linear_transformations.LinearTransformation):
    """
    Isometric projection of xyz on xy.
    https://en.wikipedia.org/wiki/Isometric_projection#Mathematics
    """
    def __init__(self, unit_size=1):
        """
        @param int: effective scaling up/down of the projection
        """
        # changing the angle changes the type of parallel projection
        INITIAL_X, INITIAL_Y, INITIAL_Z = 150, 30, -90
        # x, y, and z angles in degrees
        theta_x, theta_y, theta_z = INITIAL_X, INITIAL_Y, INITIAL_Z
        # math trigonometric functions need radians
        # x, y, and z angles in radians
        rad_x, rad_y, rad_z = list((math.pi/180) * theta for theta in [theta_x, theta_y, theta_z] )[:]
        # construct projection matrix: matrix * 3-tuple => 2-tuple
        std_matrix_repr = [
                           [math.cos(rad_x)*unit_size, math.cos(rad_y)*unit_size, math.cos(rad_z)*unit_size],
                           [math.sin(rad_x)*unit_size, math.sin(rad_y)*unit_size, math.sin(rad_z)*unit_size]
                          ]
        super().__init__(std_matrix_repr)


class PointPerspective(point_transformations.linear_transformations.LinearTransformation):
    """3 point perspective of xyzw on xy."""
    def __init__(self):
        raise NotImplementedError


