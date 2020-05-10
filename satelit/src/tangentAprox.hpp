#ifndef TANGENTAPROX_HPP
#define TANGENTAPROX_HPP

#include <cmath>
#include "ODEstruct.hpp"
class aprox {
public:
	ODEstruct Z;
	double h;

	//constructors
	aprox() {}
	aprox(const ODEstruct& z, const double& H): Z(z), h(H) {};
	~aprox() {};

	//methods
	virtual ODEstruct F(const ODEstruct& old);

	ODEstruct euler();
	ODEstruct collatz();
	ODEstruct RK();
};

class orbit: public aprox{
	public:
		const double G = 6.67408e-11;	//gravitational constant
		const double M = 5.972e24;	//mass of earth 
		
		ODEstruct F(const ODEstruct& old);
};

#endif
