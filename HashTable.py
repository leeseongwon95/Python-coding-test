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

class HashTable: 
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

ht = HashTable()
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

