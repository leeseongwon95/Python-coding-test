# Calculator 클래스를 상속하는 UpgradeCalculator 클래스를 만들고 minus 메서드를 추가

class UpgreadeCalculator(Calculator):
    def minus(self, val):
        self.value -= val

# 객체변수 value 가 100 이상의 값은 가질 수 없도록 제한하는 MaxLimitCalculator 클래스 

class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100

# 결과 예측

# 1
all([1, 2, abs(-3)-3]) # abs(-3) 은 -3의 절댓값이므로 3이되어 all([1, 2, 0]) 이 되고, 리스트의 요솟값중 0 이 있기 때문에 all 내장 함수의 결과는 False 가 된다

# 2
chr(ord('a')) == 'a' # ord('a') 의 결과는 97이 되어 chr(97)로 치환 됨. chr(97) 의 결과는 다시 'a' 가 되므로 'a' == 'a' 가 되어 True를 돌려준다


# filter 와 lambda 를 사용하여 리스트 [1, -2, 3, -5, 8, -3] 에서 음수를 모두 제거

list(filter(lambda x:x>0, [1, -2, 3, -5, 8, -3]))

# '0xea'라는 16진수 문자열을 10진수로 변경
# int 내장 함수로

int('0xea', 16)

# map과 lambda를 사용 [ 1, 2, 3, 4] 라는 리스트의 각 요솟값에 3이 곱해진 리스트 [3, 6, 9, 12] 만듦

list(map(lambda x:x*3, [1,2,3,4]))

# 리스트의 최댓값, 최솟값 의 합

a = [-8,2,7,5,-3,5,0,1]

max(a) + min(a)

# 반올림

round(17/3, 4)

# 모듈

import sys

numbers = sys.argv[1:] # 파일 이름을 제외한 명령 행의 모든 입력

result = 0
for number in numbers:
    result += int(number)
print(result)

# os 모듈

import os
os.chdir("c:/doit")
result = os.popen("dir")
print(result.read())

# glob 모듈  py 확장자 파일만 출력

import glob
glob.glob("c:/doit/*.py")

# time 모듈 

import time
time.strftime("%Y/%m/%d %H:%M:%S")


# random 모듈

import random
result = []
while len(result) < 6:
    num = random.randint(1, 45) # 1부터 45까지의 난수 발생
    if num not in result:
        result.append(num)
print(result)