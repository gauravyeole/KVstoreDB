# Base Inode class to represent the files stored in the database
# @author: Gaurav Yeole <gauravyeole@gmail.com>

class FileInode(Inode):

    def __init__(self, name):
        super().__init__(name)
        self.size = 0
        self.no_blks = 0