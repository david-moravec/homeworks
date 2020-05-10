#include <iostream>
#include <vector>
#include <cmath>
#include <fstream>
#include <stdlib.h> 

#include "src/tangentAprox.hpp"
#include "src/ODEstruct.hpp"

double pythagoras(const double& a, const double& b) {
	double c;
	
	c = sqrt(pow(a, 2) + pow(b, 2));

	return c;
}

double Energy(const ODEstruct& X) {
	double E;

	const double G = 6.67408e-11;	//gravitational constant
	const double M = 5.972e24;	//mass of earth 
	const double mu = G*M;
	const double massMoon = 7.34767309e13;

	E = 0.5 * pythagoras(X.z3, X.z4) - mu / pythagoras(X.z1, X.z2);

	return E * massMoon;
}

int main(int argc, char** argv) {

	const double h = atof(argv[1]); 	//converitng *char to double timestep
	//const double h = 200;
	const int days = 30;	//for how many days we want to simulate the orbit
	const int n = days * 24 * 3600 / h; //number of cycles

	std::vector<double> EsolCollatz;
	std::vector<ODEstruct> solCollatz;

	std::vector<double> EsolRK;
	std::vector<ODEstruct> solRK;

	//solCollatz - solution using collatz method
	//initial Z - position
	ODEstruct initConditions;
	
	initConditions.z1 = 383.4e6;
	initConditions.z2 = 0; 
	initConditions.z3 = 0;
	initConditions.z4 = 1000;
	solCollatz.push_back(initConditions);
	solRK.push_back(initConditions);
	//initial Zp - speed

	//solRK - solution using RK method
	//initial Z - position

	
	for(int i = 0; i <= n; i++) {	
		aprox tangent (solCollatz[i], h); 
		solCollatz.push_back(solCollatz[i] + h * tangent.collatz());
		EsolCollatz.push_back(Energy(solCollatz[i+1]));

		aprox tangentsolRK(solRK[i], h); 
		solRK.push_back(solRK[i] + h * tangentsolRK.RK());
		EsolRK.push_back(Energy(solRK[i+1]));
	}

	
	std::ofstream resultsCollatz("solCollatz.dat");
	std::ofstream resultsRK("solRK.dat");
	for(int i = 0; i <= solCollatz.size(); i++) {
		if( i%20 == 0) {
			double time = h * i;
			resultsCollatz << " " << solCollatz[i].z1 << " " << solCollatz[i].z2 << " " << time << " " << EsolCollatz[i] << std::endl;
			resultsRK << " " << solRK[i].z1 << " " << solRK[i].z2 << " " << time << " " << EsolRK[i] << std::endl;
		}
	}
	resultsCollatz.close();
	resultsRK.close();

	return 0;
}

