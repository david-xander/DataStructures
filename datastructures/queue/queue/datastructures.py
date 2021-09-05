

from logging import NOTSET


class Stack:
    items = []

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            last_index = len(self.items)-1
            item = self.items[last_index]
            return item
        else:
            return None

    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)


class Queue:
    
    items = []

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)

