class Queue:
    
    def __init__(self):
        self.items = []
    
    def size(self) -> int:
        return len(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        self.items.pop(0)

    def printQueue(self):
        return ','.join(self.items)

if __name__ == '__main__':
    pass
    
