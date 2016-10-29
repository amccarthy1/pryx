##
# Examples demonstrating the use of this repository to
#   approximate answers to mathematical problems.
# Author: Adam McCarthy <amccarthy@mail.rit.edu>
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
from roots import bisect, secant
from math import sin

def main():
    f = lambda x: x*x*x - 5.0

    # (bisection is pretty slow; you'd usually use newton's method for this)
    # use bisection to compute 3rd root of 5
    print("3rd root of 5: %f" % bisect(f, 0, 5))

    # pass the optional 'precision' parameter for more (or less) precise roots
    # Unlike bisection, secant does not require root bracketing.
    print("pi: %0.15f" % secant(sin, 2, 3, precision=1e-15))


    # an example of secant method that fails
    g = lambda x: x*x - 3
    try:
        print("sqrt(3): %f" % secant(g, -1, 1))
    except ValueError:
        # ValueError indicates that the algorithm was unable to converge.
        # It's a good idea to fall back on bisection in this case.
        print("Secant method went horizontal!")
        print("sqrt(3): %f" % bisect(g, 0, 2))
if __name__ == "__main__":
    main()
