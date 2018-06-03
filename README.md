# GradientDescentExample

> forked from Matt Nedrich's [GradientDescentExample](https://github.com/mattnedrich/GradientDescentExample)

Demonstrating how [Gradient Descent](http://en.wikipedia.org/wiki/Gradient_descent) algorithm can solve [Linear Regression](https://en.m.wikipedia.org/wiki/Linear_regression) problems

## Linear Regression
[Linear Regression](https://en.m.wikipedia.org/wiki/Linear_regression) helps to find a line of best fit, which goes close to the set of given points

Equation of a line is `y = mx + b` where m is the slope and b is the y-intercept

Once we have line equation, we can find any `dependent variable y` with corresponding `explanatory variable x`

That helps us find any prediction _(dependent variable)_ based on given scenario _(explanatory variable)_ as long as it relates to given set of points

## Usage
1. make sure `data.csv` & `GradientDescent.py` are in same folder 
2. run `GradientDescent.py` using [Python3](https://www.python.org/downloads/) interpreter for test - run

#### Methods
- `train_model()` takes _explanatory_ & _dependent_ variables as numpy arrays & trains the linear model
- `predict()` takes any x value(s) & returns corresponding y value(s) as a list
- `variable_set` is a tuple, containing intercept, slope average error from actual vs predicted values

#### Output
```
intercept = 0.6078985997054931
slope = 1.4675440436333027
error = 112.31533427075733
```

---
contact me @ nagasai.g9@gmail.com
