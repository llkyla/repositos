# 셋 선언
s1 = set()
s2 = set()

# 원소 추가
s1.add(10)
s1.add(20)
s1.add(30)
s1.add(40)

s2.add(10)
s2.add(11)
s2.add(22)
s2.add(33)
s2.add(44)

# 셋 출력
print("s1:", s1)
print("s2:", s2)
print()
# 순서 보장 x 

# 원소 삭제
s1.remove(20)
s1.add(40) # 중복된 원소는 추가되지 않음
print("20 삭제 후 s1:", s1)
print()

# 원소의 존재 여부 확인
print(33 in s1)
print(33 in s2)
print()

# 집합의 크기 확인
print(len(s1), len(s2))
print()

# 합집합 연산
s3 = s1 | s2
print("s1과 s2의 합집합:", s3)
print()

# 교집합 연산
s3 = s1 & s2
print("s1과 s2의 교집합:", s3)
print()

# 차집합 연산
s3 = s1 - s2
print("s1과 s2의 차집합:", s3)
print()