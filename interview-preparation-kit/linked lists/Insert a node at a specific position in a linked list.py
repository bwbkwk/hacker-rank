#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

#
# Complete the 'insertNodeAtPosition' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST llist
#  2. INTEGER data
#  3. INTEGER position
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def insertNodeAtPosition(llist, data, position):
    # so our new linked list will be consist of three
    # part which are (left)->(new node)->(right)
    
    # assign node to the head
    node = llist
    
    # find the last node from the left part
    i = 0
    while i < position-1:
        node = node.next
        i+=1
        
    # currently as we haven't insert the new node as
    # next node of the last node of the left part
    # the last still be the first node of the right part
    # put the first node of the right part to temp variable
    temp = node.next
    
    # set the next node of the last node of left part
    # to a new node that contain new data 
    node.next = SinglyLinkedListNode(data)
    
    # set next node of new node to the first node of the
    # right part
    node.next.next = temp
    
    # return head of the list
    return llist
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    data = int(input())

    position = int(input())

    llist_head = insertNodeAtPosition(llist.head, data, position)

    print_singly_linked_list(llist_head, ' ', fptr)
    fptr.write('\n')

    fptr.close()
