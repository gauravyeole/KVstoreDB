# Path Name layer implementation - enables hierarchiecal structure in file system
# @author: Gaurav Yeole <gauravyeole@gmail.com>

from Client.FileNameLayer import FileNameLayer


def first(path):
    return path.split('/')[-1]


def rest(path):
    return '/'.join((path.split('/')[:-1]))


class PathNameLayer():

    def __init__(self):
        self.file_name_layer = FileNameLayer()
        self.inode_table = self.file_name_layer.inode_table

    def path_to_inode_number(self, path, dir):
        if '/' not in path:
            self.file_name_layer.name_to_inode_number(path, dir)
        else:
            dir = self.file_name_layer.lookup(first(path), dir)
            path = rest(path)
            return self.path_to_inode_number(path, dir)

    def add_inode_table_entry(self, inode):
        return self.file_name_layer.add_inode_table_entry(inode)

