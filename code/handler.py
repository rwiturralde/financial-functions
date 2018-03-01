from __future__ import print_function
import os
import sys
sys.path.append('lib')

import numpy
import logging

# get logger level from function env var and create logger
loglevel = os.getenv('LOG_LEVEL', 'INFO')
numeric_level = getattr(logging, loglevel.upper(), None)
if not isinstance(numeric_level, int):
    raise ValueError('Invalid log level: %s' % loglevel)

logger = logging.getLogger(__name__)
logger.setLevel(numeric_level)


def lambda_handler(event, context):
    """
    Delegate method and arguments to NumPy

    event.method -- NumPy method to invoke
    event.arguments -- Array of ordered arguments to pass to the above NumPy method
    """

    # Check that we were passed the required arguments
    if 'method' in event and 'arguments' in event:
        numpy_method_name = event.get('method')
        numpy_argument_array = event.get('arguments')

        # Check that the arguments are valid
        if hasattr(numpy, numpy_method_name) and callable(getattr(numpy, numpy_method_name)):
            logger.info("Handing call to the NumPy {} method with arguments: {}".format(numpy_method_name, numpy_argument_array))
            result = getattr(numpy, numpy_method_name)(*numpy_argument_array)
            logger.info("Result from NumPy is {}".format(result))
            return {'result': result}
        else:
            error_message = "Invalid NumPy method: {}".format(numpy_method_name)
            logger.error(error_message)
            raise AttributeError(error_message)



    else:
        error_message = "Missing required argument(s). Event must contain fields for \'method\' and \'arguments\'"
        logger.error(error_message)
        raise Exception(error_message)
