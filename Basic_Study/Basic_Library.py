#####################
import numpy as np
#####################

"""Computation of vectors"""
x = np.array([i for i in range(10)])
y = np.array([i for i in range(10, 20)])

print('x:', x)
print('y:', y)
print('x+1',x+1)
print('x+y:', x+y)
print('x-y:', x-y)
print('2*x:',2*x)
print('x/2',x/2)
print('x^2', x**2, np.square(x))
print('x*y', x*y)
print('np.append(x, 1)', np.append(x, 1))

print('log(y):', np.log(y))
print('exp(x):', np.exp(x))

print("inner product:",np.inner(x, y), np.dot(x, y), sum(x*y))
print("outer product:", np.outer(x, y))
#print("concatenation of vectors:", np.concatenate(x, y))

"""Computation on matrix"""
X = np.ones((6,5))
Y = np.random.normal(0, 1, size=(5,5))
print(X)
print(Y)

sorted(Y, key=lambda x:x[0], reverse=True)

print("inner product of X and Y:", np.dot(X, Y), np.matmul(X, Y), X@Y)

print("sum of columns in Y:", Y.sum(0))
print("sum of columns in X:", X.sum(0))
print("sum of columns in X:", X.sum(1))
print("sum of all elements in X", X.sum())

print("transpose of Y", Y.transpose())
print("inverse matrix of Y", np.linalg.inv(Y))
print("trace of Y", np.trace(Y))
print("EVD", np.linalg.eig(Y))
print("SVD", np.linalg.svd(Y))

"""Statistics on matrix"""
R = np.random.normal(size=(2,100000))

print("mean of columns in R:", R.mean(0))
print("variance of columns in R:", R.var(0))
print("mean of rows in R:", R.mean(1))
print("variance of rows in R:", R.var(1))

"""Norms and normalization"""
print("frobenius norm of R:", np.linalg.norm(R))
print("1-norm of R:", np.linalg.norm(R, ord=1))
print("2-norm of R:", np.linalg.norm(R, ord=2))

def normalization(M):
  res = np.linalg.norm(M, axis=1)
  if res.all() > 0:
    for i in range(len(res)):
      M[i] = M[i]/res[i]
    return M 
  else:
    return M 

result = normalization(R)
print(np.linalg.norm(result, axis=1))



#####################
import matplotlib.pyplot as plt
#####################

x = np.linspace(-5, 5, num=50)
y = x**2+5

plt.plot(x, y)
# plt.plot(x, y+3)
plt.title('Quadratic function')
plt.legend(['y=x^2+5'])

# plt.savefig(all_dir + '/quadratic_function.png')