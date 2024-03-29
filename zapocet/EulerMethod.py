import numpy as np
import misc
import matplotlib.pyplot as plt
import parameters as par

class EulerMethod:
  def __init__(self): 
     self.u_a = par.U_A
     self.u_b = par.U_B
     self.n = par.n
     self.h = (par.B - par.A) / par.n
     self.init_cond, self.x = misc.Initialize(par.A, par.B, self.n,
                                              self.h)

  def Explicit(self, a, itr):
    r = 0.5
    U_old = self.init_cond
    U_new = np.zeros(self.n)
    U_new[0] = self.u_a
    U_new[-1] = self.u_b

    for itr in range(0, itr):
      for i in range(1, len(U_new) - 1):
        U_new[i] = U_old[i] + r * (U_old[i-1] - 2 * U_old[i] + U_old[i+1])
      U_old = misc.Update(U_old, U_new)
    self.expl = U_new

  def Implicit(self, a, dt, itr): 	
    r = dt*a / (self.h * self.h)
    U_old = self.init_cond
    #breakpoint()
    impl_matrix = misc.ImplMatrix(r, self.n, self.h)
    #print(impl_matrix[1])
 
    for itr in range(0, itr):
      U_new = np.linalg.solve(impl_matrix, U_old) 
      U_old = misc.Update(U_old, U_new)
		
    self.impl = U_new
    #print(self.impl)
