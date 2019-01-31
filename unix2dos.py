import os
import sys


def err_exit(msg):
    if msg: print('%s' % msg)
    sys.exit(0)


def getfiles(root):
    for dirpath, dirnames, filenames in os.walk(root):
        for filename in filenames:
            yield os.path.join(dirpath, filename)


def format_file(file, toformat='dos2unix'):
    print('Formatting %s:\t%s' % (toformat, file))
    if not os.path.isfile(file):
        print('ERROR: %s invalid normal file' % file)
        return
    if toformat == 'unix2dos':
        line_sep = '\r\n'
    else:
        line_sep = '\n'
    with open(file, 'r') as fd:
        tmpfile = open(file + toformat, 'w+b')
        for line in fd:
            line = line.replace('\r', '')
            line = line.replace('\n', '')
            tmpfile.write(line.encode(encoding="utf-8") + line_sep.encode(encoding="utf-8"))
        tmpfile.close()
        # os.rename(file + toformat, file)


def uni_format_proc(filename, toformat):
    if not toformat or toformat not in ['unix2dos', 'dos2unix']:
        err_exit('ERROR: %s: Invalid format param' % (toformat))
    if not filename or not os.path.exists(filename):
        err_exit('ERROR: %s: No such file or directory' % (filename))
    if os.path.isfile(filename):
        format_file(filename, toformat)
        return
    if os.path.isdir(filename):
        for file in getfiles(filename):
            uni_format_proc(file, toformat)
