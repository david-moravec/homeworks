import math
import EulerMethod as eu


A = 0
B = 2*3.14159265257
U_A = 0
U_B = 0
no_iter = 1000
dt = 0.000001
a = 100
n = 100


eqn = eu.EulerMethod(A, B, U_A, U_B, no_iter, dt, a, n)
eqn.ExplicitMethod()
eqn.ImplicitMethod()
eqn.PlotResults()
#print(eqn.matrix)

	 
     
     


	

