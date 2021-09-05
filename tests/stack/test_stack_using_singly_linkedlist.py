from datastructures.stack.stack_using_singly_linkedlist.practice import *
import unittest


class TestPractice(unittest.TestCase):

    def test_linked_list_addfront(self):
        l = LinkedList()
        l.addFront('and more')
        l.addFront('world')
        l.addFront('hello')
        self.assertEqual('hello world and more', ' '.join(l))
        self.assertEqual(3, l.size())


    def test_linked_list_popfront(self):
        l = LinkedList()
        l.addFront('and more')
        l.addFront('world')
        l.addFront('hello')
        self.assertEqual('hello', l.popFront())
        self.assertEqual('world and more', ' '.join(l))
        self.assertEqual(2, l.size())

    def test_stack_push(self):
        s = Stack()
        s.push('and more')
        s.push('world')
        s.push('hello')
        self.assertEqual('hello world and more', ' '.join(s))
        self.assertEqual(3, s.size())     

    def test_stack_pop(self):
        s = Stack()
        s.push('and more')
        s.push('world')
        s.push('hello')
        self.assertEqual('hello', s.pop())
        self.assertEqual('world and more', ' '.join(s))
        self.assertEqual(2, s.size())    


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
