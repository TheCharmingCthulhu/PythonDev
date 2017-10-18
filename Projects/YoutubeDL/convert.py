import os, subprocess

date = raw_input("subfolder? (enter: date [xx-xx-xxxx]):");
for root, dirs, files in os.walk("downloads/{0}".format(date)):
    if len(files) > 0:
        for f in files:
            if f.endswith(".m4a"):
                print f
                p = subprocess.Popen(["ffmpeg.exe", "-i", root + "\\" + f, "-f", "mp3", root + "\\" + f[:-4] + ".mp3"])

