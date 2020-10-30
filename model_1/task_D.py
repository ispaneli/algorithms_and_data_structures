import sys
import bisect
from collections import deque


class Graph:
    def __init__(self, graph_type, start_vertex, search_type):
        self._graph_type = graph_type
        self._start_vertex = start_vertex
        self._search_type = search_type
        self._pairs_of_vertex = dict()

    def append(self, start_vertex, end_vertex):
        if start_vertex in self._pairs_of_vertex:
            bisect.insort(self._pairs_of_vertex[start_vertex], end_vertex)
        else:
            self._pairs_of_vertex[start_vertex] = [end_vertex]

        if self._graph_type == "u":
            if end_vertex in self._pairs_of_vertex:
                bisect.insort(self._pairs_of_vertex[end_vertex], start_vertex)
            else:
                self._pairs_of_vertex[end_vertex] = [start_vertex]

    def start_search(self):
        if self._search_type == "b":
            self._breadth_first_search()
        elif self._search_type == "d":
            passed_vertices = set()
            self._depth_first_search(self._start_vertex, passed_vertices)

    def _depth_first_search(self, positional_vertex, passed_vertices):
        print(positional_vertex)
        passed_vertices.add(positional_vertex)

        if positional_vertex in self._pairs_of_vertex:
            for end_vertex in self._pairs_of_vertex[positional_vertex]:
                if end_vertex not in passed_vertices:
                    self._depth_first_search(end_vertex, passed_vertices)

    def _breadth_first_search(self):
        passed_vertices = {self._start_vertex}
        search_deque = deque([self._start_vertex])

        while search_deque:
            vertex = search_deque.popleft()
            print(vertex)

            if vertex in self._pairs_of_vertex:
                for next_vertex in self._pairs_of_vertex[vertex]:
                    if next_vertex not in passed_vertices:
                        passed_vertices.add(next_vertex)
                        search_deque.append(next_vertex)


if __name__ == "__main__":
    sys.setrecursionlimit(20000)
    input_commands = [cmd.replace("\n", "").split(" ") for cmd in sys.stdin.readlines()]
    graph = Graph(input_commands[0][0], input_commands[0][1], input_commands[0][2])

    for cmd in input_commands[1:]:
        if len(cmd) == 2:
            graph.append(cmd[0], cmd[1])
    graph.start_search()
