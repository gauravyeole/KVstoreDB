# Key-Value database get, put and delete implementation
# @author: Gaurav Yeole <gauravyeole@gmail.com>
import shelve

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

    def count(self):
        return len(self.kvstore)

    def checkpoint(self, ckpfile):
        persistent_file = shelve.open(ckpfile)
        try:
            persistent_file["kvstore"] = self.kvstore
            print("checkpoint: " + ckpfile + " created")
        except:
            print("Checkpoint cannot be created! ")
            return -1
        finally:
            persistent_file.close()
        return 0

    def restore(self, ckpfile):
        persistent_file = shelve.open(ckpfile)
        try:
            self.kvstore = persistent_file["kvstore"]
            print("checkpoint: " + ckpfile + " restored")
        except:
            print("checkpoint: " + ckpfile + " not found!")
            return -1
        finally:
            persistent_file.close()
        return 0

