# Block-layer of the file system
# @author: Gaurav Yeole <gauravyeole@gmail.com>
from Client.ClientInterface import KVstore


class BlockLayer:

    def __init__(self,  number_of_blks):
        self.disk = KVstore()
        self.valid_blks = dict()
        self.number_of_blks = number_of_blks
        for i in range(0, self.number_of_blks):
            self.disk.put(i, None)
            self.valid_blks[i] = 0
        # 0 - blk does not contains valid data
        # 1 - blk contains valid data

    def __str__(self):
        string = ""
        for i in range(0, self.number_of_blks):
            string = string  + str(i) + ": "  + \
                     str(self.disk.get(i)) + "; "
        return "Blocks: " + string

    def blk_number_to_data(self, blk_number):
        return self.disk.get(blk_number)

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