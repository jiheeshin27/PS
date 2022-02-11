# 리스트 정렬
sorted() # 내장함수, 정렬된 새로운 리스트를 리턴
sort() # 리스트메서드, 해당 리스트 정렬
# 정렬을 반대로 하고 싶은 경우 reverse=True

# 문자열 길이순으로 정렬하고 싶다면? => 정렬에 이용하는 키(key) 지정
L = ["파이썬", "알고리즘", "인터뷰"]
print(sorted(L, key=lambda x: len(x)))

L2.sort(key=lambda x: x["score"], reverse=True) # 성적 높은순 정렬

# 선형 탐색 linear Search
def linear_search(L, x):
    i = 0
    while i < len(L) and L[i] != x:
        i += 1
    if i < len(L):
        return i
    else:
        return -1

S = [3,4,5,6,7,8]
linear_search(S, 6)

# 이진 탐색 Binary Search O(log n)
# 탐색하려는 리스트가 이미 정렬되어 있는 경우에만 적용 가능
