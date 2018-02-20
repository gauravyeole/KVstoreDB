# Custom hierarchiecal File System Interface akin to UNIX file system
# @author: Gaurav Yeole <gauravyeole@gmail.com>

class FileSystem():

    def __init__:
        self.root = DiretoryInode("/")

    def mkdir(self, dir):
        pass

    def lookup(self, abs_path):
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