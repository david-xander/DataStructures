from practice import *
import unittest


class TestPractice(unittest.TestCase):
    def test_is_appending(self):
        l = LinkedList()
        l.append('hello')
        l.append('world')
        l.append('and more')
        self.assertEqual(3, l.length())
    
    def test_is_popping_and_returning_value(self):
        l = LinkedList()
        l.append('hello')
        l.append('world')
        l.append('and more')
        self.assertEqual('and more', l.pop())
        self.assertEqual(2, l.length())

    def test_check_is_empty(self):
        l = LinkedList()
        self.assertEqual(True, l.isEmpty())
        l.append('hello')
        l.append('world')
        l.append('and more')
        self.assertEqual(False, l.isEmpty())
        self.assertEqual('and more', l.pop())
        self.assertEqual('world', l.pop())
        self.assertEqual('hello', l.pop())
        self.assertEqual(True, l.isEmpty())

    def test_check_adding_and_popping_front(self):
        l = LinkedList()
        l.addFront('and more')
        l.addFront('world')
        l.addFront('hello')
        self.assertEqual('hello world and more', ' '.join(l))
        self.assertEqual('hello', l.popFront())
        self.assertEqual('world', l.popFront())
        self.assertEqual('and more', l.popFront()) 
        self.assertEqual(True, l.isEmpty())

if __name__ == '__main__':
    unittest.main()  # pragma: no cover
