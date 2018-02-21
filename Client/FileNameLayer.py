# File Name Layer implementation -  maps filenames with the inode numbers
# implements recurssive lookups for inode
# @author: Gaurav Yeole <gauravyeole@gmail.com>

from Client.InodeNumberLayer import InodeNumberLayer
from Client.Inode import Inode


class FileNameLayer():

    def __init__(self):
        self.inode_number_layer = InodeNumberLayer()
        self.inode_table = self.inode_number_layer.inode_table

    def lookup(self, filename, dir): # dir is inode number of the directory
        inode = self.inode_number_layer.inode_number_to_inode(dir)
        if inode.type is 0:
            print("Invalid directory")
            return None
        if filename in inode.directory:
            return inode.directory[filename]
        print("Lookup Failure")
        return None


    def name_to_inode_number(self, filename, dir):
        return self.lookup(filename, dir)

    def add_inode_table_entry(self, inode):
        return self.inode_number_layer.add_inode_table_entry(inode)

