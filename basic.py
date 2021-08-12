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



