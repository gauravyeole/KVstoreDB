# Server Network Interface
# @author: Gaurav Yeole <gauravyeole@gmail.com>

import getopt
from xmlrpc.server import SimpleXMLRPCServer

import sys

from Server.KVstore import KVstore


class Server:

    def __init__(self):
        self.database = KVstore()

    def count(self):
        return self.database.count()

    def get(self, key):
        rv = {}
        key = key
        val = self.database.get(key)
        if val is not None:
            rv = val
        return rv

    def put(self, key, val):
        return self.database.put(key, val)

    def delete(self, key):
        return self.database.delete(key)

    def reset_storage(self):
        return self.database.reset_storage()

    def checkpoint(self, ckpfile):
        return self.database.checkpoint(ckpfile)

    def restore(self, ckpfile):
        return self.database.restore(ckpfile)

    def aquire(self, key):
        return self.database.aquire(key)

    def release(self, key):
        return self.database.release(key)

def main():
    optlist, args = getopt.getopt(sys.argv[1:], "", "port=")
    ol = {}
    for k,v in optlist:
        ol[k] = v

    port = 12345
    if "--port" in ol:
        port = int(ol["--port"])

    serve(port)

def serve(port):
    server = SimpleXMLRPCServer(("localhost", port))
    server.register_introspection_functions()
    database = Server()
    server.register_function(database.count)
    server.register_function(database.get)
    server.register_function(database.put)
    server.register_function(database.delete)
    server.register_function(database.reset_storage)
    server.register_function(database.checkpoint)
    server.register_function(database.restore)
    server.register_function(database.aquire)
    server.register_function(database.release)
    server.serve_forever()

if __name__ == "__main__":
    main()