# 사다리 G5
# w1 : c = w : h2, w2 : c = w : h1
# w1 = c*w / h2, w2 = c*w / h1
# w = w1 + w2 = c*w / h2 + c*w / h1 = c*w*(h1+h2) / (h1*h2)
# -> 1 = c*(h1+h2) / (h1*h2) -> c = h1*h2 / (h1+h2)
# h1 = (x**2-w**2)**0.5, h2 = (y**2-w**2)**0.5 임을 알 수 있다.
# => h1 = (x**2-w**2)**0.5, h2 = (y**2-w**2)**0.5, c = h1*h2 / (h1+h2)로 이분탐색 진행

import sys

input = sys.stdin.readline
x, y, c = map(float, input().split())
start = 0
end = min(x, y)
result = 0


def search(x, y, w):
    h1 = (x ** 2 - w ** 2) ** 0.5
    h2 = (y ** 2 - w ** 2) ** 0.5
    tmp_c = h1 * h2 / (h1 + h2)
    return tmp_c


while end - start > 0.000001:
    mid = (start + end) / 2
    if search(x, y, mid) >= c:
        result = mid
        start = mid
    else:
        end = mid

print("{:.03f}".format(result))
