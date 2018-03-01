# Base Inode class to represent the files and directories stored in the database
# @author: Gaurav Yeole <gauravyeole@gmail.com>

import datetime

from Client import config

MAX_BLK_SIZE = config.MAX_BLK_SIZE

class Inode():

    def __init__(self, type):
        self.time_created = datetime.datetime.now()
        self.time_accessed = datetime.datetime.now()
        self.time_modified = datetime.datetime.now()
        self.blk_numbers = dict() # list of block numbers of data
        self.size = 0
        self.no_links = 2
        self.type = type # 0 - file, and 1 - directory
        self.directory = dict()
        # directory is dictionary indexed by file name and mapping to inode number

    def __str__(self):
        return "Type: " + str(self.type) + ", children: " + \
               str(self.directory) + ", size: " + str(self.size) \
               + ", block numbers: " + str(self.blk_numbers) + \
               ", links: " + str(self.no_links) + ", time created: " \
               + str(self.time_created)

    # Returns the block number of the indexth block of file
    def index_to_block_number(self, index):
        try:
            return self.blk_numbers[int(index)]
        except KeyError:
            print("Index " + str(index) + "does not exixst")
            return -1

    # Returns the blk_number from offset
    def offset_to_blk_num(self, offset):
        index = int(offset/MAX_BLK_SIZE)
        blk_num = self.index_to_block_number(index)
        return blk_num

    # Returns true if child is sucessfully added
    def add_child(self, filename, inode_number):
        self.time_modified = datetime.datetime.now()
        self.time_accessed = datetime.datetime.now()
        if filename in self.directory:
            print("File/Directory already Exists!!!")
            return False
        self.directory[filename] = inode_number
        return True

    def remove_child(self, filename):
        self.time_modified = datetime.datetime.now()
        self.time_accessed = datetime.datetime.now()
        if filename not in self.directory:
            print("File/Directory does not exist")
            return False
        self.directory.pop(filename)
        return True

    def update_blk_number(self, blk_index, blk_number):
        self.time_modified = datetime.datetime.now()
        self.time_accessed = datetime.datetime.now()
        self.blk_numbers[blk_index] = blk_number

    def get_attributes(self):
        attr = {"type": self.type, "children" : self.directory,
                "size" : self.size, "block_numbers" : self.blk_numbers,
                "links" : self.no_links, "time_created" : self.time_created,
                "time_accessed" : self.time_accessed,
                "time_modified" : self.time_modified}
        return attr

    def get_children(self):
        self.time_accessed = datetime.datetime.now()
        return self.directory