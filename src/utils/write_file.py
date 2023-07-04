def write_file(file_path, mode, content):
    f = open(file_path, mode)
    f.write(content)
    f.close()
