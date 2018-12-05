from matplotlib.pyplot import legend, plot, scatter, show
from numpy import genfromtxt, mean, sqrt, square

data_set = genfromtxt("data.csv", delimiter=",")

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
