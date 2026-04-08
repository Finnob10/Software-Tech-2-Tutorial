from graph import Graph
import time
import random

def benchmark_graph_operations(num_vertices, num_edges):
    g = Graph()

    start_time = time.time()
    for i in range(num_vertices):
        g.add_vertex(str(i))
    vertex_time = time.time()
    print(f"Added {num_vertices} vertices in {vertex_time - start_time:.4f} seconds")

    edges_added = 0
    for _ in range(num_edges):
        v1 = str(random.randint(0, num_vertices - 1))
        v2 = str(random.randint(0, num_vertices - 1))
        if v1 != v2:
            g.add_edge(v1, v2)
            edges_added += 1
    edge_time = time.time()
    print(f"Added {edges_added} edges in {edge_time - vertex_time:.4f} seconds")

    if '0' in g.adjacency_list:
        bfs_start = time.time()
        g.bfs('0')
        bfs_time = time.time()
        print(f"\nBFS completed in {bfs_time - bfs_start:.4f} seconds")
    else:
        print("Vertex '0' not found for BFS") 

    if '0' in g.adjacency_list:
        dfs_start = time.time()
        g.dfs('0')
        dfs_time = time.time()
        print(f"\nDFS completed in {dfs_time - dfs_start:.4f} seconds")
    else:
        print("Vertex '0' not found for DFS")

if __name__ == "__main__":
    benchmark_graph_operations(num_vertices=2000, num_edges=2000)