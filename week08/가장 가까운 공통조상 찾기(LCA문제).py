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

'''
수행시간:
	find_depth() 함수에서 자식 노드를 한 번씩 방문하므로 O(n)시간이 소요된다.
	find_common_ancestor() 함수에서 depth가 같아질 때까지 노드를 끌어올리는 작업은 최악의 경우 O(n)시간이 소요되고,
    depth가 같아진 상태에서 한 번에 끌어올리는 작업 또한 최악의 경우 O(1/2 * n)시간이 소요된다.
    (루트 노드를 기준으로 노드가 두 쪽으로 퍼져있는 경우)
    이를 쿼리의 수만큼 반복하므로 find+common_ancestor() 함수의 총 수행시간은 O(q * 2n) = O(qn)이다.
    따라서 코드의 총 수행시간은 O(n + qn) = O(qn)이다.
'''