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
    return { 'result': numpy.fv(*args) }
