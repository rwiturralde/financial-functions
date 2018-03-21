import pytest
import json

# make sure we can find the app code
import sys, os
my_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, my_path + '/../../code/')

import lambda_handlers as handlers
from jsonschema.exceptions import ValidationError


def test_fv_handler():
    response = handlers.fv_handler(json.load(open('../fv.json')), None)
    assert 'result' in response
    assert round(response.get('result'), 6) == 15692.928894

    # TODO test data types
    # Missing rate
    with pytest.raises(ValidationError):
        handlers.fv_handler({
            "nper": 120,
            "pmt": -100,
            "pv": -100
        }, None)

    # Missing nper
    with pytest.raises(ValidationError):
        handlers.fv_handler({
            "rate": 0.004166666666667,
            "pmt": -100,
            "pv": -100
        }, None)

    # Missing pmt
    with pytest.raises(ValidationError):
        handlers.fv_handler({
            "rate": 0.004166666666667,
            "nper": 120,
            "pv": -100
        }, None)

    # Missing pv
    with pytest.raises(ValidationError):
        handlers.fv_handler({
            "rate": 0.004166666666667,
            "nper": 120,
            "pmt": -100,
        }, None)


def test_pv_handler():
    response = handlers.pv_handler(json.load(open('../pv.json')), None)
    assert 'result' in response
    assert round(response.get('result'), 6) == -100.000671

    # TODO test data types
    # Missing rate
    with pytest.raises(ValidationError):
        handlers.pv_handler({
            "nper": 120,
            "pmt": -100,
            "fv": 15692.93
        }, None)

    # Missing nper
    with pytest.raises(ValidationError):
        handlers.pv_handler({
            "rate": 0.004166666666666666,
            "pmt": -100,
            "fv": 15692.93
        }, None)

    # Missing pmt
    with pytest.raises(ValidationError):
        handlers.pv_handler({
            "rate": 0.004166666666666666,
            "nper": 120,
            "fv": 15692.93
        }, None)

    # Missing fv
    with pytest.raises(ValidationError):
        handlers.pv_handler({
            "rate": 0.004166666666666666,
            "nper": 120,
            "pmt": -100,
        }, None)


def test_irr_handler():
    response = handlers.irr_handler(json.load(open('../irr.json')), None)
    assert 'result' in response
    assert round(response.get('result'), 5) == 0.28095

    # TODO test data types & empty values array

    # Missing values
    with pytest.raises(ValidationError):
        handlers.irr_handler({}, None)

    # Values wrong type
    with pytest.raises(ValidationError):
        handlers.irr_handler({
            "values": ["test"]
        }, None)


def test_mirr_handler():
    response = handlers.mirr_handler(json.load(open('../mirr.json')), None)
    assert 'result' in response
    assert round(response.get('result'), 2) == 0.13

    # TODO test data types & empty values array

    # Missing values
    with pytest.raises(ValidationError):
        handlers.mirr_handler({
            "finance_rate": 0.12,
            "reinvest_rate": 0.10
        }, None)

    # Missing finance_rate
    with pytest.raises(ValidationError):
        handlers.mirr_handler({
            "values": [-1000, 300, 400, 400, 300],
            "reinvest_rate": 0.10
        }, None)

    # Missing reinvest_rate
    with pytest.raises(ValidationError):
        handlers.mirr_handler({
            "values": [-1000, 300, 400, 400, 300],
            "finance_rate": 0.12,
        }, None)


def test_nper_handler():
    response = handlers.nper_handler(json.load(open('../nper.json')), None)
    assert 'result' in response
    assert round(response.get('result'), 5) == 64.07335

    # TODO test data types

    # Missing rate
    with pytest.raises(ValidationError):
        handlers.nper_handler({
            "pmt": -150,
            "pv": 8000
        }, None)

    # Missing pmt
    with pytest.raises(ValidationError):
        handlers.nper_handler({
            "rate": 0.005833333333333,
            "pv": 8000
        }, None)

    # Missing pv
    with pytest.raises(ValidationError):
        handlers.nper_handler({
            "rate": 0.005833333333333,
            "pmt": -150,
        }, None)


def test_npv_handler():
    response = handlers.npv_handler(json.load(open('../npv.json')), None)
    assert 'result' in response
    assert round(response.get('result'), 8) == -0.00847859

    # TODO test data types & empty values array

    # Missing rate
    with pytest.raises(ValidationError):
        handlers.npv_handler({
            "values": [-100, 39, 59, 55, 20]
        }, None)

    # Missing values
    with pytest.raises(ValidationError):
        handlers.npv_handler({
            "rate": 0.281,
        }, None)


def test_pmt_handler():
    response = handlers.pmt_handler(json.load(open('../pmt.json')), None)
    assert 'result' in response
    assert round(response.get('result'), 6) == -1854.02472

    # TODO test data types

    # Missing rate
    with pytest.raises(ValidationError):
        handlers.pmt_handler({
            "nper": 180,
            "pv": 200000
        }, None)

    # Missing nper
    with pytest.raises(ValidationError):
        handlers.pmt_handler({
            "rate": 0.00625,
            "pv": 200000
        }, None)

    # Missing pv
    with pytest.raises(ValidationError):
        handlers.pmt_handler({
            "rate": 0.00625,
            "nper": 180,
        }, None)


def test_ppmt_handler():
    response = handlers.ppmt_handler(json.load(open('../ppmt.json')), None)
    assert 'result' in response
    assert round(response.get('result'), 2) == -302.11

    # TODO test data types

    # Missing rate
    with pytest.raises(ValidationError):
        handlers.ppmt_handler({
            "per": 1,
            "nper": 3,
            "pv": 1000
        }, None)

    # Missing per
    with pytest.raises(ValidationError):
        handlers.ppmt_handler({
            "rate": 0.10,
            "nper": 3,
            "pv": 1000
        }, None)

    # Missing nper
    with pytest.raises(ValidationError):
        handlers.ppmt_handler({
            "rate": 0.10,
            "per": 1,
            "pv": 1000
        }, None)

    # Missing pv
    with pytest.raises(ValidationError):
        handlers.ppmt_handler({
            "rate": 0.10,
            "per": 1,
            "nper": 3,
        }, None)


def test_rate_handler():
    response = handlers.rate_handler(json.load(open('../rate.json')), None)
    assert 'result' in response
    assert round(response.get('result'), 6) == 0.054695

    # TODO test data types

    # Missing nper
    with pytest.raises(ValidationError):
        handlers.rate_handler({
            "pmt": -200,
            "pv": 1000,
            "fv": 0.10
        }, None)

    # Missing pmt
    with pytest.raises(ValidationError):
        handlers.rate_handler({
            "nper": 6,
            "pv": 1000,
            "fv": 0.10
        }, None)

    # Missing pv
    with pytest.raises(ValidationError):
        handlers.rate_handler({
            "nper": 6,
            "pmt": -200,
            "fv": 0.10
        }, None)

    # Missing fv
    with pytest.raises(ValidationError):
        handlers.rate_handler({
            "nper": 6,
            "pmt": -200,
            "pv": 1000,
        }, None)
