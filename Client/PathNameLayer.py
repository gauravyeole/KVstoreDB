# Path Name layer implementation - enables hierarchiecal structure in file system
# @author: Gaurav Yeole <gauravyeole@gmail.com>

from Client.FileNameLayer import FileNameLayer


class PathNameLayer():

    def __init__(self):
        self.file_name_layer = FileNameLayer()

    def path_to_inode_number(self, path, dir):
        if '/' not in path:
            self.file_name_layer.name_to_inode_number(path, dir)
        else:
            dir = self.file_name_layer.lookup(self.first(path), dir)
            path = self.rest(path)
            return self.path_to_inode_number(path, dir)

    def first(self, path):
        return path.split('/')[-1]

    def rest(self, path):
        return '/'.join((path.split('/')[:-1]))