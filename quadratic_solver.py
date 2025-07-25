"""
A console application that solves quadratic equations of the form ax^2 + bx + c = 0
using the quadratic formula to find real roots.
"""

import math

def main():
	"""
	Prompts user for coefficients a, b, c and calculates the roots of the quadratic equation using the discriminant method.
	"""
	print('Quadratic Equation Solver')
	a = float(input('Enter a: '))
	b = float(input('Enter b: '))
	c = float(input('Enter c: '))
	
	discriminant = b * b - 4 * a * c  # Calculate discriminant to determine number of roots
	
	if discriminant > 0:
		# Two real roots
		answer1 = (-b + math.sqrt(discriminant)) / (2 * a)
		answer2 = (-b - math.sqrt(discriminant)) / (2 * a)
		print('Two roots: ' + str(answer1) + ', ' + str(answer2))
	elif discriminant == 0:
		# One real root
		answer = (-b + math.sqrt(discriminant)) / (2 * a)
		print('One root: ' + str(answer))
	else:
		# No real roots
		print('No real roots')


if __name__ == '__main__':
	main()
