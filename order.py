# coding:utf-8
import os
import sys
from glob import glob
def main():
    print("Usage: python order.py PATH")
    if len(sys.argv) != 2:
        sys.exit(1)
    else:
        PATH = sys.argv[1]
        if not os.path.isdir(PATH):
            sys.exit(1)
    idx = 1
    for f in glob(os.path.join(PATH, "*.mp3")):
        base = os.path.basename(os.path.splitext(f)[0])
        new = os.path.join(PATH, "{:04d}-{}.mp3".format(idx, base))
        idx += 1
        os.rename(f, new)

if __name__=='__main__':
    main()
