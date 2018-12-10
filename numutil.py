import decimal
from collections import Iterable


def try_parse_list(list_vals, valid_types=None):
    """ Attempt to parse a list of valid values into the types given.
    returns: all_valid, list_of_results
    individual conversions can be tested against None
    """
    valid = True
    result = []
    for item in list_vals:
        (v, value) = try_parse(item, valid_types)
        valid = valid and v
        result.append(value)

    return v, result


def try_parse(text, valid_types=None):
    """try to parse a text string as a number.  Returns (valid, value) where
    valid represents whether the conversion was successful, and value is the result
    of the conversion, or None if failed.
    Accepts a string, and one optional parameter "valid_types" which is a list of valid number types to 
    try conversion to
    By default, only attempts Decimal
    """

    if valid_types is None:
        valid_types = [decimal.Decimal]

    if isinstance(valid_types, Iterable):
        for t in valid_types:
            if isinstance(t, type):
                try:
                    result = t(text)
                    return True, result
                except:
                    pass
            else:
                raise RuntimeError("Non-type given in type list")
    else:
        raise RuntimeError("Invalid type list provided")

    return False, None



