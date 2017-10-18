import urllib2
import settings
import time
import threading
from plyer import notification as n
from lxml import etree

running = True


def cycle():
    while running:
        #data = {"title": "Talamanc - Test", "dj": "Oversea"}
        print "[%s] Polling..." % (time.strftime("%d %b %Y ~ %H:%M"))
        file_append_track(**poll())
        time.sleep(settings.CYCLE_SECONDS)


def file_duplicate_check(filehandle, trackname):
    tracks = filehandle.readlines()
    for track in tracks:
        if trackname in track:
            return True
    return False


def file_append_track(**kwargs):
    with open("tracks.txt", "ab+") as f:
        if not file_duplicate_check(f, kwargs["title"]):
            time.ctime()
            f.write("[%s x %s] %s\n" % (kwargs["dj"], time.strftime("%d %b %Y ~ %H:%M"), kwargs["title"]))
            n.notify(
                title='New Track',
                message='[' + kwargs["title"] + ']',
                ticker='r'
            )

def poll():
    request = urllib2.Request(settings.BASE)
    response = urllib2.urlopen(request)
    tree = etree.HTML(response.read())
    return {
        "title": tree.xpath(settings.TRACK_PATH)[0].text,
        "dj": tree.xpath(settings.TRACK_DJ)[0].text
    }


if __name__ == "__main__":
    threading.Thread(target=cycle).start()

    if raw_input("") == "":
        print "Exiting..."
        running = False
        exit(1)
