#Double ended queue

class Deque(object):


    def __init__(self):
        self.items = []

    def addFront(self, item):
        self.items.insert(0, item)

    def addRead(self, item):
        self.items.append(item)

    def removeFront(self):
        return self.items.pop(0)

    def removeRear(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

if __name__ == '__main__':
    d = Deque()
    d.addFront('hello')
    d.addRead('world')
    print(d.size())
    print(d.removeFront())
    print(d.removeRear())