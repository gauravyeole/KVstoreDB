# Base Inode class to represent the files stored in the database
# @author: Gaurav Yeole <gauravyeole@gmail.com>

from Inode import Inode

class FileInode(Inode):

    def __init__(self, path):
        super().__init__(path)
        self.size = 0
        self.no_blks = 0
        self.blocks = list()

    @property
    def __str__(self):
        return ("Path: " + self.path +  ", size: " + self.size + \
                ", number of blocks: " + self.no_blks + ", blocks: " + self.no_blks + \
                ", number of links: " + self.no_links + ", time created: " + \
                self.time_created + ", time last accessed " + self.time_accessed + \
                ", time last modified: " + self.time_modified)
