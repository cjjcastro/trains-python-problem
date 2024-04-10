from collections import defaultdict
from src.controllers import Graph, create_graph


def test_create_graph():
    graph = create_graph(['AB5', 'BC4', 'CD8', 'DC8', 'DE6', 'AD5', 'CE2', 'EB3', 'AE7'])

    assert len(graph.nodes) == 5
    assert len(graph.edges) == 5
    assert graph.edges == \
        {'A': ['B', 'D', 'E'], 'B': ['C'], 'C': ['D', 'E'], 'D': ['C', 'E'], 'E': ['B']}

def test_get_distance():
    graph = create_graph(['AB5'])

    assert graph.get_distance('A', 'B') == 5
    assert graph.get_distance('a', 'b') == -1
    assert graph.get_distance('B', 'A') == -1

def test_add_node():
    graph = Graph()
    graph.add_node('A')

    assert graph.nodes == set(['A'])

def test_add_edge():
    graph = Graph()
    graph.add_node('A')
    graph.add_node('B')
    graph.add_edge('A', 'B', 2)
    edges = defaultdict(list)
    edges['A'].append('B')

    assert graph.nodes == set(['A', 'B'])
    assert graph.edges == edges
