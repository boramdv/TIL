# if 랜덤 숫자 게임

from random import randint

comNum = randint(1, 100)
myNum = randint(1, 100)

print('com : %d vs my : %d' % (comNum, myNum))

if (myNum > comNum):
    print('성공')
elif (myNum == comNum):
    print('무승부')
else:
    print('실패')


# for - sequence types

for name in ['가', '나', '다', '라']:
    print(name)

for num in range(0, 10):  #range(start, stop, step)
    print(num, end=' ')


print('\n--------------------------------------')

n = 0
for i in range(10):
    for j in range(1, 6):
        n += 1
        print(n, end='\t')

    print()
