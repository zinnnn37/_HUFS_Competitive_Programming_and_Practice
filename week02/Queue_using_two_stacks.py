'''
Stack은 Last In First Out(LIFO)의 원칙에 따라
데이터가 삽입, 삭제되는 배열 기반 자료구조이다.
Queue는 First In First Out(FIFO)의 원칙에 따라
데이터가 삽입, 삭제되는 배열 기반 자료구조이다.
Stack과 Queue의 삽입과 삭제 연산은 모두 O(1) 시간에 동작한다.

Stack 2개를 사용해서 Queue 1개를 구현할 수 있을까?
어떻게 해야 하는지 구체적으로 설명해보자.
당연히 enqueue와 dequeue연산 모두 평균적으로 O(1)시간에 동작함을 보장해야 한다!

구현: 두 개의 스택은 두 개의 배열 또는 리스트(python)를 사용해 구현한다.
입력: 연산 명령을 문자열로 연속적으로 입력 받아 각 연산에 맞게 처리한다.

연산의 종류는 아래와 같다.
1. enq x	# 정수 값 x를 큐에 enqueue한다.
2. deq		# 큐의 값을 dequeue한 후 그 값을 프린트한다. 만약, 큐가 비었다면 EMPTY를 출력한다.
3. exit		# 연산 처리를 끝낸다.
'''

'''
스택에 넣은 요소를 그대로 pop 해서 다른 스택에 push하면
원래의 스택과는 반대의 방향으로 요소가 쌓이게 된다.
즉, 가장 먼저 push된 요소가 top에 위치하게 된다.
이러한 방식으로 스택을 두 개 사용하여 큐를 구현할 수 있다.

enqueue, dequeue 모두 평균적으로 O(1) 시간에 동작한다.
그러나 dequeue는 최악의 경우 O(n) 시간이 걸릴 수 있다.
이는 s2가 비어있는 경우 s1에 있는 모든 요소를 s2로 옮긴 후 dequeue를 수행하기 때문이다.
'''

import sys

class QueueUsingStack:
	def __init__(self):
		self.s1 = []	# enqueue할 때 사용할 스택
		self.s2 = []	# dequeue할 때 사용할 스택

	def enq(self, x):	# s1에 x를 enqueue한다.
		self.s1.append(x)
	
	def deq(self):		# s2에서 dequeue한다.
		if len(self.s1) == 0 and len(self.s2) == 0:
		# 스택이 두 개 다 비었다면 큐도 비었다는 뜻이다.
			print('EMPTY')
			return
		elif len(self.s2) == 0:
		# s2만 비었다면 s1에 있는 모든 요소를 s2로 옮긴다(최악의 경우)
			while len(self.s1) != 0:
				self.s2.append(self.s1.pop())
		print(self.s2[-1])
		return self.s2.pop()

if __name__ == '__main__':
	q = QueueUsingStack()
	for line in sys.stdin:
		cmd = line.split()
		if cmd[0] == 'enq':
			q.enq(int(cmd[1]))
		elif cmd[0] == 'deq':
			q.deq()
		elif cmd[0] == 'exit':
			break
