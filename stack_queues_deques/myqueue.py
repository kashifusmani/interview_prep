class MyQueue(object):


    def __init__(self):
        self.items = []

    def enqueue(self, item):
        #self.items.append(item)
        self.items.insert(0, item)

    def dequeue(self):
        #self.items.remove(self.items[0])
        self.items.pop() #This approach is safer than using self.items[0]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

