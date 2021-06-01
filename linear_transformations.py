import numpy as np


class LinearTransformation(object):
    """Basic linear transformation object. 
    Handles multiplication of tuples and multiplication of other linear transformations."""
    def __init__(self, std_matrix_repr):
        """
        @param list of 1 dim, list of 2 dim, or numpy ndarray"""
        if isinstance(std_matrix_repr, list):
            self.std_matrix_repr = np.array(std_matrix_repr)
        elif isinstance(std_matrix_repr, np.ndarray):
            self.std_matrix_repr = std_matrix_repr
        elif self.check_nested_list(std_matrix_repr):
            self.std_matrix_repr = np.array(std_matrix_repr)
        else:
            raise NotImplementedError(type(std_matrix_repr))

    def __repr__(self):
        return f"Linear Transformation: \n {self.std_matrix_repr}"

    def __mul__(self, other):
        """Left multiplication. self * other"""
        if isinstance(other, tuple):
            return self.transform_point(other)
        if isinstance(other, list):
            return self.transform_point(other)
        if isinstance(other, LinearTransformation):
            return self.left_composition(other)
        else:
            raise TypeError(tuple, LinearTransformation)

    def __rmul__(self, other):
        """Right multiplication. other * self"""
        if isinstance(other, tuple):
            return self.transform_point(other)
        if isinstance(other, list):
            return self.transform_point(other)
        if isinstance(other, LinearTransformation):
            return self.right_composition(other)
        else:
            raise TypeError(tuple, LinearTransformation)

    def __neg__(self):
        return LinearTransformation(np.negative(self.std_matrix_repr))

    def _get_size(self, axis):
        """
        Get row or column dimensions of matrix.
            @param int: 0 (column size), 1 (row size)
            @return int: row or column size
        """
        if axis is not 0 and axis is not 1:
            raise ValueError("axis = 0 or 1")
        return np.size(self.std_matrix_repr, axis)

    def _get_size_tuple(self):
        """
        Get column and row dimensions of matrix.
            @return tuple: (m, n)
        """
        return (self._get_size(0), self._get_size(1))

    def check_nested_list(self, nested_list):
        return any(isinstance(sub_list, list) for sub_list in nested_list)

    def left_composition(self, LT_obj2):
        """Self matrix * other matrix
            @param other linear transformation object
            @return composite linear transformation object
        """
        # m x n * n x b
        left_std_matrix_repr = self.std_matrix_repr
        left_column_size = self._get_size(0)
        right_std_matrix_repr_2 = LT_obj2.std_matrix_repr
        right_row_size = LT_obj2._get_size(1)
        if left_column_size != right_row_size:
            # left column mx size must be equal to right row mx size
            raise ValueError(f"MxN * NxB: {self._get_size_tuple()}, {LT_obj2._get_size_tuple()}")
        product_arr = np.multiply(left_std_matrix_repr, right_std_matrix_repr_2)
        return self.new_linear_transformation(product_arr)

    def right_composition(self, LT_obj2):
        """Other matrix * self matrix
            @param other linear transformation object
            @return composite linear transformation object
        """
        left_std_matrix_repr = LT_obj2.std_matrix_repr
        right_std_matrix_repr_2 = self.std_matrix_repr
        product_arr = np.multiply(left_std_matrix_repr, right_std_matrix_repr_2)
        return self.new_linear_transformation(product_arr)

    def new_linear_transformation(self, std_matrix_repr):
        return LinearTransformation(std_matrix_repr)

    def transform_point(self, point):
        """Multiple the matrix by the given point.
            @param tuple: of matrix column size
            @return tuple: of matrix row size
        """
        # m x n * n x 1, tuple must be of n size
        n_dim = self._get_size(1)
        if len(point) != n_dim:
            raise ValueError(f"Point must be of {n_dim} size.")
        vector_repr = np.array(point)
        product_arr = np.dot(self.std_matrix_repr, vector_repr)
        # tuple is of m size
        return tuple(product_arr)

    def update_std_mx_repr(self, new_std_mx_repr):
        self.std_matrix_repr = new_std_mx_repr

    def apply(self, point):
        """
        This function is not needed for linear transformation, but for combination transformations.
        Multiply matrix by point.
            @param 3-tuple
            @return 3-tuple
        """
        return self*point

    def get_inverse(self):
        return np.linalg.inv(self.std_matrix_repr)
