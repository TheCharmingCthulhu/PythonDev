# IMPORTS
import os, sys

# FUNCTIONS
def Substring(length):
    for root, dirs, files in os.walk('..\\res'):
        if 'drawable' in root:
            for f in files:
                os.rename("{0}\\{1}".format(root, f), "{0}\\{1}".format(root, f[int(length)+1:]))

# VARIABLES & CONSTANTS
PREFIX = raw_input('ENTER PREFIX or -REMOVE:')
if PREFIX == '-(R)EMOVE' or PREFIX == '-R':
    PREFIX_LENGTH = raw_input('PREFIX CHARACTER LENGTH:')
    Substring(PREFIX_LENGTH);
    sys.exit(0)


IGNORED_FILES = ['thumbs.db']
FIXED_KEYS = {'ico': 'icon',
              'iconn': 'icon'}

# SCRIPT
if __name__ == '__main__':
    FULL_PREFIX = PREFIX + '_'
    for root, dirs, files in os.walk('..\\res'):
        if 'drawable' in root:
            for f in files:
                if not f.startswith(FULL_PREFIX):
                    if not f in IGNORED_FILES:
                        try:
                            print "Renamed file " + f;
                            os.rename("{0}\\{1}".format(root, f), "{0}\\{1}{2}".format(root, FULL_PREFIX, f).lower());
                        except:
                            print "Couldn't rename " + f + ", skipping."
                            continue

                for key in FIXED_KEYS:
                    if key in f:
                        if not f in IGNORED_FILES:
                            try:
                                print "Renamed file " + f;
                                os.rename("{0}\\{1}".format(root, f), "{0}\\{1}".format(root, f.replace("{0}{1}{0}".format('_', key), "{0}{1}{0}".format('_', FIXED_KEYS[key]))))
                            except:
                                print "Couldn't rename " + f + ", skipping."
                                continue;

    raw_input('Press an key to continue...');
