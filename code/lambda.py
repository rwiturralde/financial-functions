from __future__ import print_function
import sys
import log_helper
sys.path.append('lib')
import numpy
from jsonschema import validate
import validation_json_schemas as schemas

logger = log_helper.getLogger(__name__)


def fv_handler(request, context):
    schema = schemas.fv_schema

    try:
        validate(request, schema)
        logger.info("FV request: {}".format(request))
        args = [request['rate'], request['nper'], request['pmt'], request.get('pv', 0), request.get('type', 0)]
        logger.info("Calling numpy.fv with args: {}".format(args))
        return {'result': numpy.fv(*args)}
    except Exception as ex:
        logger.error("Encountered an error while handling FV request with args: {}. Exception: {}".format(request, ex))
        raise ex


def pv_handler(request, context):
    schema = schemas.pv_schema

    try:
        validate(request, schema)
        logger.info("PV request: {}".format(request))
        args = [request['rate'], request['nper'], request['pmt'], request.get('fv', 0), request.get('type', 0)]
        logger.info("Calling numpy.pv with args: {}".format(args))
        return {'result': numpy.pv(*args)}
    except Exception as ex:
        logger.error("Encountered an error while handling PV request with args: {}. Exception: {}".format(request, ex))
        raise ex


def npv_handler(request, context):
    schema = schemas.npv_schema

    try:
        validate(request, schema)
        logger.info("NPV request: {}".format(request))
        args = [request['rate'], request['values']]
        logger.info("Calling numpy.npv with args: {}".format(args))
        return {'result': numpy.npv(*args)}
    except Exception as ex:
        logger.error("Encountered an error while handling NPV request with args: {}. Exception: {}".format(request, ex))
        raise ex


def pmt_handler(request, context):
    schema = schemas.pmt_schema

    try:
        validate(request, schema)
        logger.info("PMT request: {}".format(request))
        args = [request['rate'], request['nper'], request['pv'], request.get('fv', 0), request.get('type', 0)]
        logger.info("Calling numpy.pmt with args: {}".format(args))
        return {'result': numpy.pmt(*args)}
    except Exception as ex:
        logger.error("Encountered an error while handling PMT request with args: {}. Exception: {}".format(request, ex))
        raise ex


def ppmt_handler(request, context):
    schema = schemas.ppmt_schema

    try:
        validate(request, schema)
        logger.info("PPMT request: {}".format(request))
        args = [request['rate'], request['per'], request['nper'], request['pv'], request.get('fv', 0), request.get('type', 0)]
        logger.info("Calling numpy.ppmt with args: {}".format(args))
        return {'result': numpy.ppmt(*args)}
    except Exception as ex:
        logger.error("Encountered an error while handling PPMT request with args: {}. Exception: {}".format(request, ex))
        raise ex


def irr_handler(request, context):
    schema = schemas.irr_schema

    try:
        validate(request, schema)
        logger.info("IRR request: {}".format(request))
        args = [request['values']]
        logger.info("Calling numpy.irr with args: {}".format(args))
        return {'result': numpy.irr(*args)}
    except Exception as ex:
        logger.error("Encountered an error while handling IRR request with args: {}. Exception: {}".format(request, ex))
        raise ex


def mirr_handler(request, context):
    schema = schemas.mirr_schema

    try:
        validate(request, schema)
        logger.info("MIRR request: {}".format(request))
        args = [request['values'], request['finance_rate'], request['reinvest_rate']]
        logger.info("Calling numpy.mirr with args: {}".format(args))
        return {'result': numpy.mirr(*args)}
    except Exception as ex:
        logger.error("Encountered an error while handling MIRR request with args: {}. Exception: {}".format(request, ex))
        raise ex


def nper_handler(request, context):
    schema = schemas.nper_schema

    try:
        validate(request, schema)
        logger.info("NPER request: {}".format(request))
        args = [request['rate'], request['pmt'], request['pv'], request.get('fv', 0), request.get('type', 0)]
        logger.info("Calling numpy.nper with args: {}".format(args))
        return {'result': numpy.nper(*args)}
    except Exception as ex:
        logger.error("Encountered an error while handling NPER request with args: {}. Exception: {}".format(request, ex))
        raise ex


def rate_handler(request, context):
    schema = schemas.rate_schema

    try:
        validate(request, schema)
        logger.info("Rate request: {}".format(request))
        args = [request['nper'], request['pmt'], request['pv'], request.get('fv', 0), request.get('type', 0), request.get('guess', 0.10)]
        logger.info("Calling numpy.rate with args: {}".format(args))
        return {'result': numpy.rate(*args)}
    except Exception as ex:
        logger.error("Encountered an error while handling RATE request with args: {}. Exception: {}".format(request, ex))
        raise ex

