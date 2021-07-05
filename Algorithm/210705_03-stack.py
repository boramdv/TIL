def isStackFull() :
    global SIZE, stack, top
    if (top >= SIZE-1) : ## >= 좀 더 일반적인 표현 ==보다
        return  True
    else :
        return False


def push(data) :
    global SIZE, stack, top
    if (isStackFull()) :
        print("스택 꽉 찼습니다.")
        return
    top += 1
    stack[top] = data


def isStackEmpty() :
    global SIZE, stack, top
    if (top == -1) : # 초기 세팅 top = -1
        return True
    else :
        return False


def pop() :
    global SIZE, stack, top
    # 비었는지 체크
    if (isStackEmpty()) :
        print("스택이 비었습니다.")
        return None
    # 데이터를 추출해서 리턴
    data = stack[top]
    stack[top] = None
    top -= 1
    # print(data)
    return data

# SIZE = 5
# stack = [ None for _ in range(SIZE)]
# top = -1

# SIZE = 5
# stack = ['커피', '녹차', '꿀물', '콜라', '환타']
# top = 4

SIZE = 5
stack = ['커피', '녹차', '꿀물', '콜라', None]
top = 3

# print('스택 꽉?', isStackFull())

# print(stack)
# push('환타')
# print(stack)
# push('사이다')
# print(stack)


print(stack)
pop()
print(stack)
pop()
print(stack)
pop()
print(stack)
pop()
print(stack)
pop()
print(stack)