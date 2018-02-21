# Custom hierarchiecal File System Interface akin to UNIX file system
# @author: Gaurav Yeole <gauravyeole@gmail.com>

from Client.AbsPathNameLayer import AbsPathNameLayer
from Client.Inode import Inode
from Client.PathNameLayer import rest, first


class FileSystem():

    def __init__(self):
        self.file_system = AbsPathNameLayer()

    def mkdir(self, path):
        new_inode = Inode()
        new_inode.type = 1
        new_inode_number = self.file_system.add_inode_table_entry()
        if new_inode_number is not -1:
            parent_path = rest(path)
            parent_inode = self.file_system.abs_path_to_inode(parent_path)
            if parent_inode is not None:
                return parent_inode.add_child(first(path), new_inode_number)
        print("New Directory cannot be created. File System Full!!!")
        return False

    def link(self, source, destination):
        pass

    def unlink(self, path):
        pass

    def delete(self, abs_path):
        pass

    def create(self, abs_path):
        pass

    def write(self, abs_path, data):
        pass

    def read(self, abs_path):
        pass

    def rmdir(self, path):
        pass

    def rename(self, source, destination):
        pass