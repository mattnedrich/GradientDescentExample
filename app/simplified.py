from numpy import array, genfromtxt, mean

data_set = genfromtxt("data.csv", delimiter=",")
x_list = data_set[:, 0]
y_list = data_set[:, 1]

intercept = 0
slope = 0
predicted_y = 1

learning_rate = 0.0001
count = len(x_list)

while True:
    new_y = slope * x_list + intercept

    if all(predicted_y == new_y):
        break

    predicted_y = new_y
    y_difference = y_list - predicted_y

    intercept_gradient = sum(2 / count * y_difference)
    slope_gradient = sum(2 / count * y_difference * x_list)

    intercept += learning_rate * intercept_gradient
    slope += learning_rate * slope_gradient

predicted_y = slope * x_list + intercept
rmse = mean((y_list - predicted_y) ** 2)

print("60 -", (60 * slope + intercept))

print("intercept =", intercept)
print("slope =", slope)
print("rmse =", rmse)
