# Path Name layer implementation - enables hierarchiecal structure in file system
# @author: Gaurav Yeole <gauravyeole@gmail.com>

from Client.FileNameLayer import FileNameLayer


def first(path):
    if path.split('/')[0] is '':
        return "/"
    return path.split('/')[0]


def get_parent(path):
    if '/'.join((path.split('/')[:-1])) is '':
        return "/"
    return '/'.join((path.split('/')[:-1]))


def rest(path):
    return '/'.join((path.split('/')[1:]))


class PathNameLayer():

    def __init__(self):
        self.file_name_layer = FileNameLayer()
        self.inode_table = self.file_name_layer.inode_table

    def path_to_inode_number(self, path, dir):
        if dir is None:
            print("Invalid path, Operation can not complete")
            return None
        if '/' not in path:
            return self.file_name_layer.name_to_inode_number(path, dir)
        else:
            dir = self.file_name_layer.lookup(first(path), dir)
            path = rest(path)
            return self.path_to_inode_number(path, dir)

    def add_inode_table_entry(self, inode):
        return self.file_name_layer.add_inode_table_entry(inode)

    def write_to_file(self, inode_number, offset, data):
        return self.file_name_layer.write_to_file(inode_number, offset, data)

    def read_file(self, inode_number, offset, size):
        return self.file_name_layer.read_file(inode_number, offset, size)

