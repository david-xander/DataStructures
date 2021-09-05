from datastructures.linkedlist.doubly.practice import *
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

    def test_delete_n_nodes_after_m_nodes(self):
        s = LinkedList()
        s.add(31)
        s.add(77)
        s.add(17)
        s.add(93)
        s.add(26)
        s.add(54)
        s.delete_n_nodes_after_m_nodes(n=2, m=1)
        self.assertEqual('31,93,26,54', ','.join(s))

    def test_delete_n_nodes_after_m_nodes_with_m_zero(self):
        s = LinkedList()
        s.addFront(31)
        s.addFront(77)
        s.addFront(17)
        s.addFront(93)
        s.addFront(26)
        s.addFront(54)
        s.delete_n_nodes_after_m_nodes(n=2, m=0)
        self.assertEqual('93,17,77,31', ','.join(s))

    def test_delete_n_nodes_after_m_nodes_last(self):
        s = LinkedList()
        s.addFront(31)
        s.addFront(77)
        s.addFront(17)
        s.addFront(93)
        s.addFront(26)
        s.addFront(54)
        s.delete_n_nodes_after_m_nodes(n=2, m=4)
        self.assertEqual('54,26,93,17', ','.join(s))

    def test_find_middle(self):
        s = LinkedList()
        s.add(1)
        s.add(2)
        s.add('cosa')
        s.add(4)
        s.add(5)
        self.assertEqual('cosa', s.findMiddle())        

if __name__ == '__main__':
    unittest.main()  # pragma: no cover
