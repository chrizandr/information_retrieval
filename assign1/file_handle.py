"""Handle file operations and assign IDs."""

import os
import re


def get_text(filename):
    """Get the data content from the file."""
    with open(filename, 'r') as myfile:
        data = myfile.read().replace('\n', ' ')
        regex = r'<TEXT>(.*)</TEXT>'
        searchObj = re.search(regex, data)
        if searchObj:
            return searchObj.group(1)
        else:
            return ""


def format_files(root_path, n):
    """Get all files from root path."""
    set_a, set_b = sorted(os.listdir(root_path))
    id_counter = 0
    for folder in os.listdir(root_path + set_a):
        if id_counter > n/2:
            break
        for file_ in os.listdir(root_path + set_a + '/' + folder):
            print("Processing ", file_)
            data = get_text(root_path + set_a + '/' + folder + '/' + file_)
            f = open("data/"+str(id_counter)+".txt", 'w')
            f.write(data)
            f.close()
            id_counter += 1
            if id_counter > n/2:
                break

    for folder in os.listdir(root_path + set_b):
        if id_counter > n:
            break
        for sub_folder in os.listdir(root_path + set_b + '/' + folder):
            for file_ in os.listdir(root_path + set_b + '/' + folder + '/' + sub_folder):
                print("Processing ", file_)
                data = get_text(root_path + set_b + '/' + folder + '/' + sub_folder + '/' + file_)
                f = open("data/"+str(id_counter)+".txt", 'w')
                f.write(data)
                f.close()
                id_counter += 1
                if id_counter > n:
                    break
    return None


if __name__ == "__main__":
    format_files("/home/chris/information_retrieval/assign1/data/", 5000)
