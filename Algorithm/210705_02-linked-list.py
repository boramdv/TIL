# 중요 코드 - 실제 자료구조 연결구조 사용
# (가독성) 클래스 또는 함수 선언부 / 전역 변수 부 / 메인 코드부

## 클래스 또는 함수 선언부 ##
class Node():
    def __init__(self):
        self.data = None
        self.link = None

# print 함수 생성(오류 처리 생략)
def printNodes(start) :
    current = start
    print(current.data, end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()

# 노드 삽입 함수
def insertNode(findData, insertData) :
    global memory, head, current, pre

    # 첫 번째 노드 삽입
    if head.data == findData :
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return

    # 중간 노드 삽입
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return

    # 마지막 노드 삽입
    node = Node()
    node.data = insertData
    current.link = node

def deleteNode(deleteData) :
    global memory, head, current, pre

    if head.data == deleteData :
        current = head
        head = current.link
        del(current)
        return

    current = head
    while current.link != None : ## 주의!
        pre = current
        current = current.link
        if current.data == deleteData :
            pre.link = current.link
            del(current)
            return


## 전역 변수부
memory = []
head, current, pre = None, None, None
# dataArray = ['다현', '정연', '쯔위', '사나', '지효'] # DB, 크롤링...
import random
dataArray = [ random.randint(1000,9999) for _ in range(20)]


# 위까지는 가지고 있는 것. 메인 코드부 - 프로그램의 진입점. 형식 권장 pass

## 메인 코드부
if __name__ == '__main__' : # C, Java, C++, C# ==> main() 함수

    node = Node()
    node.data = dataArray[0]
    head = node
    memory.append(node)

    for data in dataArray[1:] : # ['정연', '쯔위', '사나', '지효']
        pre = node
        node = Node()
        node.data = data # 정연, 쯔위, ...
        pre.link = node
        memory.append(node)

    printNodes(head)
