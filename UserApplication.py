# Sample User Client-side Application utilizing the Server API
# @author: Gaurav Yeole <gauravyeole@gmail.com>

from Client.FileStore import FileStore
from Client.FileSystem import FileSystem


def main():
    myFileSystem = FileSystem()

    print ("MKDIR Success:" + str(myFileSystem.mkdir("/abc")))
    print(str(myFileSystem.mkdir("/abc/pqr")))
    # file_name = "test.txt"
    # myDatabase.put_file(file_name)
    # print (myDatabase.get_file(file_name))


if __name__ == "__main__":
    main()
