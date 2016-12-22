# Numerical Derivative

## Introduction

### Compute the numerical derivative of a single-variate python to a set number of levels.

## Instructions

```
usage: derivative.py [-h] x level

positional arguments:
  x           The point at which you want the derivative to be calculated
  level       The level of derivative you want - 1 is first, etc

optional arguments:
  -h, --help  show this help message and exit
  ```

## Function Modification

Currently a sample function is defined as a lambda within the main. However, this can work with any python function, as long as it takes a 
single parameter. This code does not compute multivariate derivatives numerically.

```
func = lambda x: (-4*x*(2*x*(3 * (x ** 2)) - 3*x) + 3*x**2 - x)
```
