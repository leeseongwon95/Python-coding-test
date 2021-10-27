# 다음 코드의 결과값

a = "Life is too short, you need python"

if "wife" in a: print("wife")                           # wife 라는 단어는 a 문자열에 없으므로 거짓
elif "python" in a and "you" not in a: print("python")  # python 이라는 단어는 a 문자열에 있지만 you 역시 a 문자열에 있으므로 거짓
elif "shirt" not in a: print("shirt")                   # shirt 라는 단어가 a 문자열 앞에 없으므로 참
elif "need" in a: print("need")                         # need 라는 단어가 a 문자열에 있으므로 참
else: print("none")


# while 문을 사용해 1부터 1000 까지의 자연수 중 3의 배수의 합 구하기

result = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        result += i
    i += 1

print(result)

# while 문을 사용하여 다음과 같이 별(*) 을 표시하는 프로그램을 작성
# *
# **
# ***
# ****
# *****

i = 0
while True:
    i += 1              # while 문 수행 시 1 씩 증가
    if i > 5: break     # i 값이 5보다 크면 while 문을 벗어난다.
    print('*' * i)      # i 값 개수만큼 *를 출력

# for문을 사용해 1부터 100까지의 숫자를 출력해 보자.

for i in range(1, 101):
    print(i)



# A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.
# [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
# for문을 사용하여 A 학급의 평균 점수를 구해 보자.

A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0

for score in A:
    total += score # A학급의 점수를 모두 더한다

average = total / len(A) # 평균을 구하기 위해 총 점수를 총 학생수로 나눈다.
print(average)


# 리스트 중에서 홀수에만 2를 곱하여 저장하는 다음 코드가 있다.

# numbers = [1, 2, 3, 4, 5]
# re = []
# for n in numbers:
#     if n % 2 == 1:
#         result.append(n*2)
# 위 코드를 리스트 내포(list comprehension)를 사용하여 표현해 보자.

numbers = [1, 2, 3, 4, 5]
re = [n*2 for n in numbers if n%2 == 1]
print(re)