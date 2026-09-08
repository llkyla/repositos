# 12928

from math import sqrt

def solution(n):
	s = set()
	for i in range(1, int(sqrt(n)) + 1):
		if n % i == 0:
			s.add(i)
			s.add(n // i)
	return sum(s)

# or
def diff_sol(num):
	return sum([i for i in range(1,num+1) if num%i==0]) # [] = output as list 
                                                        # i for i in range(1, num+1) = i is list element
														#                              where i \in [1, num+1]
														# only when num % i == 0