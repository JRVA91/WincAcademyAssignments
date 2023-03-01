__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"
import os, glob
from zipfile import ZipFile

def clean_cache():
    directory = '/Users/jordy/Documents/Python/files/'
    folder_name = 'cache'
    new_path = directory + folder_name
    filelist = glob.glob(os.path.join(new_path, "*"))

    if os.path.exists(new_path):
        for file in filelist:
            print(file)
            os.remove(file)        
    else:
        return os.makedirs(folder_name)


def cache_zip(zip_file_path, cache_dir_path):
    with ZipFile(zip_file_path, 'r') as zObject:
        return zObject.extractall(cache_dir_path)

#cache_zip('/Users/jordy/Documents/Python/files/data.zip','/Users/jordy/Documents/Python/cache')

def cached_files():
    return os.listdir('/Users/jordy/Documents/Python/files/cache/')

print(cached_files())

files = cached_files()

def find_password(files=files):
    for file in files:
        with open('/Users/jordy/Documents/Python/files/cache/' + file, 'r') as f:
            for sentence in f:
                sentence = f.readlines()
                for line in sentence:
                    if line.find('password') != -1:
                        print(line)
        f.close()
#clean_cache()
find_password()