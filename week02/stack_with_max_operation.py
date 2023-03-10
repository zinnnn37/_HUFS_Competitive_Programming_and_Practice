'''
Stack은 Last In First Out(LIFO)의 원칙에 따라
데이터가 삽입, 삭제되는 배열 기반 자료구조이다.
Stack의 삽입과 삭제 연산은 모두 O(1) 시간에 동작한다.

삽입과 삭제 연산 이외에 max 연산을 지원하고 싶다.
max 연산은 현재 stack에 있는 값 중에서 최대값을 찾아 리턴하는 것이다.
push, pop은 모두 O(1) 시간에 동작해야 하고,
max 연산은 평균적으로 O(1) 시간에 동작함을 보장해야 한다.

구현: 스택을 최대 2개를 사용해 구현이 가능하다!
입력: 연산 명령을 문자열로 연속적으로 입력 받아 각 연산에 맞게 처리한다.
연산의 종류는 아래와 같다.

1. push x: 정수 값 x를 스택에 push한다.
2. pop: 스택의 값을 pop한 후 그 값을 프린트한다. 만약 스택이 비어있다면 EMPTY를 출력한다.
3. max: 스택에 있는 값 중 최대값을 찾아 프린트한다. 만약 스택이 비어있다면 EMPTY를 출력한다.
4. exit: 명령 처리를 종료한다.
'''

import sys

class Stack:
	def __init__(self):
		self.s1 = []	# 일반 스택
		self.s2 = []	# 최대값을 저장하는 스택

	def push(self, x):
		self.s1.append(x)
		if len(self.s2) == 0 or self.s2[-1] <= x:
		# 최대값을 저장하는 스택이 비어있거나, top이 x보다 작다면(x가 최대값이라면) append()
			self.s2.append(x)

	def pop(self):
		if len(self.s1) == 0:
			print('EMPTY')
		else:
			if self.s1[-1] == self.s2[-1]:
			# pop() 하려는 요소가 최대값인 경우 최대값을 저장하는 스택도 함께 pop()
				self.s2.pop()
			print(self.s1[-1])
			return self.s1.pop()
	
	def max(self):
		if len(self.s2) == 0:
			print('EMPTY')
		else:	# 최대값을 저장하는 스택의 top을 출력
			print(self.s2[-1])
			return self.s2[-1]

if __name__ == '__main__':
	s = Stack()
	for line in sys.stdin:	# EOF까지 한 줄씩 입력 받음
		cmd = line.split()
		if cmd[0] == 'push':
			s.push(int(cmd[1]))
		elif cmd[0] == 'pop':
			s.pop()
		elif cmd[0] == 'max':
			s.max()
		elif cmd[0] == 'exit':
			break;