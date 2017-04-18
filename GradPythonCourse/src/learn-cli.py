"""
Generate a random tree of directories populated with a set number
of files, distributed at random locations.  User has to move files
to their correct locations within the filesystem and then run this
script again.  Files will contain clues about where they should be
located, which can be viewed with `cat`.  In sum, this is an exercise
for students to learn:
* ls
* pwd
* cat
* cp/mv
"""

import os
import random

def namingway():
    """
    Generate a random name
    :return:
    """
    vowels = 'aeiuo'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    return ''.join([random.choice(consonants)+random.choice(vowels) for i in range(3)])


def mkdir(path):
    if not os.path.exists(path):
        os.mkdir(path)


def recursive_mkdir(parent, paths, depth, max_depth=5, limit=20):
    """
    Recursively generate a binary tree of nested directories.
    :param limit:
    :return:
    """
    if limit==0 or depth > max_depth:
        return limit, paths

    try:
        os.chdir(parent)
    except:
        print os.getcwd()
        print parent
        raise

    dirs = []
    while limit > 0 and len(dirs) < 2:
        this_dir = namingway()
        os.mkdir(this_dir)
        dirs.append(this_dir)
        limit -= 1

    paths.extend(map(lambda x: os.path.abspath(x), dirs))

    # recursive calls
    for this_dir in dirs:
        depth += 1
        limit, paths = recursive_mkdir(this_dir, paths, depth, max_depth, limit)

    os.chdir('..')  # climb back up
    return limit, paths


def populate(paths):
    """
    Distribute files at random
    :return:
    """
    # 2017 Central North Pacific Tropical Cyclone names
    names = ['Akoni', 'Ema', 'Hone', 'Iona', 'Keli', 'Lala', 'Moke', 'Nolo', 'Olana', 'Pena', 'Ulana', 'Wale']
    



def main():
    root = os.path.join(os.getcwd(), 'start')
    mkdir(root)
    limit, paths = recursive_mkdir(root, [], 0)
    print paths

if __name__ == '__main__':
    main()
