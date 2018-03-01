# Block-layer of the file system
# @author: Gaurav Yeole <gauravyeole@gmail.com>
import pickle
from xmlrpc.client import Binary

from Client import config
from Client.ClientInterface import KVstore
from Client.Inode import Inode

MAX_NUM_INODES = config.MAX_NUM_INODES
MAX_BLK_SIZE = config.MAX_BLK_SIZE
NUM_OF_BLKS = config.NUM_OF_BLKS

class BlockLayer:

    def __init__(self):
        self.disk = KVstore()
        # self.valid_blks = dict()
        self.number_of_blks = NUM_OF_BLKS
        self.valid_blks = dict()
        try:
            self.valid_blks = pickle.loads(self.disk.get("valid_blks").data)
        except:
            for i in range(0, self.number_of_blks):
                self.disk.put(i, None)
                self.valid_blks[i] = 0
            # 0 - blk does not contains valid data
            # 1 - blk contains valid data
        self.disk.put("valid_blks", Binary(pickle.dumps(self.valid_blks)))
        print("Block Layer Initialised")

    def __str__(self):
        string = ""
        for i in range(0, self.number_of_blks):
            string = string  + str(i) + ": "  + \
                     str(self.disk.get(i)) + "; "
        return "Blocks: " + string

    def import_inode_table(self):
        try:
            return pickle.loads(self.disk.get("inode_table").data)
        except:
            print("Error in importing inode table")
            return None

    def export_inode_table(self, inode_table):
        self.disk.put("inode_table", Binary(pickle.dumps(inode_table)))

    def import_valid_blk(self):
        try:
            self.valid_blks = pickle.loads(self.disk.get("valid_blks").data)
            return True
        except:
            print("Error in importing the SuperBlock")
            return False

    def export_valid_blk(self):
        self.disk.put("valid_blks", Binary(pickle.dumps(self.valid_blks)))

    def blk_number_to_data(self, blk_number):
        return self.disk.get(blk_number)

    # returns block number where data is stored
    def store_data(self, data):
        for i in range(0, self.number_of_blks):
            if self.valid_blks[i] is 0:
                self.disk.put(i, data)
                self.validate_blk(i)
                return i
        print("Disk Full!! No free blocks available to store data")
        return -1

    def is_blk_valid(self, blk_number):
        return self.valid_blks[i]

    def invalid_blk(self, blk_number):
        self.valid_blks[blk_number] = 0

    def validate_blk(self, blk_number):
        self.valid_blks[blk_number] = 1

    def checkpoint(self, ckpfile):
        return self.disk.checkpoint(ckpfile)

    def restore(self, ckpfile):
        return self.disk.restore(ckpfile)
