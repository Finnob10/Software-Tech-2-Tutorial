from collections import deque 

class Graph:
    def __init__(self, directed=False, weighted=False):
        self.adjacency_list = {}
        self.directed = directed
        self.weighted = weighted

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, v1, v2, weight=None):
        edge = (v2, weight) if self.weighted else v2
        self.adjacency_list[v1].append(edge)
        if not self.directed:
            reverse_edge = (v1, weight) if self.weighted else v1
            self.adjacency_list[v2].append(reverse_edge)

    def remove_edge(self, v1, v2):
        if v1 in self.adjacency_list:
            self.adjacency_list[v1] = [
                e for e in self.adjacency_list[v1]
                if (e[0] if self.weighted else e) != v2
            ]
        if not self.directed and v2 in self.adjacency_list:
            self.adjacency_list[v2] = [
                e for e in self.adjacency_list[v2]
                if (e[0] if self.weighted else e) != v1
            ]

    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list:
            del self.adjacency_list[vertex]
        for v in self.adjacency_list:
            self.adjacency_list[v] = [
                e for e in self.adjacency_list[v]
                if (e[0] if self.weighted else e) != vertex
            ]

    def print_graph(self):
        for vertex, edges in self.adjacency_list.items():
            if self.weighted:
                edge_str = ", ".join(f"{v}({w})" for v, w in edges)
            else:
                edge_str = ", ".join(edges)
            print(f"{vertex}: [{edge_str}]") 

    def bfs(self, start):
        visited = {start}
        queue = deque([start])

        while queue:
            node = queue.popleft()
            for neighbor in self.adjacency_list[node]:
                actual = neighbor[0] if self.weighted else neighbor
                if actual not in visited:
                    visited.add(actual)
                    queue.append(actual)  
        return(visited)

    
    def dfs(self, node, visited=None):
        if visited is None:
            visited = set()
    
    # Mark the current node as visited
        visited.add(node)

    # Recursively visit all unvisited neighbors
        for neighbor in self.adjacency_list[node]: 
            actual = neighbor[0] if self.weighted else neighbor
            if actual not in visited:
                self.dfs(actual, visited)   
        return(visited)   
    
    def has_undirected_cycle(self):
        visited = set()

        def dfs1(node, parent):
            visited.add(node)

            for neighbor in self.adjacency_list[node]:
                actual = neighbor[0] if self.weighted else neighbor

                if actual not in visited:
                    if dfs1(actual, node):
                        return True
                elif actual != parent:
                    return True

            return False

        for vertex in self.adjacency_list:
            if vertex not in visited:
                    if dfs1(vertex, None):
                        return True

        return False

