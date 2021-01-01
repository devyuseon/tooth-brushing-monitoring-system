# publisher

import time
import paho.mqtt.client as mqtt
import circuit  # 초음파 센서 입력 모듈 임포트

broker_ip = "localhost"  # 현재 이 컴퓨터를 브로커로 설정
distanceStd = 10

client = mqtt.Client()
client.connect(broker_ip, 1883)
client.loop_start()


def calcactive(distance):
    if distance > distanceStd or distance == distanceStd:
        return '하고'
    if distance < distanceStd:
        return '안 하고'


while(True):
    distance1 = circuit.measureDistance(1)
    msg1 = calcactive(distance1)
    distance2 = circuit.measureDistance(2)
    msg2 = calcactive(distance2)
    client.publish("old", msg1, qos=0)
    client.publish("young", msg2, qos=0)
    # client.publish("young", distance2, qos=0)
    time.sleep(1)

client.loop_stop()
client.disconnect()
