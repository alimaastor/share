
import itertools

def run_length(text):
    try:
        c, l = max([[char, len(list(i))] for char, i in itertools.groupby(text)], key=lambda x: x[1])
    except ValueError:
        return ''
    else:
        return c*l

