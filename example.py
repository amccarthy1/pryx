##
# Examples demonstrating the use of this repository to
#   approximate answers to mathematical problems.
# Author: Adam McCarthy <amccarthy@mail.rit.edu>
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
from roots import bisect
from math import sin

def main():
    f = lambda x: x*x*x - 5.0

    # (bisection is pretty slow; you'd usually use newton's method for this)
    # use bisection to compute 3rd root of 5
    print("3rd root of 5: %f" % bisect(f, 0, 5))

    # pass the optional 'precision' parameter for more (or less) precise roots
    print("pi: %0.15f" % bisect(sin, 2, 4, precision=1e-15))
if __name__ == "__main__":
    main()
