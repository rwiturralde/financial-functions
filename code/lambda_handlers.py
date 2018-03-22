from __future__ import print_function
import sys
import log_helper
sys.path.append('lib')
import numpy
from jsonschema import validate
from jsonschema.exceptions import ValidationError
import validation_json_schemas as schemas

logger = log_helper.getLogger(__name__)


def __validate_arguments(function_name, arguments_json, json_schema):
    """
    Validate the arguments in the provided JSON against the provided json schema
    :param function_name:
    :param arguments_json:
    :param json_schema:
    :return: Dict containing whether the provided json is valid and an error message if validation failed.
    """
    try:
        validate(arguments_json, json_schema)
        return {'isValid': True}
    except ValidationError as err:
        logger.error("Invalid {} request with args: {}. Exception: {}".format(function_name, arguments_json, err))
        return {'isValid': False, 'error': err.message}


def __call_numpy(method, args):
    """
    Call a NumPy method with a given set of arguments
    :param method: NumPy method to call
    :param args: Arguments for the provided NumPy method
    :return: Result from NumPy
    """
    logger.info("Calling numpy.{} with args: {}".format(method, args))
    return {'result': getattr(numpy, method)(*args)}


def fv_handler(request, context):
    """
    Future Value calculation
    :param request: Dict containing the parameters to pass to the formula.
    :param context: Lambda execution context
    :return: Dict with a 'result' entry containing the result of the calculation
    """
    logger.info("FV request: {}".format(request))

    validation_result = __validate_arguments('FV', request, schemas.fv_schema)
    if not validation_result.get('isValid'):
        return {'error': validation_result.get('error')}

    args = [request['rate'], request['nper'], request.get('pmt', 0), request.get('pv', 0), request.get('type', 0)]
    return __call_numpy('fv', args)


def pv_handler(request, context):
    """
    Present Value calculation
    :param request: Dict containing the parameters to pass to the formula.
    :param context: Lambda execution context
    :return: Dict with a 'result' entry containing the result of the calculation
    """
    logger.info("PV request: {}".format(request))

    validation_result = __validate_arguments('PV', request, schemas.pv_schema)
    if not validation_result.get('isValid'):
        return {'error': validation_result.get('error')}

    args = [request['rate'], request['nper'], request.get('pmt', 0), request.get('fv', 0), request.get('type', 0)]
    return __call_numpy('pv', args)


def npv_handler(request, context):
    """
    Net Present Value of a cash flow series
    :param request: Dict containing the parameters to pass to the formula.
    :param context: Lambda execution context
    :return: Dict with a 'result' entry containing the result of the calculation
    """
    logger.info("NPV request: {}".format(request))

    validation_result = __validate_arguments('NPV', request, schemas.npv_schema)
    if not validation_result.get('isValid'):
        return {'error': validation_result.get('error')}

    args = [request['rate'], request['values']]
    return __call_numpy('npv', args)


def pmt_handler(request, context):
    """
    Compute the payment against loan principal plus interest
    :param request: Dict containing the parameters to pass to the formula.
    :param context: Lambda execution context
    :return: Dict with a 'result' entry containing the result of the calculation
    """
    logger.info("PMT request: {}".format(request))

    validation_result = __validate_arguments('PMT', request, schemas.pmt_schema)
    if not validation_result.get('isValid'):
        return {'error': validation_result.get('error')}

    args = [request['rate'], request['nper'], request['pv'], request.get('fv', 0), request.get('type', 0)]
    return __call_numpy('pmt', args)


def ppmt_handler(request, context):
    """
    Compute the payment against loan principal
    :param request: Dict containing the parameters to pass to the formula.
    :param context: Lambda execution context
    :return: Dict with a 'result' entry containing the result of the calculation
    """
    logger.info("PPMT request: {}".format(request))

    validation_result = __validate_arguments('PPMT', request, schemas.ppmt_schema)
    if not validation_result.get('isValid'):
        return {'error': validation_result.get('error')}

    args = [request['rate'], request['per'], request['nper'], request['pv'], request.get('fv', 0), request.get('type', 0)]
    return __call_numpy('ppmt', args)


def irr_handler(request, context):
    """
    Internal Rate of Return calculation.
    :param request: Dict containing the parameters to pass to the formula.
    :param context: Lambda execution context
    :return: Dict with a 'result' entry containing the result of the calculation
    """
    logger.info("IRR request: {}".format(request))

    validation_result = __validate_arguments('IRR', request, schemas.irr_schema)
    if not validation_result.get('isValid'):
        return {'error': validation_result.get('error')}
    else:
        # IRR requires at least one positive and one negative value
        sorted_values = sorted(request.get('values'))
        values_length = len(request.get('values'))
        if sorted_values[0] > 0 or sorted_values[values_length - 1] <= 0:
            return {'error': "IRR requires at least one positive and one negative value"}

    args = [request['values']]
    return __call_numpy('irr', args)



def mirr_handler(request, context):
    """
    Modified Internal Rate of Return calculation.
    :param request: Dict containing the parameters to pass to the formula.
    :param context: Lambda execution context
    :return: Dict with a 'result' entry containing the result of the calculation
    """
    logger.info("MIRR request: {}".format(request))

    validation_result = __validate_arguments('MIRR', request, schemas.mirr_schema)
    if not validation_result.get('isValid'):
        return {'error': validation_result.get('error')}
    else:
        # MIRR requires at least one positive and one negative value
        sorted_values = sorted(request.get('values'))
        values_length = len(request.get('values'))
        if sorted_values[0] > 0 or sorted_values[values_length - 1] <= 0:
            return {'error': "MIRR requires at least one positive and one negative value"}

    args = [request['values'], request['finance_rate'], request['reinvest_rate']]
    return __call_numpy('mirr', args)


def nper_handler(request, context):
    """
    Number of periodic payments required to pay off a loan.
    :param request: Dict containing the parameters to pass to the formula.
    :param context: Lambda execution context
    :return: Dict with a 'result' entry containing the result of the calculation
    """
    logger.info("NPER request: {}".format(request))

    validation_result = __validate_arguments('NPER', request, schemas.nper_schema)
    if not validation_result.get('isValid'):
        return {'error': validation_result.get('error')}

    args = [request['rate'], request.get('pmt', 0), request['pv'], request.get('fv', 0), request.get('type', 0)]
    return __call_numpy('nper', args)


def rate_handler(request, context):
    """
    Rate of interest period.
    :param request: Dict containing the parameters to pass to the formula.
    :param context: Lambda execution context
    :return: Dict with a 'result' entry containing the result of the calculation
    """
    logger.info("Rate request: {}".format(request))

    validation_result = __validate_arguments('Rate', request, schemas.rate_schema)
    if not validation_result.get('isValid'):
        return {'error': validation_result.get('error')}

    args = [request['nper'], request.get('pmt', 0), request['pv'], request.get('fv', 0), request.get('type', 0), request.get('guess', 0.10)]
    return __call_numpy('rate', args)

