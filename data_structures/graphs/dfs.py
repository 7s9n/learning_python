from typing import Dict , List , Set , Any

class Graph:
    def __init__(self) ->None:
        self.vertices: Dict[Any , List[Any]] = {}

    def add_edge(self , from_vertex: Any , to_vertex: Any) -> bool:
        if from_vertex == None or to_vertex == None:
            raise ValueError('None is invalid arguments')

        if not to_vertex in self.vertices:
            self.vertices[to_vertex] = []

        if from_vertex not in self.vertices:
            self.vertices[from_vertex] = []

        if not self.__edge_exist(from_vertex , to_vertex):
            self.vertices[from_vertex].append(to_vertex)
            return True

        return False


    def __edge_exist(self , v: Any , u: Any) -> bool:
        adjacent_vertices = self.vertices.get(v)

        if u in adjacent_vertices:
            return True

        return False

    def dfs(self , start):
        if not start in self.vertices:
            raise IndexError(f"{start} doesn't exist in the graph")
        # initialize set for storing already visited vertices
        visited = set()

        #create sack last in first out (LIFO)
        stack = [start]

        traversal_list = []
        while stack:
            vertex = stack.pop()
            visited.add(vertex)
            traversal_list.append(vertex)
            # Differences from BFS:
            # 1) pop last element instead of first one
            # 2) add adjacent elements to stack without exploring them
            for adjacent_vertex in self.vertices[vertex]:
                if adjacent_vertex not in visited:
                    stack.append(adjacent_vertex)
        return traversal_list

def main():
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print(g.dfs(1))
if __name__ == '__main__':
    main()
