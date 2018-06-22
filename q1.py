# coding: utf-8
import sys
import math

lines = sys.stdin.readlines()
n = int(lines[0])
bsize = int(math.sqrt(n))
a = map(int, lines[1].split())


class Query(object):
    def __init__(self, id_, left, right, k):
        self.id = id_
        self.left, self.right = left - 1, right - 1
        self.k = k
        self.block = left / bsize

m = int(lines[2])
qs = []
for i in range(m):
    left, right, k = map(int, lines[i + 3].split())
    qs.append(Query(i, left, right, k))

qs.sort(key=lambda x: (x.block, x.right))

buf = {}
ans = [0] * m
def insert(x):
    if x in buf:
        buf[x] += 1
    else:
        buf[x] = 1


def erase(x):
    buf[x] -= 1
    if(buf[x] == 0):
        del buf[x]



left = right = 0
insert(a[0])
for i in range(m):
    q = qs[i]
    while right < q.right:
        right += 1
        insert(a[right])
    while left > q.left:
        left -= 1
        insert(a[left])
    while right > q.right:
        erase(a[right])
        right -= 1
    while left < q.left:
        erase(a[left])
        left += 1
    ans[q.id] = buf.get(q.k, 0)

for i in ans:
    print i


