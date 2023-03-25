# 우선순위큐: 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조
# 힙 -> 우선순위 큐를 구현하기 위해 사용하는 자료구조(최소힙, 최대힙)

# 최소힙 예제
import heapq

arr = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]


# 오름차순 힙 정렬(최소 힙)
def heapsort1():
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for val in arr:
        heapq.heappush(h, val)
    # 힙에 합입된 모든 원소를 차례대로 꺼내어 담기 -> 파이썬 라이브러리에서는 낮은 우선순위부터 pop
    for i in range(len(h)):
        result.append(heapq.heappop(h))

    return result

#내림차순 힙 정렬(최대 힙)
def heapsort2():
    h = []
    result = []
    for val in arr:
        # 라이브러리가 최소 힙만을 지원하므로 최대 힙 구현을 위해서는 부호를 바꾸어 push
        heapq.heappush(h, -val)
    for i in range(len(h)):
        # pop을 할때도 부호를 바꾸어 pop
        result.append(-heapq.heappop(h))


print(heapsort1())
print()
print(heapsort2())