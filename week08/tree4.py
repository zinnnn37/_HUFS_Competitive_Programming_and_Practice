from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**8)

def find_depth():
    queue = deque()
    queue.append(1)
    while queue:
        cur = queue.popleft()
        for child in tree[cur]:
            if child not in parent:
                depth[child] = depth[cur] + 1
                parent[child] = cur
                queue.append(child)

def find_common_ancestor():
    for _ in range(q):
        # depth가 같아질 때까지 더 깊은 노드를 끌어올림
        u, v = map(int, input().split())
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

if __name__ == "__main__":
    # 입력 받기
    n, q = map(int, input().split())
    tree = {i: [] for i in range(1, n+1)}
    for _ in range(n-1):
        p, c = map(int, input().split())
        tree[p].append(c)
        tree[c].append(p)
        
    parent = {1: 0}
    depth = {1: 0}
    find_depth()

    find_common_ancestor()