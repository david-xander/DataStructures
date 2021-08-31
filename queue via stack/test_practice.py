from practice import *
import unittest

class TestBasics(unittest.TestCase):

    def test_enqueue_enqueue_dequeue(self):
        q = Queue()
        q.enqueue("hello")
        q.enqueue("world")
        self.assertEqual('hello,world', q.printQueue())
        deq = q.dequeue()
        self.assertEqual('hello', deq)
        self.assertEqual('world', q.printQueue())


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
