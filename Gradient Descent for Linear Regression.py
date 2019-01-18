# plotting library (completely optional)
from matplotlib.pyplot import legend, plot, scatter, show
# for numeric operations. just to make code easy
from numpy import array, mean, sqrt, square

# dataset with x & y values
data_set = array([
    [32,31], [53,68], [60,62], [47,71], [59,87],
    [55,78], [52,79], [39,59], [48,75], [52,71],
    [45,55], [54,82], [44,62], [58,75], [56,81],
    [48,60], [44,82], [60,97], [45,48], [38,56],
    [66,83], [65,11], [47,57], [41,51], [51,75]
])

# seperating x & y from dataset
x_list = data_set[:, 0]
y_list = data_set[:, 1]

# initial model's parameters (for line equation)
intercept = 0
slope = 0

# training rate & iteration cycle count
learning_rate = 0.0001
iteration_cycles = 1000

count = len(x_list)

# formula to plot a straight line with given x-axis coordinate
line_equation = lambda x: slope * x + intercept

# training for 1000 runs. rate of improving accuracy reduces with each iteration
for _ in range(1000):
    
    # getting new y-axis coordinates for all actual x-axis coordinates using line equation
    new_y = list(map(line_equation, x_list))
    
    # differencfe between actual coordinare & the one with the new one
    y_difference = y_list - new_y
    
    # getting changes for intercept & slope values with respect to error (bigger error make big change to intercept & slope)
    intercept_gradient = sum(2 / count * y_difference)
    slope_gradient = sum(2 / count * y_difference * x_list)
    
    # updating intercept & slope 
    intercept += learning_rate * intercept_gradient
    slope += learning_rate * slope_gradient

# finding new y-axis coordinates with slope & intercept after 1000 corrections
predicted_y = list(map(line_equation, x_list))

# error function (there are a lot. we can choose anything)
rmse = sqrt(mean(square(y_list - predicted_y)))

# printing new values
print("intercept =", intercept)
print("slope =", slope)
print("rmse =", rmse)

# finding y-coordinates for new x-coordinates
test_x = [44, 32, 63]
test_y = list(map(line_equation, test_x))

# plotting actual points, new predictions & line of best fit for actual points
scatter(x_list, y_list, label='original')
scatter(test_x, test_y, label='prediction')
plot(x_list, predicted_y, label='line of best fit')
legend()
show()
