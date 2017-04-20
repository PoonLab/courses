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

import sys
import os
import random
from argparse import ArgumentParser as ArgParser
import subprocess
import time

__manifest__ = '.learn-cli.manifest'

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


def recursive_mkdir(parent, paths, depth, max_depth=4, limit=20):
    """
    Recursively generate a binary tree of nested directories.
    :param limit:
    :return:
    """
    if limit==0 or depth >= max_depth:
        return limit, paths

    os.chdir(parent)
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
    content = ['(^_^)', '(-_-)zzz', '(T_T)', '\(^o ^ )/', '(>_<)', '(=_=)']
    content2 = random.sample(content*2, len(content)*2)
    files = []
    # random permutation
    for i, fn in enumerate(random.sample(names, len(names))):
        dest = os.path.join(random.choice(paths), fn)
        files.append(dest)
        with open(dest, 'w') as f:
            f.write(content2[i]+'\n')
    return files

def write_manifest(root, paths):
    with open(__manifest__, 'w') as f:
        for path in paths:
            f.write(path+'\n')


def reset():
    """
    Attempt to remove files and directories created by this script
    in a fairly safe way (without inadvertently deleting anything created
    by the user.
    :return:
    """
    if not os.path.exists(__manifest__):
        print ("Uh oh.  The manifest file created by this script is missing.")
        print ("Manually `rm` files and folders under `./start`.")
        sys.exit()
    with open(__manifest__, 'rU') as f:
        paths = [line.strip('\n') for line in f]

    mfiles = [os.path.basename(path) for path in paths]
    for dirpath, dirnames, files in os.walk('start', topdown=False):
        for f in files:
            if f in mfiles:
                os.remove(os.path.join(dirpath, f))
        for dir in dirnames:
            os.rmdir(os.path.join(dirpath, dir))

    # remove the parent directory
    try:
        os.rmdir('start')
    except:
        print ('ERROR: Failed to remove parent directory')
        pass
    else:
        os.remove(__manifest__)


def diff(f1, f2):
    with open(os.devnull, 'w') as devnull:
        retcode = subprocess.call(['diff', '-q', f1, f2], stdout=devnull)
    return (retcode==0)


def check():
    """
    Determine if files are placed together correctly
    :return:
    """
    devnull = open(os.devnull, 'w')
    success = True
    total_count = 0
    for dirpath, dirnames, files in os.walk('start'):
        nf = len(files)
        if nf == 0:
            continue
        if nf % 2 == 1:
            # orphaned file!
            success = False
            print ("Whoops!  Directory %s has an odd number of files.." % (dirpath,))
            break

        total_count += nf
        for i in range(nf):
            f1 = os.path.join(dirpath, files[i])
            result = []
            for j in range(nf):
                if i == j:
                    continue
                f2 = os.path.join(dirpath, files[j])
                result.append(diff(f1, f2))

            if not any(result):
                success = False
                print ("File %s has no match in its directory %s" % (f1, dirpath))
                break
        if not success:
            break

    if total_count < 12:
        print ('Missing some files; did you accidentally delete or move above ./start?')
        success = False

    return success


def timer():
    mod_time = os.path.getmtime('start')  # seconds since UNIX epoch
    elapsed = time.time() - mod_time
    hours, remain = divmod(int(elapsed), 3600)
    minutes, seconds = divmod(remain, 60)
    return hours, minutes, seconds

def argparser():
    parser = ArgParser(
        description="The objective of this exercise is to use the UNIX commands "
                    "`ls`, `pwd`, `cd`, `cat`, `cp` or `mv` to locate and move "
                    "textfiles in the file tree under the ./start directory "
                    "so that files containing the same ASCII emoticon are in the "
                    "same directory. "
                    "(1) Create the exercise with the --start command. "
                    "(2) When you have found and relocated the files in ./start, "
                    "   run this script with the --check command. "
                    "(3) To clean up, run the --reset command."
    )
    parser.add_argument(
        '--start',
        help="Create file tree.",
        action="store_true"
    )
    parser.add_argument(
        '--reset',
        help="Remove directories and files created by this script.",
        action="store_true"
    )
    parser.add_argument(
        '--check',
        help='Check if distribution of files is correct and get time.',
        action="store_true"
    )
    return parser



def main():
    root = os.path.join(os.getcwd(), 'start')

    parser = argparser()
    args = parser.parse_args()
    if args.start:
        if os.path.exists(root):
            print ('Error, start directory already exists.\n'
                   'Run: `python learn-cli.py --reset` to erase.')
            sys.exit()

        os.mkdir(root)

        limit, paths = recursive_mkdir(root, [], 0)
        files = populate(paths)
        write_manifest(root, paths+files)

    elif args.reset:
        reset()
    elif args.check:
        success = check()
        if success:
            print ('*** SUCCESS! ***')
            print ('Elapsed time: %d hours, %d minutes, %d seconds' % timer())
            print ('Run `python learn-cli.py --reset` to clean up dirs and files')
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
