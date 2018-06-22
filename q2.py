# coding: utf-8

import sys


n, m, c = map(int, sys.stdin.readline().split())
colors = []
s1 = {}.fromkeys(range(1, c + 1), 0)
s2 = {}.fromkeys(range(1, c + 1), 0)
for i in range(n):
    r = map(int, sys.stdin.readline().split())
    for j in range(r[0]):
        c = r[1 + j]
        if j - s2[c] > m:
            s1[c] = 1
            s2[c] = j
        else:
            s2[c] += 1

        if c not in colors and s2[c] > 1:
            colors.append(c)


print len(colors)

