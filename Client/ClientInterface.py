# Key-Value database server network interface
# @author: Gaurav Yeole <gauravyeole@gmail.com>

import xmlrpc
from xmlrpc.client import Binary


class KVstore:

    def __init__(self):
        self.server = xmlrpc.client.ServerProxy("http://localhost:12345", allow_none=True)
        print("INIT called")

    def reset_storage(self):
        return self.server.reset_storage()

    def put(self, key, value):
        return self.server.put(key, value)
        # return self.server.put(key, Binary(pickle.dumps(value)))

    def get(self, key):
        return self.server.get(key)
        # return pickle.loads(self.server.get(key).data)

    def delete(self, key):
        return self.server.delete(key)

    def count(self):
        return self.server.count()