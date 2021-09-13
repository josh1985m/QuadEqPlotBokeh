import math
from bokeh import plotting

a = -.5
b = 40
c = -600

x_plus_eq = (-b + math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
x_minus_eq = (-b - math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
print(x_minus_eq)
print(x_plus_eq)
x_values = []
y_values = []
for x in range(-100, 100):
    z = (-.5*x**2)+(40*x)-300   # Equation #
    y_values.append(z)
    x_values.append(x)

print(x_values)
print(y_values)

p = plotting.figure(title="Quad Eq", x_axis_label='x', y_axis_label='y')
p.circle(x_plus_eq, 0, legend_label='x+,0', size=5)
p.circle(x_minus_eq, 0, legend_label='x-,0', size=5)
p.line(x_values, y_values, legend_label='(-.5*x**2)+(40*x)-300', line_width=1)
plotting.show(p)