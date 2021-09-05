from datastructures.queue.queue.practice import Queue
import unittest


class TestingQueue(unittest.TestCase):

    def test_empty(self):
        s = Queue()
        self.assertEqual(True, s.isEmpty())
    
    def test_enqueue_chain(self):
        s = Queue()
        s.enqueue('cosa')
        s.enqueue(1)
        self.assertEqual(2, s.size())

    def test_enqueue_and_dequeue_chain(self):
        s = Queue()
        s.enqueue('cosa')
        s.enqueue(1)
        self.assertEqual('cosa', s.dequeue())        

if __name__ == '__main__':
    unittest.main()  # pragma: no cover
