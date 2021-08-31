from practice import *
import unittest

class TestBasics(unittest.TestCase):

    def test_enqueue_enqueue_dequeue(self):
        q = Queue()
        q.enqueue("world")
        q.enqueue("hello")
        self.assertEqual('hello,world', q.printQueue())
        q.dequeue()
        self.assertEqual('world', q.printQueue())


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
