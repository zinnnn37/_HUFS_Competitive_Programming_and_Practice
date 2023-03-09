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
A를 정렬한 후 중간값을 기준으로 왼쪽과 오른쪽을 나눈다.
이 때, A의 길이가 홀수라면 중간값을 구한 후 +1을 해준다.
배열의 왼쪽은 B의 홀수번째 인덱스에, 오른쪽은 B의 짝수번째 인덱스에 차례대로 넣는다.
배열의 길이가 홀수라면, 오른쪽 배열의 길이가 왼쪽 배열의 길이보다 1만큼 작으므로
i == mid - 1 and length % 2 == 1일 때(A의 길이가 홀수이고 왼쪽의 마지막 요소를 append했을 때)
append 연산은 진행하지 않는다.

Big-O 분석
파이썬은 Timsort를 사용하므로 A를 정렬하는데 O(nlogn)의 시간이 소요된다.
len()과 append() 연산은 O(1)의 시간이 소요되므로
이 코드의 시간복잡도는 O(nlogn)이다.
'''


def solve(A):
	# return a list B such that B[0] <= B[1] >= B[2] <= B[3] ...\
	B = []
	length = len(A)
	# 중간값 구하기
	if length % 2 == 0:
		mid = length // 2
	else:
		mid = length // 2 + 1
	A.sort()

	for i in range(mid):
		# 왼쪽 요소를 B에 추가
		B.append(A[i])
		if i == mid - 1 and length % 2 == 1:
			# i == mid - 1: 왼쪽의 마지막 요소를 append 했고
			# length % 2 == 1: A의 길이가 홀수라면 append 연산을 진행하지 않는다.
			break
		# 오른쪽 요소를 B에 추가
		B.append(A[i + mid])
		i += 1
	return B

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