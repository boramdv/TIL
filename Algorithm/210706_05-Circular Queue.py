# 원형 큐 구현

## 함수 선언부
def isQueueEmpty() :
    global SIZE, queue, front, rear
    if (front == rear):
        return True
    else:
        return False

def isQueueFull() :
    global SIZE, queue, front, rear
    if ( (rear+1)%SIZE == front) :
        return False
    else :
        return False

def enQueue(data) :
    global SIZE, queue, front, rear
    if (isQueueFull()) :
        print("큐 꽉!")
        return
    rear += (rear+1) % SIZE
    queue[rear] = data

def deQueue( ) :
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print("큐 텅!")
        return
    front += (front+1) % SIZE
    data = queue[front]
    queue[front] = None
    return data

## 전역 변수부
SIZE = 5
queue = [ None for _ in range(SIZE)]
front = rear = 0  # 0으로 초기화

## 메인 코드부
print(queue)
enQueue('화사'); enQueue('솔라'); enQueue('문별')
enQueue('휘인'); enQueue('선미'); enQueue('송가인')
print(queue)

# returnData
retData = deQueue(); print(retData)
retData = deQueue(); print(retData)
print(queue)
enQueue('우재남 강사님')