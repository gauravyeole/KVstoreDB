# Key-Value database get, put and delete implementation
# @author: Gaurav Yeole <gauravyeole@gmail.com>

import shelve
import os

from multiprocessing import Lock

from Server.DataBaseAbstract import DataBaseAbstract


class KVstore(DataBaseAbstract):

    def __init__(self):
        self.kvstore = dict()
        self.locks = dict()
        # dictionary of locks indexed by key

    def __str__(self):
        return str(self.kvstore)

    def reset_storage(self):
        self.kvstore = dict()

    def put(self, key, value):
        if key not in self.locks:
            self.locks = Lock()
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
        print("restore before if: " + str(self))
        if ckpfile + ".db" in os.listdir():
            self.kvstore = dict()
            print("restore should be clean: "+ str(self))
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

    def aquire(self, key):
        try:
            lock = self.locks[key]
            lock.aquire()
            return True
        except KeyError:
            print("Can not aquire lock for key: " + str(key))
            return False

    def release(self, key):
        try:
            lock = self.locks[key]
            lock.release()
            return True
        except KeyError:
            print("Can not release lock for key: " + str(key))
            return False