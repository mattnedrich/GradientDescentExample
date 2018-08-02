# Gradient Descent for Linear Regression

Demonstrating how `Gradient Descent` algorithm can solve `Linear Regression` problems

## Linear Regression

`Linear Regression` helps to find a line of best fit, which goes close to the set of given points

Equation of straight line is,

![Line Equation](http://latex2png.com/output//latex_36e24d2caaa6ec79a0967c31517d8d58.png) 

where m is the slope, b is the y-intercept for each point p(x, y)

Once we have line equation, we can find any "dependent variable" `y` with corresponding "explanatory variable" `x`

We can get Y-values for each X and it may not match with actual Y-value
difference is then calculated using

![error Equation](http://latex2png.com/output//latex_cc30596a0cab8136c6aa10e8efe99c84.png)

We have to minimise this error by changing `slope m` & `y-intercept b` for the next iteration to best fit the line

Obtained `line of best fit` helps us find any prediction _(dependent variable)_ based on given scenario _(explanatory variable)_ as long as it relates to given set of points

In order to get better results, we have to set `learning rate` to minimum and `iterations` to maximum. but this takes lot of time and resources
so the sweet spot shold be decided based on data-set

## Usage
download this repo & run python file

1. make sure `data.csv` & `GradientDescent.py` are in same folder
2. run `GradientDescent.py` using `Python3` interpreter for test - run

### Methods
I've created just 3 methods to train, predect and to see formula values

- `train_model(x[...], y[...])` takes _explanatory_ & _dependent_ variables as numpy arrays & trains the linear model
- `predict(x[...])` takes any x value(s) & returns corresponding y value(s) as a list
- `variable_set` is a tuple, containing intercept, slope average error from actual vs predicted values

### Output
output of current code. try to beat this

```
intercept = 0.6078985997054931
slope = 1.4675440436333027
error = 112.31533427075733
```

## References

- [Linear Regression](https://en.m.wikipedia.org/wiki/Linear_regression)
- [Gradient Descent](http://en.wikipedia.org/wiki/Gradient_descent)
- [Line Equation](https://en.wikipedia.org/wiki/Linear_equation)

---
contact me @ nagasai.g9@gmail.com
