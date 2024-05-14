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

    - 매개변수를 받아서 동일한 로직을 처리하는 영역, `def`키워드를 통해 정의
    - 전역변수 : 특정 지역 밖에서 선언된 변수, 지역과 관계없이 어느 곳에든 유효 
    - 지역변수 : 중괄호 안에서 선언된 변수, 선언된 지역 내에서만 유효

## 2일차
- 파이썬 기초 복습

![자료구조](https://t1.daumcdn.net/cfile/tistory/23202B4C53FDC5600C)

- 파이썬 자료구조
    - 선형리스트(배열)
    - 단순 연결 리스트 = 파이썬의 list와 동일

    ![연결리스트](https://upload.wikimedia.org/wikipedia/commons/9/9c/Single_linked_list.png)

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