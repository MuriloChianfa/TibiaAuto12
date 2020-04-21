def rgb(rgb):  # Function to translate color to RGB
    return "#%02x%02x%02x" % rgb


def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)

    return combined_func
