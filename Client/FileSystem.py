# Custom hierarchiecal File System Interface akin to UNIX file system
# @author: Gaurav Yeole <gauravyeole@gmail.com>

from Client.AbsPathNameLayer import AbsPathNameLayer


#TODO: update timestamps
class FileSystem():

    def __init__(self):
        self.file_system = AbsPathNameLayer()

    def mkdir(self, path):
        return self.file_system.add_new_inode(path, 1)

    def create(self, path):
        return self.file_system.add_new_inode(path, 0)

    # returns true if file is written successfully
    def write(self, path, data, offset=0):
        return self.file_system.write_to_file(path, offset, data)

    def read(self, abs_path, offset=0, size=-1):
        return self.file_system.read_file(abs_path, offset, size)

    def rmdir(self, path):
        return self.file_system.remove_dir(path)

    def remove(self, path):
        return self.file_system.remove_file(path)

    # arguments: path of existing file/directory and its new name
    def rename(self, path, new_name):
        return self.file_system.rename(path, new_name)

    def link(self, source, destination):
        pass

    def unlink(self, path):
        pass
