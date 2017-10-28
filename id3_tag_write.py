# coding:utf-8
import os
from glob import glob
import eyed3
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

for albums in os.listdir("."):
    if albums[4] == ".":
        year = albums[:4]
        album = albums[5:]
        for filename in glob(os.path.join(albums, "*.mp3")):
            filename = filename.decode("utf-8").encode("utf-8")
            title = os.path.basename(os.path.splitext(filename)[0])
            try:
                af = eyed3.load(filename)
                af.tag.title = unicode(title)
                af.tag.album = unicode(album)
                af.tag.year = unicode(year)
                af.tag.save()
            except Exception as e:
                print title


