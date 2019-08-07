# Gradient Descent for Linear Regression

Demonstrating how `Gradient Descent` algorithm can solve `Linear Regression` problems

## Linear Regression

`Linear Regression` helps to find a `line of best fit`, which goes close to the set of given points

Equation of straight line is,

> ` y = mx + b `

where m is the slope, b is the y-intercept for each point p(x, y)

Once we have line equation, we can find any "dependent variable" `y` with corresponding "explanatory variable" `x`

We can get Y-values for each X and it may not match with actual Y-value
difference is then calculated using

> ` error = sqrt(mean((actual - predicted)^2) `

We have to minimise this error by changing `slope m` & `y-intercept b` for the next iteration to best fit the line

Obtained `line of best fit` helps us find any prediction _(dependent variable)_ based on given scenario _(explanatory variable)_ as long as it relates to given set of points

In order to get better results, we have to set `learning rate` to minimum and `iterations` to maximum. but this takes lot of time and resources
so the sweet spot shold be decided based on data-set

### Use-Case
used to find dependent variable in a linear relation on providing an explanatory variable

## Usage
download this repo & run python file using `Python3` interpreter for test-run

### Credits
all credits to [Matt Nedrich](https://github.com/mattnedrich/GradientDescentExample)
