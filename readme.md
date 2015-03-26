## Gradient Descent Example for Linear Regression oguzhan
This example project demonstrates how the [gradient descent](http://en.wikipedia.org/wiki/Gradient_descent) algorithm may be used to solve the [linear regression](http://en.wikipedia.org/wiki/Linear_regression) problem. A more detailed description of this example can be found [here](https://spin.atomicobject.com/2014/06/24/gradient-descent-linear-regression/).

### Code Requirements
The example code is in Python. The only requirement is [NumPy](http://www.numpy.org/).

### Description
This code demonstrates how a gradient descent search may be used to obtain a line that fits a set of points.

The code contains a main function called `run`. This functions defines a set of parameters used in the gradient descent algorithm including an initial guess of the line slope and y-intercept, the learning rate to use, and the number of iterations to run gradient descent for. 

```python
initial_b = 0 # initial y-intercept guess
initial_m = 0 # initial slope guess
num_iterations = 1000
``` 

Using these parameters a gradient descent search is executed on a sample data set of 100 ponts. Here is a visualization of the search running for 200 iterations using an initial guess of `m = 0`, `b = 0`, and a learning rate of `0.000005`.

![alt tag](https://github.com/mattnedrich/GradientDescentExample/blob/master/gradient_descent_example.gif)

### Execution
To run the example, simply run the `gradient_descent_example.py` file using Python

```
python gradient_descent_example.py
```

The output will look like this

```
Starting gradient descent at b = 0, m = 0, error = 5565.10783448
Running...
After 1000 iterations b = 0.0889365199374, m = 1.47774408519, error = 112.614810116
```
