from numpy import array, genfromtxt, mean


class GradientDescent():

    def __init__(self):
        self.initial_b = 0
        self.initial_m = 0

    def _compute_error(self, b, m):
        predected_y = self.x_list*m+b
        avg_error = mean((self.y_list - predected_y) ** 2)
        return avg_error

    def _step_gradient(self, b, m, learningRate):
        N = float(len(self.x_list))

        predected_y = m * self.x_list + b
        y_difference = self.y_list - predected_y

        b_gradient = sum(2 / N * y_difference)
        m_gradient = sum(2 / N * self.x_list * y_difference)

        b += learningRate * b_gradient
        m += learningRate * m_gradient

        return b, m

    def _gradient_descent_runner(self):
        b = self.initial_b
        m = self.initial_m

        num_iterations = len(self.x_list) * 100
        learning_rate = 1 / num_iterations

        for _ in range(num_iterations):
            b, m = self._step_gradient(b, m, learning_rate)

        return b, m

    def load_csv(self, csv_file):
        data_set = genfromtxt(csv_file, delimiter=",")
        self.x_list = data_set[:, 0]
        self.y_list = data_set[:, 1]

    def load_arrays(self, x_list, y_list):
        self.x_list = x_list
        self.y_list = y_list

    def get_predection(self):
        b, m = self._gradient_descent_runner()
        error = self._compute_error(b, m)
        return b, m, error


if __name__ == '__main__':
    gradient_descent = GradientDescent()
    gradient_descent.load_csv("data.csv")

    b, m, error = gradient_descent.get_predection()

    print("intercept =", b)
    print("slope =", m)
    print("error =", error)
