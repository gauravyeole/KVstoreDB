# Custom hierarchiecal File System Interface akin to UNIX file system
# @author: Gaurav Yeole <gauravyeole@gmail.com>

from DirectoryInode import DirectoryInode


class FileSystem():

    def __init__:
        self.inode_table =

    def lookup(self, path_list):
        pass

    def mkdir(self, path):
        pass

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