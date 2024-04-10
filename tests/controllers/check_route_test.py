from src.controllers import Graph, create_graph, check_route, shortest_route, check_all_routes

def test_check_route():
    graph = create_graph(['AB5'])

    assert check_route(graph, 'A-B') == 5
    assert check_route(graph, 'B-A') == 'NO SUCH ROUTE'

def test_shortest_route():
    graph = create_graph(['AB5', 'BD4'])

    assert shortest_route(graph, 'A', 'B') == 5
    assert shortest_route(graph, 'A', 'D') == 9
    assert shortest_route(graph, 'A', 'C') == 'NO SUCH ROUTE'

def test_check_all_routes():
    graph = create_graph(['AB5', 'BD4'])

    assert check_all_routes(graph, 'C', 'C', maximum=3) == 'NO SUCH ROUTE'
    assert check_all_routes(graph, 'A', 'D', maximum=3) == 1
    assert check_all_routes(graph, 'A', 'D', exactly=2) == 1
    assert check_all_routes(graph, 'A', 'D', exactly=4) == 'NO SUCH ROUTE'
