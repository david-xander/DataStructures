from practice import *
import unittest


class TestPractice(unittest.TestCase):

    def test_node_equality(self):
        self.assertTrue(Graph.node('hello') == \
            Graph.node('hello'))

    def test_edge_equality(self):
        nodeA = Graph.node('hello')
        nodeB = Graph.node('world')
        
        self.assertTrue( Graph.edge(nodeA, nodeB) == \
            Graph.edge(nodeA, nodeB))        

        self.assertTrue( Graph.edge(nodeB, nodeA) == \
            Graph.edge(nodeA, nodeB))  

    def test_graph_add_node(self):
        g = Graph()
        root = g.add_node(Graph.node('root'))
        hello = g.add_node(Graph.node('hello'))
        world = g.add_node(Graph.node('world'))
        and_more = g.add_node(Graph.node('and more'))
        self.assertEqual('root,hello,world,and more', \
             ','.join(g.get_nodes_data()))
        self.assertEqual(4, g.nodes_size())

    def test_graph_add_edge(self):
        g = Graph()
        g.add_edge(Graph.node('root'), Graph.node('hello'))
        g.add_edge(Graph.node('root'), Graph.node('world'))
        self.assertEqual('root,hello,world', \
            ','.join(g.get_nodes_data()))
        self.assertEqual(2, g.adjacency_list_size())            

    def test_graph_should_fail_adding_two_times_same_edge(self):
        g = Graph()
        g.add_edge(Graph.node('root'), Graph.node('hello'))
        g.add_edge(Graph.node('root'), Graph.node('world'))
        self.assertEqual(2, g.adjacency_list_size())

        with self.assertRaisesRegex(ValueError, 'repeated edge$'):
            g.add_edge(Graph.node('root'), Graph.node('world'))

        self.assertEqual(2, g.adjacency_list_size())

    def test_tree_add_node(self):
        root = Tree(Tree.node('root'))
        root.add(Tree.node('hello'))
        root.add(Tree.node('world'))
        root.node(Tree.node('hello')).add(Tree.node('n1'))
        root.node(Tree.node('hello')).add(Tree.node('n2'))
        root.node(Tree.node('world')).add(Tree.node('A'))
        root.node(Tree.node('A')).add(Tree.node('last'))
       
        


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
