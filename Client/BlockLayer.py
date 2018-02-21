# Block-layer of the file system
# @author: Gaurav Yeole <gauravyeole@gmail.com>

from Server.KVstore import KVstore

class BlockLayer:

    def __init__(self,  number_of_blks):
        self.disk = KVstore()
        for i in range(0,number_of_blks):
            self.disk.put(i, None)


    def blk_number_to_data(self, blk_number):
        return self.disk.get(blk_number)

    def store_data(self, blk_number, data):
        return self.disk.put(blk_number, data)
