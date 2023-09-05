"""General purpose functions. Most probably for methods_functions simplifying."""
import json
from pathlib import Path

PATH_SRC = str(Path(__file__).parents[1])
PATH_DATA_FOLDER = '{path_src}/data'.format(path_src=PATH_SRC)


def path_to_file(file_name: str) -> str:
    """
    Return path to file to be read.

    :param file_name: name of file with extension
    :returns: path to file
    """
    return '{path_data_folder}/{file_name}'.format(
        path_data_folder=PATH_DATA_FOLDER,
        file_name=file_name,
    )


def read_json_to_dict(file_name: str) -> dict:
    """
    Read default store positions.

    :param file_name: name of file with extension
    :returns: Validated via StorePositions class default store positions
    """
    file_path = path_to_file(file_name=file_name)
    with open(file_path) as file_object:
        dict_object = json.load(file_object)

    return dict_object


def read_txt_to_list(file_name: str) -> list:
    """
    Read default products substrs.

    :param file_name: name of file with extension
    :returns: List of substrs
    """
    file_path = path_to_file(file_name=file_name)
    with open(file_path) as file_object:
        list_object = file_object.read().split('\n')

    return list(filter(None, list_object))
