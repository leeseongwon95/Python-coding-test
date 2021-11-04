# 해쉬 테이블
# 해쉬 구조란?
# Key 와 Value 쌍으로 이루어진 데이터 구조를 의미함. Key를 이용하여 데이터를 찾으므로, 속도는 빠르게 만드는 구조
# 파이썬에서는 딕셔너리(Dictionary) 타입이 해쉬 테이블과 같은 구조
# 기본적으로, 배열은 미리 Hash Table 크기만큼 생성해서 사용함. 공간은 많이 사용하지만 시간은 빠르다는 장점
# 검색이 많이 필요한 경우, 저장, 삭제, 읽기가 많은 경우, 캐쉬를 구현할 때 주로 사용

# 장점
# 데이터 저장, 검색 속도가 빠르다
# 해쉬는 키에 대한 데이터가 있는지(중복) 확인이 쉽다.

# 단점
# 일반적으로 저장공간이 좀 더 많이 필요함
# 여러 키에 해당하는 주소가 동일할 경우 충돌을 해결하기 위한 별도 자료구조가 필요함 (충돌 해결 알고리즘)

# 시간복잡도
# 일반적인 경우 (충돌이 없는경우) : O(1)
# 최악의 경우 (모든 경우에 충돌이 발생하는 경우) : O(n)

# 용어
# 해쉬(Hash) : 임의 값을 고정 길이로 변환하는 것을 의미함
# 해쉬 함수(Hash Function) : 특정 연산을 이용하여 키 값을 받아서 value 를 가진 공간의 주소로 바꾸어주는 함수를 의미함
# 해쉬 테이블 (Hash Table) : 해쉬 구조를 사용하는 데이터 구조
# 해쉬 값 (해쉬 주소, Hash Value or Address) : Key 값을 해쉬 함수에 넣어서 얻은 주소값을 의미함 이 값을 통해 슬롯을 찾아감
# 슬롯(Slot) : 한 개의 데이터를 저장할 수 있는 공간을 의미함 

# 해쉬 함수와 키 생성 함수
# 키 생성 함수를 파이썬 기본라이브러리의 Hash() 함수를 사용함
# SHA(Secure Hash Algorithm)은 어떤 데이터도 고정된 크기의 유일한 값으로 리턴해주기 때문에 많이 사용됨

# SHA-1
# SHA-1은 해쉬값의 크기를 160으로 고정하는 알고리즘

import hashlib

data = 'test'.encode()
hash_object = hashlib.sha1()
hash_object.update(data)
hex_dig = hash_object.hexdigest()
print(hex_dig)

data2 = 'hello world'.encode()
hash_object2 = hashlib.sha1()
hash_object2.update(data2)
hex_dig2 = hash_object2.hexdigest()
print(hex_dig2)

# Hashlib 이란 라이브러리는 SHA함수들을 가지고 있는 라이브러리
# 'test' 라는 문자와 'hello world' 라는 문자를 각각 SHA-1 으로 해쉬값을 출력

# SHA-256

# SHA -1 에서 해쉬값의 크기를 256으로 늘려서 더 안전한 알고리즘임
# 위의 메소드에서 sha1() 대신 sha256() 쓰면 됨

# 파이썬의 딕셔너리
# key, value 구조의 데이터를 가지는 형태로 이루어져있음

dic = {'name':'Lee', 'phone':'01023010540', 'birth':'950403'}

# key 값과 value 값으로 구성
# 파이썬의 딕셔너리는 Value 에 다양한 데이터 구조를 넣을 수 있음

# 생성, 요소추가, 삭제, 접근 코드
# 딕셔너리 생성
a = {1:'a'}

# key(2), value(3) 쌍 추가
a[2] = 'b'

# key(3), value([1,2,3]) 추가
a[3] = [1,2,3]

# key 2인 요소 삭제
del a[2]

# key 1인 요소 접근
a[1]

# key list 만듦
a.keys()

# key : Value 쌍 얻기
a.items()

# key로 value 얻기
a.get(1)

# Key : value 쌍 모두지우기
a.clear()

# # 중복 주의
a = {1 : 'a', 1 : 'b'}
# {1 : 'b'} 가 출력됨
# 딕셔너리의 key 값은 중복되면, 가장 뒷쪽의 key,value 쌍만을 가지고, 기존의 쌍은 무시함
# 또한, key 값에서는 리스트는 쓸 수 없음 key 값으로 쓸 수 있는 값은 변하지 않는 값에 해당함

# 리스트로 해쉬 테이블 만들기
# 우선 먼저 간단히 해쉬테이블을 만들면

class HashTable1: 
    def __init__(self):
        self.hash_table = list([0 for i in range(8)])

    def hash_function(self, key):
        return key % 8
    
    def insert(self, key, value):
        hash_value = self.hash_function(hash(key))
        self.hash_table[hash_value] = value

    def read(self, key):
        hash_value = self.hash_function(hash(key))
        return self.hash_table[hash_value]

    def print(self):
        print(self.hash_table)

# 해당 테이블의 해쉬 함수는 간단하게 key % 8 로 설정하였고, 해당 해쉬테이블의 공간은 8자리
# 0으로만 이루어진 리스트가 가장 먼저 생성 
# 해쉬 키를 생성하는 건 파이썬 기본 라이브러리의 hash 함수를 사용
# insert함수를 통해 key, value 쌍을 넣을 수 있고 
# read를 통해 key 값을 이용하여 value 값 얻을 수 있음 (이때 기본 라이브러리 hash 함수는 랜덤 연산작용으로 실행마다 값이 달라짐)

ht = HashTable1()
ht.insert(1, 'a')
ht.print()
ht.insert('name', 'Lee')
ht.print()
ht.insert(2, 'b')
ht.print()
ht.insert(3, 'c')
ht.print()
print(ht.read(2))
ht.insert(4, 'd')
ht.print()

# ('name' : 'Lee') 쌍이 삭제를 안했는데도 (2 : 'b') 가 들어가자 없어짐 
# hash 의 계산 값이 겹쳐져서 이러는데 이걸 충돌이 라고 함

# 리스트로 만든 개선된 해쉬테이블 (충돌 해결 알고리즘)
# 충돌을 해결하려면 크게 3가지의 개선 기법 존재

# 1. Chaining 기법
# Open Hashing 기법 중 하나 : 해쉬테이블 저장공간 외에 공간을 더 추가해서 사용하는 방법
# 충돌이 발생시, 링크드 리스트로 데이터를 추가로 뒤에 연결시키는 방법임
# key , value 쌍이 리스트로 들어가고 제한된 hash value index도 각각 리스트가 되도록 만들어봄

class HashTable2:
    def __init__(self):
        self.hash_table = list([0 for i in range(8)])
    
    def hash_function(self, key):
        # Custom Hash Function
        return key % 8
    
    def insert(self, key, value):
        gen_key = hash(key)
        hash_value = self.hash_function(gen_key)

        if self.hash_table[hash_value] != 0:
            # 해당 hash value index를 이미 사용하고 있는경우 (충돌 시)
            for i in range(len(self.hash_table[hash_value])):
                # 이미 같은 키 값이 존재하는 경우 -> value 교체
                # 이때 0은 key, 1은 value 값이 존재하는 인덱스
                if self.hash_table[hash_value][i][0] == gen_key:
                    self.hash_table[hash_value][i][1] = value
                    return
            # 같은 키 값이 존재하지 않는 경우 [key, value] 를 해당 인덱스에 삽입
            self.hash_table[hash_value].append([gen_key, value])
        else:
            # 해당 hash_value 를 사용하고 있지 않는 경우
            self.hash_table[hash_value] = [[gen_key, value]]
        
    def read(self, key):
        gen_key = hash(key)
        hash_value = self.hash_function(gen_key)

        if self.hash_table[hash_value] != 0:
            # 해당 해쉬 값 index에 데이터가 존재 할때
            for i in range(len(self.hash_table[hash_value])):
                if self.hash_table[hash_value][i][0] == gen_key:
                    # 키와 동일할 경우 -> 해당 value return
                    return self.hash_table[hash_value][i][1]
            # 동일한 키가 존재하지 않으면 None return
            return None
        else:
            # 해당 해쉬 값 index에 데이터가 없을 때
            return None
    
    def print(self):
        print(self.hash_table)

# 해쉬 값이 같은 자리에는 리스트를 만들어서 추가하는 방식으로 구현, 리스트에는 key 값과 value 를 넣어서 구현

ht = HashTable2()
ht.insert(1, 'a')
ht.print()
ht.insert('name', 'Lee')
ht.print()
ht.insert(2, 'b')
ht.print()
ht.insert(3, 'c')
ht.print()
print(ht.read(2))
ht.insert(4, 'd')
ht.print()
# [key, value] 가 리스트에 들어가며, 기존의 인덱스가 이미 사용중이라면 해당 인덱스의 리스트에 추가하는 방식
# 이 방식은 끝없이 key, value 쌍들을 넣을 수 있지만 공간 효율성이 떨어짐, 하나의 hash value index 에만 들어가면 불균형한 구조가 될 가능성 농후


# 2. Linear Probing 기법
# Close Hashing 기법 중 하나 : 해쉬테이블 저장공간 안에서 충돌 문제를 해결하는 방법
# 충돌이 일어나면, 해당 hash value (hash address) 의 다음 index 부터 맨 청므 나오는 빈공간에 저장하는 기법 (저장 공간 활용도 증가)

class HashTable3:
    def __init__(self):
        self.hash_table = list([0 for i in range(8)])

    def hash_function(self, key):
        # Custom Hash Function
        return key % 8

    def insert(self, key, value):
        gen_key = hash(key)
        hash_value = self.hash_function(gen_key)

        if self.hash_table[hash_value] != 0:
            # 해당 hash value index 를 이미 사용하고 있는 경우 (충돌 시)
            for i in range(hash_value, len(self.hash_table)):
                # 해당 hash value index 부터 마지막 index 까지
                # 돌면서 비어있거나 key 가 같은 값을 찾는다.
                if self.hash_table[i] == 0:
                    # 해당 인덱스가 비어있을 때,
                    self.hash_table[i] = [gen_key, value]
                    return
                elif self.hash_table[i][0] == gen_key:
                    # 이미 같은 키 값이 존재하는 경우 덮어쓰기
                    self.hash_table[i][1] = value
                    return

        else:
            # 해당 hash_value 를 사용하고 있지 않는 경우
            self.hash_table[hash_value] = [gen_key, value]

    def read(self, key):
        gen_key = hash(key)
        hash_value = self.hash_function(gen_key)

        if self.hash_table[hash_value] != 0:
            # 해당 해쉬 값 index 에 데이터가 존재 할 때
            for i in range(hash_value, len(self.hash_table)):
                if self.hash_table[i] == 0:
                    # 비어있는 경우,
                    return None
                elif self.hash_table[i][0] == gen_key:
                    # 키와 동일할 경우 -> 해당 value return
                    return self.hash_table[i][1]
        else:
            # 해당 해쉬 값 index에 데이터가 없을 때,
            return None

    
    def print(self):
        print(self.hash_table)

# 이 코드는 hash value index 에 자리가 없을 때, 그 이후의 리스트를 돌면서 빈공간을 찾아서 key, value 쌍을 넣는 방법임

ht = HashTable3()
ht.insert(1, 'a')
ht.print()
ht.insert('name', 'Lee')
ht.print()
ht.insert(2, 'b')
ht.print()
ht.insert(3, 'c')
ht.print()
print(ht.read(2))
ht.insert(4, 'd')
ht.print()

# 빈공간을 찾아서 key, value 값들이 충돌하지 않고 들어가는 모습을 확인 할 수 있음 
# 근데 이 알고리즘은 미리 지정한 자릿 수를 넘어가면 충돌이 일어나게 된다는 단점이 있음
# 8개 이상의 쌍을 넣으면 key 값이 7인 키 쌍에서 충돌이 일어남


# 3. 공간을 확장하는 방법
# Linear Probing 방식에서 공간을 늘린다면 1번에 비해 균형적인 구조로 사용가능

class HasTable4:
    def __init__(self, n):
        self.n = n
        self.hash_tabel = list([0 for i in range(n)])

    def hash_function(self, key):
        # Custom Hash Function
        return key % self.n

# n을 생성자의 매개변수로 사용해서 받고, 해당 n을 큰 수로 늘리면 많은 공간 사용할 수 있겠음.