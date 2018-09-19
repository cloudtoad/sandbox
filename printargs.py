#! /usr/bin/python2.7

import sys
import json


def out(*args):
    if sys.stdout.isatty():
        for key in args[0].keys():
            print key + ": " + ", ".join(args[0][key])
    else:
        print json.dumps(args[0])


def myfunc(*args):
    out(args[0])


myfunc_args = dict()

if not sys.stdin.isatty():
    for line in sys.stdin:
        lined = json.loads(line)
        for k, v in lined.items():
            if k in myfunc_args:
                myfunc_args[k] += v
            else:
                myfunc_args[k] = v

for arg in sys.argv[1:]:
    kvp = arg.split("--", 1)[1].split("=", 1)
    k = kvp[0]
    v = kvp[1].split(",")
    if k in myfunc_args:
        myfunc_args[k] += v
    else:
        myfunc_args[k] = v

myfunc(myfunc_args)
