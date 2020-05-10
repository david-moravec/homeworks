#ifndef OPERATORS_HPP
#define OPERATORS_HPP

struct ODEstruct {
	double z1;
	double z2;
	double z3;
	double z4;
};

inline ODEstruct operator*(const double& S, const ODEstruct& a) {
	ODEstruct c;
	c.z1 = a.z1 * S;
	c.z2 = a.z2 * S;
	c.z3 = a.z3 * S;
	c.z4 = a.z4 * S;
	return c;
}
inline ODEstruct operator*(const ODEstruct& a, const double& S)  {
	ODEstruct c;
	c.z1 = a.z1 * S;
	c.z2 = a.z2 * S;
	c.z3 = a.z3 * S;
	c.z4 = a.z4 * S;
	return c;
}

inline ODEstruct operator+(const ODEstruct& a, const ODEstruct& b) {
	ODEstruct c;
	c.z1 = a.z1 + b.z1;
	c.z2 = a.z2 + b.z2;
	c.z3 = a.z3 + b.z3;
	c.z4 = a.z4 + b.z4;
	return c;
}

#endif
