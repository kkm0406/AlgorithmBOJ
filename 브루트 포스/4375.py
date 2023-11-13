# 1 S3
import sys

input = sys.stdin.readline
while True:
    # 종료 조건이 따로 없으므로 try-catch로 예외처리
    try:
        # n보다 큰 1로만 이루어진 숫자의 자리수 찾기(ex: 111, 11111)
        n = int(input())

        num = '1'  # 1부터 시작
        while True:
            # 나누어 떨어지지 않으면
            if int(num) % n != 0:
                # 기존 숫자에 1추가
                num += '1'
            else:
                print(len(num))
                break
    except:
        break
