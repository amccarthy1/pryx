# Pryx
Numerical Methods implemented using numpy and matplotlib. For example usage,
see below or see `example.py`.

(The name '`pryx`' is somewhat of a mixture between 'python' and 'approx')

# Components
The contents of this repository are broken down by purpose into separate
files. The different components are as follows

## Root Finding
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

### Secant Method
Secant method typically will converge faster than bisection, but in certain
instances will not converge. In particular:
 * The method may find two points x1 and x2 where f(x1) = f(x2), in which it cannot proceed
 * The method may encounter a monotonic horizontal asymptote, in which case it will continue along the
    asymptote until timing out
 * The method may get stuck in some kind of cycle in which it never arrives at a guess anywhere near the root.

For simple functions, these are unlikely circumstances, but they can occur.
