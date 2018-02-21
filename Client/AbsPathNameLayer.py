# Absolute path name layer implementation - enables hierarchical file
# structure with root("/") as the root of tree
# @author: Gaurav Yeole <gauravyeole@gmail.com>

from Client.PathNameLayer import PathNameLayer


class AbsPathNameLayer():

    def __init__(self):
        self.path_name_layer = PathNameLayer()

    # wd is inode number of working directory
    def abs_path_to_inode_number(self, path, wd):
        if path[0] is '/':
            self.path_name_layer.path_to_inode_number(path, 0)
        else:
            self.path_name_layer.path_to_inode_number(path, wd)