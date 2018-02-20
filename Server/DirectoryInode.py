# Base Inode class to represent the directories stored in the database
# @author: Gaurav Yeole <gauravyeole@gmail.com>


class DirectoryInode(Inode):

    def __init__(self, name):
        super().__init__(name)
        self.children = list()