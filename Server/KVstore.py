# Key-Value database get, put and delete implementation
# @author: Gaurav Yeole <gauravyeole@gmail.com>
from Server.DataBaseAbstract import DataBaseAbstract


class KVstore(DataBaseAbstract):

    def __init__(self):
        self.kvstore = dict()

    def reset_storage(self):
        self.kvstore = dict()

    def put(self, key, value):
        self.kvstore[key] = value
        if self.kvstore[key] is None:
            return False
        return True

    def get(self, key):
        return self.kvstore[key]

    def delete(self, key):
        removed_val = self.kvstore.pop(key, None)
        if removed_val is None:
            return False
        return True
