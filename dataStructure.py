# 자료구조
# 정의
# 대량의 데이터를 효율적으로 관리할 수 있도록 하는 데이터의 구조를 의미함
# 데이터 특성에 따라서, 체계적인 데이터 구조화가 필요하며, 이러한 데이터 구조는 코드의 효율성, 성능을 결정

# 종류
# 대표적인 자료구조로는 배열(Array), 스택(Stack), 큐(Queue), 링크드 리스트(Linked List), 해쉬 테이블(Hash Table), 힙(Heap)

# Python 에서는 대표적으로 List, tuple, set, dictionary 가 존재하고 자료구조 대부분 모두 구현 가능

# 배열 
# 배열은 같은 종류의 데이터를 순차적으로 저장하는 자료구조
# Python 에서는 list로 구현되어 있음
# index를 통해 직접 접근 가능
# 빠른 접근이 가능함
# 데이터 추가와 삭제에 비용이 많이 사용됨. 데이터 추가시, 공간이 많이 필요하고, 삭제시 빈 공간이 생겨 이를 관리해주어야 함. 길이 조절이 어려움

# 예제 : 특정 Alphabet 빈도수 측정 함수
# 특정 데이터 세트에서 특정한 알파벳이 몇번이나 사용되었는지를 찾아보는 함수를 작성

def find_alphabet(dataset, alpabet):
    count = 0
    for data in dataset:
        for i in range(len(data)):
            if data[i] == alpabet:
                count += 1
    print(count)

d = 'asdasdasdasdasdasdasd'
a = 'a'
find_alphabet(d, a)

# 큐(Queue)
# 먼저 넣은 데이터를 가장 먼저 꺼내는 데이터 구조
# FIFO(First-In, First-Out : 선입선출) 또는 LILO(Last-In, Last-Out) 방식 사용

# 기능
# Enqueue : 큐에 데이터를 넣는 기능을 의미 python list 의 appen() 매서드와 유사
# Dequeue : 큐에서 데이터를 꺼내는 기능을 의미 python list 의 pop(0) 매서드와 유사

# 종류
# Python에서는 Queue 라이브러리를 제공함 하지만 대부분의 큐와 관련된 자료구조는 list를 통해 구현 가능

import queue

# Queue() : 일반적인 큐 자료구조
data_queue = queue.Queue()
data_queue.put(1) # 1 
data_queue.put(2) # 1 - 2
data_queue.put(3) # 1 - 2 - 3
data_queue.get() # 1 출력
data_queue.get() # 2 출력

# LifoQueue() : 나중에 입력된 데이터가 먼저 출력되는 구조 (Stack) 구조
data_LifoQueue = queue.LifoQueue()
data_LifoQueue.put(1) # 1
data_LifoQueue.put(2) # 2 - 1
data_LifoQueue.put(3) # 3 - 2 - 1
data_LifoQueue.get() # 3 출력
data_LifoQueue.get() # 2 출력

# PriortyQueue() : 데이터마다 우선순위를 지정하여, 정령된 큐로, 우선순위 높은 순으로 출력하는 자료 구조
data_PriorityQueue = queue.PriorityQueue()
data_PriorityQueue.put((10, 1)) # (10, 1)
data_PriorityQueue.put((5, 2)) # (5, 2) - (10 , 1)
data_PriorityQueue.put((15, 3)) # (5, 2) - (10, 1) - (15, 3)
data_PriorityQueue.get() # (5, 2) 출력
data_PriorityQueue.get() # (10, 1) 출력

# 큐는 멀티 테스킹을 위한 프로세스 스케쥴링 방식에 사용됨

# 리스트로 Queue 구현
class ListQueue:
    def __init__(self):
        self.my_list = list()
    def put(self, element):
        self.my_list.append(element)
    def get(self):
        return self.my_list.pop(0)
    def qsize(self):
        return len(self.my_list)
# 간단하게 Enqueue 기능을 가지는 put 메서드, Dequeue 기능을 가진 get 메서드, 큐의 길이를 반환하는 qsize 메서드를 구현한 코드

# 리스트로 PriorityQueue 구현
class ListPriorityQueue:
    def __init__(self):
        self.my_list = list()
    def put(self, element):
        self.my_list.append(element)
        self.my_list.sort(key = lambda x: x[0])

    def get(self):
        return self.my_list.pop(0)

    def qsize(self):
        return len(self.my_list)

# list 의 메소드 중 하나인, sort를 이용하여 구현 , lambda 함수를 사용하여 첫 번째 원소가 작은 순서로 우선순위 정렬


# Stack
# 가장 나중에 쌓은 데이터를 가장 먼저 뺼 수 있는 데이터 구조
# LIFO(Last-In, First-Out) 방식을 사용하는 구조
# 스택은 내부 프로세스 구조 함수의 동작 방식으로 사용

# 기능
# push() : 데이터를 스택에 쌓는 기능을 의미. python list의 append 메서드와 같음
# pop() : 데이터를 스택에서 꺼내는 기능을 의미 python list 에 같은 메서드가 있음

data_stack = list()
data_stack.append(1) # [1]
data_stack.append(2) # [1 2]
data_stack.pop() # 2 출력

# 장단점

# 장점
# 구조가 단순, 구현 쉬움
# 데이터 저장 , 불러오기 속도 빠름

# 단점
# 데이터 최대 개수를 사전에 정해 주어야함 (python 재귀 함수는 1000번 까지 가능)
# 저장 공간 낭비가 발생할 수 있음. (미리 최대 갯수를 넣을 공간을 확보하기 때문)

# 단점이 상당히 크기 때문에 보통 배열로 대체하여 사용

# 리스트로 스택 구현
class ListStack:
    def __init__(self):
        self.my_list = list()
    def push(self, data):
        self.my_list.append(data)
    def pop(self):
        return self.my_list.pop()

# Linked List
# 연결 리스트라고도 불리는 링크드 리스트는 배열과 달리 연결되지 않고, 떨어진 곳에 존재하는 데이터를 경로로 지정하여 관리하는 데이터 구조. 파이썬에서는 리스트 자료구조가 링크드 리스트 기능을 모두 지원함

# 기능
# Node : 데이터 저장 단위로, 데이터 값 + 포인터로 구성되어있음
# Pointer : 각 노드 안에서, 다음이나 이전의 노드의 주소를 가지는 값을 의미함

# 장단점

# 장점 
# 미리 데이터 공간을 미리 할당할 필요가 없음

# 단점
# 연결을 위한 별도의 데이터 공간이 필요하므로 효율이 낮음
# 데이터를 찾는데 접근성이 안 좋아서 속도가 느림
# 중간 데이터 삭제시, 앞 뒤를 모두 고려하여 재구성하는 코드를 작성해야 함

# 파이썬으로 Node 의 구현
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 노드는 data를 저장하는 변수와 다음 노드를 가리키는 포인터가 있음. 위에 코드엔 next 라고 함

# 파이썬으로 Linked List 구현
# 링크드 리스트에서는 간단한 코드 구현만, 중간 데이터 삽입 코드는 귀찮아서 작성안함

class LinkedList: 
    def __init__(self):
        self.head = None 
    
    def add(self, data): 
        new_node = Node(data) 
        if not self.head: 
            self.head = new_node 
        else: 
            node = self.head 
            while node.next: 
                node = node.next 
                node.next = new_node 
    def delete(self, data): 
        node = self.head 
        if node.data == data: 
            self.head = node.next 
            del node 
        else: 
            while node.next: 
                next_node = node.next 
                if next_node.data == data: 
                    node.next = next_node.next 
                    del next_node 
                else: 
                    node = node.next 
    
    def find(self, data): 
        node = self.head 
        while node:
            if node.data == data: 
                return node 
            else: 
                node = node.next 
    
    def print(self): 
        node = self.head 
        while node: 
            print(node.data) 
            node = node.next
# 링크드 리스트에서는 head인 첫 번째 노드 정보만 알면 됨. 그리고 데이터들을 받아서 Node를 만들어서 리스트에 추가시켜줄 add 함수 
# node 의 data 값을 통해 리스트에서 제거하는 delete 함수, data 값으로 node를 찾아주는 find 함수, 현재 링크드 리스트의 모든 노드의 
# 데이터값을 출력하는 print 함수를 간단하게 구현

# Doubly Linked List
# 이중 연결 리스트라고도 하는 더블 링크드 리스트는 양방향으 ㅣ노드 주소 값을 모두 가지고 있어서 양 방향으로 탐색이 가능하다는 장점을 가진 링크드 리스트

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# 기존의 링크드 리스트에서 prev라는 이전의 노드를 가리키는 변수를 추가함

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head

    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            new_node.prev = node
            node.next = new_node
            self.tail = new_node

# 이전의 링크드 리스트 클래스에서 init에 tail 변수가 추가됨 
# add 시 tail 변수를 고려해 주는 점이 다름




