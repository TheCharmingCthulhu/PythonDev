# Imports
import subprocess
import os, sys, shutil
import __future__

# Input Files
INPUT_DIR = 'input';
if not os.path.exists(INPUT_DIR):
    os.mkdir(INPUT_DIR);

# Drawable Directories

# BASE DRAWABLE
BASE_DIR = 'drawable'

# MDPI DRAWABLE
DRAWABLE_DIR = BASE_DIR
if os.path.exists(DRAWABLE_DIR):
    shutil.rmtree(DRAWABLE_DIR)
os.mkdir(DRAWABLE_DIR);

# HDPI DRAWABLE
DRAWABLE_DIR = BASE_DIR + '-hdpi'
if os.path.exists(DRAWABLE_DIR):
    shutil.rmtree(DRAWABLE_DIR)
os.mkdir(DRAWABLE_DIR);

# XHDPI DRAWABLE
DRAWABLE_DIR = BASE_DIR + '-xhdpi'
if os.path.exists(DRAWABLE_DIR):
    shutil.rmtree(DRAWABLE_DIR)
os.mkdir(DRAWABLE_DIR);

# XXHDPI DRAWABLE
DRAWABLE_DIR = BASE_DIR + '-xxhdpi'
if os.path.exists(DRAWABLE_DIR):
    shutil.rmtree(DRAWABLE_DIR)
os.mkdir(DRAWABLE_DIR);

# Application Path
INKSCAPE_PATH = "C:\Program Files (x86)\Inkscape\inkscape.exe";

# REDIRECT PRINT
print "PROCESSING FOUND .SVG FILES";
LOG_FILE = open('log.txt', 'a');
sys.stdout = LOG_FILE;
print ""
print "#" * 50;

# SCRIPT
if __name__ == '__main__':
    for root, dirs, files in os.walk(INPUT_DIR):
        for f in files:
            SIZE = 0;
            if '.w' in f:
                SIZE = int(f[f.index('.w')+2:][:-4]);
            if f.endswith('.svg'):
                EXPORT_PATH_BASE = (BASE_DIR + '\\' + f[:f.index('.')] + '.png')
                EXPORT_PATH_HDPI = (BASE_DIR + '-hdpi\\' + f[:f.index('.')] + '.png')
                EXPORT_PATH_XHDPI = (BASE_DIR + '-xhdpi\\' + f[:f.index('.')] + '.png')
                EXPORT_PATH_XXHDPI = (BASE_DIR + '-xxhdpi\\' + f[:f.index('.')] + '.png')


                if not SIZE:
                    SIZE = input('"' + f + '" EXPORT SIZE:');
                SIZE_HDPI = (SIZE * 1.5);
                SIZE_XHDPI = SIZE * 2;
                SIZE_XXHDPI = SIZE * 3;

                print '- SVG FOUND -> "' + f + '"!"';
                print '- CREATING ANDROID SIZES!';

                # EXPORT BASE SIZE MDPI
                print '- BASE SIZE 160dpi 1:1'
                print '- FINAL SIZE: -w ' + str(SIZE);
                subprocess.call([INKSCAPE_PATH, '-z', '-f', INPUT_DIR + '\\' + f, '-w ' + str(SIZE), '-j', '-e',
                                 EXPORT_PATH_BASE])

                print '-' * 50;

                # EXPORT HDPI
                print '- HDPI SIZE 160dpi 1:1,5'
                print '- FINAL SIZE: -w ' + str(SIZE_HDPI);
                subprocess.call([INKSCAPE_PATH, '-z', '-f', INPUT_DIR + '\\' + f, '-w ' + str(SIZE_HDPI), '-j', '-e',
                                 EXPORT_PATH_HDPI])

                print '-' * 50;

                # EXPORT XHDPI
                print '- XHDPI SIZE 160dpi 1:2'
                print '- FINAL SIZE: -w ' + str(SIZE_XHDPI);
                subprocess.call([INKSCAPE_PATH, '-z', '-f', INPUT_DIR + '\\' + f, '-w ' + str(SIZE_XHDPI), '-j', '-e',
                                 EXPORT_PATH_XHDPI])

                print '-' * 50;

                # EXPORT XXHDPI
                print '- XHDPI SIZE 160dpi 1:2'
                print '- FINAL SIZE: -w ' + str(SIZE_XXHDPI);
                subprocess.call([INKSCAPE_PATH, '-z', '-f', INPUT_DIR + '\\' + f, '-w ' + str(SIZE_XXHDPI), '-j', '-e',
                                 EXPORT_PATH_XXHDPI])

                print '#' * 50;

    LOG_FILE.close();
