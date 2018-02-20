# Base Inode class to represent the files and directories stored in the database
# @author: Gaurav Yeole <gauravyeole@gmail.com>

import datetime


class Inode():

    def __init__(self, name):
        self.time_created = datetime.now()
        self.time_accessed = datetime.now()
        self.time_modified = datetime.now()
        self.name = name
        self.no_links = 2
        # self.children = list()

    def __str__(self):
        return ("Name: " + self.name +  ", isFile: " + str(self.is_file) + ", size: " + str(self.size) +
                ", number of blocks: " + str(self.no_blks) + ", time file created: " +
                str(self.time_created) + ", time file accessed: " + str(self.time_accessed) +
                ", time file modified: " + str(self.modified)
                )



