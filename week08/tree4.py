# 입력 받기
n, q = map(int, input().split())
tree = {i: [] for i in range(1, n+1)}
for _ in range(n-1):
    p, c = map(int, input().split())
    tree[p].append(c)

# LCA 구하기
parent = {1: 0}
depth = {1: 0}
stack = [1]
while stack:
    curr = stack[-1]
    if tree[curr]:
        child = tree[curr].pop()
        if child not in parent:
            depth[child] = depth[curr] + 1
            parent[child] = curr
            stack.append(child)
    else:
        stack.pop()

for _ in range(q):
    u, v = map(int, input().split())
    # depth가 같아질 때까지 더 깊은 노드를 끌어올림
    while depth[u] != depth[v]:
        if depth[u] > depth[v]:
            u = parent[u]
        else:
            v = parent[v]
    # depth가 같아진 상태에서 한 번에 끌어올림
    while u != v:
        u = parent[u]
        v = parent[v]
    print(u)