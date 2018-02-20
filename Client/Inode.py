# Base Inode class to represent the files and directories stored in the database
# @author: Gaurav Yeole <gauravyeole@gmail.com>

import datetime


class Inode():

    def __init__(self, path):
        self.time_created = datetime.now()
        self.time_accessed = datetime.now()
        self.time_modified = datetime.now()
        self.path = path
        self.no_links = 2





