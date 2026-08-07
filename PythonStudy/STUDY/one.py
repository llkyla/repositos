# 5층짜리 피라미드 별 찍기
for i in range(5):
    space = ' ' * (4 - i)
    stars = '*' * (2 * i + 1)
    print(space + stars)
