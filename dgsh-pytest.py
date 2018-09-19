#!/usr/bin/python2.7
import json
import sys

for arg in sys.argv[1:]:

    print arg
    # kvp = arg.split("--", 1)[1].split("=", 1)
    # k = kvp[0]
    # v = kvp[1].split(",")
    # if k in myfunc_args:
    #     myfunc_args[k] += v
    # else:
    #     myfunc_args[k] = v
