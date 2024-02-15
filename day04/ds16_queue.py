# date : 2024-02-15
# desc : 큐 일반구현

# Queue 풀 확인함수
def isQueueFull():
    global SIZE, rear, front, rear
    if rear != (SIZE - 1): # 큐가 아직 빈상태
        return False
    elif rear == (SIZE-1) and front == -1: # 큐가 꽉 찬 상태
        return True
    else: # 큐가 앞쪽이 비어있는 상태, rear가 끝까지 간 상태
        while front != -1: # 완전히 앞으로 당긴다. front가 -1이 될때까지
            for i in range(front+1, SIZE):
                queue[i-1] = queue[i] # front에다가 front+1의 값을 할당
                queue[i] = None
            front -= 1
            rear -= 1
        return False
    
# Queue 엠티 확인함수
def isQueueEmpty():
    global front, rear
    if front == rear:
        return True
    else:
        return False
    
# Queue 데이터 삽입함수
def enQueue(data):
    global queue, rear
    if isQueueFull() == True: # queue가 꽉차서 데이터 입력불가
        print('큐가 꽉 찼습니다.')
        return # 함수탈출
    else:
        rear += 1
        queue[rear] = data

# Queue 데이터 추출함수
def deQueue():
    global queue, front
    if isQueueEmpty() == True:
        print('큐가 비었습니다.')
        return # 함수탈출
    else:
        front += 1
        data = queue[front]
        queue[front] = None
        return data

# 추출데이터 확인함수
def peek():
    global queue, front
    if isQueueEmpty() == True:
        print('큐가 비었습니다.')
        return None
    else:
        return queue[front+1]


# 전역변수
SIZE = int(input('큐 크기 입력(정수) > ')) # 상수(constant)
queue = [None for _ in range(SIZE)]
front = rear = -1

if __name__ == '__main__': # 메인시작
    while True:
        select = input('삽입(e), 추출(d), 확인(p), 종료(x) ')

        if select.lower() == 'e':
            data = input('입력 데이터 > ')
            enQueue(data)
            print(f'큐 상태 : {queue}')
        elif select.lower() == 'd':
            data = deQueue()
            print(f'추출 데이터 > {data}')
            print(f'큐 상태 : {queue}')
        elif select.lower() == 'p':
            data = peek()
            print(f'추출 데이터 > {data}')
            print(f'큐 상태 : {queue}')
        elif select.lower() == 'x':
            break
        else:
            continue
