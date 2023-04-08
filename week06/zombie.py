'''
좀비 n명이 직선으로 된 산 길에 일렬로 서 있다.
길 양 끝 지점은 깊이를 알 수 없는 절벽으로 이어져 있다.
각 좀비에 대해 초기 위치와 처음 이동 방향(왼쪽과 오른쪽 방향 중 하나) 정보가 주어진다.
	좀비의 아이디는 0이 아닌 -n부터 n까지의 서로 다른 정수이다
	초기 위치는 정수 좌표로 주어지며 좀비의 위치는 서로 다르다
	왼쪽 방향은 -, 오른쪽 방향은 +를 의미하며 이를 좀비의 아이디 값과 함께 표시한다.
	예를 들어 아이디가 -2라면 2번 좀비의 처음 이동 방향은 왼쪽이라는 의미이고,
	아이디가 5라면 5번 좀비는 오른쪽 방향으로 움직인다는 의미이다.
모든 좀비는 초기 위치에서 처음에 움직일 방향으로 일정한 속력(1거리단위/1초)으로 움직인다.
도중에 두 좀비가 만날 수 있다.
이 경우에는 각자 움직이는 방향과 반대 방향으로 돌아서 계속 움직인다.
단, 만나서 방향을 반대로 바꾸기 위한 시간은 0이라고 가정한다.
길의 양 쪽 끝에 도달해서 더 진행하면 절벽으로 바로 떨어지게 된다.
(만약, 두 좀비가 양쪽 끝에서 동시에 같은 시간에 떨어진다면
부호를 포함한 아이디가 더 작은 좀비가 더 먼저 떨어지는 것으로 가정한다.)

입력:
	첫 줄에 n, L, k 세 정수가 주어진다(각각 좀비 수, 길의 길이, 1과 n 사이의 자연수)
		길의 왼쪽 끝 점의 좌표를 0, 오른쪽 끝 점의 좌표가 L이 된다.
	다음 n개의 줄에는 각 좀비의 초기 위차와 좀비의 아이디(정수)가 주어진다.

출력:
	k번째로 떨어지는 좀비의 아이디를 출력한다.
	(아이디가 음수라면 음수 형식으로, 양수라면 + 부호 없이 값만 출력한다.)
'''

from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()

def drop_zombie():
	zombie = deque()		# 양 옆으로 떨어질 수 있기 때문에 덱으로 선언	
	sorted_lst = []
	ans = []
	
	for _ in range(n):
		loc, i = map(float, input().split())
		zombie.append(i)	# 좀비 순서 저장용
		sorted_lst.append([loc, i] if i < 0 else [L-loc, i])
		# 음수: 왼쪽 이동 -> 그냥 저장
		# 양수: 오른쪽 이동 -> L-idx로 저장
	sorted_lst.sort()	# 빨리 떨어지는 순으로 정렬

	i = 0
	while zombie:
		# 떨어지는 시간이 같음
		if i != n-1 and sorted_lst[i][0] == sorted_lst[i+1][0]:
			# 왼쪽 좀비 id가 더 작은 경우 왼쪽부터 떨어트린다
			if zombie[0] < zombie[-1]:
				ans.append(zombie.popleft())
				ans.append(zombie.pop())
			# 아닌 경우 오른쪽부터
			else:
				ans.append(zombie.pop())
				ans.append(zombie.popleft())
			i += 2	# 좀비 두 마리를 떨어트렸으니 +2
		# 떨어지는 시간이 다름
		else:
			# 음수: 왼쪽
			if sorted_lst[i][1] < 0:
				ans.append(zombie.popleft())
			# 양수: 오른쪽
			else:
				ans.append(zombie.pop())
			i += 1
	print(int(ans[k-1]))

if __name__ == '__main__':
	n, L, k = map(int, input().split())
	drop_zombie()

'''
알고리즘:
	좀비의 위치는 바뀌지만 인덱스는 바뀌지 않는다.

수행시간:
	반복문을 한 번만 돌리나, sort()를 사용하므로 O(nlogn)이다.
'''