class RingBuffer:
    def __init__(self, capacity):
       self.capacity = capacity
       self.data = []
       self.cur_node = 0

    def append(self, item):
        if self.data == self.capacity:
            self.cur_node = 0
        self.data[self.cur_node] = item
        self.cur_node = [self.cur_node+1] % self.capacity
        return self.data

    def get(self):
        return self.data     

    