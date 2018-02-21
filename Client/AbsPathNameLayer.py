# Absolute path name layer implementation - enables hierarchical file
# structure with root("/") as the root of tree
# @author: Gaurav Yeole <gauravyeole@gmail.com>

from Client.PathNameLayer import PathNameLayer


class AbsPathNameLayer():

    def __init__(self):
        self.path_name_layer = PathNameLayer()
        self.inode_table = self.path_name_layer.inode_table

    # wd is inode number of working directory
    def abs_path_to_inode_number(self, path, wd = 0):
        self.path_name_layer.path_to_inode_number(path, wd)

    def abs_path_to_inode(self, path):
        inode_number = self.abs_path_to_inode_number(path)
        return self.inode_table[inode_number]

    def add_inode_table_entry(self, inode):
        return self.path_name_layer.add_inode_table_entry(inode)