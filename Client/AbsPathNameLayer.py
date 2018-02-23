# Absolute path name layer implementation - enables hierarchical file
# structure with root("/") as the root of tree
# @author: Gaurav Yeole <gauravyeole@gmail.com>

from Client.PathNameLayer import PathNameLayer, get_parent


class AbsPathNameLayer():

    def __init__(self):
        self.path_name_layer = PathNameLayer()
        self.inode_table = self.path_name_layer.inode_table

    def __str__(self):
        string = ""
        for inode in self.inode_table:
            string = string + "[" + str(inode) + ": " + str(self.inode_table[inode]) + "]; "
        return string

    # wd is inode number of working directory
    def abs_path_to_inode_number(self, path, wd=0):
        inode_number =  self.path_name_layer.path_to_inode_number(path[1:], wd)
        if inode_number is not None:
            return inode_number
        print("Invalid Operation, Directory/File does not exist")
        return None

    def abs_path_to_inode(self, path):
        if path is "/":
            return self.inode_table[0]
        inode_number = self.abs_path_to_inode_number(path)
        if inode_number is not None:
            return self.inode_table[inode_number]
        return None

    def add_inode_table_entry(self, inode):
        return self.path_name_layer.add_inode_table_entry(inode)

    def remove_inode_table_entry(self, inode_number):
        return self.path_name_layer.remove_inode_table_entry(inode_number)

    def write_to_file(self, abs_path, offset, data):
        inode_number = self.abs_path_to_inode_number(abs_path)
        status = self.path_name_layer.write_to_file(inode_number, offset, data)
        return status

    def read_file(self, abs_path, offset, size):
        inode_number = self.abs_path_to_inode_number(abs_path)
        return self.path_name_layer.read_file(inode_number, offset, size)

    def remove_file(self, abs_path):
        parent_path = get_parent(abs_path)
        parent_inode = self.abs_path_to_inode(parent_path)
        parent_inode.remove_child(abs_path.split('/')[-1])
        inode_number = self.abs_path_to_inode_number(abs_path)
        self.path_name_layer.remove_file(inode_number)
        return