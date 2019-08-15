"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        # Add a vertex to the graph.
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        # Add a directed edge to the graph.
        self.vertices[v1].add(v2)

    def bft(self, starting_vertex):
        # Print each vertex in breadth-first order beginning from starting_vertex.
        breadth = Queue()
        visited = []
        breadth.enqueue(starting_vertex)

        while breadth.size():
            node = breadth.dequeue()
            visited.append(node)

            for vertex in self.vertices[node]:
                if vertex not in visited and vertex not in breadth.queue:
                    breadth.enqueue(vertex)

        print(visited)

    def dft(self, starting_vertex):
        # Print each vertex in depth-first order beginning from starting_vertex.
        depth = Stack()
        visited = []
        depth.push(starting_vertex)

        while depth.size():
            node = depth.pop()
            visited.append(node)

            for vertex in self.vertices[node]:
                if vertex not in visited and vertex not in depth.stack:
                    depth.push(vertex)

        print(visited)

    def dft_recursive(self, starting_vertex, visited=list()):
        # Print each vertex in depth-first order beginning from starting_vertex. This should be done using recursion.
        if starting_vertex in visited:
            print(visited)
            return visited

        else:
            visited.append(starting_vertex)
            for neighbor in self.vertices[starting_vertex]:
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):

        # Return a list containing the shortest path from
        # starting_vertex to destination_vertex in
        # breath-first order.

        breadth = Queue()
        visited = []
        breadth.enqueue([starting_vertex])
        while breadth.size():

            path = breadth.dequeue()
            node = path[-1]

            if node not in visited:
                visited.append(node)
                if node == destination_vertex:
                    print(visited)
                    return path

                for neighbor in self.vertices[node]:
                    copy_path = path[:]
                    copy_path.append(neighbor)
                    breadth.enqueue(copy_path)

        print(visited)

    def dfs(self, starting_vertex, destination_vertex):

        # Return a list containing a path from
        # starting_vertex to destination_vertex in
        # depth-first order.

        depth = Stack()
        visited = []
        depth.push([starting_vertex])
        while depth.size():
            path = depth.pop()
            node = path[-1]

            if node not in visited:
                visited.append(node)

                if node == destination_vertex:
                    return path

                for neighbor in self.vertices[node]:
                    new_path = path[:]
                    new_path.append(neighbor)
                    depth.push(new_path)


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
