class RingBuffer:
    def __init__(self, capacity):
       self.capacity = capacity
       self.data = []
       self.size = 0

    def append(self, item):
        # check if full
        if self.data == self.capacity:
            return None
        # if stmt to check if adding will hit capacity
        if len(self.data) == self.capacity:
               self.data[self.size] = item
               if self.size + 1 == self.capacity:
                   self.size = 0
               else: 
                   self.size += 1
        # add to list
        else: 
            self.data.append(item)

    def get(self):
        return self.data     

    