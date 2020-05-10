#include "tangentAprox.hpp"
#include "ODEstruct.hpp"


//function for evaluation of constant, that tangent coefficient in Zp equation 
ODEstruct aprox::F(const ODEstruct& old) {
	ODEstruct F;

	const double G = 6.67408e-11;	//gravitational constant
	const double M = 5.972e24;	//mass of earth 
	const double length = sqrt( pow(old.z1, 2) + pow(old.z2, 2) ); //length of radius vector

	F.z1 = old.z3;
	F.z2 = old.z4;
	F.z3 = -G * M / pow(length ,2) *  1 / length * old.z1;
	F.z4 = -G * M / pow(length ,2) *  1 / length * old.z2;
	return(F);
}

ODEstruct aprox::euler() {
	ODEstruct k1;

	k1 = F(Z);
	return k1;	
}

ODEstruct aprox::collatz() {
	ODEstruct k1, k2;

	k1 = F(Z);
	k2 = F(Z + 0.5 * h * k1);
	return 0.5 * (k1 + k2); 	//Collatz
}

ODEstruct aprox::RK() {
	ODEstruct k1, k2, k3, k4;

	k1 = F(Z);
	k2 = F(Z + 0.5 * h * k1);
	k3 = F(Z + 0.5 * h * k2);
	k4 = F(Z + h * k3);
	return 1./6. * (k1 + 2*k2 + 2*k3 + k4);
}




