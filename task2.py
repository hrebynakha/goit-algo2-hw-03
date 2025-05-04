"""
Task 2.
Розробіть програму для зберігання великого набору даних про товари
у двох структурах даних — OOBTree та dict —
і проведіть порівняльний аналіз їхньої продуктивності
для виконання діапазонних запитів.

"""

from timeit import timeit
from BTrees.OOBTree import OOBTree
from helpers import load_data_from_csv


def parse_items(row: dict) -> dict:
    """Parse item ID,Name,Category,Price from CSV row."""
    return {
        "id": int(row["ID"]),
        "name": row["Name"],
        "category": row["Category"],
        "price": float(row["Price"]),
    }


class SimpleOOBTree:
    """OOBTree."""

    def __init__(self, data: list[dict]) -> None:
        self.tree = OOBTree()
        self.load_data_into_tree(data)

    def load_data_into_tree(self, data: list[dict]) -> None:
        """Load data into tree."""
        for item in data:
            self.add_item_to_tree(item)

    def add_item_to_tree(self, item: dict) -> None:
        """Add item to tree."""
        self.tree[item["price"], item["id"]] = item

    def range_qurey_tree(self, start_price: float, end_price: float) -> list[dict]:
        """Range query tree."""
        return list(
            self.tree.items(min=(start_price, 0), max=(end_price, len(self.tree)))
        )


class SimpleDict:
    """Simple dict."""

    def __init__(self, data: list[dict]) -> None:
        self.dict = {}
        self.load_data_into_dict(data)

    def load_data_into_dict(self, data: list[dict]) -> dict:
        """Load data into dict."""
        for item in data:
            self.add_item_to_dict(item)

    def add_item_to_dict(self, item: dict) -> None:
        """Add item to dict."""
        self.dict[item["id"]] = item

    def range_qurey_dict(self, start_price: float, end_price: float) -> list[dict]:
        """Range query dict."""
        result = []
        for item in self.dict.values():
            if start_price <= item["price"] <= end_price:
                result.append(item)
        return result


def main() -> None:
    """Main function."""
    data = load_data_from_csv(
        "data/generated_items_data.csv",
        parse_items,
    )
    oobtree = SimpleOOBTree(data)
    simple_dict = SimpleDict(data)
    run_test(oobtree, simple_dict, 0, 100)
    run_test(oobtree, simple_dict, 123.45, 223.45)


def run_test(
    oobtree: SimpleOOBTree,
    simple_dict: SimpleDict,
    start: int,
    end: int,
    count: int = 100,
) -> None:
    """Run test function."""
    elapsed_time_oobtree = timeit(
        lambda: oobtree.range_qurey_tree(start, end), number=count
    )
    elapsed_time_dict = timeit(
        lambda: simple_dict.range_qurey_dict(start, end), number=count
    )
    print(f"Total range_query time for OOBTree: {elapsed_time_oobtree} seconds")
    print(f"Total range_query time for Dict: {elapsed_time_dict} seconds")


if __name__ == "__main__":
    main()
