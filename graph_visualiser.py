from graph import Graph
import tkinter as tk
import math

class GraphVisualizer(tk.Tk):
    def __init__(self, graph):
        super().__init__()
        self.title("Graph Visualizer")
        self.graph = graph
        self.canvas = tk.Canvas(self, width=400, height=400, bg='white')
        self.canvas.pack()
        self.vertex_positions = {}
        self.draw_graph()

    def draw_graph(self):
        self.canvas.delete("all")
        radius = 20
        spacing = 100

        # Arrange vertices in a circle
        n = len(self.graph.adjacency_list)
        angle_gap = 360 / n if n else 0
        center_x, center_y = 200, 200

        for i, v in enumerate(self.graph.adjacency_list):
            angle = i * angle_gap
            x = center_x + spacing * math.cos(math.radians(angle))
            y = center_y + spacing * math.sin(math.radians(angle))
            self.vertex_positions[v] = (x, y)
            self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill='lightblue')
            self.canvas.create_text(x, y, text=v)

        # Draw edges
        for v in self.graph.adjacency_list:
            x1, y1 = self.vertex_positions[v]
            for neighbor in self.graph.adjacency_list[v]:
                actual = neighbor[0] if self.graph.weighted else neighbor
                x2, y2 = self.vertex_positions[actual]
                self.canvas.create_line(x1, y1, x2, y2, arrow=tk.LAST if self.graph.directed else None)
                if self.graph.weighted:
                    w = neighbor[1]
                    mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
                    self.canvas.create_text(mid_x, mid_y, text=str(w), fill="red")

if __name__ == "__main__":
    g = Graph(directed=True, weighted=True)
    g.add_vertex('A')
    g.add_vertex('B')
    g.add_vertex('C')
    g.add_edge('A', 'B', 10)
    g.add_edge('B', 'C', 20)
    g.add_edge('C', 'A', 30)
    app = GraphVisualizer(g)
    app.mainloop()

