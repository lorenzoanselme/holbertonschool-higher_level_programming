#!/usr/bin/python3
"""This module defines a Node and a SinglyLinkedList class."""


class Node:
    """This class represents a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new node with data and an optional next node."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data stored in the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data value of the node after validation."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next node reference."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node reference after validation."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """This class represents a singly linked list."""

    def __init__(self):
        """Initialize an empty singly linked list."""
        self.__head = None

    def __str__(self):
        """Return a string representation of the list."""
        lines = []
        current = self.__head
        while current is not None:
            lines.append(str(current.data))
            current = current.next_node
        return "\n".join(lines)

    def sorted_insert(self, value):
        """Insert a new node into the list in sorted order."""
        new_node = Node(value)

        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node
