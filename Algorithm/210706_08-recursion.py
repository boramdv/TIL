# 재귀 호출 예시

# 숫자 합
def addNumber(num) :
    if num <= 1:
        return 1
    return num + addNumber(num-1)

print(addNumber(10))


'''
def addNumber(3) :
    if num <= 1:
        return 1
    return 3 + 2 + 1

def addNumber(2) :
    if num <= 1:
        return 1
    return 2 + 1

def addNumber(1) :
    if num <= 1:
        return 1
'''


# 팩토리얼.v1
def factorial(num) :
    if num <= 1 :
        return 1
    return num * factorial(num-1)

print(factorial(5))

# 팩토리얼.v2
def factorial(num) :
    if num <= 1 :
        print('1 반환')
        return 1
    print("%d * %d! 호출" % (num, num-1))
    retVal = factorial(num-1)

    print("%d * %d! (=%d) 반환" % (num, num-1, retVal))
    return num * retVal

print('\n5! = ', factorial(5))


# 카운트다운
def countDown(n) :
    if n == 0 :
        print('발사!!')
    else :
        print(n)
        return countDown(n-1)

countDown(5)


# 별 모양 출력.v0
def printStar(n):
    if n == 0 :
        return
    else :
        print('*' * n)
        return printStar(n-1)

printStar(5)

# 별 모양 출력.v1
def printStar(n):
    if n > 0 :
        printStar(n-1)
        print('*' * n)

printStar(5)


# 구구단 출력
def gugu(dan, num):
    print('%d * %d = %d' % (dan, num, dan*num))
    if num < 9 :
        gugu(dan, num+1)

gugu(2, 3)

for dan in range(2, 10) :
    print("%d 단" %dan)
    gugu(dan, 1)


# N제곱 계산
tab = ''
def pow(x, n) :
    global tab
    tab += ' '
    if n == 0 :
        return 1
    return x * pow(x, n-1)

print('답 : ', pow(2, 4))


# 배열의 합 계산
import random

def arySum(arr, n) :
    if n <= 0 :
        return arr[0]
    return arr[n] + arySum(arr, n-1)

ary = [random.randint(0, 255) for _ in range(random.randint(10, 20))]
print(ary)
print('배열 합계 : ', arySum(ary, len(ary)-1))