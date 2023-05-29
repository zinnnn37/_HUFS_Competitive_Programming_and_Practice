def query(x):
	sum = 0
	i = x
	while i >= 1:
		sum += T[i]
		i -= i & (-i)
	return sum  

def update(x, val):
	i = x
	while i <= MAX_RANGE:
		T[i] += val
		i += i & (-i)

MAX_RANGE = 1000000
n = int(input())
P = [int(x) for x in input().split()]
Q = [int(x) for x in input().split()]
A = list(zip(P, Q))
A.sort(key=lambda x: (x[0], -x[1]))
T = [0] * (MAX_RANGE+1)

# L[i] = number of values less than A[i] for A[0][1] ... A[i-1][1]
L = [0] * n
R = [0] * n
for i in range(n):
    L[i] = query(A[i][1]-1) # count for 1 <= values < A[i][1]
    update(A[i][1], 1)
    
T = [0] * (MAX_RANGE+1)
for i in range(n):
    R[i] = query(A[i][1]-1)
    update(A[i][1], L[i])

print(sum(R))