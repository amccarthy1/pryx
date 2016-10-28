# Pryx
Numerical Methods implemented using numpy and matplotlib. For example usage,
see below or see `example.py`.

# Components
The contents of this repository are broken down by purpose into separate
files. The different components are as follows

## Roots
Contained within `roots.py`, Pyrx Roots contains pure-python implementations
of common root-approximation methods including bisection, secant method,
false position, and Newton's Method.

### Bisection Method
Bisection achieves guaranteed linear convergence for any function as long as
it is given two points such that
`f(x) > 0` for one point and `f(x) < 0` for the other. It is typically the
slowest of the provided methods, but also the most stable, as it makes no
assumptions about the nature of the function.

In the event that the given function has no zeros but a vertical asymptote
or a jump discontinuity that crosses the x-axis, Bisection may find the point of
discontinuity instead of a zero.
