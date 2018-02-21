# Base Inode class to represent the files and directories stored in the database
# @author: Gaurav Yeole <gauravyeole@gmail.com>

import datetime

from Client import config

MAX_BLK_SIZE = config.MAX_BLK_SIZE

class Inode():

    def __init__(self):
        self.time_created = datetime.now()
        self.time_accessed = datetime.now()
        self.time_modified = datetime.now()
        # self.path = path
        self.blk_numbers = dict() # dictionaty indexed by index of blk of data and mapping to blk_number
        self.size = 0
        self.no_links = 2
        self.type = 0 # 0 - file, and 1 - directory
        self.directory = dict() # directory is dictionary indexed by file name and mapping to inode number

    # Returns the block number of the indexth block of file
    def index_to_block_number(self, index):
        return self.blk_numbers.pop(index, None)

    # Returns the blk_number from offset
    def offset_to_blk_num(self, offset):
        index = offset/MAX_BLK_SIZE
        blk_num = self.index_to_block_number(index)
        return blk_num







