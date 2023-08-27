"""General purpose functions. Most probably for methods_functions simplifying.

Сделать чтение с помощью либы oc и проверить будет ли метод работать если его импортировать в файл из хрен знает откуда
"""
import json

from src.data_types import StorePositions


def read_default_positions() -> StorePositions:
    """
    Read default store positions.

    :returns: Validated via StorePositions class default store positions
    """
    with open("/home/alexnazarv/Desktop/repos_private/training-project-api/src/data/default.json") as default:
        default_positions = json.load(default)

    return StorePositions(**default_positions)
