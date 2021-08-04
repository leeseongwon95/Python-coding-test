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

# 2의 거듭제곱 배로 곱해 출력하기

a, b = input().split()
a = int(a)
b = int(b)
print(a<<b)

