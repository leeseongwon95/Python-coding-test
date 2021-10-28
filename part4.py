# 주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd) 작성

def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False
is_odd(3)
is_odd(4)

# 람다와 조건부 표현식 사용
is_odd = lambda x: True if x % 2 == 1 else False
is_odd(3)

# 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수 작성

def avg_numbers(*args): # 입력 개수에 상관없이 사용하기 위해 *args 를 사용
    result =  0
    for i in args:
        result += i
    return result / len(args)

avg_numbers(1, 2)
avg_numbers(1, 2, 3, 4, 5)

# 3과 6을 입력했을 때 9가 아닌 36이라는 결괏값을 돌려주었다. 이 프로그램의 오류를 수정

input1 = input("첫 번째 숫자를 입력")
input2 = input("두 번째 숫자를 입력")

total = int(input1) + int(input2) # 입력은 항상 문자열이므로 숫자로 바꾸어 줘야함

print("두수의 합은 %s 입니다" % total)

# 출력 결과가 다른 것

print("you" "need" "python")
print("you"+"need"+"python")
print("you","need","python") # 콤마가 있는 경우 공백이 삽입되어 더해 짐
print("".join(["you","need","python"]))

# 예상한 값 출력
# 문제의 예와 같이 파일을 닫지 않은 상태에서 다시 열면 파일에 저장한 데이터를 읽을 수 없다. 
# 따라서 열린 파일 객체를 close 로 닫아준 후 다시 열어서 파일의 내용을 읽어야 한다.

f1 = open("test.txt", 'w')
f1.write("Life is too short!")
f1.close()

f2 = open("test.txt", 'r')
print(f2.read())
f2.close()

# 또 다음과 같이 close를 명시적으로 할 필요가 없는 with 구문을 사용

with open("test.txt", 'w') as f1:
    f1.write("Life is too short! ")
with open("test.txt", 'r') as f2:
    print(f2.read())

# 사용자의 입력을 파일에 저장하는 프로그램
# 기존 내용을 유지하고 새로운 내용을 덧붙이기 위해서 다음과 같이 'a' 모드를 사용해야 함

user_input = input("저장할 내용을 입력하세요 : ")
f = open('test.txt', 'a') # 내용을 추가하기 위해 'a'를 사용
f.write(user_input)
f.write("\n")             # 입력된 내용을 줄 단위로 구분하기 위해 줄 바꿈 문자  
f.close()

# 다음과 같은 내용을 지닌 파일 test.txt 가 있다. 이 파일의 내용 중 "java"라는 문자열을 "python"으로 바꾸어서 저장해 보자.
# 파일을 모두 읽은 후에 문자열의 replace  함수를 사용하여 java 라는 문자열을 python 으로 변경한 다음 저장한다

f = open('test.txt', 'r')
body = f.read()
f.close()

body = body.replace('java', 'python')

f = open('test.txt', 'w')
f.write(body)
f.close()