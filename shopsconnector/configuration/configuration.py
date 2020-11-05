"""
    This module is to provide setting the new config file.
"""

# TODO: Finish commenting
# TODO: Think about renaming the scripts.
# TODO: Parametric test.

from abc import ABCMeta,abstractmethod


class _SetWebAreal(metaclass=ABCMeta):
    """
        This class is blue print for setting the all needed configs.
    """

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'reset_config') and
                hasattr(subclass, 'input_cnf') and
                hasattr(subclass, 'output_cnf')  or
                NotImplemented
                )

    @abstractmethod
    def __init__(self, input_cnf, output_cnf):
        self.__input_cnf = input_cnf
        self.__output_cnf = output_cnf

    @abstractmethod
    def reset_config(self):
        pass

    @property
    @abstractmethod
    def input_cnf(self):
        return self.__input_cnf

    @input_cnf.setter
    @abstractmethod
    def input_cnf(self, path):
        self.__input_cnf = path

    @property
    @abstractmethod
    def output_cnf(self):
        return self.__output_cnf

    @output_cnf.setter
    @abstractmethod
    def output_cnf(self, path):
        self.__output_cnf = path


class SetWebAreal(_SetWebAreal):

    def __init__(self):
        self.__input_cnf = None
        self.__output_cnf = None

    def reset_config(self):
        from shopsconnector.connector.connector import ConnectionManager
        pass
        # TODO: Finish calling the website and save it ot the file.


    @property
    def input_cnf(self):
        if self.input_cnf is None:
            raise ValueError("Path to input config was not set!")
        return self.__input_cnf

    @input_cnf.setter
    def input_cnf(self, path):
        from os.path import isfile
        if isfile(path) and isinstance(path, str):
            self.__input_cnf = path
        raise FileNotFoundError("The file at {} was not found!".format(path))

    @property
    def output_cnf(self):
        if self.input_cnf is None:
            raise ValueError("Path to output config was not set!")
        return self.__output_cnf

    @output_cnf.setter
    def output_cnf(self, path):
        if isinstance(path, str):
            self.__output_cnf = path
        raise TypeError("Wrong type of path - Not a string")


if __name__ == '__main__':
    pass