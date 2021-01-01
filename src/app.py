from flask import Flask, render_template, request
app = Flask(__name__)

# 초기 홈페이지


@app.route('/')
def index():
    return render_template('index.html')

# 첫째 데이터 조회


@app.route('/old/', methods=['GET'])
def old():
    f = open('./data/1.txt', 'r')  # 파일 열기
    data = f.readline().strip()  # 한 줄씩 읽기
    dic = {}  # 빈 딕셔너리 생성

    while data:
        nowTime, executionTime = data.split(',')  # ',' 기준으로 문자열 분리
        dic[nowTime] = executionTime  # 딕셔너리에 저장
        data = f.readline().strip()

    f.close()
    return render_template('old.html', dict=dic)

# 둘째 데이터 조회


@app.route('/young/', methods=['GET'])
def young():
    f = open('./data/2.txt', 'r')  # 파일 열기
    data = f.readline().strip()  # 한 줄씩 읽기
    dic = {}  # 빈 딕셔너리 생성

    while data:
        nowTime, executionTime = data.split(',')  # ',' 기준으로 문자열 분리
        dic[nowTime] = executionTime  # 딕셔너리에 저장
        data = f.readline().strip()

    f.close()
    return render_template('young.html', dict=dic)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
