from datastructures import UnOrderedList
import unittest


class TestingQueue(unittest.TestCase):

    def test_empty(self):
        s = UnOrderedList()
        self.assertEqual(True, s.isEmpty())

    def test_length(self):
        s = UnOrderedList()
        self.assertEqual(0, s.length())

    def test_list_add_length(self):
        s = UnOrderedList()
        s.add('cosa')
        s.add(1)
        self.assertEqual(2, s.length())

    def test_add_and_remove_chain(self):
        s = UnOrderedList()
        s.add('cosa')
        s.add(1)
        s.remove(1)
        self.assertEqual(1, s.length())

    def test_print(self):
        s = UnOrderedList()
        s.add(31)
        s.add(77)
        s.add(17)
        s.add(93)
        s.add(26)
        s.add(54)
        self.assertEqual('54,26,93,17,77,31', s.printList())

    def test_delete_n_nodes_after_m_nodes(self):
        s = UnOrderedList()
        s.add(31)
        s.add(77)
        s.add(17)
        s.add(93)
        s.add(26)
        s.add(54)
        s.delete_n_nodes_after_m_nodes(n=2, m=1)
        self.assertEqual('54,17,77,31', s.printList())

    def test_delete_n_nodes_after_m_nodes_with_m_zero(self):
        s = UnOrderedList()
        s.add(31)
        s.add(77)
        s.add(17)
        s.add(93)
        s.add(26)
        s.add(54)
        s.delete_n_nodes_after_m_nodes(n=2, m=0)
        self.assertEqual('93,17,77,31', s.printList())

    def test_delete_n_nodes_after_m_nodes_last(self):
        s = UnOrderedList()
        s.add(31)
        s.add(77)
        s.add(17)
        s.add(93)
        s.add(26)
        s.add(54)
        s.delete_n_nodes_after_m_nodes(n=2, m=4)
        self.assertEqual('54,26,93,17', s.printList())

    def test_find_middle(self):
        s = UnOrderedList()
        s.add(1)
        s.add(2)
        s.add('cosa')
        s.add(4)
        s.add(5)
        self.assertEqual('cosa', s.findMiddle())

if __name__ == '__main__':
    unittest.main()  # pragma: no cover
