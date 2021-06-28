# 최적의 코딩을 결정하는 기본 알고리즘

## 3차시 활용도가 높은 자료구조: 트리 자료구조

### 트리(Tree)

- 계층적인 구조 표현
- 용어
  - root  node : 최상위 노드
  - leaf node : 자식이 없는 노드
  - size : 모든 노드 개수
  - depth : 루트 노드부터의 거리
  - height : 깊이 중 최댓값
  - degree : 각 노드의 (자식 방향) 간선 개수
- 기본적으로 size가 N이면, 전체 간선의 개수 N-1



#### 이진 탐색 트리(Binary Search Tree)

- 왼쪽 자식 노드 < 부모 노드 < 오른쪽 자식 노드
- 데이터 조회 과정
  1. 루트 노드 탐색
  2. 찾고자 하는 값보다 작으면 오른쪽



#### 트리의 순회(Tree Traversal)

- 트리 자료구조에 포함된 노드를 특정한 방법으로 한 번씩 방문하는 방법
- 대표적인 트리 순회 방법
  - 전위 순회(pre-order traverse) : 루트를 가장 먼저 방문
  - 중위 순회(in-order traverse) : 왼쪽 자식 (왼쪽 leaf -> 상위 노드 -> 오른쪽 leaf) -> 루트 -> 오른쪽
  - 후위 순회(post-order traverse) : 왼쪽 자식(왼쪽 leaf -> 오른쪽 leaf -> 상위 노드) -> 오른쪽 자식 -> 루트



Python

```python
class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node
        
# 전위 순회(Preorder Traversal)
def pre_order(node):
    print(node.data, end = ' ')
    if node.left_node != None:
        pre_order(tree[node.left_node])
	if node.right_node != None:
        pre_order(tree[node.right_node])

# 중위 순회(Inorder Traversal)
def in_order(node):
    if node.left_node != None:
        in_order(tree[node.left_node])
    print(node.data, end=' ')
    if node.right_node != None:
        in_order(tree[node.right_node])

# 후위 순회(Postorder Traversal)
def post_order(node):
    if node.left_node != None:
        post_order(tree[node.left_node])
    if node.right_node != None:
        post_order(tree[node.right_node])
    print(node.data, end=' ')
    
n = int(input())
tree = {}

for i in range(n):
    data, left_node, right_node = input().split()
    if left_node == "None":
        left_node = None
    if right_node == "None":
        right_node = None
    tree[data] = Node(data, left_node, right_node)
    
pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])
print()
```

