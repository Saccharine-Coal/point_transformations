import math

import point_transformations.linear_transformations


class IsometricProjection(point_transformations.linear_transformations.LinearTransformation):
    """Isometric projection of xyzw on xy."""
    def __init__(self, unit_size=1, offset=0):
        theta_x, theta_y, theta_z = 150+offset, 30+offset, -90
        rad_x, rad_y, rad_z = list((math.pi/180) * theta for theta in [theta_x, theta_y, theta_z] )[:]
        std_matrix_repr = [
                           [math.cos(rad_x)*unit_size, math.cos(rad_y)*unit_size, math.cos(rad_z)*unit_size],
                           [math.sin(rad_x)*unit_size, math.sin(rad_y)*unit_size, math.sin(rad_z)*unit_size]
                          ]
        super().__init__(std_matrix_repr)


class PointPerspective(point_transformations.linear_transformations.LinearTransformation):
    """3 point perspective of xyzw on xy."""
    def __init__(self):
        raise NotImplementedError


