# Sample User Client-side Application utilizing the Server API
# @author: Gaurav Yeole <gauravyeole@gmail.com>

from Client.FileSystem import FileSystem


def main():
    myFileSystem = FileSystem()

    print ("MKDIR Success:" + str(myFileSystem.mkdir("/abc")))
    print(str(myFileSystem.mkdir("/abc/pqr")))
    myFileSystem.create("/xyz")
    myFileSystem.write("/xyz", "this is my test data, dnsjfndddnddfmndnfmfmsdnfmnds ", 0)
    myFileSystem.write("/xyz", "this is my test data, dnsjfndddnddfmndnfmfmsdnfmnds ", 5)
    data = myFileSystem.rename("/abc", "lmn")
    myFileSystem.create_checkpoint("first_checkpoint")
    print(data)
    myFileSystem.create("/ghj")
    myFileSystem.create("/ert")
    myFileSystem.create("/pou")
    myFileSystem.restore_checkpoint("first_checkpoint")
    myFileSystem.write("/pou", "this is my test data, dnsjfndddnddfmndnfmfmsdnfmnds ", 5)
    print("xyz")
    file_name = "test.txt"
    # myDatabase.put_file(file_name)
    # print (myDatabase.get_file(file_name))


if __name__ == "__main__":
    main()
