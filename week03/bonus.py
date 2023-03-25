'''
n개의 정수 값이 저장된 배열 A를 가지고 게임을 한다.
한 번에 하나의 값을 선택해서 A에서 지운다.
A[i]를 선택했다면, A[i]-1 값과 A[i]+1과 같은 값도 찾아 있다면 모두 A에서 지운다
그러면 여러분은 점수 A[i]를 얻는다.
이 과정을 A의 모든 값이 삭제될 때까지 반복한다.
여러분이 얻을 수 있는 최대 점수는 몇 점인가?
	첫 줄에 n(1 <= n <= 100,000) 
	두 번째 줄에 n개의 A[i] 값 (1 <= A[i] <= 100,000)

주의:
	A[i]와 같은 값이 여러 개 있을 수 있다.
	만약, A[i]를 선택해서 지우더라도 같은 값들이 함께 삭제되지는 않는다
	(문제 설명에 그렇게 하라고 되어 있는 게 아니므로)

접근 방법: DP

매우 강력한 힌트
	A[i]가 선택되면 A[i]-1, A[i]+1은 모두 함께 삭제되기 때문에
	A[i]와 같은 값이 나중에 선택되더라도 함께 삭제될 A[i]-1, A[i]+1 값은 없다.
	그냥 그 값만 삭제되고 그 만큼 포인트를 얻게 된다.
	그래서 A에 등장하는 값이 몇 번씩 등장하는지 세서 저장해 놓으면 매우 유용하게 사용할 수 있다.
	포인트를 최대화해야 하기 때문에 현재 범위에서 가장 큰 값부터 선택을 고려하면 된다.
	(가장 큰 값 + 1)이 없기 때문에 제거될 수가 더 적기 때문이다.
	결국, 현재 값 중에서 가장 큰 값인 k를 선택했다면
	이후에 선택될 k와 같은 값에 대한 포인트까지 함께 고려하면
	k * (k의 개수)만큼의 포인트를 얻는다.
	여기에 k-1은 (있다면) 삭제되어 이후 선택에는 고려하지 않아야 하기에
	k-2 이하의 값들에 대해 부문제를 풀면 된다.

시간을 줄일 수 있는 힌트:
	DP 점화식을 세워보자.
	점회식에 max(DP[a], ..., DP[b])가 포함되어 있다면, 특정 구간의 최대값이 된다.
	특정 구간의 최대값을 연속해서 구해야 하는데, 효율적인 방법은? [sliding window 방법?]
'''
'''
from heapq import heapify, heappop
import sys
input = lambda: sys.stdin.readline().rstrip()

def deal_cnt():
	pre = nums[0]
	for _ in range(n):
		cur = heappop(nums)
		if pre < cur:
			cnt.append([0, 0])
			cnt[-1][1] = cur
		cnt[-1][0] += cur
		pre = cur

def do_dp():
	length = len(cnt)
	if length == 1:
		print(cnt[0])
	else:
		dp = [0] * length
		dp[-1] = cnt[-1][0]
		if abs(cnt[-1][1] - cnt[-2][1]) != 1:
			dp[-2] = dp[-1] + cnt[-2][0]
		else:
			dp[-2] = max(dp[-1], cnt[-2][0])
		for i in range(length - 3, -1, -1):
			if abs(cnt[i + 2][1] - cnt[i + 1][1]) != 1:
				dp[i] = dp[i + 2] + dp[i + 1]
			else:
				dp[i] = max(dp[i + 2] + cnt[i][0], dp[i + 1])
		print(dp[0])

if __name__ == '__main__':
	n = int(input())
	nums = list(map(int, input().split()))
	heapify(nums)

	cnt = [[0, nums[0]]]
	deal_cnt()

	do_dp()
'''
import sys
input = lambda: sys.stdin.readline().rstrip()

# 동일한 수가 몇 개씩 입력되었는지 확인
def deal_cnt():
	for n in nums:
		cnt[n] += 1

def do_dp():
	dp = [0] * 100001
	# 제일 큰 수와 두 번째로 큰 수를 선택했을 때의 점수
	dp[100000] = cnt[100000] * 100000
	dp[99999] = cnt[99999] * 99999

	# 점화식
	for i in range(99998, -1, -1):
		dp[i] = max(dp[i + 1], dp[i + 2] + cnt[i] * i)
	
	return dp[0]

if __name__ == '__main__':
	n = int(input())
	nums = list(map(int, input().split()))
	cnt = [0] * 100001
	deal_cnt()
	print(do_dp())

'''
점화식:
	DP[i] = max(DP[i + 2] + cnt[i] * i, DP[i + 1])
	(i + 2를 골랐을 때의 점수) + (i를 골랐을 때의 점수)와
	(i + 1을 골랐을 때의 점수) 중 더 큰 수가 DP[i]의 값이 된다.

설명:
	deal_cnt()를 통해 입력받은 숫자 배열에 공통된 숫자가 몇 개 있는지 구한다.
	이 때, 인덱스가 숫자이고 값이 갯수가 된다.
	([1, 1, 5, 3, 2]가 들어왔다면 [0, 2, 1, 1, 0, 1])

	do_dp()에서 반복문을 통해 dp 배열을 완성한다.
	반복문 진행하기 전 초기값으로 dp[100000]과 dp[99999]를
	각각 100000을 선택했을 때와 99999를 선택했을 때의 점수로 설정한다.
	이후 반복문 내에서 점화식을 바탕으로 dp 배열에 값을 채워넣는다.
	dp 배열의 마지막 인덱스부터 채웠으므로
	가장 첫 번째 인덱스에 저장된 값이 최대 점수가 된다.

수행시간:
	입력값의 크기과 관계없이 수행시간이 일정하므로 O(1)의 시간복잡도를 가진다.
'''