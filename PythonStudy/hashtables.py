# 해시테이블 선언
dt = {}

# 특정 키에 대한 값 할당
dt["apple"] = 500
dt["banana"] = 1000
dt["cherry"] = 700

# 딕셔너리 출력
print("딕셔너리:", dt)
print()

# 특정 키의 값 조회
print("banana의 값:", dt["banana"])
print()

# 특정 키의 값 삭제
del dt["cherry"]
print("cherry 삭제 후 딕셔너리:", dt)
print()

# 딕셔너리의 크기 확인
print("딕셔너리의 크기:", len(dt))
print()

# 특정 키의 존재 여부 확인
print("apple" in dt)
print("pineapple" in dt)
print(142 in dt)