
#Alex Bello
#3/13/2020
#Creates a linked list

class node:
    def __init__(self, data):
        self.data = data
        self.next = none

class linked_list:
    def __init__(self):
        self.head = none

    def __repr__(self):
        nodes = []
        curr = self.head
        while curr.next != none:
            nodes.append(repr(curr))
            curr = curr.next
        return str(nodes)

    def clear(self):
        head = none


