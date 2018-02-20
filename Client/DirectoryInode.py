# Base Inode class to represent the directories stored in the database
# @author: Gaurav Yeole <gauravyeole@gmail.com>

from Inode import Inode

class DirectoryInode(Inode):

    def __init__(self, path):
        super().__init__(path)
        self.children = list()

    @property
    def __str__(self):
        return ("Path: " + self.path + ", children: " + self.children + \
                ", number of links: " + self.no_links + ", time created: " + \
                self.time_created + ", time last accessed " + self.time_accessed + \
                ", time last modified: " + self.time_modified)