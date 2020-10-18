from fuzzy_system.fuzzy_variable_output import FuzzyOutputVariable
from fuzzy_system.fuzzy_variable_input import FuzzyInputVariable
# from fuzzy_system.fuzzy_variable import FuzzyVariable
from fuzzy_system.fuzzy_system import FuzzySystem

temp = FuzzyInputVariable('Temperature', 0, 1, 2)
temp.add_triangular('Cold', 0, 0, 1)
temp.add_triangular('Medium', 0, 1, 2)
temp.add_triangular('Hot', 1, 2, 2)

humidity = FuzzyInputVariable('Humidity', 0, 1, 2)
humidity.add_triangular('Wet', 0, 0, 1)
humidity.add_trapezoidal('Normal', 0, 1, 1, 2)
humidity.add_triangular('Dry', 1, 2, 2)

motor_speed = FuzzyOutputVariable('Speed', 0, 100, 100)
motor_speed.add_triangular('Slow', 0, 0, 50)
motor_speed.add_triangular('Moderate', 10, 50, 90)
motor_speed.add_triangular('Fast', 50, 100, 100)

system = FuzzySystem()
system.add_input_variable(temp)
system.add_input_variable(humidity)
system.add_output_variable(motor_speed)

system.add_rule(
		{ 'Temperature':'Cold',
			'Humidity':'Wet' },
		{ 'Speed':'Slow'})

system.add_rule(
		{ 'Temperature':'Cold',
			'Humidity':'Normal' },
		{ 'Speed':'Slow'})

system.add_rule(
		{ 'Temperature':'Medium',
			'Humidity':'Wet' },
		{ 'Speed':'Slow'})

system.add_rule(
		{ 'Temperature':'Medium',
			'Humidity':'Normal' },
		{ 'Speed':'Moderate'})

system.add_rule(
		{ 'Temperature':'Cold',
			'Humidity':'Dry' },
		{ 'Speed':'Moderate'})

system.add_rule(
		{ 'Temperature':'Hot',
			'Humidity':'Wet' },
		{ 'Speed':'Moderate'})

system.add_rule(
		{ 'Temperature':'Hot',
			'Humidity':'Normal' },
		{ 'Speed':'Fast'})

system.add_rule(
		{ 'Temperature':'Hot',
			'Humidity':'Dry' },
		{ 'Speed':'Fast'})

system.add_rule(
		{ 'Temperature':'Medium',
			'Humidity':'Dry' },
		{ 'Speed':'Fast'})

output = system.evaluate_output({
				'Temperature':0.5,
				'Humidity':0.7
		})

print(output)
# print('fuzzification\n-------------\n', info['fuzzification'])
# print('rules\n-----\n', info['rules'])

system.plot_system()