#!/usr/bin/env python3.10
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"Node({self.val}, next={self.next})"


head = Node(val=1, next=Node(val=2, next=Node(val=3, next=Node(val=4))))


def traverse(node):
    while node:
        print(node.val, end=" ")
        node = node.next
    print()


def reverse(node):
    prev = None
    while node:
        node.next, node, prev = prev, node.next, node
    return prev


traverse(head)
traverse(reverse(head))
