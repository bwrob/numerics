def outside_value_only(f):
    def wrapped(*args, **kwargs):
        result = f(*args, **kwargs)
        value, _ = result
        return result if __name__ == '__main__' else value

    return wrapped
