from numpy import array, genfromtxt, mean


class GradientDescent:
    """
        This uses Gradient Descent algorithm to solve Linear Regression problems
    """

    def train_model(self, x_list, y_list):
        """
            Takes X & Y values and learns their relation
        """

        intercept = 0
        slope = 0
        predicted_y = 0

        count = len(x_list)

        learning_rate = 0.0001

        predicted_y = 1

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
        avg_error = mean((y_list - predicted_y) ** 2)

        self.variable_set = intercept, slope, avg_error

    def predict(self, *x):
        """
            Takes unknown X and returns corresponding guessed Y
        """

        return array(x) * slope + intercept


if __name__ == '__main__':
    data_set = genfromtxt("data.csv", delimiter=",")
    x = data_set[:, 0]
    y = data_set[:, 1]

    gradient_descent = GradientDescent()
    gradient_descent.train_model(x, y)

    intercept, slope, error = gradient_descent.variable_set

    print("60 -", gradient_descent.predict(60))

    print("intercept =", intercept)
    print("slope =", slope)
    print("error =", error)
