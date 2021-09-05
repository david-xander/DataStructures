class Node:    
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.count = 0
    
    def __iter__(self):
        current_node = self.head
        while not current_node == None:
            yield str(current_node.data)
            current_node = current_node.next
    
    def addFront(self, item):
        new_item = Node(item)
        if self.head == None:
            self.head = new_item
        else:
            new_item.next = self.head
            self.head.prev = new_item
            self.head = new_item

        if self.tail == None:
            self.tail = self.head

        self.count += 1

    def addBack(self, item):
        new_item = Node(item)
        if self.tail == None:
            self.tail = new_item
        else:
            new_item.prev = self.tail
            self.tail.next = new_item
            self.tail = new_item

        if self.head == None:
            self.head = self.tail

        self.count += 1

    def popFront(self):
        if not self.head == None:
            item = self.head
            
            if not self.head.next == None:
                self.head.next.prev = None

            self.head = self.head.next

            if self.head == None:
                self.tail = None

            self.count -= 1
            return item.data
        else:
            raise Exception('No item to pop')
    
    def popBack(self):
        if not self.tail == None:
            item = self.tail
            
            if not self.tail.prev == None:
                self.tail.prev.next = None

            self.tail = self.tail.prev

            if self.tail == None:
                self.head = None

            self.count -= 1 
            return item.data     
        else:
            raise Exception('No item to pop')
    
    def append(self, item):
        self.addBack(item)

    def add(self, item):
        self.addBack(item)

    def pop(self):
        return self.popBack()

    def isEmpty(self):
        return self.count == 0
    
    def length(self) -> int:
        return self.count
    
    def findMiddle(self):
        node = self.head
        half = self.length()/2
        i = 0.
        while i < half:
            if i + 1 >= half:
                pass
            else:
                node = node.next
            i += 1

        return node.data

    def delete_n_nodes_after_m_nodes(self, n, m):
        node = self.head
        start_node = None
        j = 0
        k = 0
        while j < n and not node == None:
            if k == m:
                if j == 0 and j < n:
                    start_node = node.prev                   
                elif j + 1 == n:
                    # m = 0
                    if start_node == None:
                        self.head = node.next
                        node.next.prev = None
                    # m points to last nodes
                    if node.next == None:
                        start_node.next = None
                        self.tail = start_node
                    # in the middle
                    elif not start_node == None:
                        start_node.next = node.next
                        node.next.prev = start_node

                self.count -= 1
                j += 1
            else:
                k += 1
            
            node = node.next

    
if __name__ == '__main__':
    s = LinkedList()
    s.add(1)
    s.add(2)
    s.add('cosa')
    s.add(4)
    s.add(5)
    print(s.findMiddle())

