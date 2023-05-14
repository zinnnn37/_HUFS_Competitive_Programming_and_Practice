from collections import deque
from math import log2, ceil

def update(v, d):
    while v <= n:
        bit[v] += d
        v += v & -v

def query(v):
    res = 0
    while v > 0:
        res += bit[v]
        v -= v & -v
    return res

if __name__ == "__main__":
    n, qu = map(int, input().split())
    w = [0] + list(map(int, input().split()))
    tree = [[] for _ in range(n+1)]
    for _ in range(n-1):
        p, c = map(int, input().split())
        tree[p].append(c)
        tree[c].append(p)
        
    lg = ceil(log2(n))

    parent = [[0]*(lg+1) for _ in range(n+1)]
    depth = [0]*(n+1)
    order = []
    q = deque([1])
    while q:
        v = q.popleft()
        order.append(v)
        for child in tree[v]:
            if child != parent[v][0]:
                parent[child][0] = v
                depth[child] = depth[v] + 1
                q.append(child)
    for i in range(1, lg+1):
        for v in range(1, n+1):
            parent[v][i] = parent[parent[v][i-1]][i-1]

    left = [0]*(n+1)
    right = [0]*(n+1)
    for i, v in enumerate(order):
        left[v] = i+1
    for i in range(n, 0, -1):
        v = order[i-1]
        right[v] = i

    bit = [0]*(n+1)
    for i, v in enumerate(order):
        update(i+1, w[v])

    for _ in range(qu):
        cmd, *v = input().split()
        v = list(map(int, v))
        if cmd == 'subtree':
            res = query(right[v[0]]) - query(left[v[0]]-1)
            print(res)
        elif cmd == 'update':
            d = v[1] - w[v[0]]
            w[v[0]] = v[1]
            update(left[v[0]], d)
            update(right[v[0]]+1, -d)
