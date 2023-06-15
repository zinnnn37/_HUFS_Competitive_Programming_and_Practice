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

'''
일반적인 stack의 연산을 수행하는 스택과
최대값을 저장하는 스택 총 두 개로 구현할 수 있다.

일반 스택에 push() 연산을 수행할 때,
최대값을 저장하는 스택에도 push() 연산을 수행한다.
이 때, 최대값을 저장하는 스택의 top이 push()하는 값보다 작거나 같다면
push()하는 값이 최대값이므로 최대값을 저장하는 스택에도 push()한다.
그렇지 않은 경우 push()연산을 수행하지 않는다.
pop() 연산을 수행할 때, 일반 스택에서 pop() 하려는 요소가 최대값인지 확인한다.
만약 최대값이라면 최대값을 저장하는 스택에서도 pop() 연산을 수행한다.

이런 식으로 max()의 시간복잡도를 O(1)로 구현할 수 있다.
'''

import sys

class Stack:
	def __init__(self):
		self.stack = []	# 일반 스택
		self.maximum = []	# 최대값을 저장하는 스택

	def push(self, x):
		self.stack.append(x)
		if len(self.maximum) == 0 or self.maximum[-1] <= x:
		# 최대값을 저장하는 스택이 비어있거나, top이 x보다 작거나 같다면(x가 최대값이라면) append()
			self.maximum.append(x)

	def pop(self):
		if len(self.stack) == 0:
			print('EMPTY')
		else:
			if self.stack[-1] == self.maximum[-1]:
			# pop() 하려는 요소가 최대값인 경우 최대값을 저장하는 스택도 함께 pop()
				self.maximum.pop()
			print(self.stack[-1])
			return self.stack.pop()
	
	def max(self):
		if len(self.maximum) == 0:
			print('EMPTY')
		else:	# 최대값을 저장하는 스택의 top을 출력
			print(self.maximum[-1])
			return self.maximum[-1]

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