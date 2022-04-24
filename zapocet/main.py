import os
import math
import EulerMethod as eu
import misc

import parameters as par


eqn = eu.EulerMethod()

for a in par.coefs:
  for itr in par.no_iter:
    
    eqn.Explicit(a, itr)
    eqn.Implicit(par.dt_impl, a, itr)
    print('koeficient a = {}, pocet iteraci no_iter = {}'
           .format(a, itr))
    
    if not os.path.exists('./results/a_{}'.format(a)):
      os.makedirs('./results/a_{}'.format(a))
    
    misc.Plot(eqn.x, eqn.impl, "imlicit", eqn.expl, "explicit", a, itr)
