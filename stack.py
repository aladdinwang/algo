# coding: utf-8

a = []
a.append(1)
a.append(2)

import sys

while True:
    print '------'
    a = sys.stdin.readlines()
    print a
    for i in a:
        print i
