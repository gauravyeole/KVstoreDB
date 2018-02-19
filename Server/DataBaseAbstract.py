# DataBase Interface class
# @author: Gaurav Yeole <gauravyeole@gmail.com>

from abc import ABCMeta, abstractmethod


class DataBaseAbstract(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def put(self, key, value):
        pass

    @abstractmethod
    def get(self, key):
        pass

    @abstractmethod
    def delete(self, key):
        pass
