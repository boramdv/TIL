# 최적의 코딩을 결정하는 기본 알고리즘

## 2차시 우선순위에 따라 데이터를 꺼내는 자료구조

### 우선순위 큐(Priority Quere)

- 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조
- 우선순위에 따라 데이터를 처리하고 싶을 때
- 우선순위 정보를 함께 저장



1. 리스트를 이용하여 구현

2. 힙 heap 을 이용하여 구현



시간 복잡도

​	N개의 데이터를 힙에 넣었다가 모두 꺼내는 작업은 정렬과 동일 (힙 정렬)

​	시간 복잡도 **O(NlogN)**



### 힙 (Heap)

- 완전 이진 트리(Complete Binary Tree) 자료 구조의 일종
  - 루트 노드부터 시작하여 왼쪽 자식 노드, 오른쪽 자식 노드 순서대로 데이터가 삽입되는 트리
- 루트 노드(root node)를 항상 제거
- 최소 힙(min leap) : 루트 노드가 가장 작은 값, 값이 작은 데이터가 우선적으로 제거됨
- 최대 힙(max leap) : 루트 노드가 가장 큰 값, 값이 큰 데이터가 우선적으로 제거됨



Min-Heapify() 최소 힙 구성 함수

​	- 부모 노드로 거술러 올라가며(상향식), 부모보다 자신의 값이 더 작은 경우 위치 교체

시간 복잡도

​	시간 복잡도 **O(logN)**





Python

```python
import sys
import heapq
input = sys.stdin.readline

# min heap -> minus 붙여서 max heap

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

n= = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))
    
res = heapsort(arr)

for i in range(n):
    print(res[i])
```



C++

```c++
#include <bits/stdc++.h>

using namespace std;

void heapSort(vector<int>& arr) {
    priority_quere<int> h;
    // 모든 원소를 차례대로 힙에 ㅅ바입
    for (int i = 0; i < arr.size(); i++) {
        h.push(-arr[i]);
    }
    // 힙에 삽입된 모든 원소를 차례대로 꺼내어 출력
    while (!h.empty()) {
        printf("%d\n", -h.top());
        h.pop();
    }
}

int n;
vector<int> arr;

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        int x;
        scanf("%d", &x);
        arr.push_back(x);
    }
    heapSort(arr);
}
```
