#!/usr/bin/python3
"""A module of class MyInt that inherits from int:"""


class MyInt(int):
    """
    Class representing a rebel integer.

    The class inverts the behavior of the equality (==) and
    inequality (!=) operators.

    Methods:
    - __eq__(self, other): Inverts the equality operator.
    - __ne__(self, other): Inverts the inequality operator.
    """
    def __eq__(self, other):
        """
        Inverts the equality operator.

        Args:
        - other: The other object to compare.

        Returns:
        - True if the objects are not equal, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the inequality operator.

        Args:
        - other: The other object to compare.

        Returns:
        - True if the objects are equal, False otherwise.
        """
        return super().__eq__(other)
