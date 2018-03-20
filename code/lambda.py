from __future__ import print_function
import sys
import log_helper
sys.path.append('lib')
import numpy

logger = log_helper.getLogger(__name__)


def fv_handler(request, context):
    # TODO: validate arguments

    logger.info("FV request: {}".format(request))
    args = [request['rate'], request['nper'], request['pmt'], request.get('pv', 0), request.get('type', 0)]
    logger.info("Calling numpy.fv with args: {}".format(args))
    return {'result': numpy.fv(*args)}


def pv_handler(request, context):
    # TODO: validate arguments

    logger.info("PV request: {}".format(request))
    args = [request['rate'], request['nper'], request['pmt'], request.get('fv', 0), request.get('type', 0)]
    logger.info("Calling numpy.pv with args: {}".format(args))
    return {'result': numpy.pv(*args)}


def npv_handler(request, context):
    # TODO: validate arguments

    logger.info("NPV request: {}".format(request))
    args = [request['rate'], request['values']]
    logger.info("Calling numpy.npv with args: {}".format(args))
    return {'result': numpy.npv(*args)}


def pmt_handler(request, context):
    # TODO: validate arguments

    logger.info("PMT request: {}".format(request))
    args = [request['rate'], request['nper'], request['pv'], request.get('fv', 0), request.get('type', 0)]
    logger.info("Calling numpy.pmt with args: {}".format(args))
    return {'result': numpy.pmt(*args)}


def ppmt_handler(request, context):
    # TODO: validate arguments

    logger.info("PPMT request: {}".format(request))
    args = [request['rate'], request['per'], request['nper'], request['pv'], request.get('fv', 0), request.get('type', 0)]
    logger.info("Calling numpy.ppmt with args: {}".format(args))
    return {'result': numpy.ppmt(*args)}


def irr_handler(request, context):
    # TODO: validate arguments

    logger.info("IRR request: {}".format(request))
    args = [request['values']]
    logger.info("Calling numpy.irr with args: {}".format(args))
    return {'result': numpy.irr(*args)}


def mirr_handler(request, context):
    # TODO: validate arguments

    logger.info("MIRR request: {}".format(request))
    args = [request['values'], request['finance_rate'], request['reinvest_rate']]
    logger.info("Calling numpy.mirr with args: {}".format(args))
    return {'result': numpy.mirr(*args)}


def nper_handler(request, context):
    # TODO: validate arguments

    logger.info("NPER request: {}".format(request))
    args = [request['rate'], request['pmt'], request['pv'], request.get('fv', 0), request.get('type', 0)]
    logger.info("Calling numpy.nper with args: {}".format(args))
    return {'result': numpy.nper(*args)}


def rate_handler(request, context):
    # TODO: validate arguments

    logger.info("Rate request: {}".format(request))
    args = [request['nper'], request['pmt'], request['pv'], request.get('fv', 0), request.get('type', 0), request.get('guess', 0.10)]
    logger.info("Calling numpy.rate with args: {}".format(args))
    return {'result': numpy.rate(*args)}

