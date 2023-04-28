'''
0부터 n-1까지 서로 다른 수로 구성된 순열 A에 대해
새로운 리스트 S와 L을 준비했다.
	S[i] = A[0]부터 A[i-1]까지 수 중에서 A[i]보다 작은 수의 개수(S[0] = 0)
	L[i] = A[i+1]부터 A[n-1]까지 수 중에서 A[i]보다 큰 수의 개수(L[n-1] = 0)
실수로 리스트 A를 잃어버려서 S와 L만 가지고 있다.
여러분은 S, L을 이용해 A를 재구성해야한다.

입력
	첫 줄에 리스트 S의 n개의 값, 첫 줄에 리스트 L의 n개의 값
	n의 값은 1 이상 1000 이하

출력
	print(A)
'''

def reconstruct(S, L):
	# S, L로부터 A를 재구성해 리턴
	# 이 함수를 작성합니다~
	n = len(S)
	A = []
	for i in range(n):
		A.append(n + S[i] - L[i] - i - 1)
	return A

# S와 L을 차례로 읽어들임
S = [int(x) for x in input().split()]
L = [int(x) for x in input().split()]
A = reconstruct(S, L)
print(A)

# 1. 본인이 작성한 알고리즘의 수행시간을 간략히 분석해보자
# 
# 2. 수행시간 T(n)을 Big-O료 표기해보자
# 