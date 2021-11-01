from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series

def test_fibonacci_9():
    expect=34
    actual=fibonacci(9)
    assert expect == actual

def test_fibonacci_10():
    expect=55
    actual=fibonacci(10)
    assert expect == actual

def test_fibonacci_30():
    expect=832040
    actual=fibonacci(30)
    assert expect == actual

def test_lucas_9():
    expect=4
    actual=lucas(3)
    assert expect == actual

def test_lucas_10():
    expect=123
    actual=lucas(10)
    assert expect == actual

def test_lucas_20():
    expect=15127
    actual=lucas(20)
    assert expect == actual

def test_sumSeries_10_fibonacci():
    expect=55
    actual=sum_series(10)
    assert expect == actual

def test_sumSeries_20_lucas():
    expect=15127
    actual=sum_series(20,2,1)
    assert expect == actual