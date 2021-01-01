import time
import circuit
from multiprocessing import Process

distanceStd = 4  # 양치질 유무의 기준이 되는 거리


# 각 초음파 센서의 정보를 각 파일에 저장
def storetotxt(nowTime, executionTime, child):

    if child == 1:
        filename = "./data/1.txt"
    elif child == 2:
        filename = "./data/2.txt"

    file = open(filename, 'a')
    data = "%s,%s\n" % (nowTime, executionTime)
    file.write(data)
    file.close()

# 자식 번호 구분하여 LED제어


def controlLED(onoff, child):
    if child == 1:
        if onoff == True:
            circuit.turnOnGreenLED()
        else:
            circuit.turnOffGreenLED()
    if child == 2:
        if onoff == True:
            circuit.turnOnRedLED()
        else:
            circuit.turnOffRedLED()

# 초음파 센서의 값으로 양치질 유무 판정 후 시간을 문자열로 변환함


def calcTime(child):
    active = False  # 현재상태 (False = 양치질 X)

    while(True):
        distance = circuit.measureDistance(child)  # 초음파 센서 측정
        global execution, nowTime, executionTime
        executionTime = None  # 실행 시간 init

        # 양치질 하고 있지 않을 때
        if active == False:
            # 양치질 시작
            if distance > distanceStd or distance == distanceStd:  # 초음파 센서에서 멀어짐 == 양치질 시작함
                active = True  # 양치질 하고 있는 상태
                controlLED(True, child)
                now = time.localtime()  # 시작 한 시간을 기준으로 타임라인 기록 위함
                # now로 받은 현재 시간을 nowTime에 저장
                nowTime = "%04d/%02d/%02d %02d:%02d" % (
                    now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min)
                start = time.time()  # 시작한 시간 초단위 저장

        # 양치질 안 할 때
        if active == True:
            # 양치질 끝남
            if distance < distanceStd:  # 초음파 센서에서 가까워짐 == 양치질 끝냄
                controlLED(False, child)
                end = time.time()  # 양치질 끝낸 시간 초단위 기록
                # 수행 시간 측정
                execution = end - start
                executionTime = "%2d분 %02d초" % (
                    execution / 60, execution % 60)
                active = False  # 양치질 멈춤 상태
                storetotxt(nowTime, executionTime, child)  # 파일에 저장

        time.sleep(1)


# calcTime(1)과 calcTime(2)를 동시에 돌리기 위해 사용
if __name__ == '__main__':
    Process(target=calcTime, args=(1,)).start()
    Process(target=calcTime, args=(2,)).start()
