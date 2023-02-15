import collections
import os
import sys
import string

script_name = sys.argv[0]

try:
    textfile = sys.argv[1]
    n = int(sys.argv[2])
    with open(textfile, "r", encoding = "utf_8") as f:
        data = f.read()

        l = collections.Counter(data.split()).most_common(n)

        print(l)

    #print(data)
except IndexError:
    print('Usage: %s TEXTFILE' % script_name)
except IOError:
    print('"%s" cannot be opened.' % textfile)