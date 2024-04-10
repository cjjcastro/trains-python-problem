from collections import defaultdict


class Graph:
    """
    Define a directed graph with nodes, edges and distances
    """

    def __init__(self):
        """
        Init class
        """
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        """
        Add a new node

        Input:
        value (str): a node key name
        """
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        """
        Add a new edge

        Input:
        from_node (str): initial node name
        to_node (str): target node name
        distance (int): distance value of route
        """
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance

    def get_distance(self, from_node, to_node):
        """
        Return a distance of two nodes

        Output (int): a distance value
        """
        if (from_node, to_node) in self.distances.keys():
            return self.distances[from_node, to_node]
        else:
            return -1

    def __str__(self) -> str:
        """
        Create a printable graph

        Output (str): all graph informations in string format
        """
        output = set()
        for from_node in self.nodes:
            for to_node in self.edges[from_node]:
                output.add((
                    from_node,
                    to_node,
                    self.get_distance(from_node, to_node)
                ))
        return str(output)


def create_graph(nodes):
    """
    Create a graph with a list in format:
        AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7
    The first value is a initial node, the second value is a destiny node,
    and the third value is a distance of the two nodes

    Input:
    nodes (list(str)): list with all nodes and edges

    Output (Graph): a created graph
    """
    graph = Graph()
    for node in nodes:
        from_node = node[0]
        to_node = node[1]
        distance = int(node[2:])

        graph.add_node(from_node)
        graph.add_node(to_node)
        graph.add_edge(from_node, to_node, distance)

    return graph
