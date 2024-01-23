#!/usr/bin/python3
"""defines a node of a singly linked list"""


class Node:
    """Represents a node singly listed list"""
    def __init__(self, data, next_node=None):
        """initializes the next node in singly linked list
        Args:
            data(int): the data to work with
            next_node: the node object
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """gets the data for the node of a singly linked list"""
        return self._data

    @data.setter
    def data(self, value):
        """sets the data for the node of a singly linked list"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """gets the next_node"""
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """sets the next_node"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    """represents a singly linked list"""
    def __init__(self):
        """initializes a singly linkes list
        Args:
            head: head of a singly linked list
        """
        self.head = None

    def sorted_insert(self, value):
        """ inserts a new Node into the correct sorted
        position in the list (increasing order)
        """
        new_node = Node(value)
        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        nodes = []
        current = self.head
        while current is not None:
            nodes.append(current.data)
            current = current.next_node
        return "\n".join(str(node) for node in nodes)
