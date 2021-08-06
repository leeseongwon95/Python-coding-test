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




