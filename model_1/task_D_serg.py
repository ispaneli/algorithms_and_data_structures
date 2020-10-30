import collections
import sys
import bisect

sys.setrecursionlimit(3000)


def breadth_first_search(graph, start):
    visited = set()
    queue = collections.deque([start])
    visited.add(start)
    while queue:
        vertex = queue.popleft()
        print(vertex)
        if vertex in graph:
            for neighbour in graph[vertex]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)


def start_dfs(graph, vertex):
    visited = set()
    depth_first_search(graph, vertex, visited)


def depth_first_search(graph, vertex, visited):
    visited.add(vertex)
    print(vertex)
    if vertex in graph:
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                depth_first_search(graph, neighbour, visited)


def make_graph():
    graph = {}

    graph_params = input().split()
    graph_type = graph_params[0]
    start_vertex = graph_params[1]
    type_search = graph_params[2]

    for line in sys.stdin:
        vertex = line.split()
        if len(vertex) != 2:
            continue
        if vertex[0] in graph:
            bisect.insort(graph[vertex[0]], vertex[1])
        else:
            graph[vertex[0]] = [vertex[1]]

        if graph_type == 'u':
            if vertex[1] in graph:
                bisect.insort(graph[vertex[1]], vertex[0])
            else:
                graph[vertex[1]] = [vertex[0]]

    return graph, start_vertex, type_search


if __name__ == '__main__':
    g, v, s_type = make_graph()

    if s_type == 'b':
        breadth_first_search(g, v)
    else:
        start_dfs(g, v)