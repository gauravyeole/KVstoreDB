# Custom hierarchical File System Interface akin to UNIX file system
# @author: Gaurav Yeole <gauravyeole@gmail.com>

from Client.AbsPathNameLayer import AbsPathNameLayer


class FileSystem():

    def __init__(self):
        self.file_system = AbsPathNameLayer()

    def mkdir(self, path):
        rv = False
        if self.file_system.import_superblk() is True:
            rv = self.file_system.add_new_inode(path, 1)
        self.file_system.export_superblk()
        return rv

    def create(self, path):
        rv = False
        if self.file_system.import_superblk() is True:
            rv = self.file_system.add_new_inode(path, 0)
        self.file_system.export_superblk()
        return rv

    # returns true if file is written successfully
    def write(self, path, data, offset=0):
        rv = False
        if self.file_system.import_superblk() is True:
            rv = self.file_system.write_to_file(path, offset, data)
        self.file_system.export_superblk()
        return rv

    def read(self, abs_path, offset=0, size=-1):
        rv = False
        if self.file_system.import_superblk() is True:
            rv = self.file_system.read_file(abs_path, offset, size)
        self.file_system.export_superblk()
        return rv

    def rmdir(self, path):
        rv = False
        if self.file_system.import_superblk() is True:
            rv = self.file_system.remove_dir(path)
        self.file_system.export_superblk()
        return rv

    def remove(self, path):
        rv = False
        if self.file_system.import_superblk() is True:
            rv = self.file_system.remove_file(path)
        self.file_system.export_superblk()
        return rv

    # arguments: path of existing file/directory and its new name
    def rename(self, path, new_name):
        rv = False
        if self.file_system.import_superblk() is True:
            rv = self.file_system.rename(path, new_name)
        self.file_system.export_superblk()
        return rv

    def link(self, source, destination):
        pass

    def unlink(self, path):
        pass

    def create_checkpoint(self, ckpfile):
        return self.file_system.checkpoint(ckpfile)

    def restore_checkpoint(self, ckpfile):
        return self.file_system.restore(ckpfile)

    def aquire(self, path):
        return self.file_system.aquire(path)

    def release(self, path):
        return self.file_system.release(path)