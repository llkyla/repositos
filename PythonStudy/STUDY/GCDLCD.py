from math import sqrt

def get_divisors(n):
	s = set()
	for i in range(1, int(sqrt(n)) + 1):
		if n % i == 0:
			s.add(i)
			s.add(n // i)
	return s



print("------")

def divisors(n):
	div = []
	for i in range(1, n+1):
		if(n % i == 0):
			div.append(i)
	return div

# def get_GCD(a, b):
	set_a = get_divisors(a)
	set_b = get_divisors(b)
	return max(set_a & set_b)

#print(get_GCD(12, 8))

from math import sqrt

def get_divisors(n):
	s = set()
	for i in range(1, int(sqrt(n)) + 1):
		if n % i == 0:
			s.add(i)
			s.add(n // i)
	return s

def is_prime(n):
	return (len(get_divisors(n)) == 2)

print(is_prime(7))
print(is_prime(8))