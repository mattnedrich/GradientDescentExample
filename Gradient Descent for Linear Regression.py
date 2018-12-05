from matplotlib.pyplot import legend, plot, scatter, show
from numpy import array, mean, sqrt, square

data_set = array([
    [32,31], [53,68], [60,62], [47,71], [59,87],
    [55,78], [52,79], [39,59], [48,75], [52,71],
    [45,55], [54,82], [44,62], [58,75], [56,81],
    [48,60], [44,82], [60,97], [45,48], [38,56],
    [66,83], [65,11], [47,57], [41,51], [51,75]
])

x_list = data_set[:, 0]
y_list = data_set[:, 1]

intercept = 0
slope = 0

learning_rate = 0.0001
iteration_cycles = 1000

count = len(x_list)

line_equation = lambda x: slope * x + intercept

for _ in range(1000):
    
    new_y = list(map(line_equation, x_list))
    
    y_difference = y_list - new_y
    
    intercept_gradient = sum(2 / count * y_difference)
    slope_gradient = sum(2 / count * y_difference * x_list)
    
    intercept += learning_rate * intercept_gradient
    slope += learning_rate * slope_gradient

predicted_y = list(map(line_equation, x_list))

rmse = sqrt(mean(square(y_list - predicted_y)))

print("intercept =", intercept)
print("slope =", slope)
print("rmse =", rmse)

test_x = [44, 32, 63]
test_y = list(map(line_equation, test_x))

scatter(x_list, y_list, label='original')
scatter(test_x, test_y, label='prediction')
plot(x_list, predicted_y, label='line of best fit')
legend()
show()
