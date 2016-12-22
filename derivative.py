"""
derivative.py - compute the numerical derivative of a function
"""
import argparse
from decimal import Decimal
import numpy as np

def deriv(func, point, epsilon):
    """
    Calculate first derivative using regular equation
    """
    return (func(point + epsilon)-func(point)) / epsilon

def gradient(point1, point2, value1, value2):
    """
    Given two x and two y values, compute the straight line gradient.
    """
    return (value2 - value1) / (point2-point1)

def split_points(epsilon, point, level):
    """
    Return the range of points needed for a particular derivative level.
    """
    return [point + Decimal(i) * epsilon for i in range(1-level, level, 1)]

def format_level(level):
    """
    Return string suffix depending on level.
    """
    digit = level % 10
    return "st" if digit == 1 else "nd" if digit == 2 else "rd" if digit == 3 else "th"

def nderiv(func, point, level, epsilon=1e-6):
    """
    Compute derivatives to a certain level and epsilon as specified by the kwargs.
    """
    epsilon = Decimal(epsilon) #epsilon for gradients etc
    if level == 1:
        return [point], [deriv(func, point, epsilon)]
    points = split_points(epsilon, point, level)
    derivs = [deriv(func, i, epsilon) for i in points]
    for _ in range(2, level+1):
        temp = []
        rtemp = []
        for i in range(len(derivs) - 1):
            temp.append(gradient(points[i], points[i+1], derivs[i], derivs[i+1]))
            rtemp.append(points[i])
        derivs = temp
        points = rtemp
    return points, derivs

def main():
    """
    Entry point for module
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("x", help="The point at which you want the derivative to be calculated")
    parser.add_argument("level", help="The level of derivative you want - 1 is first, etc")
    args = parser.parse_args()
    point = Decimal(args.x)
    level = int(args.level)
    func = np.exp
    points, derivs = nderiv(func, point, level)
    print("x : {0}, {1}{2} derivative : {3}".format(points[-1], level,
                                                    format_level(level), derivs[-1]))
