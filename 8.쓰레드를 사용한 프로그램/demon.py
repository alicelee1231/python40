#demon thread는 백그라운드에서 실행되는 쓰레드로 메인 쓰레드가 종료되면 즉시 함께 종료


import threading, requests, time

def getHtml(url):
    resp = requests.get(url)
    time.sleep(1)
    print(url, len(resp.text), ' chars')
 
# 데몬 쓰레드
t1 = threading.Thread(target=getHtml, args=('http://google.com',))

#true면 demon으로 메인이 끝나면 함께 바로 끝남. false라서 start가 진행됨
t1.daemon = False
t1.start()
 
print("### End ###")