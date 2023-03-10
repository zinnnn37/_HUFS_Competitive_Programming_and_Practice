'''
[배열, 스캔] 오르락 내리락~
n개의 정수를 배열 A에 저장한다.
A의 값을 재배치해서 새로운 배열 B를 만드는데,
B[0] <= B[1] >= B[2] <= B[3] >= B[4] <= ... 이 만족하도록 B를 만들어라.
2 <= n <= 100,000
당연히 정답은 유일하지 않다.

solve 함수는 A를 입력으로 받아 위의 조건을 만족하는 B를 리턴한다.
이 배열 B가 조건에 맞는지 검사하는 check 함수를 호출해 그 결과를 출력한다.
(check 함수와 입력 처리 코드는 수정하지 않는다)

- 주석 필요: 알고리즘의 수행시간을 분석하고 Big-O로 표기하여라

예: A = [1, 3, 4, 9, 2] 인 경우에 B = [1, 4, 3, 9, 2]가 답이 될 수 있고,
B = [1, 3, 2, 9, 4]도 답이다.
'''

'''
A를 순차적으로 탐색하면서 조건에 맞게끔 swap한다.
i가 홀수이고 A[i] < A[i+1]이라면 swap하고,
i가 짝수이면서 A[i] > A[i+1]라면 swap한다.
마지막 인덱스의 값은 비교할 대상이 없으므로 (A의 길이) - 1만큼만 반복문을 돌린다.

Big-O: O(n)
반복문을 한 번 진행하므로 시간복잡도는 O(n)이다.
'''


def solve(A):
	for i in range(len(A)-1):
		if i % 2 == 1 and A[i] < A[i+1]:	# 인덱스가 홀수인 경우 다음 인덱스의 값이 더 작아야 한다.
			A[i], A[i+1] = A[i+1], A[i]
		if i % 2 == 0 and A[i] > A[i+1]:	# 인덱스가 짝수인 경우 다음 인덱스의 값이 더 커야 한다.
			A[i], A[i+1] = A[i+1], A[i]
	return A

def check(B):
	if not (B[0] <= B[1]): return False
	for i in range(1, len(B)-1):
		if i%2 == 1 and not (B[i] >= B[i+1]):
			return False
		if i%2 == 0 and not (B[i] <= B[i+1]):
			return False
	return True		
	
A = [int(x) for x in input().split()]
B = solve(A)
print(check(B))