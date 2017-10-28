# coding:utf-8
import os
from glob import glob

def get_albums(Dir):
    albums = {}
    for filename in glob(os.path.join(Dir, "*.m3u")):
        base = os.path.basename(os.path.splitext(filename)[0])
        urls = open(filename).readlines()
        urls = [i.strip() for i in urls]
        albums[base] = urls
    return albums

def download(url, targetDir):
    os.system("wget \"%s\" -P \"%s\"" %(url, targetDir))

def run(PATH):
    albums = get_albums(PATH)
    for album, urls in albums.items():
        newDir = os.path.join(PATH, album)
        # make album dir.
        if  not os.path.exists(newDir):
            os.mkdir(newDir)
        # download songs.
        for url in urls:
            download(url, newDir)    
    # change into utf-8.
    order = "convmv -f gbk -t utf-8 -r --notest {}".format(PATH)
    os.system(order)

if __name__ == "__main__":
    PATH = r"./王菲/"
    run(PATH)
