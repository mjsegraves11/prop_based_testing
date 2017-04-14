import math

class Queue(object):
    def __init__(self):   # default no-arg constructor
        self.q = []
        pass

    def enqueue(self, v): # adds v to the back of the queue; no return value
        if v is None:
            raise ValueError
        if isinstance(v, float):
            if math.isnan(v) or math.isinf(v):
                raise ValueError
        self.q.append(v)
        print(self.q)
        pass

    def dequeue(self): # removes and returns the element at the front of the queue
        if (len(self.q) > 0):
            self.q.reverse()
            element = self.q.pop()
            self.q.reverse()
            return element
        else:
            return None
        pass

    def len(self):        # returns the number of elements in the queue
        return len(self.q)
        pass