# 리스트 컴프리헨션
res = [n * 2 for n in range(1, 10+1) if n % 2 == 1]
print(res)

res = {key: value for key, value in original.items()}

# 제너레이터
# 루프의 반복 동작을 제어할 수 있는 루틴 형태. yield로 제너레이터가 여기까지 실행 중이던 값을 내보냄.
# 내보낸 뒤 다음 함수는 종료되지 않고 맨 끝에 도달할 때까지 계속됨.

def get_natural_number():
    n = 0
    while True:
        n += 1
        yield n

g = get_natural_number()

for _ in range(0, 100):
    print(next(g))

# enumerate
# 여러가지 자료형을 인덱스를 포함한 enumerate 객체로 리턴

a = [1,2,3,4,5,6]

for i, v in enumerate(a):
    print(i, v)
