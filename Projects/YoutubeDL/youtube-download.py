import os, subprocess, time, shutil

date_time = time.strftime("%d-%m-%Y")
dest_path = "downloads\\" + date_time + "\\%(title)s.%(ext)s"
export_path = os.getcwd() + "\\exports\\" + date_time
export_format = "mp3"
youtube_url = raw_input("Enter a youtube video url: ")
subprocess.call(["youtube-dl.exe", youtube_url, "-o", dest_path, "-i", "-f", "bestaudio"])

if not os.path.exists(export_path):
    os.makedirs(export_path)

for root, dirs, files in os.walk("downloads\\"):     
    if len(files) > 0:
        for f in files:
            file_path = "{0}\\{1}".format(root, f)
            export_path = "{0}\\{1}.{2}".format(export_path, f[:-5], export_format)
            subprocess.call(["ffmpeg.exe", "-i", file_path, "-f", export_format, export_path])
# CLEANUP
shutil.rmtree('/downloads')
raw_input("Press enter to continue...")
