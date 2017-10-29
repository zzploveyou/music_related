# coding:utf-8
import os
import sys
from shutil import copy
def main():
    if len(sys.argv) != 3:
        print("Usage: python cpmp3.py sourceDir targetDir")
        sys.exit(0)
    else:
        sourceDir = sys.argv[1]
        targetDir = sys.argv[2]
        if not os.path.isdir(sourceDir):
            print("Usage: python cpmp3.py sourceDir targetDir")
            sys.exit(1)
        if not os.path.isdir(targetDir):
            print("Usage: python cpmp3.py sourceDir targetDir")
            sys.exit(1)
    cp = 0
    print("copying mp3 file from '{}' to '{}' ... ".format(sourceDir, targetDir))
    for d, sd, fs in os.walk(sourceDir):
        for f in fs:
            src = os.path.join(d, f)
            if ".mp3" in f:
                copy(src, targetDir)
                cp += 1
                print "\r{}: {}".format(cp, f),
                sys.stdout.flush()
    print("")
    print("copy num: {}".format(cp))

if __name__ == '__main__':
    main()
