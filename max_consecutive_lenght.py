
import itertools

def run_length(text):
    return max([''.join(i) for _, i in itertools.groupby(text)], key=lambda x: len(x)) if text else ''

