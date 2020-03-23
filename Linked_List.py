
#Alex Bello
#3/13/2020
#Creates a linked list

class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None

    def __repr__(self):
        nodes = []
        curr = self.head
        while curr.next is not None:
            nodes.append(repr(curr))
            curr = curr.next
        return str(nodes)

    def clear(self):
        head = None

    def add_to_head(self,data):
        new_node = node(data)
        # creates new node
        new_node.next = self.head
        # makes new node point to the same node head does
	    self.head = new_node
        #makes the head point to new node

    def add_end(self, data):
        new_node = node(data)
        curr = self.head
        if self.head is None:
            self.head = new_node
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def pop_head(self, ):
