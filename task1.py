"""
Task 1.

Розробіть програму для моделювання мережі потоків
для логістики товарів зі складів до магазинів,
використовуючи алгоритм максимального потоку.
Проведіть аналіз отриманих результатів
і порівняйте їх з теоретичними знаннями.

"""

from helpers import load_data_from_csv
from graph import Graph


def parse_connection(row: dict) -> dict:
    """Parse connection from CSV row."""
    return {
        "from": row["From"],
        "to": row["To"],
        "capacity": int(row["Capacity"]),
    }


class LogisticsNetwork(Graph):
    """Logistics network."""

    def __init__(
        self,
        connections: list[dict],
        source_name: str,
        sink_name: str,
        target_name: str,
    ) -> None:
        super().__init__()
        self.connections = connections
        self.source = self.get_source_map(source_name)
        self.sink = self.get_sink_map(sink_name)
        self.target = self.get_target_map(target_name)
        self.map = {
            **self.source,
            **self.sink,
            **self.target,
        }
        self.ids = self.get_ids()

    def get_ids(self) -> dict[str, int]:
        """Get ids."""
        ids, id_ = {}, 0
        for node in self.map:
            ids[node] = id_
            id_ += 1
        return ids

    def get_edges(self) -> list[tuple[int, int, int]]:
        """Get edges."""
        edges = []
        for connection in self.connections:
            edges.append(
                (
                    self.ids[connection["from"]],
                    self.ids[connection["to"]],
                    connection["capacity"],
                )
            )
        return edges

    def get_map(self, filter_="", key="") -> dict[str, int]:
        """Get map of nodes."""
        source_ids, i = {}, 0
        for connection in self.connections:
            source = connection[key]
            if filter_ in source and source not in source_ids:
                source_ids[source] = i
                i += 1
        return source_ids

    def get_source_map(self, name: str) -> dict[str, int]:
        """Get map of sources."""
        return self.get_map(name, "from")

    def get_sink_map(self, name: str) -> dict[str, int]:
        """Get map of sinks."""
        return self.get_map(name, "to")

    def get_target_map(self, name: str) -> dict[str, int]:
        """Get map of targets."""
        return self.get_map(name, "to")

    def get_nodes_config(
        self,
    ) -> tuple[dict[int, str], dict[int, str], dict[int, tuple[int, int]]]:
        """Get nodes config."""
        node_types, node_labels, pos, i, x, prev_y = {}, {}, {}, 0, 0, None

        def _get_y(node_type):
            return {"source": 2, "sink": 1, "target": 0}.get(node_type, -1)

        def _get_type(node):
            if node in self.source:
                return "source"
            if node in self.sink:
                return "sink"
            if node in self.target:
                return "target"
            return "node"

        for node in self.map:
            node_type = _get_type(node)
            y = _get_y(node_type)
            x = 0 if prev_y != y else x + 1
            node_types[i], node_labels[i], pos[i] = node_type, node, (x, y)
            i, prev_y = i + 1, y
        return node_types, node_labels, pos


conn = load_data_from_csv("data/task1.csv", parse_connection)
ln = LogisticsNetwork(conn, "Термінал", "Склад", "Магазин")
ln.add_edges(ln.get_edges())
ln.set_nodes_config(*ln.get_nodes_config())
ln.draw()
