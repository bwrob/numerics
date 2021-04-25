import collections


# decorator for debugging purposes
# debug - gather debugging info during computation:
#   y   full
#   n   none
# value - output result only rather than named tuple with auxiliary data:
#   y   value
#   n   all data
# sleep - sleep between iterations fo animation purposes:
#   y   yes
#   n   no
# best to use with default control so that the settings for all functions can be switched at once
def debugging(control="nyn"):
    debug, value, sleep = control

    def wrapper(f):
        def wrapped(*args, **kwargs):
            result = f(debug, sleep, *args, **kwargs)
            if value == "y":
                try:
                    return result.value
                except AttributeError:
                    print("Failed in {}".format(f.__name__))
            else:
                return result

        return wrapped

    return wrapper


# function wrapping data into named tuple type
def result(**data):
    Result = collections.namedtuple('Result', data)
    output = Result._make(data.values())
    return output