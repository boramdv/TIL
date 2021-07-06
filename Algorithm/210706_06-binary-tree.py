# 이진 탐색 트리

class TreeNode() :
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


## 전역 변수
memory = []
root = None
# 데이터베이스 또는 크롤링으로 얻은 로우 데이터 집합
nameAry = ['블랙핑크', '레드벨벳', '에이핑크', '걸스데이', '트와이스', '마마무']

# 첫 번째 노드 생성 (두 번째부터는 반복)
name = nameAry[0]
node = TreeNode()
node.data = name
root = node
memory.append(node)

# 전제 - 데이터 다르다.
for name in nameAry[1:] :
    node = TreeNode()
    node.data = name
    current = root
    while True :
        if name < current.data :
            if current.left == None :
                current.left = node
                break
            current = current.left
        else :
            if current.right == None :
                current.right = node
                break
            current = current.right

    memory.append(node)

# print(memory)

### 데이터 검색
findName = '마마무'
#findName = '마마쀼'
current = root
while True :
    if findName == current.data :
        print(findName, '를 찾음')
        break
    elif findName < current.data :
        if current.left == None :
            print('없음')
            break
        current = current.left
    else :
        if current.right == None :
            print('없음')
            break
        current = current.right
