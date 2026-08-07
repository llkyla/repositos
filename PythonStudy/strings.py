# 문자열 선언
s = "abcdef"

# 문자열 출력
print(s)
print()

# 문자열 연결
s1 = "Hello"
s2 = "World"
s3 = s1 + s2
print("연결된 문자열:", s3)
print()

# 문자열 길이 확인
print("문자열의 길이:", len(s))
print()

# 특정 위치의 문자 접근
print("인덱스 1의 문자:", s[1])
print()

# 문자열 자르기
print("자른 부분 문자열:", s[2:5])
print()

# 특정 문자 또는 부분 문자열의 존재 여부 확인
print("abc" in "PPabcPPP")
print("abc" in "PPAbcaPP")