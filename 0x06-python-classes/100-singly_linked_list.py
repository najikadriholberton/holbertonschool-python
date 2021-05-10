#!/usr/bin/python3
"""module for singly linked lists"""


class Node:
    """A node class for singly linked lists"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """a class that creates a singly linked list"""

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """add nodes in an order manner"""
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None \
                    and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __repr__(self):
        """represent and print class"""
        result = ""
        current = self.__head
        while current is not None:
            if current.next_node is None:
                result += "{}".format(current.data)
            else:
                result += "{}\n".format(current.data)
            current = current.next_node
        return result
