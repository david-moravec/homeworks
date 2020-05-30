import numpy as np
from scipy.linalg import toeplitz
import matplotlib.pyplot as plt

def Initialize(A, B, r, n, h):
  x = np.linspace(A, B, n)
  init_cond = np.sin(x) + 1/10 * np.sin(10*x)

  #matrix construction
  return init_cond, x

def ImplMatrix(r, n, h):
  row = np.zeros(n)
  row[0] = 1 + 2*r 
  row[1] = -r

  mat = toeplitz(row) 
  return mat

def Update(old, new):
  old = new
  return old

def Plot(x, data1, lbl1, data2, lbl2, a, itr):
  plot = plt.figure()
  plt.axvline(linewidth=0.5, color='black')
  plt.axhline(linewidth=0.5, color='black')
  plt.grid(axis='both')
  plt.title('koeficient difuse {} iterace {}'.format(a, itr))
  subplot = plot.add_subplot(111)

  axes = plt.gca()
  axes.set_xlim([0,2*3.1415926])
  plt.plot(x, data1, label=lbl1, 
           linewidth=0.8, color='green')
  plt.plot(x, data2, label=lbl2, 
           linewidth=0.8, color='red')
  plt.legend()
  plt.savefig('./results/a_{}/iter_{}.png'.format(a, itr), bbox_inches='tight')
