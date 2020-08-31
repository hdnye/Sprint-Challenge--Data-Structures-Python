class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):

        # Compare target value to node.value
        # if value > node.value:
        if value >= self.value:

            # if value is greater, go right
            # Check if single element
            # if node.right is none: create new node there
            if self. right is None:
                self.right = BSTNode(value)

            # Else right.node != none:
            else:
                # Insert value into node.right
                right_child = self.right
                right_child.insert(value)

        # Else/if value < node.value
        if value < self.value:
            # check if single element
            # if node.left is none: create new node there
            if self.left is None:
                self.left = BSTNode(value)
            # else left.node != none:
            else:
                # insert value into self.left.insert(value)
                left_child = self.left
                left_child.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):

       # Compare target to root
       if target == self.value:
           return True

       # if target > go right
       if target > self.value:
           # if node.right is None:
           # return false b/c it doesn't exist in the tree
           if self.right is None:
               return False
           # else: go right
           # return node.right.contains(value)
           else:
               return self.right.contains(target)

       # if target < go left
       if target < self.value:
           # if node.left is None:
           # return false b/c it doesn't exist in the tree
           if self.left is None:
               return False
           # else: go left, return node.left.contains(value)
           else:
               return self.left.contains(target)
