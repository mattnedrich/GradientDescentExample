from numpy import array, genfromtxt, mean


class GradientDescent():

    def _print_values(self, message, b, m, error):
        print("\n" + message)
        print("\tintercept =", b)
        print("\tslope =", m)
        print("\terror =", error)

    def _compute_error(self, x_list, y_list, b, m):
        predected_y = x_list*m+b
        avg_error = mean((y_list - predected_y) ** 2)
        return avg_error

    def _step_gradient(self, x_list, y_list, b, m, learningRate):
        N = float(len(x_list))

        predected_y = m * x_list + b
        y_difference = y_list - predected_y

        b_gradient = sum(2 / N * y_difference)
        m_gradient = sum(2 / N * x_list * y_difference)

        b += learningRate * b_gradient
        m += learningRate * m_gradient

        return b, m

    def gradient_descent_runner(self, x_list, y_list, starting_b, starting_m):
        b, m = starting_b, starting_m

        num_iterations = len(self.x_list) * 100
        learning_rate = 1 / num_iterations

        for _ in range(num_iterations):
            b, m = self._step_gradient(x_list, y_list, b, m, learning_rate)

        return b, m

    def load_file(self, csv_file):
        points = genfromtxt(csv_file, delimiter=",")
        self.x_list = points[:, 0]
        self.y_list = points[:, 1]

    def run(self):
        initial_b = 0
        initial_m = 0

        self._print_values("initial values :", initial_b, initial_m, self._compute_error(
            self.x_list, self.y_list, initial_b, initial_m))

        b, m = self.gradient_descent_runner(
            self.x_list, self.y_list, initial_b, initial_m)

        self._print_values("values after gradiant descent :", b,
                           m, self._compute_error(self.x_list, self.y_list, b, m))


if __name__ == '__main__':
    gradient_descent = GradientDescent()
    gradient_descent.load_file("data.csv")
    gradient_descent.run()
