from controllers import (
    create_graph,
    check_route,
    shortest_route,
    check_all_routes,
    different_routes_less_a_distance
)


if __name__ == '__main__':
    input_data = list(input().split(', ' or ','))

    graph = create_graph(input_data)

    print('Output #1:', check_route(graph, 'A-B-C'))
    print('Output #2:', check_route(graph, 'A-D'))
    print('Output #3:', check_route(graph, 'A-D-C'))
    print('Output #4:', check_route(graph, 'A-E-B-C-D'))
    print('Output #5:', check_route(graph, 'A-E-D'))
    print('Output #6:', check_all_routes(graph, 'C', 'C', maximum=3))
    print('Output #7:', check_all_routes(graph, 'A', 'C', exactly=4))
    print('Output #8:', shortest_route(graph, 'A', 'C'))
    print('Output #9:', shortest_route(graph, 'C', 'C'))
    print(
        'Output #10:',
        different_routes_less_a_distance(graph, 'C', 'C', 30)
    )
