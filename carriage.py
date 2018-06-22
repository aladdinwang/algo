# coding: utf-8

from collections import deque
def feasible(a, b):
    q1 = deque()
    q2 = deque()

    def find(x):
        for q in [q1, q2]:
            if q and q[0] == x:
                q.popleft()
                return True
        if not a or x < a[0]:
            return False
        if all((q1, q2)):
            return False

        q = filter(None, [q1, q2])
        if not q:
            q = q1

        i = x - a[0]            
        q.extend(a[:i])
        del a[:i+1]
        return True
    for x in b:
        if not find(x):
            return False
        
    return True


print feasible(range(1, 6), [3, 4, 2, 1, 5])
print feasible(range(1, 6), [3, 4, 1, 5, 2])
