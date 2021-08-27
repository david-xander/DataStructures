

class Stack:
    items = []

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
        return len(self.items) > 0
    
    def size(self):
        return len(self.items)
