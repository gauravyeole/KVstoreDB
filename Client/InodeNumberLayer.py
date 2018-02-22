# Inode Number layer implementation creates the inode table
# @author: Gaurav Yeole <gauravyeole@gmail.com>

from Client import config
from Client.BlockLayer import BlockLayer
from Client.Inode import Inode


MAX_NUM_INODES = config.MAX_NUM_INODES
MAX_BLK_SIZE = config.MAX_BLK_SIZE
num_of_blks = config.NUM_OF_BLKS

class InodeNumberLayer:

    # InodeTable contains dictionary of all the inodes indexed by inode numbers and mapping to corresponding inode object
    def __init__(self):
        self.inode_table = dict()
        self.blocks = BlockLayer(num_of_blks)
        for i in range(0, MAX_NUM_INODES):
            self.inode_table[i] = None
        root = Inode()
        root.type = 1
        self.inode_table[0] = root

    def __str__(self):
        string = ""
        for inode in self.inode_table:
            string = string + "[" + str(inode) + ": " + str(self.inode_table[inode]) + "]; "
        return string


    def inode_number_to_inode(self, inode_number):
        return self.inode_table.pop(inode_number, None)

    # returns the the block number (key in database)where offset lies
    def inode_number_to_block(self, offset, inode_number):
        inode = self.inode_number_to_inode(inode_number)
        if inode is not None:
            blk_index = offset/MAX_BLK_SIZE
            blk_number = inode.index_to_blk_number(blk_index)
            return blk_number
        else:
            print("Invalid Offset")
            return -1

    def offset_to_blk_data(self, offset, inode): # inode_to_blk
        blk_num = inode.offset_to_blk_num(offset)
        return self.blocks.blk_number_to_data(blk_num)

    # Adds new entry in inode table and returns inode number upon success
    def add_inode_table_entry(self, inode):
        for i in range(0 , MAX_NUM_INODES):
            if self.inode_table[i] is None:
                self.inode_table[i] = inode
                return i
        print("Inode Table Overloading! No new File/Directory can be created.")
        return -1

    def remove_inode_table_entry(self, inode_number):
        self.inode_table[inode_number] = None
