import pytest

# make sure we can find the app code
import sys, os
my_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, my_path + '/../../code/')

from datetime import date
import financial_functions as ff

def test_fvschedule():
    assert ff.fvschedule(10000, [0.05, 0.05, 0.035, 0.035, 0.035]) == 12223.614571875
    assert ff.fvschedule(100, [0.04, 0.06, 0.05]) == 115.752
    
def test_xnpv():
    assert ff.xnpv(
        0.05,
        [-10000, 2000, 2400, 2900, 3500, 4100],
        [date(2016, 1, 1), date(2016, 2, 1), date(2016, 5, 1), date(2016, 7, 1), date(2016, 9, 1), date(2017, 1, 1)]
    ) == 4475.448794482614
    
    assert ff.xnpv(
        0.05,
        [-10000, 2000, 2400, 2900, 3500, 4100, 5300],
        [date(2016, 1, 1), date(2016, 2, 1), date(2016, 5, 1), date(2016, 7, 1), date(2016, 9, 1), date(2017, 1, 1), date(2017, 2, 3)]
    ) == 9500.179287007002
    
    assert ff.xnpv(
        0.05,
        [-1000, 300, 400, 400, 300],
        [date(2011, 12, 1), date(2012, 1, 1), date(2013, 2, 1), date(2014, 3, 1), date(2015, 4, 1)]
    ) == 289.90172260419456
    
def test_xnpv_mismatched_lists():
    with pytest.raises(ValueError):
        ff.xnpv(0.05, [-100], [])
    
def test_xnpv_dates_not_chronological_order():
    with pytest.raises(ValueError):
        ff.xnpv(
            0.05,
            [-10000, 2000],
            [date(2016, 2, 1), date(2016, 1, 1)])
    
def test_xirr():
    assert ff.xirr(
        [-100, 20, 40, 25],
        [date(2016, 1, 1), date(2016, 4, 1), date(2016, 10, 1), date(2017, 2, 1)]
    ) == -0.19674386129832788
    
    assert ff.xirr(
        [-100, 20, 40, 25, 8, 15],
        [date(2016, 1, 1), date(2016, 4, 1), date(2016, 10, 1), date(2017, 2, 1), date(2017, 3, 1), date(2017, 6, 1)]
    ) == 0.0944390744445201
    
    assert ff.xirr(
        [-1000, 300, 400, 400, 300],
        [date(2011, 12, 1), date(2012, 1, 1), date(2013, 2, 1), date(2014, 3, 1), date(2015, 4, 1)],
        0.1
    ) == 0.23860325587217
    
def test_xirr_mismatched_lists():
    with pytest.raises(ValueError):
        ff.xirr([-100], [])
    
def test_xirr_dates_not_chronological_order():
    with pytest.raises(ValueError):
        ff.xirr(
            [-100, 20],
            [date(2016, 4, 1), date(2016, 1, 1)])
