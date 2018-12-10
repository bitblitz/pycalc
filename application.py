from flask import *
from decimal import *
# from fractions import *
from numutil import try_parse_list

app = Flask(__name__)

# constants
# key for a value parameter
INPUT_VALUE_KEY = 'val'

# Error Response Codes
GOOD_REQUEST = 200
BAD_REQUEST = 400

# configuration.
BROWSER_RESPONSE = False


def set_decimal_context():
    # disallow mixing float and decimal objects due
    # to rounding peculiarities
    getcontext().traps[FloatOperation] = True
    # arbitrary precision to 100 for this toy project.
    getcontext().prec=100


def error_response(code, text):
    if BROWSER_RESPONSE:
        return str.format("<html><body>Error: {0} {1}<body><html>", code, text)
    else:
        return jsonify(error=text), code


def good_response(result):
    if BROWSER_RESPONSE:
        return str(result), GOOD_REQUEST
    else:
        # jsonify doesn't work if result is a Decimal or Fraction, so convert to a string first
        s = str(result)
        return jsonify(value=s)


@app.route("/calc/v1/multiply", methods=['GET'])
def v1_multiply():
    set_decimal_context()
    if INPUT_VALUE_KEY in request.args:
        values = request.args.getlist(INPUT_VALUE_KEY)
        if len(values) == 2:
            (valid, (dec1, dec2)) = try_parse_list([values[0], values[1]], valid_types=[Decimal])
            if valid:
                return good_response(dec2 * dec1)

            return error_response(BAD_REQUEST, str.format("Invalid value given.{0},{1}", dec1, dec2))

    return error_response(BAD_REQUEST, "Wrong number of arguments.  Require two 'val' arguments")


@app.route("/calc/v1/add", methods=['GET'])
def v1_add():
    set_decimal_context()
    if INPUT_VALUE_KEY in request.args:
        values = request.args.getlist(INPUT_VALUE_KEY)
        if len(values) == 2:
            (valid, (dec1, dec2)) = try_parse_list([values[0], values[1]], valid_types=[Decimal])
            if valid:
                return good_response(dec1 + dec2)

            return error_response(BAD_REQUEST, "Invalid value given.")

    return error_response(BAD_REQUEST, "Wrong number of arguments.  Require two 'val' arguments")

