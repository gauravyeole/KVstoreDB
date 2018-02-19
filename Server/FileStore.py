# File storage API - getFile, putFile and delFile
# @author: Gaurav Yeole <gauravyeole@gmail.com>

class FileStore(Object):

    def __init__(self):
        self.datastore = KVstore()
        self.MAX_KEY_SIZE = 256
        self.MAX_VALUE_SIZE = 64*2014
        self.file_size_map = dict()


    def putFile(self):
        pass

    def getFile(self):
        pass

    def deleteFile(self):
        pass


