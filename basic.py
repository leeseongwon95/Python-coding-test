# 정수 3개 입력받아 짝수만 출력하기

a, b, c = map(int, input().split())

if a % 2 == 0:
    print(a)
if b % 2 == 0:
    print(b)
if c % 2 == 0:
    print(c)


# 정수 3개 입력받아 짝/홀 출력하기

if a % b == 0:
    print("even")
else:
    print("odd")

if b % 2 == 0:
    print("even")
else:
    print("odd")
if c % 2 == 0:
    print("even")
else:
    print("odd")

# 정수 3개 입력받아 합과 평균을 출력

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
hap = a + b + c
avg = hap / 3
print(hap, format(avg, ".2f"))

# 정수 1개 입력받아 2배 곱해 출력하기

n = int(input())
print(n<<1)

# 2의 거듭제곱 배로 곱해 출력하기

a, b = input().split()
a = int(a)
b = int(b)
print(a<<b)

# 정수 2개 입력받아 비교하기

a, b = input().split()
a = int(a)
b = int(b)
print(a<b)
print(a==b)

# 정수 입력받아 참 거짓 평가하기

n = int(input())
print(bool(n))

# 참 거짓 바꾸기

a = bool(int(input()))
print(not a)

# 둘 다 참일 경우만 참 출력하기

a, b = input().split()
print(bool(int(a)) and bool(int(b)))

# 참/거짓이 서로 다를 때에만 참 출력하기

a, b = input().split()
c = bool(int(a))
d = bool(int(b))
print((c and (not d)) or ((not c) and d))

# 참/거짓이 서로 같은 때에만 참 출력하기

a, b = input().split()
a = bool(int(a))
b = bool(int(b))
print(a == b)

# 둘 다 거짓일 경우만 참 출력하기

a, b = input().split()
c = bool(int(a))
d = bool(int(b))

print( not (c or d))

# 비트단위로 NOT 하여 출력하기

a = int(input())
print(~a)

# 비트단위로 AND 하여 출력하기

a, b = input().split()
print(int(a) & int(b))

# 비트단위로 OR하여 출력하기

a, b = input().split()
print(int(a) | int(b))

# 비트단위로 XOR 하여 출력하기

a, b = input().split()
print(int(a) ^ int(b))

# 정수 1개 입력받아 분류하기

n = int(input())

if n < 0:
    if n % 2 == 0:
        print('A')
    else:
        print('B')
else:
    if n % 2 == 0:
        print('C')
    else:
        print('D')

# 정수 2개 입력받아 큰 값 출력하기

a, b = input().split()
a = int(a)
b = int(b)
c = a if a >= b else b
print(c)

# 정수 3개 입력받아 가장 작은 값 출력하기

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

d = a if a < b else b
e = d if d < c else c

# 정수 3개 입력받아 짝수만 출력하기

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if a%2 == 0:
    print(a)

if b%2 == 0:
    print(b)

if c%2 == 0:
    print(c)

# 정수 3개 입력받아 짝/홀 출력하기

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if a%2 == 0:
    print("even")
else:
    print("odd")

if b%2 == 0:
    print("even")
else:
    print("odd")

if c%2 == 0:
    print("even")
else:
    print("odd")

# 점수 입력받아 평가 출력하기

a = int(input())

if a >= 90:
    print("A")
elif a >= 70:
    print("B")
elif a >= 40:
    print("C")
else:
    print("D")

# 평가 입력받아 다르게 출력하기

a = input()

if a=='A':
    print("best!!!")
elif a == 'B':
    print("good!!")
elif a == 'C':
    print("run!")
elif a == 'D':
    print("slowly~")
else:
    print("what?")

# 월이 입력될 때 계절 이름이 출력되도록 해보자.

a = int(input())

if a//3 == 1:
    print("spring")
elif a//3 == 2:
    print("summer")
elif a//3 == 3:
    print("fall")
else:
    print("winter")

# 0이 입력될 때까지 무한 출력하기

while True:
    a = input()
    a = int(a)
    if a == 0:
        break
    else:
        print(a)

# 정수 1개 입력받아 카운트다운 출력하기 1

a = int(input())

while a != 0:
    print(a)
    a = a - 1

# 정수 1개 입력받아 카운트다운 출력하기 2

a = int(input())

while a != 0:
    a = a - 1
    print(a)

# 문자 1개 입력받아 알파벳 출력하기

a = input()
start = ord('a')

while True:
    print(chr(start), end = ' ')

    if (chr(start) == a):
        break

    start = start + 1

# 정수 1개 입력받아 그 수까지 출력하기

a = int(input())

i = 0
while i <= a:
    print(i)
    i += 1

# 정수 1개 입력받아 그 수까지 출력하기

a = int(input())

for i in range(a+1):
    print(i)

# 짝수 합 구하기

n = int(input())

sum = 0
for i in range(1, n+1):
    if i % 2 == 0:
        sum = sum + 1

print(sum)

# 원하는 문자가 입력될 때까지 반복 출력하기

while True:
    x = input()
    print(x)
    if x == 'q':
        break
    
# 언제까지 더해야 할까?

n = int(input())

s = 0
t = 0
while s < n:
    t = t + 1
    s = s + 1

print(t)

# 주사위 2개 던지기

n, m = input().split()

n = int(n)
m = int(m)

for i in range(1, n + 1):
    for j in range(1, m + 1):
        print(i, j)

# 16 진수 구구단 출력하기

n = int(input(), 16)

for i in range(1, 16):
    print('%X'%n, '+%X'%i, '=%X'%(n*i), sep='')

# 3 6 9 게임의 왕이 되자

n = int(input())

for i in range(1, n+1):
    if i%10 == 3 or i%10 == 6 or i%10 == 9:
        print("X", end=' ')
    else:
        print(i, end = ' ')