import threading


def sum(name, value):
    for i in range(0, value):
        print(f"{name}: {i}")

t1 = threading.Thread(target=sum, args=("thread_1",10))
t2 = threading.Thread(target=sum, args=("thread_2",10))

t1.start()
t2.start()

print("main thread")