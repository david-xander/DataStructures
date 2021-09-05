
class Node:
    def __init__(self, input) -> None:
        self.data = input
    
    def __eq__(self, o: object) -> bool:
        return self.data == o.data

class NodeList:
    def __init__(self) -> None:
        self.nodes = []
    def __iter__(self):
        for node in self.nodes:
            yield node
    def add(self, item):
        if not item in self.nodes:
            self.nodes.append(item)
        return Node(item)
    def pop(self):
        return self.nodes.pop()
    def size(self):
        return len(self.nodes)

class Edge:
    def __init__(self, nodeA, nodeB) -> None:
        self.nodeA = nodeA
        self.nodeB = nodeB
    def __eq__(self, o: object) -> bool:
        return (self.nodeA == o.nodeA and \
            self.nodeB == o.nodeB) or \
            (self.nodeB == o.nodeA and \
            self.nodeA == o.nodeB)

class EdgeList:
    def __init__(self) -> None:
        self.edges = []
    def __iter__(self):
        for edge in self.edges:
            yield edge
    def add(self, nodeA, nodeB):
        if not Edge(nodeA, nodeB) \
            in self.edges:        
            self.edges.append(Edge(nodeA, nodeB))
        else:
            raise ValueError('repeated edge')       
    def pop(self):
        return self.edges.pop()
    def size(self):
        return len(self.edges)

# undirected graph
class Graph:
    def __init__(self) -> None:
        self.nodes = NodeList()
        self.adjancency_list = EdgeList()
    def add_node(self, data):
        self.nodes.add(data)
    def add_edge(self, dataA, dataB):
        nodeA = self.nodes.add(dataA)
        nodeB = self.nodes.add(dataB)
        self.adjancency_list.add(nodeA, nodeB)
    def get_nodes_data(self):
        nodes_str = [node.data for node in self.nodes]
        return nodes_str
    def nodes_size(self):
        return self.nodes.size()
    def adjacency_list_size(self):
        return self.adjancency_list.size()
    @staticmethod
    def node(item):
        return Node(item)
    @staticmethod
    def edge(nodeA, nodeB):
        return Edge(nodeA, nodeB)

class TreeNode(Node):
    def __init__(self, input) -> None:
        super().__init__(input)
        self.is_root = False
    def parent (self):
        pass
    def children(self):
        pass
    def is_leaf(self):
        pass
    @staticmethod
    def node(item):
        return TreeNode(item)    

class Tree(Graph):
    def __init__(self, root):
        super(Graph, self).__init__()
        self.root = root
    def sibling(self, node):
        pass
    def level(self):
        pass
    def height(self):
        pass
    def add(self, item):
        self.add_edge(self.root)


class BinaryTree(Tree):
    def add_node(self, item):
        pass

if __name__ == '__main__':
    pass
    
