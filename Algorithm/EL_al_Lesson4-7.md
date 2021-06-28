# 최적의 코딩을 결정하는 기본 알고리즘

## 4차시 특수한 목적의 자료구조: 바이너리 인덱스 트리

### 바이너리 인덱스 트리 (Binary Indexed Tree)

- 펜윅 트리(fenwick tree)
- 데이터 업데이트 상황 구간 합 (Interval Sum)



(추후 다른 강의 수강 혹은 복습 후 업로드 예정)





## 5차시 정렬 알고리즘: 선택 정렬과 삽입 정렬

### 정렬 알고리즘

- **선택 정렬**: 처리되지 않은 데이터 중 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것을 반복
  - 시간 복잡도 빅오 표기법 O(N^2)
  - 공간 복잡도 O(N)

- **삽입 정렬**: 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입, 일반적으로 선택 정렬에 비해 구현 난이도가 높으나 더 효율적으로 동작

  - 시간 복잡도 O(N^2), 최선의 경우 O(N)
  - 공간 복잡도 O(N)

  

### 6차시 정렬 알고리즘: 퀵 정렬과 계수 정렬

- **퀵 정렬**: 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치 변경
  - 일반적인 상황에서 가장 많이 사용
  - 병합 정렬과 더불어 대부분의 프로그래밍 언어 정렬 라이브러리의 근간
  - 가장 기본적인 퀵 정렬은 첫 번째 데이터를 기준 데이터 Pivot로 설정
  - 동작
    - 기준 데이터와 왼쪽, 오른쪽 양쪽에서 데이터를 비교
    - 위치가 엇갈리는 경우 서로 변경
    - **분할(Divide)** - 왼쪽은 기준 데이터보다 작은 값, 오른쪽은 큰 값 묶음
    - 재귀적 수행
  - 시간 복잡도 평균 O(NlogN), 최악의 경우 O(N^2) 매번 선형 탐색
  - 공간 복잡도 O(N)



- **계수 정렬**: 데이터의 크기 범위가 제한되어 정수 형태로 표현가능할 때만 사용 가능, 매우 빠르게 동작
  - 시간 복잡도 - 데이터 개수 N, 데이터(양수) 중 최댓값 K 최악이 경우 O(N+K)
  - 공간 복잡도 O(N+K)
  - 동작
    - 데이터 -> 인덱스, 인덱스를 개수만큼 출력
