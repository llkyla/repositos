# 2628

a, b = map(int, input().split(' '))
c, d = map(int, input().split(' '))

if a > b:
    a, b = b, a

if c > d:
    c, d = d, c

if (a < c < b) != (a < d < b):
    print("cross")
else:
    print("not cross")

'''
if (((c > a) or (c < b)) and ((d < a) or (d > b))) or (((d > a) or (d < b)) and ((c < a) or (c > b))):
    print("cross")

else:
    print("not cross")
'''
