#쓰레드란 코드를 실행하는 하나의 동작 -> 파이썬은 하나의 메인 쓰레드가 파이썬 코드를 순차적으로 실행

import threading
import threading, requests, time

def getHtml(url):
    resp = requests.get(url)
    time.sleep(1)
    print(url, len(resp.text), ' chars')

t1 = threading.Thread(target=getHtml, args=('http://google.com',))
t1.start()