# File storage API - getFile, putFile and delFile
# @author: Gaurav Yeole <gauravyeole@gmail.com>

import hashlib
from KVstore import KVstore


class FileStore():

    def __init__(self):
        self.datastore = KVstore()
        self.MAX_KEY_SIZE = 256
        self.MAX_VALUE_SIZE = 64 * 2014
        self.file_size_map = dict()
        # maps file names stored in database with its no of blocks.

    def put_file(self, file_name):
        file_data = self.get_file_as_string(file_name)
        blocks = [file_data[start:start + self.MAX_VALUE_SIZE] for start in
                  xrange(0, len(file_data), self.MAX_VALUE_SIZE)]
        for i in range(0, len(blocks)):
            val = blocks[i]
            key = self.get_key(file_name, i)
            if self.datastore.put(key, val) is False:
                return False
        self.file_size_map[file_name] = len(blocks)
        return True

    def get_file(self, file_name):
        no_blks = self.file_size_map.pop(file_name, -1)
        file_data = ""
        if no_blks >= 0:
            for i in range(0, no_blks):
                key = self.get_key(file_name, i)
                file_data += self.datastore.get(key)
            return file_data
        else:
            print("File " + file_name + " is not stored in the database")
            return ""

    def delete_file(self, file_name):
        no_blks = self.file_size_map.pop(file_name, -1)
        if no_blks >= 0:
            for i in range(0, no_blks):
                key = self.get_key(file_name, i)
                if self.datastore.delete(key) is False:
                    return False
            return True
        else:
            print("File " + file_name + " is not stored in the database")
            return False

    def get_file_as_string(self, file_name):
        data = ""
        with open(file_name, 'r') as f:
            data = f.read()
        return data

    def get_key(self, file_name, block_no):
        raw_key = file_name + str(block_no)
        m = hashlib.md5()
        m.update(raw_key)
        return m.hexdigest()
