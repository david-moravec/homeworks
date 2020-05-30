import numpy as np
import misc
import matplotlib.pyplot as plt

class EulerMethod:
  def __init__(self, 
               A, B, U_A,
               U_B, no_itr, a, n):
     self.u_a = U_A
     self.u_b = U_B
     self.iter = no_itr
     self.n = n

     self.h = (B - A) / n
     self.dt = 1e-6
     self.r = a * self.dt / (self.h*self.h)

     self.init_cond, self.x = misc.Initialize(A, B, self.r,
                                             n, self.h)

  def ExplicitMethod(self):
    U_new = np.zeros(self.n)
    U_new[0] = self.u_a
    U_new[-1] = self.u_b

    U_old = self.init_cond
    r = self.r

    for itr in range(0, self.iter):
      for i in range(1, len(U_new) - 1):
        U_new[i] = U_old[i] + r * (U_old[i-1] - 2 * U_old[i] + U_old[i+1])

      U_old = misc.Update(U_old, U_new)
    
    self.expl = U_new

  def ImplicitMethod(self): 	
    r = self.r
    U_old = self.init_cond
    #breakpoint()
    impl_matrix = misc.ImplMatrix(r, self.n, self.h)
    #print(impl_matrix[1])
 
    for itr in range(0, self.iter):
      U_new = np.linalg.solve(impl_matrix, U_old) 
      U_old = misc.Update(U_old, U_new)
		
    self.impl = U_new
    #print(self.impl)
