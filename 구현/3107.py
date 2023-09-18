# IPv6 G5

import sys

input = sys.stdin.readline

ip = input().strip()
ip = ip.split(":")
if ip[0] == "":  # ex) ::1
    ip = ip[1:]
if ip[-1] == "":  # ex)1::
    ip = ip[:-1]

result = ""

for item in ip:
    if item == "":  # "::"가 있는 경우 0000으로 채움
        result += "0000:" * (8 - len(ip) + 1)
    else:  # 4자리 채우기
        result += item.zfill(4) + ":"

print(result[:-1])
