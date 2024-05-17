# 자료구조와 알고리즘 2024
:pencil2:부경대 IoT 개발자 파이썬 자료구조와 알고리즘 학습 리포지토리:closed_book:

## 1일차
1. 콘솔출력

    - 변수 앞 i를 쓰면 정수형, f를 쓰면 실수형, s를 쓰면 문자열형, is를 쓰면 Boolean형
    - 포맷스트링

        ```
        name = "홍길동"
        age = 32
        print(f"{name}의 나이는 {age}살이다.")
        ```

2. 입력

    - 입력은 문자열의 결합
    - 숫자를 입력하려면 정수 또는 실수...로 변경해줘야 함
    - 입력값이 두 개 이상이면 `map`과 `split`을 활용

        ```
        x, y = map(float, input('두 실수를 입력(구분자 스페이스) > ').split())
        print(f'{x:.2f} * {y:.2f} = {x * y:.4f}')
        ```

3. 연산자

    - 산술연산 : 사칙연산자(`+,-,*,/`)와 거듭제곱(`**`), 나머지(`%`), 정수 몫(`//`)등이 있음
    - 대입연산자 : 오른쪽 값을 왼쪽에 할당
    - 관계연산자 : 등호(`==`), 같지않음(`!=`), 부등호(`<,>,<=,>=`)등이 있음

4. 형변환(Type casting)

    - 실수 문자열을 정수로 변환x

        ```
        int('3.14') # 오류
        ```
    - 실수형을 정수형으로 변환 가능, 소수점이하 생략

        ```
        int(3.14) # 3
        ```

5. 흐름제어

    - 조건문 : 중첩 if문을 여러번 쓰면 경우의 수가 기하급수적으로 증가(경우를 모두 처리해줘야함)

        ```
        army = 300

        if army < 300:
            print('싸우면 집니다.')
        else:
            print('이깁니다') 
        ```
    - for문

        ```
        for i in range(1, 11, 2):
        print(i, end=', ') # 1, 3, 5, 7, 9
        ```
    - while문
        - continue : 반복문에서 조건이 맞으면 로직을 실행하지 않고 다음 반복으로 계속 반복
        - break : 반복문에서 조건이 맞으면 반복문 블록을 빠져나가는 것

            ```
            while True: # 무한루프
            print('ㅎ', end='') # ㅎ
            break
            ```

6. 함수

    - 매개변수를 받아서 동일한 로직을 처리하는 영역, (`def`)키워드를 통해 정의
    - 전역변수 : 특정 지역 밖에서 선언된 변수, 지역과 관계없이 어느 곳에든 유효 
    - 지역변수 : 중괄호 안에서 선언된 변수, 선언된 지역 내에서만 유효

## 2일차
1. 파이썬 기초 복습

<!-- ![자료구조](https://t1.daumcdn.net/cfile/tistory/23202B4C53FDC5600C) -->

2. 선형리스트(배열)

    - 맨 끝에 빈칸 확보
    - 삽입하고자 하는 공간에 빈칸이 없으므로, 삽입하고자 하는 공간 뒤에 있는 요소들을 한칸씩 뒤로 옮김
    - 빈자리에 요소 삽입

        ```
        kakaotalk = ['다현', '정연', '쯔위', '사나', '지효']

        # 선형리스트에 데이터를 삽입하는 함수
        def insert_data(pos, friend):
            if pos < 0 or pos > len(kakaotalk): 
                print('데이터 삽입범위 초과')
                return # 함수를 빠져나감
    
            kakaotalk.append(None) # 빈칸추가, ['다현', '정연', '쯔위', '사나', '지효', None]
            size = len(kakaotalk) # 배열의 현재크기

            # 삽입위치까지 데이터를 하나씩 뒤로 보냄
            for i in range(size-1, pos, -1): # 역순, None을 pos까지 옮기기
                kakaotalk[i] = kakaotalk[i-1]
                kakaotalk[i-1] = None 

            kakaotalk[pos] = friend
        ```

    - 데이터 삭제시 빈칸을 그대로 두지않고 뒤의 요소들을 앞으로 한칸씩 이동

        ```
        # 선형리스트에서 데이터를 삭제하는 함수
        def delete_data(pos): # 데이터 삭제시는 위치값만 
            if pos < 0 or pos >= len(kakaotalk): 
                print('데이터 삭제범위 초과')
                return
    
            size = len(kakaotalk)
            kakaotalk[pos] = None # 데이터 삭제, ['다현', '정연', None, '쯔위', '사나', '지효']

            for i in range(pos+1, size): 
                kakaotalk[i-1] = kakaotalk[i] # None을 배열 끝으로 옮기기
                kakaotalk[i] = None
    
            del(kakaotalk[size-1]) # 배열의 맨 마지막값 삭제
        ```

3. 단순 연결 리스트 = 파이썬의 list와 동일

    - 데이터와 링크로 구성된 항목인 `노드(Node)`로 구성
    - 단순 연결 리스트는 첫 번째 노드를 가리키는 `헤드(Head)`를 사용(헤드를 이용하여 처음부터 다시 진행가능)

        <!-- ![연결리스트](https://upload.wikimedia.org/wikipedia/commons/9/9c/Single_linked_list.png) -->
    
        - 단순 연결 리스트 생성과정

        ```
        # 노드 생성(노드는 클래스를 사용하여 구현)
        class Node():
            # data, link 두 개의 멤버변수 존재
            # 생성자 추가 
            def __init__(self): # 생성자 함수 : 데이터형을 생성할 때, 자동으로 실행
                self.data = None
                self.link = None
            
        # 노드 생성 및 확인
        node1 = Node('다현')
        print(node1.data, end = ' ')
        print(node1.link) # 다현 None

        # 노드 연결
        node2 = Node('정연')
        node1.link = node2 # 첫 번째 노드의 링크에 두 번째 노드를 넣어 연결
        ...
        node5 = Node('지효')
        node4.link = node5

        # 단순연결리스트 출력방법
        current = node1
        print(current.data, end = ' ') # 첫 번째 노드를 현재(current)로 지정하고 출력
        while current.link != None: # 노드가 비어있지 않은동안
            current = current.link # 다음 노드를 현재노드로 지정
            print(current.data, end = ' ')
        ```

        - 노드 삽입과정
        
        ```
        # 다현 정연 재남 쯔위 사나 지효
        newNode = Node('재남')
        newNode.link = node2.link
        node2.link = newNode
        ```

        - 노드 삭제과정

        ```
        node2.link = node3.link # 쯔위의 링크를 정연의 링크로 복사
        del(node3) # 쯔위 삭제
        ```

4. 선형리스트와 연결리스트의 차이

    - 선형리스트 : 메모리 저장장소의 최적화는 있지만, 삽입/삭제 시 오버헤드 존재(거의 사용x)
    - 연결리스트 : 메모리 공간 오버헤드는 존재하지만, 삽입/삭제 시 처리시간 최적화

## 3일차
1. 단순 연결 리스트 복습

2. 원형 연결 리스트(패스) : 마지막 노드가 첫 노드와 연결

3. 스택 : Last In First Out (LIFO)

    - 삽입과 추출이 한쪽에서만 진행됨
    - 데이터를 삽입하는 동작을 `push`, 데이터를 추출하는 동작을 `pop`이라고 함
    - 현재 스택에 들어있는 가장 위의 데이터 위치를 `top`
    - 스택은 배열형태로 구현

        - 스택 생성과정

        ```
        # 스택 선언
        stack = [None for _ in range(5)]
        top = -1
        ```

        - 스택 삽입과정

        ```
        # push
        top += 1 # 0
        stack[top] = '커피'
        top += 1 # 1
        stack[top] = '녹차'
        top += 1 # 2
        stack[top] = '꿀물'

        # 현재 스택확인
        for i in range(len(stack)-1,-1,-1): # 4~0으로 역순
            print(stack[i]) # 커피-> 녹차 -> 꿀물 -> None -> None 순으로 쌓임
        ```

        - 추출 과정

        ```
        # pop
        stack = ['커피', '녹차', '꿀물', None, None]

        data = stack[top] # top의 데이터를 밖으로 추출, 꿀물
        stack[top] = None
        top -= 1

        data = stack[top] # 녹차
        stack[top] = None
        top -= 1

        data = stack[top] # 커피
        stack[top] = None
        top -= 1

        # 현재 스택확인
        for i in range(len(stack)-1, -1, -1): # 4~0으로 역순
            print(stack[i]) # None None None None None 순
        ```

    <!-- ![stack](https://cs.lmu.edu/~ray/images/stack.gif) -->

4. 큐 : First In First Out (FIFO)

    - 큐는 양쪽이 뚫려있는 구조, 한쪽에서는 삽입만 진행되고 다른 쪽에서는 추출만 진행
    - 큐에 데이터를 삽입하는 동작을 `enQueue(인큐)`, 데이터를 추출하는 동작을 `deQueue(데큐)`라고 함
    - 큐의 `머리`는 저장된 데이터를 첫 번째를 가리킴, 큐의 `꼬리`는 마지막 데이터를 가리킴
    - 첫 번째 데이터 앞을 front가 가리켜야 함

        - 큐 선언과정
        ```
        queue = [None for _ in range(5)]
        front = rear = -1 # 둘 다 -1이면 초기상태이고, 큐가 비었다고 해석
        ```

        - enqueue 구현과정
        ```
        rear += 1
        queue[rear] = '화사'
        rear += 1
        queue[rear] = '솔라'
        rear += 1
        queue[rear] = '문별'

        print('[out] ', end=' <- ')
        for i in range(0, len(queue), 1):
            print(queue[i], end=' <- ')

        print('[in]') # [out]  <- 화사 <- 솔라 <- 문별 <- None <- None <- [in]
        ```
        
        - dequeue 구현과정
        ```
        queue = ['화사', '솔라', '문별', None, None]
        front = -1
        rear = 2

        front += 1
        data = queue[front]
        queue[front] = None
        print(f'dequeue -> {data}') # 화사

        front += 1
        data = queue[front]
        queue[front] = None
        print(f'dequeue -> {data}') # 솔라

        front += 1
        data = queue[front]
        queue[front] = None
        print(f'dequeue -> {data}') # 문별

        front += 1
        data = queue[front]
        queue[front] = None
        print(f'dequeue -> {data}') # None
        ```

    <!-- ![queue](https://raw.githubusercontent.com/guswlrla/ds-and-algorithm/main/images/queue.png) -->
    

## 4일차
1. 큐 복습

2. 이진트리
    - 트리의 맨 위를 뿌리(Root, 루트)라고 함
    - 위 노드와 아래 노드의 관계를 부모-자식 관계라고 함
    - 자식 노드의 개수를 차수(Degree)라고 함
    
        - 이진트리 생성과정

        ```
        class TreeNode():
            left = data = right = None
            def __init__(self) -> None:
                self.left = self.right = self.data = None

        node1 = TreeNode()
        node1.data = '화사'

        node2 = TreeNode()
        node2.data = '솔라'
        node1.left = node2

        node3 = TreeNode()
        node3.data = '문별'
        node1.right = node3

        node4 = TreeNode()
        node4.data = '휘인'
        node2.left = node4

        node5 = TreeNode()
        node5.data = '쯔위'
        node2.right = node5

        node6 = TreeNode()
        node6.data = '선미'
        node3.left = node6
        ```

    - 이진트리 순회(traversal)

        - 전위순회 : 데이터를 먼저 처리
        ```
        def preorder(node):
            if node == None: return

            print(node.data, end='->')
            preorder(node.left)
            preorder(node.right)
        ```

        - 중위순회 : 데이터를 중간에 처리

        ```
        def inorder(node):
            if node == None: return

            inorder(node.left)
            print(node.data, end='->')
            inorder(node.right)
        ```

        - 후위순회 : 데이터를 마지막에 처리

        ```
        def postorder(node):
            if node == None: return

            postorder(node.left)
            postorder(node.right)
            print(node.data, end='->')
        ```

    <!-- ![이진트리](https://kahee.github.io//assets/post_img/tree3.png) -->

## 5일차
1. 그래프 : 여러 노드가 서로 연결된 자료구조

    - 루트에서 하위 노드 방향으로 가는 트리와는 달리, 여러 노드가 연결되어 있을 수 있음
    - 그래프의 종료
        - 무방향 그래프 : 간선은 연결하는 두 정점을 ()로 표현

        ```
        E(G1) = { (A, B), (A, C), (A, D), (B, C), (C, D) }
        E(G2) = { (A, B), (B, D), (D, C) }
        ```

        - 방향 그래프 : 간선은 연결하는 두 정점을 <>로 묶어 표현

        ```
        E(G1) = { <A, B>, <A, C>, <D, A>, <D, C> }
        E(G2) = { <A, B>, <C, B>, <C, D> }
        ```
    
    - 그래프 순회 방식 : 그래프의 모든 정점을 한 번씩 방문
        - 깊이 우선 탐색(DFS)
        - 너비 우선 탐색(BFS) 

    <!-- ![그래프](https://raw.githubusercontent.com/guswlrla/ds-and-algorithm/main/images/graph02.png) -->

## 6일차
1. 재귀호출 : 자신을 다시 호출하는 것

2. 정렬
    - 선택정렬(Selection Sort) : 최소값을 찾아서 맨 앞으로 보내는 정렬

        ```
        def selectionSort(ary):
            n = len(ary)
            for i in range(0, n-1): # 6
                minIdx = i
                for k in range(i+1, n):
                    if ary[minIdx] > ary[k]:
                        minIdx = k
        
                tmp = ary[i] # 원래있던 (최초 0)
                ary[i] = ary[minIdx] # minIdx에 있는 최소값을 가져옴
                ary[minIdx] = tmp 

            return ary  
        ```

    - 삽입정렬(Insertion Sort) : 기준값 기준으로 앞뒤로 보내는 정렬

        ```
        def insertionSort(ary):
            n = len(ary) 
            for end in range(1, n): # 앞에서 뒤로
                for cur in range(end, 0, -1): # 뒤에서 앞으로
                    if ary[cur-1] > ary[cur]:
                        tmp = ary[cur]
                        ary[cur] = ary[cur-1]
                        ary[cur-1] = tmp

            return ary
        ```

    - 버블정렬(Bubble Sort) : 기준값 기준으로 제일 큰 값을 뒤로 보내는 정렬

        ```
        def bubbleSort(ary):
            n = len(ary)
            for end in range(n-1, 0, -1): # 7부터 1까지 역순
                for cur in range(0, end):  # 0, 6까지 순차
                    if ary[cur] > ary[cur+1]: # 앞의 값이 뒤의 값보다 크면 뒤로보냄
                        tmp = ary[cur]
                        ary[cur] = ary[cur+1]
                        ary[cur+1] = tmp
            return ary
        ```
    
    - 퀵 정렬(Quick Sort) : 기준값 기준으로 왼쪽, 오른쪽 그룹분리한 뒤 다시 정렬

        ```
        def quickSort(ary):
            n = len(ary)
            if n <= 1: return ary # 정렬할 리스트가 1개이하면 정렬필요없음

            pivot = ary[n // 2] # 기준값(중앙값) 지정
            leftAry, rightAry = [], []

            for data in ary:
                if data < pivot:
                    leftAry.append(data)
                elif data == pivot:
                    pass
                else:
                    rightAry.append(data)

            return quickSort(leftAry) + [pivot] + quickSort(rightAry) # 재귀호출
        ```

    <!-- ![정렬](https://raw.githubusercontent.com/guswlrla/ds-and-algorithm/main/images/sorting.jpg) -->


## 7일차
1. 검색 : 어떤 집합에서 원하는 것을 찾는 것
    - 검색 결과로 특정 집합의 위치인 인덱스를 알려줌 
    - 검색의 종류
        - 순차 검색
        - 이진 검색
        - 트리 검색

2. 코딩테스트