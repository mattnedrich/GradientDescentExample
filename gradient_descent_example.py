from numpy import array, genfromtxt, mean


def compute_error(x_list, y_list, b, m):
    predected_y = x_list*m+b
    avg_error = mean((y_list - predected_y) ** 2)
    return avg_error


def step_gradient(x_list, y_list, b, m, learningRate):
    N = float(len(x_list))

    predected_y = m * x_list + b
    y_difference = y_list - predected_y

    b_gradient = sum(2 / N * y_difference)
    m_gradient = sum(2 / N * x_list * y_difference)

    b += learningRate * b_gradient
    m += learningRate * m_gradient

    return b, m


def gradient_descent_runner(x_list, y_list, starting_b, starting_m, learning_rate, num_iterations):
    b, m = starting_b, starting_m

    for i in range(num_iterations):
        b, m = step_gradient(x_list, y_list, b, m, learning_rate)

    return b, m


def print_values(message, b, m, error):
    print(message)
    print("intercept =", b)
    print("slope =", m)
    print("error =", error)
    print("-----")


if __name__ == '__main__':
    points = genfromtxt("data.csv", delimiter=",")
    x_list = points[:, 0]
    y_list = points[:, 1]

    num_iterations = len(x_list) * 100
    learning_rate = 1 / num_iterations

    initial_b = 0
    initial_m = 0

    print_values("initial values :", initial_b, initial_m, compute_error(
        x_list, y_list, initial_b, initial_m))

    b, m = gradient_descent_runner(
        x_list, y_list, initial_b, initial_m, learning_rate, num_iterations)

    print_values("values after gradiant descent :", b,
                 m, compute_error(x_list, y_list, b, m))
