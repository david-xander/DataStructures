from practice import *
import unittest


class TestPractice(unittest.TestCase):
    def test_linkedlist_addfront(self):
        l = LinkedList()
        l.addFront('world')
        l.addFront('hello')
        self.assertEqual('hello world', ' '.join(l))
        self.assertEqual(2, l.size())
    
    def test_linkedlist_popBack(self):
        l = LinkedList()
        l.addFront('world')
        l.addFront('hello')
        self.assertEqual('world', l.popBack())
        self.assertEqual('hello', ' '.join(l))
        self.assertEqual(1, l.size())
    
    def test_queue_enqueue_and_dequeue(self):
        l = Queue()
        l.enqueue('hello')
        l.enqueue('world')
        self.assertEqual(2, l.size())    
        self.assertEqual('hello', l.dequeue())
        self.assertEqual('world', ' '.join(l))
        self.assertEqual(1, l.size())        

if __name__ == '__main__':
    unittest.main()  # pragma: no cover
