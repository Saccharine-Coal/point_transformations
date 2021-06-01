
import point_transformations.projections
import point_transformations.translations

class Camera(object):
    """Combination of linear transformations and a projection transformation to represent
    position of the camera as the game screen.
    """
    def __init__(self, projection_matrix, position = (0, 0, 0), unit_size=1, rotation=None):
        self.projection_matrix = projection_matrix
        self.position = position
        self.translation_matrix = self._get_translation_matrix(position)
        self.rotation = rotation
        self.rotation_matrix = self._get_rotation_matrix(self.rotation)
        self.unit_size = unit_size

    def __repr__(self):
        return f"pos: {self.position}, unit size: {self.unit_size}"

    def _get_projection_matrix(self, unit_size):
        projection_type = type(self.projection_matrix)
        return projection_type(unit_size)

    def _get_translation_matrix(self, position):
        return point_transformations.translations.TranslationMatrix3(position)

    def _get_rotation_matrix(self, rotation):
        if rotation is None:
            return None
        else:
            print(rotation)
            # return list of rotation matrices [x, y, z]
            raise NotImplementedError

    def scale(self, delta):
        self.unit_size += delta
        self.projection_matrix = self._get_projection_matrix(self.unit_size)

    def translate(self, dx=0, dy=0, dz=0):
        x, y, z = self.position[:]
        x += dx
        y += dy 
        z += dz
        self.position = (x, y, z)
        # update translation matrix
        self.translation_matrix = self._get_translation_matrix(self.position)

    def rotate(self, dx=0, dy=0, dz=0):
        if self.rotation_matrix is None:
            pass
        else:
            raise NotImplementedError

    def apply(self, iter_of_points):
        projected_points = []
        # rotate, translate, then project
        for point in iter_of_points:
            if self.rotation_matrix is not None:
                point = self.rotation_matrix * point
            point = self.translation_matrix * point
            point = self.projection_matrix * point
            projected_points.append(point)
        return projected_points


class IsometricCamera(Camera):
    """Camera object that uses isometric projection."""
    def __init__(self, position, unit_size):
        projection_matrix = point_transformations.projections.IsometricProjection(unit_size)
        super().__init__(projection_matrix, position, unit_size)