import math

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


class Deque:
    items = []

    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)
    
    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)



class ListNode:
    value = None
    next = None
    
    def __init__(self, input):
        self.value=input
    
class UnOrderedList:

    head = None

    def __init__(self):
        self.nodes = []

    def isEmpty(self):
        return self.head == None
    
    def add(self, item):
        node = ListNode(item)
        node.next = self.head
        self.head=node

    def remove(self, item):
        continue_searching = True
        current_node = self.head
        previous = None
        while continue_searching:
            if current_node.value == item: 
                if not previous == None:
                    previous.next = current_node.next
                continue_searching = False
            elif not current_node == None:
                current_node = current_node.next
            
            previous = current_node
        
        if not previous == None:
            self.head = previous.next

    def length(self):
        continue_searching = True
        current_node = self.head
        res = 0
        if not current_node == None:
            while continue_searching:
                res += 1
                if current_node.next == None: continue_searching = False
                else: current_node = current_node.next
            
        return res
    
    def findMiddle(self):
        # get lenth without method
        length = 1
        current_node = self.head
        while not current_node.next == None:
            length += 1
            current_node = current_node.next

        current_node = self.head
        half = int(math.ceil(length/2))
        count = 1
        found = None
        while found == None and not current_node.next == None:
            if count == half:
                found = current_node
            count += 1
            current_node = current_node.next

        return found.value

    def delete_n_nodes_after_m_nodes(self, n, m):
        current_node = self.head
        m_found = False
        previous = None
        start_node = None
        last_node = None
        j = 0
        k = 0
        while not current_node == None:
            if j >= m:
                if not m_found and previous == None:
                    pass
                elif not m_found and start_node == None:
                    start_node = previous
                if k < n:
                    last_node = current_node
                    k += 1
                m_found = True
            previous = current_node
            current_node = current_node.next
            j += 1
        
        if start_node == None:
            self.head = last_node.next
        else:
            start_node.next = last_node.next

    def printList(self):
        continue_printing = True
        res = ''
        current_node = self.head
        while continue_printing:
            if res == '':
                res = str(current_node.value)
            else:
                res += ','+str(current_node.value)
            
            if not current_node.next == None:
                current_node = current_node.next
            else:
                continue_printing = False
        return res

if __name__ == '__main__':
    s = UnOrderedList()
    s.add(1)
    s.add(2)
    s.add(3)
    s.add(3)
    s.add(5)
    print(s.findMiddle())