# Tooth-brushing-monitoring-system

## :sparkles: Description
라즈베리파이4를 이용한 IOT System. 
- Rasberry Pi에 초음파센서와 Led를 연결하여 칫솔걸이와 칫솔간의 거리를 측정해 양치질 여부를 판단. 이를 txt파일에 저장하고 웹에서 불러온다.
- Mosquitto MQTT borker을 통해 웹에 접속해 실시간으로 양치질 유무에대한 정보를 받는다.

### Directory structure
![directory-structure](https://user-images.githubusercontent.com/67352902/103431908-1f6d0b00-4c1b-11eb-8c9c-546439975185.PNG)

[**실행화면 보기**](https://developeryuseon.tistory.com/13?category=826002)

## :bulb: Features
- 집에 없을 때, 웹에 접속하여 자녀들이 양치질을 하고있는지, 언제했는지 확인
- 양치질 한 기록 확인

## :pencil2: Build With
- Flask
- Mosquitto MQTT broker (Paho)

## :key: How to Use

### Prerequisites
**가상환경에서 실행(myEnv라는 디렉터리에서 진행함)**
``` 
$ cd myEnv
$ source bin/activate
```

- Flask
```
(myEnv) $ pip install flask   
```
- MQTT (paho)
```
(myEnv) $ pip install paho.mqtt
(myEnv) $ pip install PILLOW
```
- mosquitto
```
$ sudo apt update
$ sudo apt install -y mosquitto mosquitto-clients
```

### Installation
```
(myEnv) $ python3 calctime.py&
(myEnv) $ python3 mqtt.py&
(myEnv) $ python3 mosquitto -c /ect/mosquitto/mosquitto.conf&
(myEnv) $ python3 app.py
```
