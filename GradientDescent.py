from numpy import array, genfromtxt, mean


class GradientDescent:
    """
        This uses Gradient Descent algorithm to solve Linear Regression problems
    """

    def train_model(self, x_list, y_list):
        """
            Takes X & Y values and learn their relation

            :param x_list: explanatory variable
            :param y_list: dependent variable
            :return: None
        """

        intercept = 0
        slope = 0
        predicted_y = 0

        count = len(x_list)

        num_iterations = count * 100
        learning_rate = 1 / num_iterations

        for _ in range(num_iterations):
            predicted_y = slope * x_list + intercept
            y_difference = y_list - predicted_y

            b_gradient = sum(2 / count * y_difference)
            m_gradient = sum(2 / count * x_list * y_difference)

            intercept += learning_rate * b_gradient
            slope += learning_rate * m_gradient

        avg_error = mean((y_list - predicted_y) ** 2)

        self.variable_set = intercept, slope, avg_error

    def predict(self, *x):
        """
            Takes unknown X and returns corresponding guessed Y

            :param x: explanatory variable(s)
            :return: array of dependent variable(s)
        """

        return array(x) * slope + intercept


if __name__ == '__main__':
    data_set = genfromtxt("data.csv", delimiter=",")
    x = data_set[:, 0]
    y = data_set[:, 1]

    gradient_descent = GradientDescent()
    gradient_descent.train_model(x, y)

    intercept, slope, error = gradient_descent.variable_set

    print("intercept =", intercept)
    print("slope =", slope)
    print("error =", error)
