from collections import deque

# 재귀 돌면서 부트리 합 구하기
def query_subtree(v):
    res = w[v]
    for child in tree[v]:
        res += query_subtree(child)
    return res

# 가중치 배열 업데이트
def query_update(v, d):
    w[v] += d

if __name__ == "__main__":
    n, q = map(int, input().split())
    w = [0] + list(map(int, input().split()))
    tree = [[] for _ in range(n+1)]
    
    for _ in range(n-1):
        p, c = map(int, input().split())
        tree[p].append(c)
        
    for _ in range(q):
        cmd, *v = input().split()
        v = list(map(int, v))
        if cmd == 'subtree':
            print(query_subtree(v[0]))
        elif cmd == 'update':
            query_update(v[0], v[1])
            
'''
수행시간:
	query_subtree() 함수에서 자식 노드를 한 번씩 방문하므로 O(n)시간이 소요되고
	query_update() 함수에서 인덱스를 통해 가중치 배열을 업데이트하므로 O(1)시간이 소요된다.
	따라서 총 수행시간은 O(n)이다.
'''