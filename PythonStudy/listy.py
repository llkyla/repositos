# 리스트 선언
lst = [100, 200]

# 맨 뒤에 원소 삽입
lst.append(10)
lst.append(20)
lst.append(30)

# 리스트 출력
print("리스트:", lst)
print()

# 원소 삭제
deleted_value = lst.pop(2)
print("삭제된 원소:", deleted_value)
print("삭제 후 리스트:", lst)
print()

# 맨 뒤의 원소 삭제
deleted_value = lst.pop()
print("삭제된 원소:", deleted_value)
print("삭제 후 리스트:", lst)
print()

# 특정 위치의 원소 접근
print("인덱스 1의 원소:", lst[1])
print()

# 리스트의 크기 확인
print("리스트의 크기:", len(lst))
print()

# 특정 값의 존재 여부 확인
value1 = 20
print(value1 in lst)
value2 = 40
print(value2 in lst)