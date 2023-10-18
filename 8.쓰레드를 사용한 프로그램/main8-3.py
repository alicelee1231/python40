import threading
import time

def thread_1():
    while True:
        print("thread 1")
        time.sleep(1.0)

t1 = threading.Thread(target=thread_1)

#기존 8-2에는 daemon을 설정해 놓지 않았기 때문에 실행파일을 중지 시켰을 때도 계속 돌아감. 
#그러나 이번에는 daemon을 설정해 놓았기 때문에 중지하면 함께 정지됨
t1.daemon=True
t1.start()

while True:
    print("main")
    time.sleep(2.0)