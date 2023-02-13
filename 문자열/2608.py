# 로마 숫자 S1
import sys

alpha1 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
alpha2 = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

rome1 = sys.stdin.readline().strip()
rome2 = sys.stdin.readline().strip()


def get_num(s):
    l = len(s)  # 문자열 길이
    num = 0
    visited = [False] * l  # 방문 여부 저장
    for i in range(l):
        if not visited[i]:  # 아직 방문안한 문자이면
            # 작은 숫자가 큰 숫자 왼쪽에 오는 경우
            if i + 1 < len(s) and s[i:i + 2] in alpha2.keys():
                visited[i], visited[i + 1] = True, True
                num += int(alpha2[s[i:i + 2]])
            else:
                visited[i] = True
                num += int(alpha1[s[i]])
    return num


def get_rome(n):
    # if문으로 일일히 문자를 확인해주고 문자를 s라는 변수에 계속 더해줌
    s = ""
    while n > 0:
        if n >= 1000:
            s += "M"
            n -= 1000
        elif n >= 900:
            s += "CM"
            n -= 900
        elif n >= 500:
            s += "D"
            n -= 500
        elif n >= 400:
            s += "CD"
            n -= 400
        elif n >= 100:
            s += "C"
            n -= 100
        elif n >= 90:
            s += "XC"
            n -= 90
        elif n >= 50:
            s += "L"
            n -= 50
        elif n >= 40:
            s += "XL"
            n -= 40
        elif n >= 10:
            s += "X"
            n -= 10
        elif n >= 9:
            s += "IX"
            n -= 9
        elif n >= 5:
            s += "V"
            n -= 5
        elif n >= 4:
            s += "IV"
            n -= 4
        elif n >= 1:
            s += "I"
            n -= 1
    return s


result1 = get_num(rome1) + get_num(rome2)
result2 = get_rome(result1)

print(result1)
print(result2)
