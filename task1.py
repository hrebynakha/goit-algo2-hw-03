"""
Task 1.

Розробіть програму для моделювання мережі потоків
для логістики товарів зі складів до магазинів,
використовуючи алгоритм максимального потоку.
Проведіть аналіз отриманих результатів
і порівняйте їх з теоретичними знаннями.

"""

from helpers import load_data_from_csv, load_pos_from_json
from graph import Graph
from algorithms import edmonds_karp


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
        intermediate_name: str,
        sink_name: str,
        pos: dict[int, tuple[int, int]],
    ) -> None:
        super().__init__()
        self.connections = connections
        self.source = self.get_source_map(source_name)
        self.intermediate = self.get_intermediate_map(intermediate_name)
        self.sink = self.get_sink_map(sink_name)

        self.map = {
            **self.source,
            **self.intermediate,
            **self.sink,
        }
        self.ids = self.get_ids()
        self.set_positions(pos)

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
        source_map, i = {}, 0
        for connection in self.connections:
            source = connection[key]
            if filter_ in source and source not in source_map:
                source_map[source] = i
                i += 1
        return source_map

    def get_ids(self) -> dict[str, int]:
        """Get ids."""
        ids, id_ = {}, 0
        for node in self.map:
            ids[node] = id_
            id_ += 1
        return ids

    def get_source_map(self, name: str) -> dict[str, int]:
        """Get map of sources."""
        return self.get_map(name, "from")

    def get_intermediate_map(self, name: str) -> dict[str, int]:
        """Get map of sinks."""
        return self.get_map(name, "to")

    def get_sink_map(self, name: str) -> dict[str, int]:
        """Get map of targets."""
        return self.get_map(name, "to")

    def get_nodes_config(
        self,
    ) -> tuple[
        dict[int, str],
        dict[int, str],
    ]:
        """Get nodes config."""
        node_types, node_labels, i = {}, {}, 0

        def _get_type(node):
            if node in self.source:
                return "source"
            if node in self.intermediate:
                return "intermediate"
            if node in self.sink:
                return "sink"
            return "node"

        for node in self.map:
            node_type = _get_type(node)
            node_types[i], node_labels[i] = node_type, node
            i += 1

        return node_types, node_labels

    def get_capacity_matrix(self) -> list[list[int]]:
        """Get capacity matrix."""
        size = len(self.ids)
        matrix = [[0] * size for _ in range(size)]
        for connection in self.connections:
            from_idx = self.ids[connection["from"]]
            to_idx = self.ids[connection["to"]]
            matrix[from_idx][to_idx] = connection["capacity"]
        return matrix

    def get_report(self) -> None:
        """
        Get report of maximum flow.
        Print maximum flow for each source and sink.
        """
        capacity_matrix = self.get_capacity_matrix()
        print("source,sink,max_flow")  # header
        counters = {}
        for source in self.source:
            count = 0
            for sink in self.sink:
                max_flow = edmonds_karp(
                    capacity_matrix, self.ids[source], self.ids[sink]
                )
                print(f"{source},{sink},", end="")
                if max_flow > 0:
                    print(f"\033[92m{max_flow}\033[0m", end="")
                else:
                    print(f"\033[91m{max_flow}\033[0m", end="")
                count += max_flow
                print()
            counters[source] = count
        print()
        for source, count in counters.items():
            print(f"Total for {source}: {count}")


def main() -> None:
    """Main function."""
    debug = False

    if debug:
        index, *conf = 0, "Джерело", "Вуз", "Споживач"
    else:
        index, *conf = 1, "Термінал", "Склад", "Магазин"

    conn = load_data_from_csv(f"data/task{index}.csv", parse_connection)
    positions = load_pos_from_json(f"data/pos{index}.json")
    ln = LogisticsNetwork(conn, *conf, positions)
    ln.add_edges(ln.get_edges())
    ln.set_nodes_config(*ln.get_nodes_config())
    ln.draw()
    ln.get_report()


if __name__ == "__main__":
    main()
