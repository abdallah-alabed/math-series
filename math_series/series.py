def fibonacci(n):
    """
    This Function Represent the Fibonnaci Series function for any number (n)
    """
    if n==0:
        return 0

    if n==1:
        return 1

    return fibonacci(n-1)+fibonacci(n-2)

def lucas(n):
    """
    This Function Represent the lucas Series function for any number (n)
    """
    if n==0:
        return 2

    if n==1:
        return 1

    return lucas(n-1)+lucas(n-2)  

def sum_series(n,zero=0,one=1):
    """
    This Function Represent both the Fibonnaci and lucas Series function for any number (n).
    please note: the zero and one parameters define the value of the first two values in the series.
    please note: to get the fibonnaci series please enter n as the only parameter.
    please note: to get the lucas series please enter all the parameters (n,zero,one).

    """
    if n==0:
        return zero

    if n==1:
        return one

    return sum_series(n-1,zero,one)+sum_series(n-2,zero,one)  