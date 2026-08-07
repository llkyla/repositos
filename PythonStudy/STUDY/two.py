# 5층짜리 역피라미드 별 찍기
for i in range(5):
    space = ' ' * i
    stars = '*' * (9 - 2 * i)
    print(space + stars)
