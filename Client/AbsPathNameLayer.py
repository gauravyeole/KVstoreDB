# Absolute path name layer implementation - enables hierarchical file
# structure with root("/") as the root of tree
# @author: Gaurav Yeole <gauravyeole@gmail.com>
import copy

from Client.Inode import Inode
from Client.PathNameLayer import PathNameLayer, get_parent


class AbsPathNameLayer():

    def __init__(self):
        self.path_name_layer = PathNameLayer()
        # self.inode_table = self.path_name_layer.inode_table

    # def __str__(self):
    #     string = ""
    #     for inode in self.inode_table:
    #         string = string + "[" + str(inode) + ": " + str(self.inode_table[inode]) + "]; "
    #     return string

    # wd is inode number of working directory
    def abs_path_to_inode_number(self, path, wd=0):
        inode_number =  self.path_name_layer.path_to_inode_number(path[1:], wd)
        if inode_number is not None:
            return inode_number
        print("Invalid Operation, Directory/File does not exist")
        return None

    def abs_path_to_inode(self, path):
        if path is "/":
            return self.path_name_layer.inode_number_to_inode(0)
        inode_number = self.abs_path_to_inode_number(path)
        if inode_number is not None:
            return self.path_name_layer.inode_number_to_inode(inode_number)
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

    def add_new_inode(self, path, type):
        if type is 1:
            new_inode = Inode(1)
        else:
            new_inode = Inode(0)
        new_inode_number = self.add_inode_table_entry(new_inode)
        if new_inode is not -1:
            parent_path = get_parent(path)
            parent_inode = self.abs_path_to_inode(parent_path)
            if parent_inode is not None:
                if parent_inode.add_child(path.split('/')[-1], \
                                              new_inode_number):
                    return True
                else:
                    self.remove_inode_table_entry(new_inode_number)
                    return False
        print("New Directory cannot be created. File System Full!!!")
        return False


    def remove_file(self, abs_path):
        parent_path = get_parent(abs_path)
        inode_number = self.abs_path_to_inode_number(abs_path)
        parent_inode = self.abs_path_to_inode(parent_path)
        parent_inode.remove_child(abs_path.split('/')[-1])
        self.path_name_layer.remove_file(inode_number)
        return

    def remove_dir(self, abs_path):
        inode_number = self.abs_path_to_inode_number(abs_path)
        inode = self.abs_path_to_inode(abs_path)
        parent_path = get_parent(abs_path)
        parent_inode = self.abs_path_to_inode(parent_path)
        children = copy.deepcopy(inode.get_children())
        for k, val in children.items():
            child_inode = self.path_name_layer.inode_number_to_inode(val)
            if child_inode.type is 0:
                self.remove_file(abs_path + "/" + k)
            else:
                self.remove_dir(abs_path + "/" + k)
        self.path_name_layer.remove_inode_table_entry(inode_number)
        parent_inode.remove_child(abs_path.split('/')[-1])
        return

    def rename(self, abs_path, new_name):
        try:
            parent_path = get_parent(abs_path)
            parent_inode = self.abs_path_to_inode(parent_path)
            inode_number = self.abs_path_to_inode_number(abs_path)
            parent_inode.remove_child(abs_path.split('/')[-1])
            parent_inode.add_child(new_name, inode_number)
            return True
        except:
            print("Unable to rename!!")
            return False

    def checkpoint(self, ckpfile):
        return self.path_name_layer.checkpoint(ckpfile)

    def restore(self, ckpfile):
        return self.path_name_layer.restore(ckpfile)

    def import_superblk(self):
        return self.path_name_layer.import_superblk()

    def export_superblk(self):
        return self.path_name_layer.export_superblk()