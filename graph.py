"""Graph module."""

import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    """Graph."""

    def __init__(
        self,
    ):
        self.graph = nx.DiGraph()
        self.pos = {}
        self.node_types = {}
        self.custom_labels = {}
        self.color_map = {
            "source": "skyblue",
            "sink": "blue",
            "target": "green",
        }
        self.node_colors = []

    def set_positions(self, position_map):
        """Set positions."""
        self.pos = position_map

    def set_node_types(self, node_types):
        """Set node types."""
        self.node_types = node_types

    def set_color_map(self, color_map):
        """Set color map."""
        self.color_map = color_map

    def set_node_colors(self):
        """Set node colors."""
        self.node_colors = [
            self.color_map[self.node_types[node]] for node in self.graph.nodes()
        ]

    def add_edges(self, edges: list[tuple[int, int, int]]):
        """Add edges."""
        self.graph.add_weighted_edges_from(edges)

    def set_nodes_config(
        self,
        node_types: dict[int, str],
        node_labels: dict[int, str],
        position_map: dict[int, tuple[int, int]],
    ):
        """
        Set nodes config, for drawing graph.
        Set node types, colors, labels and positions.

        Args:
            node_types: dict[int, str]
            node_labels: dict[int, str]
            position_map: dict[int, tuple[int, int]]

        """
        self.set_node_types(node_types)
        self.set_node_colors()
        self.set_custom_labels(node_labels)
        self.set_positions(position_map)

    def set_custom_labels(self, labels):
        """Set custom labels."""
        self.custom_labels = labels

    def draw(self):
        """Draw graph."""
        plt.figure(figsize=(10, 6))
        nx.draw(
            G=self.graph,
            pos=self.pos,
            labels=self.custom_labels,  # <- custom labels here
            with_labels=True,
            node_size=2000,
            node_color=self.node_colors,
            font_size=12,
            font_weight="bold",
            arrows=True,
        )
        labels = nx.get_edge_attributes(self.graph, "weight")
        nx.draw_networkx_edge_labels(self.graph, self.pos, edge_labels=labels)
        plt.show()


if __name__ == "__main__":
    edges_ = [
        (0, 2, 15),  # Джерело 1 -> Проміжний Вузол 1
        (0, 3, 10),  # Джерело 1 -> Проміжний Вузол 2
        (1, 2, 20),  # Джерело 2 -> Проміжний Вузол 1
        (2, 4, 10),  # Проміжний Вузол 1 -> Споживач 1
        (2, 5, 5),  # Проміжний Вузол 1 -> Споживач 2
        (3, 6, 15),  # Проміжний Вузол 2 -> Споживач 3
    ]
    g = Graph()
    g.add_edges(edges_)
    g.draw()
    # capacity_matrix = [
#     [0, 0, 15, 10, 0, 0, 0],  # Джерело 1
#     [0, 0, 20, 0, 0, 0, 0],  # Джерело 2
#     [0, 0, 0, 0, 10, 5, 0],  # Проміжний Вузол 1
#     [0, 0, 0, 0, 0, 0, 15],  # Проміжний Вузол 2
#     [0, 0, 0, 0, 0, 0, 0],  # Споживач 1
#     [0, 0, 0, 0, 0, 0, 0],  # Споживач 2
#     [0, 0, 0, 0, 0, 0, 0],  # Споживач 3
# ]

# source = 1  # Джерело 1
# sink = 5  # Споживач 3

# print(
#     f"Максимальний потік Джерело 1-->Споживач 3: {edmonds_karp(capacity_matrix, source, sink)}"
# )
