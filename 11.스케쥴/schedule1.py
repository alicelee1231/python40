import schedule
import time


def test():
    print("start")

schedule.every(1).seconds.do(test)


while True:
    schedule.run_pending()
    time.sleep(1)