# Additional financial functions not already provided by numpy

import datetime
from scipy import optimize

def fvschedule(principal, schedule=[]):
    """
    Calculates future value with a variable interest rate schedule.
    """
    return reduce(lambda x, y: x + (x * y), schedule, principal)

def xnpv(rate, values=[], dates=[]):
    """
    Calculates the Net Present Value for a schedule of cash flows that is not necessarily periodic.
    """
    if len(values) != len(dates):
        raise ValueError('values and dates must be the same length')
    if sorted(dates) != dates:
        raise ValueError('dates must be in chronological order')
        
    first_date = dates[0]
    return sum([value / ((1 + rate) ** ((date - first_date).days/365.0)) for (value, date) in zip(values, dates)])

def xirr(values=[], dates=[], guess=0.1):
    """
    Returns the internal rate of return for a schedule of cash flows that is not necessarily periodic. 
    """
    return optimize.newton(lambda r: xnpv(r, values, dates), guess)