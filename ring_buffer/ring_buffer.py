class RingBuffer:
    def __init__(self, capacity):
       self.capacity = capacity
       self.data = []
       self.size = 0

    def append(self, item):
        if self.data == self.capacity:
            return None
        if len(self.data) == self.capacity:
               self.data[self.size] = item
               if self.size + 1 == self.capacity:
                   self.size = 0
               else: 
                   self.size += 1
        else: 
            self.data.append(item)

    def get(self):
        return self.data     

    