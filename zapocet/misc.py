import numpy as np
from scipy.linalg import toeplitz

def Initialize(A, B, n):
  h = (A - B) / n
  x = np.linspace(A, B, n)
  init_cond = np.sin(x) + 1/10 * np.sin(10*x)

  row = np.zeros(n)
  row[0] = -1
  row[1] = 2
  mat = toeplitz(row) 
  return mat, init_cond, x

def Update(old, new):
  old = new
  return old


