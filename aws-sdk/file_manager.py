def read_file(file_path):
    f = open(file_path, "r")
    return f.read()

def write_file(contents):
    f = open("test.txt", "w")
    f.write(contents)
    f.close()

write_file(read_file("README.md"))
