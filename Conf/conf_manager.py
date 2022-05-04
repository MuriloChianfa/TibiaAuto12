"""
ConfManager module consists of get and set
confs in json format fot bot
"""

from json import load, dump


class ConfManager:
    """
    Get and Set confs in json file
    """

    def __init__(self):
        pass

    @staticmethod
    def get_conf(file):
        """
        This function loads a json file
        and return your data.
        """

        with open(f'Scripts/{file}', 'r', encoding='UTF-8') as file_descriptor:
            return load(file_descriptor)

    @staticmethod
    def set_conf(data, file):
        """
        This function loads a json file
        and return your data.
        """

        with open(f'Scripts/{file}', 'w', encoding='UTF-8') as file_descriptor:
            dump(data, file_descriptor, indent=2)
