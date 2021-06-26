from typing import Dict , List, Set , Any

graph: Dict[int , List[int]] = {
1:[2 , 3 , 4],
2:[4 , 1],
3:[4],
4:[4] ,#loop
5:[6 , 1],
6:[5]
}

def dfs(graph , vertex , visited: list[Any] = None) ->List[Any]:
    visited.append(vertex)
    adjacent_vertices = graph.get(vertex)

    if adjacent_vertices:
        for adjacent_vertex in adjacent_vertices:
            if adjacent_vertex not in visited:
                dfs(graph , adjacent_vertex , visited)

    return visited

def count_components(graph: Dict[Any , List[Any]]) -> int:
    marked_vertices: Set[Any] = set()
    cnt = 0
    for vertex in graph:
        if vertex not in marked_vertices:
            marked_vertices.update( dfs(graph , vertex , []) )
            cnt += 1
    return cnt

if __name__ == '__main__':
    print( count_components(graph) )
