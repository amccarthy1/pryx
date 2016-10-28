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

    return x1
