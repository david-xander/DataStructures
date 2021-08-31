# class Node:
#     def __init__(self, data) -> None:
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self) -> None:
#         self.items = None
#         self.head = None
    
#     def __iter__(self):
#         current_now = self.head
#         while not current_now == None:
#             yield current_now.data
#             current_now = current_now.next        
    
#     def add(self, item):
#         new = Node(item)
#         new.next = self.head
#         self.head = new

#     def remove(self, data):
#         found = False
#         node = self.head
#         previous = None
#         while not found:
#             if node.data == data:
#                 found = True
#                 if previous == None:
#                     self.head = node.next
#                 else:
#                     previous.next=node.next
            
#             if node.next == None:
#                 raise Exception('Index not found')
#             else:
#                 previous = node
#                 node = node.next

#     def size(self):
#         count = 0
#         node = self.head
#         while not node == None:
#             count += 1
#             node = node.next   
#         return count

class Stack:
    def __init__(self) -> None:
        self.items = [] #using List
    
    def __iter__(self):
        for item in self.items:
            yield item        

    def push(self, item):
        self.items.insert(0, item)
    
    def pop(self):
        return self.items.pop(0)
    
    def peek(self):
        return self.items[0]

    def size(self):
        self.items.size()

class Queue:
    def __init__(self) -> None:
        self.items = Stack()
    
    def enqueue(self, item):
        self.items.push(item)
    
    def dequeue(self):
        #return self.items.pop(0)
        
    
    def printQueue(self):
        return ','.join(self.items)



if __name__ == '__main__':
    pass
    
