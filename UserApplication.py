from Client.FileStore import FileStore


def main():
    myDatabase = FileStore()

    file_name = "test.txt"
    myDatabase.put_file(file_name)
    print (myDatabase.get_file(file_name))


if __name__ == "__main__":
    main()
