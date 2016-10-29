##
# Numerical root-finding methods.
# Author: Adam McCarthy <amccarthy@mail.rit.edu>
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

DEFAULT_PRECISION = 1e-8
DEFAULT_MAX_ITERATIONS = 5000 # used in methods that are not guaranteed convergence

def _midpoint(f1, f2):
    return (f1 + (f2 - f1) / 2.0)

##
# bisect: Approximates a zero of a function within a given precision
#   runtime is proportional to log_2(|x2-x1| / precision)
# parameter func: The function for which to find a root
# parameter x1: An x-value serving as one of two horizontal bounds for bisection
# parameter x2: An x-value serving as one of two horizontal bounds for bisection
# parameter precision [default: 1e-8]: desired level of precision
# returns: (float) a numeric approximation of a root of f between x1 and x2
# error: ValueError if f(x1) * f(x2) > 0
def bisect(func, x1, x2, precision=DEFAULT_PRECISION):
    (y1, y2) = (func(x1), func(x2))

    # root must be bracketed. If not, cannot bisect to find root.
    if (y1 * y2 > 0):
        raise ValueError(
            "Bisect requires one positive and one negative root. " +
            "Got y1=%0.4f, y2=%0.4f instead." % (y1, y2)
        )

    while (abs(x2 - x1) > precision):
        x_next = _midpoint(x1, x2)
        y_next = func(x_next)

        if (abs(y_next) < precision):
            return x_next

        # Find the endpoint whose sign is opposite that of x_next
        if (y1 * y_next < 0): (x2, y2) = (x_next, y_next)
        else: (x1, y1) = (x_next, y_next)

    return midpoint(x1, x2)

# calculate the x-intercept of a line between (x1, y1) and (x2, y2)
# raises ValueError if y1 = y2
def _intercept(x1, x2, y1, y2):
    if (y1 == y2):
        raise ValueError("Horizontal line does not intercept x-axis")
    return (x1 * y2 - x2 * y1) / (y2 - y1)

##
# secant: Approximates a zero of a function within a given precision, using
#   a maximum number of iterations. Runtime is somewhat unpredictable, but
#   usually faster than bisection.
# parameter func: The function for which to find a root
# parameter x1: An x-value to use as a starting point
# parameter x2: A second x-value to use as a starting point
# parameter precision [default: 1e-8]: desired level of precision
# parameter max_iterations [default: 5000]: max number of iterations to run
# returns: (float) a numeric approximation of a root of f
# errors: ValueError if the approximation doesn't converge after max_iterations
#   steps
#         ValueError if the algorithm finds 2 consecutive points with equal y-
#   values (This indicates a horizontal line which has no intercept)
def secant(func, x1, x2,
        precision=DEFAULT_PRECISION, max_iterations=DEFAULT_MAX_ITERATIONS):
    (y1, y2) = (func(x1), func(x2))
    if abs(y1) < precision:
        return x1
    for _ in range(max_iterations):
        if abs(y2) < precision:
            return x2
        (x1, x2) = (x2, _intercept(x1, x2, y1, y2))
        (y1, y2) = (y2, func(x2))
    raise ValueError("Secant Method did not converge after %d steps" % max_iterations)
