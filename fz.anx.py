from fuzzy_system.fuzzy_variable_output import FuzzyOutputVariable
from fuzzy_system.fuzzy_variable_input import FuzzyInputVariable
# from fuzzy_system.fuzzy_variable import FuzzyVariable
from fuzzy_system.fuzzy_system import FuzzySystem

inp1 = FuzzyInputVariable('Neurotocism', 45, 51, 100)
inp1.addTriangular('SB1', 45, 45, 47
	).addTriangular('SB2', 45, 47, 49
	).addTriangular('SB3', 47, 49, 51
	).addTriangular('SB4', 49, 51, 51)

inp2 = FuzzyInputVariable('Extroversion', 40, 50, 100)
inp2.addTriangular('SD1', 40, 40, 43.25
	).addTriangular('SD2', 40, 43.25, 46.75
	).addTriangular('SD3', 43.25, 46.75, 50
	).addTriangular('SD4', 46.75, 50, 50)

out1 = FuzzyOutputVariable('Anxiety', 0, 60, 100)
out1.addTriangular('L', 0, 0, 20
	).addTriangular('M', 0, 20, 40
	).addTriangular('H', 20, 40, 60
	).addTriangular('E', 40, 60, 60)

system = FuzzySystem()
system.add_input_variable(inp1)
system.add_input_variable(inp2)
system.add_output_variable(out1)

system.add_rule({'Neurotocism':'SB1','Extroversion':'SD3'},{'Anxiety':'M'})
system.add_rule({'Neurotocism':'SB1','Extroversion':'SD3'},{'Anxiety':'H'})
system.add_rule({'Neurotocism':'SB1','Extroversion':'SD4'},{'Anxiety':'M'})
system.add_rule({'Neurotocism':'SB1','Extroversion':'SD4'},{'Anxiety':'H'})
system.add_rule({'Neurotocism':'SB2','Extroversion':'SD1'},{'Anxiety':'L'})
system.add_rule({'Neurotocism':'SB2','Extroversion':'SD1'},{'Anxiety':'M'})
system.add_rule({'Neurotocism':'SB2','Extroversion':'SD2'},{'Anxiety':'L'})
system.add_rule({'Neurotocism':'SB2','Extroversion':'SD2'},{'Anxiety':'M'})
system.add_rule({'Neurotocism':'SB2','Extroversion':'SD2'},{'Anxiety':'H'})
system.add_rule({'Neurotocism':'SB2','Extroversion':'SD3'},{'Anxiety':'L'})
system.add_rule({'Neurotocism':'SB2','Extroversion':'SD3'},{'Anxiety':'M'})
system.add_rule({'Neurotocism':'SB2','Extroversion':'SD3'},{'Anxiety':'H'})
system.add_rule({'Neurotocism':'SB2','Extroversion':'SD4'},{'Anxiety':'L'})
system.add_rule({'Neurotocism':'SB2','Extroversion':'SD4'},{'Anxiety':'M'})
system.add_rule({'Neurotocism':'SB2','Extroversion':'SD4'},{'Anxiety':'H'})
system.add_rule({'Neurotocism':'SB3','Extroversion':'SD1'},{'Anxiety':'L'})
system.add_rule({'Neurotocism':'SB3','Extroversion':'SD1'},{'Anxiety':'M'})
system.add_rule({'Neurotocism':'SB3','Extroversion':'SD2'},{'Anxiety':'L'})
system.add_rule({'Neurotocism':'SB3','Extroversion':'SD2'},{'Anxiety':'H'})
system.add_rule({'Neurotocism':'SB3','Extroversion':'SD3'},{'Anxiety':'L'})
system.add_rule({'Neurotocism':'SB3','Extroversion':'SD3'},{'Anxiety':'M'})
system.add_rule({'Neurotocism':'SB3','Extroversion':'SD3'},{'Anxiety':'H'})
system.add_rule({'Neurotocism':'SB3','Extroversion':'SD3'},{'Anxiety':'E'})
system.add_rule({'Neurotocism':'SB3','Extroversion':'SD4'},{'Anxiety':'L'})
system.add_rule({'Neurotocism':'SB3','Extroversion':'SD4'},{'Anxiety':'M'})
system.add_rule({'Neurotocism':'SB3','Extroversion':'SD4'},{'Anxiety':'H'})
system.add_rule({'Neurotocism':'SB3','Extroversion':'SD4'},{'Anxiety':'E'})
system.add_rule({'Neurotocism':'SB4','Extroversion':'SD2'},{'Anxiety':'M'})
system.add_rule({'Neurotocism':'SB4','Extroversion':'SD2'},{'Anxiety':'H'})
system.add_rule({'Neurotocism':'SB4','Extroversion':'SD3'},{'Anxiety':'L'})
system.add_rule({'Neurotocism':'SB4','Extroversion':'SD3'},{'Anxiety':'M'})
system.add_rule({'Neurotocism':'SB4','Extroversion':'SD3'},{'Anxiety':'H'})
system.add_rule({'Neurotocism':'SB4','Extroversion':'SD3'},{'Anxiety':'E'})
system.add_rule({'Neurotocism':'SB4','Extroversion':'SD4'},{'Anxiety':'L'})
system.add_rule({'Neurotocism':'SB4','Extroversion':'SD4'},{'Anxiety':'M'})
system.add_rule({'Neurotocism':'SB4','Extroversion':'SD4'},{'Anxiety':'H'})
system.add_rule({'Neurotocism':'SB4','Extroversion':'SD4'},{'Anxiety':'E'})


output = system.evaluate_output({
	'Neurotocism':45,
	'Extroversion':45
})

print(output)
# print('fuzzification\n-------------\n', info['fuzzification'])
# print('rules\n-----\n', info['rules'])

system.plot_system()