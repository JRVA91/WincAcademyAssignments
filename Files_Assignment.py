__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"
import os, glob
from zipfile import ZipFile

directory = os.path.join(os.getcwd(), 'files', 'cache')

def clean_cache():
    filelist = glob.glob(os.path.join(directory, "*"))

    if os.path.exists(directory):
        for file in filelist:
            os.remove(file)        
    else:
        return os.makedirs(directory)

def cache_zip(zip_file_path, cache_dir_path):
    with ZipFile(zip_file_path, 'r') as zObject:
        return zObject.extractall(cache_dir_path)

#cache_zip('/Users/jordy/Documents/Python/files/data.zip','/Users/jordy/Documents/Python/files/cache')

def cached_files():
    list = os.listdir(directory)
    temp = []
    for item in list:
        temp.append((os.path.abspath(os.path.join(directory, item))))
    return temp

print(cached_files())

files = cached_files()

def find_password(files=files):
    for file in files:
        with open(os.path.join(directory, file), 'r') as f:
            for sentence in f:
                sentence = f.readlines()
                for line in sentence:
                    if line.find('password') != -1:
                        return line[line.find(" ")+1:].strip()

print(find_password())


