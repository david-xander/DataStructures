from datastructures.queue.queue_using_stack_usnig_linked_list.practice import *
import unittest

class TestBasics(unittest.TestCase):

    def test_linkedlist(self):
        l = LinkedList()
        l.add("hola")
        l.add("mundo")
        self.assertEqual(2, l.size())
        self.assertEqual('mundo', l.pop())

    def test_stack(self):
        l = Stack()
        l.push("hola")
        l.push("mundo")
        self.assertEqual(2, l.size())
        self.assertEqual('mundo', l.pop())

    def test_enqueue_enqueue(self):
        q = Queue()
        q.enqueue("hello")
        q.enqueue("world")
        self.assertEqual('hello,world', q.printQueue())

    def test_dequeue(self):
        q = Queue()
        q.enqueue("hello")
        q.enqueue("world")
        deq = q.dequeue()
        self.assertEqual('hello', deq)
        self.assertEqual('world', q.printQueue())


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
