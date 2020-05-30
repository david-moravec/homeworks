import os
import math
import EulerMethod as eu
import misc


A = 0  # okraj intervalu - A
B = 2*3.14159265257 #okraj intervalu - B
U_A = 0  # dirichlet v bode A
U_B = 0  # dirichlet v bode B
no_iter = [1, 10, 100] #pocet iteraci
coefs = [1, 10, 100]  #koeficienty difuze
n = 100
dt_impl = 0.01 # expl time step je zadan podle stability

eqn = eu.EulerMethod(A, B, U_A, U_B, n)

for a in coefs:
  for itr in no_iter:
    
    eqn.Explicit(a, itr)
    eqn.Implicit(dt_impl, a, itr)
    print('koeficient a = {}, pocet iteraci no_iter = {}'
           .format(a, itr))
    
    if not os.path.exists('./results/a_{}'.format(a)):
      os.makedirs('./results/a_{}'.format(a))
    
    misc.Plot(eqn.x, eqn.impl, "imlicit", eqn.expl, "explicit", a, itr)
