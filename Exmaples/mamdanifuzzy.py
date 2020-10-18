from fuzzy_system.fuzzy_variable_output import FuzzyOutputVariable
from fuzzy_system.fuzzy_variable_input import FuzzyInputVariable
# from fuzzy_system.fuzzy_variable import FuzzyVariable
from fuzzy_system.fuzzy_system import FuzzySystem

# import numpy as np
# np.seterr(divide='ignore', invalid='ignore')
# name.add_triangular("X"x,x,x)
# name.add_trapezoidal('X', x,x,x,x)

Bitter = FuzzyInputVariable('Bitter', 1, 2, 3)
Bitter.add_triangular('Low', 1, 1, 2)
Bitter.add_triangular('Medium', 1, 2, 3)
Bitter.add_triangular('High', 2, 3, 3)

Sweet = FuzzyInputVariable('Sweet', 1, 2, 3)
Sweet.add_triangular('Poor', 1, 1, 2)
Sweet.add_triangular('Average', 1, 2, 3)
Sweet.add_triangular('Maximum', 2, 3, 3)

Points = FuzzyOutputVariable('Points', 1, 2, 3)
Points.add_triangular('Less', 1, 1, 1)
Points.add_triangular('More', 2, 2, 2)
Points.add_triangular('Most', 3, 3, 3)

system = FuzzySystem()
system.add_input_variable(Bitter)
system.add_input_variable(Sweet)
system.add_output_variable(Points)

system.add_rule(
		{ 'Bitter':'Low',
			'Sweet':'Poor' },
		{ 'Points':'Less'})

system.add_rule(
		{ 'Bitter':'Medium',
			'Sweet':'Poor' },
		{ 'Points':'More'})

system.add_rule(
		{ 'Bitter':'High',
			'Sweet':'Poor' },
		{ 'Points':'More'})

system.add_rule(
		{ 'Bitter':'Low',
			'Sweet':'Average' },
		{ 'Points':'Less'})

system.add_rule(
		{ 'Bitter':'Medium',
			'Sweet':'Average' },
		{ 'Points':'Most'})

system.add_rule(
		{ 'Bitter':'High',
			'Sweet':'Average' },
		{ 'Points':'Most'})

system.add_rule(
		{ 'Bitter':'Low',
			'Sweet':'Maximum' },
		{ 'Points':'Less'})

system.add_rule(
		{ 'Bitter':'Medium',
			'Sweet':'Maximum' },
		{ 'Points':'More'})

system.add_rule(
		{ 'Bitter':'High',
			'Sweet':'Maximum' },
		{ 'Points':'Most'})

xzad1=input('Введите точку на линии абсцисс для входа 1 \n')
xzad2=input('Введите точку на линии абсцисс для входа 2 \n')

output = system.evaluate_output({
				'Bitter':xzad1,
				'Sweet':xzad2
		})

print(output)
print('fuzzification\n-------------\n', info['fuzzification'])
print('rules\n-----\n', info['rules'])

system.plot_system()