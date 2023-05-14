n, q = map(int, input().split())
tree = {i: [] for i in range(1, n+1)}
for _ in range(n-1):
    p, c = map(int, input().split())
    tree[p].append(c)

for _ in range(q):
    u, v = map(int, input().split())
    path_u = [u]
    while u != 1:
        u = next(node for node, children in tree.items() if u in children)
        path_u.append(u)
    path_u.reverse()

    path_v = [v]
    while v != 1:
        v = next(node for node, children in tree.items() if v in children)
        path_v.append(v)
    path_v.reverse()

    common_ancestor = 1
    for a, b in zip(path_u, path_v):
        if a == b:
            common_ancestor = a
        else:
            break
    print(common_ancestor)
