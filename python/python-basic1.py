print('Hello')

x = 10
y = 10
z = 10

x, y, z = 10, 20, 30

x = y = z = 0

del x

# string

name = "이름"
age = 20
address = '서울'

print(name + '은' + str(age) + '살입니다.')
print(name + '은' + address + '에 삽니다.')

int_number = 12345
float_number = 12345.6789

print('string : %s' % name)
print('integer : %d' % int_number)
print('float : %f' % float_number)
print('float : %10.2f' % float_number)

print('이름 : %s, 나이 : %d' % (name, age))

rate = 80
print('percent : %d%%' % rate) # %%

# format()
# print(format(float_number, '전체자릿수.소숫점자리수f'))
print(format(float_number, '10.2f'))
print(f'숫자는 {float_number}이다.')

# 천 단위 ,
print(format(int(float_number), ','))
print(format(float_number, '9,.2f'))
print(format(int_number, ',d'))

# Integer Literal

a = 0b1010
b = 0o123 # octal
c = 0x12fc # hexadecimal
d = 1.23456e6

print(a, b, c, d)

print(type(a))
print(type(b))
print(type(c))
print(type(d))

print(bin(11))
print(oct(11))
print(hex(11))


# eval() 숫자형으로 변환 및 계산
# ex. str -> int

# id()


# escape \n \t \\ \" \'


# 형변환 함수
# str()
# int()
# float()


# Operator 연산자

# 산술연산자 : + - * /
# //(몫) %(나머지) **(지수)
# ( ) > ** > * / // % > + -

# 할당연산자 : =
# 대입연산자 : += -= *= /= //= %= **=

# 관계연산자 : > < >= <= ==(항등식) !=
# => True False

# 논리연산자 : and or not

# 비트연산자 : 정수를 2진수로 변환 후 비트별 연산
    # & : 논리곱 and
    # | : 논리합 or
    # ^ : 논리적배타합 xor
    # ~ : 부정 not
    # << >> shift 2**n