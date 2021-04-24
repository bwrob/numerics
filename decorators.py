def value_only(f):
    def wrapped(*args, **kwargs):
        kwargs['debug'] = False
        result = f(*args, **kwargs)
        try:
            return result.value
        except AttributeError:
            print("Failed in {}".format(f.__name__))

    return wrapped
