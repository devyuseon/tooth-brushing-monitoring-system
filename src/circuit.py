import time
import RPi.GPIO as GPIO

# 전역 변수 선언 및 초기화
trig1 = 23
trig2 = 12
echo1 = 24
echo2 = 16
green_led = 6  # 녹색 LED 첫째상태 표시
red_led = 13  # 적색 LED 둘째상태 표시

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(trig1, GPIO.OUT)
GPIO.setup(echo1, GPIO.IN)
GPIO.output(trig1, False)
GPIO.setup(trig2, GPIO.OUT)
GPIO.setup(echo2, GPIO.IN)
GPIO.output(trig2, False)
GPIO.setup(green_led, GPIO.OUT)
GPIO.setup(red_led, GPIO.OUT)

# 초음파 센서 값 측정


def measureDistance(child):

    global trig, echo

    # 초음파 센서 구분
    if child == 1:
        trig = trig1
        echo = echo1
    elif child == 2:
        trig = trig2
        echo = echo2

    GPIO.output(trig, True)  # 신호 1 발생
    time.sleep(0.00001)  # 짧은시간후 0으로 떨어뜨려 falling edge를 만들기 위함
    GPIO.output(trig, False)  # 신호 0 발생(falling 에지)

    while(GPIO.input(echo) == 0):
        pass
    pulse_start = time.time()  # 신호 1. 초음파 발생이 시작되었음을 알림
    while(GPIO.input(echo) == 1):
        pass
    pulse_end = time.time()  # 신호 0. 초음파 수신 완료를 알림

    pulse_duration = pulse_end - pulse_start
    return 340*100/2*pulse_duration

# 매개변수 'color'에 따라 다른 LED점등.

# 녹색 LED 켜기


def turnOnGreenLED():
    GPIO.output(green_led, True)

# 녹색 LED 끄기


def turnOffGreenLED():
    GPIO.output(green_led, False)

# 적색 LED 켜기


def turnOnRedLED():
    GPIO.output(red_led, True)

# 적색 LED 끄기


def turnOffRedLED():
    GPIO.output(red_led, False)
