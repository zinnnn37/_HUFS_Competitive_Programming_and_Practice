def updatefen(i):
	while i<=M:
		fen[i] += 1
		i += i&-i

def sumfen(i):
	SUM = 0
	while i:
		SUM += fen[i]
		i -= i&-i
	return SUM

def find(x,i,c):
	s = i-1-sumfen(i)
	if x==s and not seq[i]:
		return i
	if x>s:
		return find(x,i+(1<<c),c-1)
	return find(x,i-(1<<c),c-1)

#N = int(input())
M = 1<<17
data = [*map(int,input().split())]
N = len(data)
seq = [0]*(N+1)
fen = [0]*(M+1)
for i in range(1,N+1):
	idx = find(data[-i],M,16)
	seq[idx] = N+1-i
	updatefen(idx)
print(*reversed(seq[1:]))