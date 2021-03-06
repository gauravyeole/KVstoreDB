# Inode Number layer implementation creates the inode table
# @author: Gaurav Yeole <gauravyeole@gmail.com>

from Client import config
from Client.BlockLayer import BlockLayer
from Client.Inode import Inode


MAX_NUM_INODES = config.MAX_NUM_INODES
MAX_BLK_SIZE = config.MAX_BLK_SIZE
num_of_blks = config.NUM_OF_BLKS

class InodeNumberLayer:

    # InodeTable contains dictionary of all the inodes indexed by inode numbers
    # and mapping to corresponding inode object
    def __init__(self):
        self.blocks = BlockLayer()
        self.inode_table = self.blocks.import_inode_table()
        if self.inode_table is None:
            self.inode_table = dict()
            for i in range(0, MAX_NUM_INODES):
                self.inode_table[i] = None
            root = Inode(1)
            self.inode_table[0] = root
        self.blocks.export_inode_table(self.inode_table)
        print("Inode Table Layer Initialised")

    def __str__(self):
        string = ""
        for inode in self.inode_table:
            string = string + "[" + str(inode) + ": " + \
                     str(self.inode_table[inode]) + "]; "
        return string


    def inode_number_to_inode(self, inode_number):
        return self.inode_table[inode_number]

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
        if blk_num > 0:
            return self.blocks.blk_number_to_data(blk_num)
        else:
            print("InodeNumberLayer: Invalid Offset!")
        return -1

    # def blk_number_to_blk_data(self, blk_number):
    #     return self.blocks.blk_number_to_data(blk_number)

    def write_to_file(self, inode_number, offset, data):
        inode = self.inode_number_to_inode(inode_number)
        if inode is not None and inode.type is 0:
            if offset is 0:
                blocks = [data[start:start + MAX_BLK_SIZE] for start in
                          range(0, len(data), MAX_BLK_SIZE)]
                last_blk_index = 0
            else:
                last_blk_index = int(offset/MAX_BLK_SIZE)
                last_blk_data = self.offset_to_blk_data(offset, inode)
                if last_blk_data == -1:
                    return False
                for i in range(last_blk_index, len(inode.blk_numbers)):
                    self.blocks.invalid_blk(inode.blk_numbers.pop(i))
                print("DEBUG: last_blk_data: " + last_blk_data)
                last_blk_data = last_blk_data[:offset%MAX_BLK_SIZE] + \
                                data[:MAX_BLK_SIZE-offset%MAX_BLK_SIZE]
                data = last_blk_data + data[MAX_BLK_SIZE-offset%MAX_BLK_SIZE:]
                blocks = [data[start:start + MAX_BLK_SIZE] for start in
                          range(0, len(data), MAX_BLK_SIZE)]
            for i in range(0, len(blocks)):
                blk_index = last_blk_index + i
                blk_number = self.blocks.store_data(blocks[blk_index])
                if blk_number is -1:
                    return False
                inode.update_blk_number(blk_index, blk_number)
            inode.size = len(inode.blk_numbers)*MAX_BLK_SIZE
            return True
        else:
            print("File does not exists...")
            return False

    def read_file(self, inode_number, size, offset):
        inode = self.inode_number_to_inode(inode_number)
        if size is -1:
            size = inode.size
        first_block_index = int(offset/MAX_BLK_SIZE)
        last_block_index = int((offset+size)/MAX_BLK_SIZE)
        string = ""
        try:
            blks = range(first_block_index, last_block_index)
            for i in blks:
                string = string + self.blocks.blk_number_to_data(inode.blk_numbers[i])
            return string
        except KeyError:
            print("Invalid offset or size")

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

    def remove_file(self, inode_number):
        inode = self.inode_number_to_inode(inode_number)
        for k, val in inode.blk_numbers.items():
            self.blocks.invalid_blk(val)
        self.remove_inode_table_entry(inode_number)
        return True

    def checkpoint(self, ckpfile):
        return self.blocks.checkpoint(ckpfile)

    def restore(self, ckpfile):
        if self.blocks.restore(ckpfile) is 0 and self.import_superblk() is True:
            return True
        return False

    def import_superblk(self):
        inode_table =  self.blocks.import_inode_table()
        if inode_table is not None:
            self.inode_table = inode_table
            return self.blocks.import_valid_blk()
        return False

    def export_superblk(self):
        self.blocks.export_inode_table(self.inode_table)
        return self.blocks.export_valid_blk()

    def aquire(self, inode_number):
        inode = self.inode_number_to_inode(inode_number)
        try:
            if inode.type is 0:
                for k, v in inode.blk_numbers.items():
                    self.blocks.aquire(v)
            else:
                children = inode.get_children()
                for k, v in children.items():
                    self.aquire(v)
            return True
        except:
            print("Inode Number: " + str(inode_number) + " cannot aquire lock!")
            return False

    def release(self, inode_number):
        inode = self.inode_number_to_inode(inode_number)
        try:
            if inode.type is 0:
                for k, v in inode.blk_numbers.items():
                    self.blocks.release(v)
            else:
                children = inode.get_children()
                for k, v in children.items():
                    self.release(v)
            return True
        except:
            print("Inode Number: " + str(inode_number) + " cannot release lock!")
            return False
