import numpy as np
import misc
import matplotlib.pyplot as plt

class EulerMethod:
  def __init__(self,A, B, U_A, U_B, no, dt, a, n):
     self.a = A
     self.b = B
     self.u_a = U_A
     self.u_b = U_B
     self.iter = no
     self.A = a
     self.dt = dt
     self.n = n

     self.h = (self.b - self.a) / self.n
     self.r = self.A * self.dt / (self.h*self.h)
     self.matrix, self.initCond, self.x = misc.Initialize(self.a, self.b, self.n)



  def ExplicitMethod(self):
    U_new = np.zeros(self.n)
    U_new[0] = self.u_a
    U_new[-1] = self.u_b

    U_old = self.initCond
    r = self.r

    for t in range(0, self.iter):
      for i in range(1, len(U_new) - 1):
        U_new[i] += U_old[i] + r * (U_old[i-1] - 2 * U_old[i] + U_old[i+1])

      U_old = misc.Update(U_old, U_new)

    self.expl = U_new

  def ImplicitMethod(self): 	
    r = self.r
    temp_matrix = self.matrix; 	
    time_diag = (1 / r) * np.ones(self.n)
    self.matrix = r * temp_matrix + np.diag(time_diag)
    U_old = self.initCond
 
    for t in range(0, self.iter):
    	U_new = np.linalg.solve(self.matrix, U_old)
    	U_old = misc.Update(U_old, U_new)
		
    self.impl = U_new

  def PlotResults(self):
    x = self.x
    plot = plt.figure()
    subplot = plot.add_subplot(111)
    plt.plot(x, self.impl, label='implicit')
    plt.plot(x, self.expl, label='expl')
    plt.legend(loc='upper left')
    plt.show()
