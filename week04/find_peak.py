import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**8)

def find_peak(start, end):
	if start == end:
		print(start)
		return
	mid = (start + end) // 2
	print(mid)
	if nums[mid] > nums[mid + 1]:
		find_peak(start, mid)
	else:
		find_peak(mid + 1, end)

if __name__ == '__main__':
	nums = list(map(int, input().split()))
	find_peak(0, len(nums)-1)