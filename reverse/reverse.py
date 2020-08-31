class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # check for head
        if self.head is None:
            return None

        cur_node = node
        # set head
        cur_node = self.head
        # set prev
        prev = None   
      
        # while loop to reverse
        while cur_node != None:
            # set to next node
            after = cur_node.next
            # reverse the list
            cur_node.next = prev
            # move prev to next 
            prev = cur_node
            # move cur to next
            cur_node = after
            # set pointer if not last node
            if after:
                after = after.next 
            if after.next is None:
                break      
        # process
        self.head = prev
        return prev



