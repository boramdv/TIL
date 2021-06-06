# 최적의 코딩을 결정하는 기본 알고리즘

## 1차시 가장 기본이 되는 자료구조: 스택과 큐

### 스택 자료구조

선입후출의 자료구조

입구와 출구가 동일한 형태

박스 쌓기 

DFS 알고리즘 외에도 다양하게 사용됨



연산 두 가지 종류

- 삽입
- 삭제



Python - list 자료형

```python
stack = []

stack.append()
stack.pop()

print(stack[::-1]) # 최상단 원소부터 출력(순서를 뒤집어서 출력)
print(stack) # 최하단 원소부터 출력
```



C++

```c++
#include <bits/stdc++.h>

using namespace std;

stack<int> s;

int main(void) {
    s.push();
    s.pop();
    // 스택의 최상단 원소부터 출력
    while (!s.empty()) {
        cout << s.top() << ' ';
        s.pop();
    }
}
```



Java

```java
import java.util.*;

public class Main {
    
    public static void main(String[] args) {
        Stack<Integer> s = new Stack<>();
        
        s.push();
        s.pop();
        // 스택의 최상단 원소부터 출력
        while (!s.empty()) {
            System.out.print(s.peek() + " ");
            s.pop();
        }
    }
}
```





### 큐 자료구조

선입선출의 자료구조

입구와 출구가 모두 뚫려 있는 터널 같은 형태

대기열. 차례대로



Python deque(덱 라이브러리)

```python
from collections import deque

queue = deque()

queue.append()
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력

queue.reverse() # 역순으로 바꾸기
print(queue) # 나중에 들어온 원소부터 출력
```

오른쪽으로 들어와서 왼쪽으로 나간다!

list보다 시간적으로 우수



시간 복잡도



C++

```c++
#include <bits/stdc++.h>

using namespace std;

quere<int> q;

int main(void) {
    q.push();
    q.pop();
    // 먼저 들어온 원소부터 추출
    while (!q.empty()) {
        cout << q.front() << ' ';
        q.pop();
    }
}
```



Java - 연결리스트 형태를 이용하는 것이 기본

```java
import java.util.*;

public class Main {
    
    public static void main(Stirng[] args) {
        Queue<Integer> q = new LinkedList<>();
        
        q.offer();
        q.poll();
        // 먼저 들어온 원소부터 출력
        while (!q.isEmpty()) {
            System.out.pring(q.poll() + " ");
        }
    }
}
```

