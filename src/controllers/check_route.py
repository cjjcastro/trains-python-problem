def check_route(graph, route):
    """
    Check if a route is possible

    Input:
    graph (Graph)
    route (str)

    Output (int): Route distance
    """
    route = list(route.split('-'))
    distance = 0
    for i in range(1, len(route)):
        aux = graph.get_distance(route[i-1], route[i])

        if aux == -1:
            return 'NO SUCH ROUTE'
        distance = distance + aux

    return distance


def check_all_routes(graph, initial, ending, maximum=False, exactly=False):
    """
    Search the number of trips starting at a node
    and ending at a node

    Input:
    graph (Graph)
    initial (str)
    ending (str)
    maximum (int/bool)
    exactly (int/bool)

    Output (int): number of routes
    """
    path = []
    all_paths = []
    rout = check_all_routes_util(
        graph,
        initial,
        ending,
        path,
        all_paths,
        first=True
    )

    if maximum:
        rout_response = \
            len([(route) for route in rout if len(route) <= maximum+1])
    elif exactly:
        cicle_path = []
        cicle_all_paths = []
        cicle_rout = check_all_routes_util(
            graph,
            ending,
            ending,
            cicle_path,
            cicle_all_paths,
            first=True
        )

        rout = ([(route) for route in rout if len(route) <= exactly+1])

        aux = True
        while aux:
            aux = False
            for node_i in rout:
                for node_j in cicle_rout:
                    if len(node_i) + len(node_j)-1 == exactly+1 and not node_i + node_j[1:] in rout:
                        rout.append(node_i + node_j[1:])
                        aux = True

        rout_response = len([(route) for route in rout if len(route) == exactly+1])

    if rout_response:
        return rout_response
    else:
        return 'NO SUCH ROUTE'


def check_all_routes_util(graph, initial, ending, path, all_paths, first=False):
    """
    Search the number of trips starting at a starting node
    and ending at a node using  Depth First Traversal algorithm

    Input:
    graph (Graph)
    initial (str)
    ending (str)
    path (list(str))
    all_path (list(list(str)))
    first (bool)

    Output (list(list(str))): all routes
    """
    path.append(initial)

    if initial == ending and not first:
        all_paths.append(path.copy())
    else:
        for node in graph.edges[initial]:
            all_paths = check_all_routes_util(
                graph,
                node,
                ending,
                path,
                all_paths
            )

    path.pop()

    return all_paths


def shortest_route(graph, initial, ending):
    """
    Find the shortest route distance using dijkstra algorithm

    Input:
    graph (Graph)
    initial (str): initial node
    ending (str): last node

    Output (int): shortest trip
    """
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            weight = current_weight + graph.get_distance(min_node, edge)
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node
            elif edge == initial and visited[edge] == 0:
                visited[edge] = weight
                path[edge] = min_node
    if ending in visited:
        return visited[ending]
    else:
        return 'NO SUCH ROUTE'


def different_routes_less_a_distance(graph, initial, ending, max_distance):
    """
    Search the number of trips starting a node
    and ending at a node with distance smaller a max_distance

    Input:
    graph (Graph)
    initial (str)
    ending (str)
    max_distance (int)

    Output (int): number of routes
    """
    path = []
    all_paths = []
    routs = check_all_routes_util(
        graph,
        initial,
        ending,
        path,
        all_paths,
        first=True
    )

    routs_with_distances = {}

    for node in routs:
        routs_with_distances[check_route(graph, '-'.join(node))] = node

    aux_list = list(routs_with_distances.values())
    aux = True
    while aux:
        aux = False
        new_routes = {}
        for node_i_key, node_i_value in routs_with_distances.items():
            for node_j_key, node_j_value in routs_with_distances.items():
                if node_i_key + node_j_key <= max_distance and not list(node_i_value) + list(node_j_value)[1:] in aux_list:
                    new_routes[node_i_key + node_j_key] = list(node_i_value) + list(node_j_value)[1:]
                    aux_list.append(list(node_i_value) + list(node_j_value)[1:])
                    aux = True
        routs_with_distances.update(new_routes)

    if len(routs_with_distances):
        return len(routs_with_distances)
    else:
        return 'NO SUCH ROUTE'
