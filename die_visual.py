import pygal
from die import Die


die_2 = Die()
die_1 = Die()
results = []
for roll_num in range(100):
    result = die_1.roll() + die_2.roll()
    results.append(result)
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
hist = pygal.Bar()
hist.title = 'results of rolling two D6 1000 times.'
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10' '12']
hist.x_title  = 'Result'
hist.y_title = 'frequency of result'
hist.add('D6+ D6', frequencies)
hist.render_to_file('die_visual.svg')
print (frequencies)