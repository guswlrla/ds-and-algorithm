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

![자료구조](https://t1.daumcdn.net/cfile/tistory/23202B4C53FDC5600C)

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
        
        # 사용 예시
        insert_data(2, '솔라') # ['다현', '정연', '솔라', '쯔위', '사나', '지효']
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
        
        # 사용 예시
        delete_data(2) # ['다현', '정연', '쯔위', '사나', '지효']
        ```

3. 단순 연결 리스트 = 파이썬의 list와 동일

    - 데이터와 링크로 구성된 항목인 `노드(Node)`로 구성
    - 단순 연결 리스트는 첫 번째 노드를 가리키는 `헤드(Head)`를 사용(헤드를 이용하여 처음부터 다시 진행가능)

        ![연결리스트](https://upload.wikimedia.org/wikipedia/commons/9/9c/Single_linked_list.png)
    
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

        ```

4. 선형리스트와 연결리스트의 차이

    - 선형리스트 : 메모리 저장장소의 최적화는 있지만, 삽입/삭제 시 오버헤드 존재(거의 사용x)
    - 연결리스트 : 메모리 공간 오버헤드는 존재하지만, 삽입/삭제 시 처리시간 최적화

## 3일차
- 파이썬 자료구조
    - 단순 연결 리스트 다시
    - 원형 연결 리스트(패스) : 마지막 노드가 첫 노드와 연결
    - 스택 : Last In First Out (LIFO)
        - pop - list.pop()
        - push - list.append() 와 동일

    ![stack](https://cs.lmu.edu/~ray/images/stack.gif)
    - 큐 : First In First Out (FIFO)

    ![queue](https://raw.githubusercontent.com/guswlrla/ds-and-algorithm/main/images/queue.png)
    

## 4일차
- 파이썬 자료구조
    - 큐 다시
    - 이진트리

    ![이진트리](https://kahee.github.io//assets/post_img/tree3.png)

## 5일차
- 파이썬 자료구조/알고리즘
    - 그래프

    ![그래프](https://raw.githubusercontent.com/guswlrla/ds-and-algorithm/main/images/graph02.png)

## 6일차
- 파이썬 자료구조/알고리즘
    - 재귀호출
    - 정렬
        - 선택정렬 Selection Sort : 최소값을 찾아서 맨 앞으로 보내는 정렬
        - 삽입정렬 Insertion Sort : 기준값 기준으로 앞뒤로 보내는 정렬
        - 버블정렬 Bubble Sort : 기준값 기준으로 제일 큰 값을 뒤로 보내는 정렬
        - 퀵정렬 Quick Sort : 기준값 기준으로 작은 값 그룹 / 큰 값 그룹 분리한 뒤 다시 정렬 재귀호출

    ![정렬](https://raw.githubusercontent.com/guswlrla/ds-and-algorithm/main/images/sorting.jpg)


## 7일차
- 파이썬 자료구조/알고리즘
    - 검색
- 코딩테스트