"""
Helper functions
"""

from typing import Callable
import csv
import json


def load_data_from_csv(
    filepath: str, fn: Callable[[dict[str, str]], dict[str, str]]
) -> list[dict[str, str]]:
    """
    Load data from CSV file.

    Args:
        filepath: path to CSV file
        fn: function to parse row
    Returns:
        list of parsed rows
    """
    data = []
    with open(filepath, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(fn(row))
    return data


def load_pos_from_json(filepath: str) -> dict[str, tuple[int, int]]:
    """
    Load node positions from JSON file.

    Args:
        filepath: path to JSON file
    Returns:
        dict of nodes positions
    """
    pos = {}
    with open(filepath, "r", encoding="utf-8") as jsonfile:
        pos = json.load(jsonfile)

    positions = {int(k): tuple(v) for k, v in pos.items()}

    return positions
