import networkx as nx
import matplotlib.pyplot as plt


class Node(object):
    def __init__(self, value: int):
        self.value = value
        self.edges: list[Edge] = []


class Edge(object):
    def __init__(self, value: int, node_from: Node, node_to: Node):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to


# TODO:
# 1. Node can't be inserted if exisited
# 2. get_adjacency_matrix currently assume node is in numeric order
class Graph(object):

    def __init__(self, nodes: list[Node] = [], edges: list[Edge] = []):
        self.nodes = nodes
        self.edges = edges

    def insert_node(self, new_node_val):
        new_node = Node(new_node_val)
        self.nodes.append(new_node)

    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        from_found = None
        to_found = None
        for node in self.nodes:
            if node_from_val == node.value:
                from_found = node
            if node_to_val == node.value:
                to_found = node
        if from_found == None:
            from_found = Node(node_from_val)
            self.nodes.append(from_found)
        if to_found == None:
            to_found = Node(node_to_val)
            self.nodes.append(to_found)
        new_edge = Edge(new_edge_val, from_found, to_found)
        from_found.edges.append(new_edge)
        to_found.edges.append(new_edge)
        self.edges.append(new_edge)

    def get_node_list(self):
        result = []
        for node in self.nodes:
            result.append(node.value)
        return result

    def get_edge_list(self):
        """Don't return a list of edge objects!
        Return a list of triples that looks like this:
        (Edge Value, From Node Value, To Node Value)"""
        result = []
        for edge in self.edges:
            result.append(
                (edge.value, edge.node_from.value, edge.node_to.value))
        return result

    def get_adjacency_list(self):
        """Don't return any Node or Edge objects!
        You'll return a list of lists.
        The indecies of the outer list represent
        "from" nodes.
        Each section in the list will store a list
        of tuples that looks like this:
        (To Node, Edge Value)"""
        result = []
        for node in self.nodes:
            tmp = []
            for edge in node.edges:
                if edge.node_from.value == node.value:
                    tmp.append((edge.node_to.value, edge.value))
            result.append(tmp if len(tmp) != 0 else None)
        return result

    def get_adjacency_matrix(self):
        """Return a matrix, or 2D list.
        Row numbers represent from nodes,
        column numbers represent to nodes.
        Store the edge values in each spot,
        and a 0 if no edge exists."""
        result = []
        for node in self.nodes:
            tmp = [0]*len(self.nodes)
            for edge in node.edges:
                if edge.node_from.value == node.value:
                    tmp[edge.node_to.value] = edge.value
            result.append(tmp)

        return result

    def adjacency_matrix_to_graph(self):
        matrix = self.get_adjacency_matrix()
        G = nx.Graph()
        for i in range(len(matrix)):
            for j in range(i, len(matrix[i])):
                if matrix[i][j] != 0:
                    G.add_edge(i, j, weight=matrix[i][j])
        return G

    def plot_graph(self, node_color: str, node_size: int, show_label: bool):
        G = self.adjacency_matrix_to_graph()
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True,
                node_color=node_color, node_size=node_size)
        labels = nx.get_edge_attributes(G, 'weight' if show_label else None)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()
        return
