#!/usr/bin/python3
"""A module that multiplies 2 matrices by using the module NumPy"""


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
        numpy.ndarray: The resulting matrix.

    Raises:
        TypeError: If m_a or m_b is not a list or a list of lists.
        ValueError: If m_a or m_b is empty, contains non-numeric elements,
                    or is not a rectangle, or can't be multiplied using NumPy.
    """
    try:
        np_m_a = np.array(m_a)
        np_m_b = np.array(m_b)
        result = np.dot(np_m_a, np_m_b)
        return result.tolist()
    except Exception as e:
        raise ValueError(f"NumPy Error: {str(e)}")

if __name__ == "__main__":
    print(lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
    print(lazy_matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
