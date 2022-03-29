#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

#
# Complete the 'sortedInsert' function below.
#
# The function is expected to return an INTEGER_DOUBLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_DOUBLY_LINKED_LIST llist
#  2. INTEGER data
#

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#

def sortedInsert(llist, data):
    # create new node with the given data
    newNode = DoublyLinkedListNode(data)
    
    # check if data less than the first one
    # if so add node as first node then connect its next node
    # to the old first node and set the old first node prev 
    # to new node
    if llist.data > data:
        temp = llist
        llist = newNode
        llist.next = temp
        return llist
    
    node = llist
    # set node to next node while the new node data is
    # bigger than node data
    while node.data < newNode.data and node.next != None:
        node = node.next
    
    # if new node data bigger than node.data, that must
    # indicate that the new node will be the new last node
    if node.data < newNode.data:
        node.next = newNode
        newNode.prev = node
    # else connect node to the double linked list chain
    else:
        newNode.prev = node.prev
        newNode.next = node.prev.next
        newNode.prev.next = newNode
        newNode.next.prev = newNode
    return llist

if __name__ == '__main__':
