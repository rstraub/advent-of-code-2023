import re


def sanitize(string):
    """Gets rid of leading and trailing whitespace"""
    # remove trailing whitespace
    result = re.sub(r'\s+$', '', string, flags=re.MULTILINE)
    # remove leading whitespace
    result = re.sub(r'^\s+', '', result, flags=re.MULTILINE)
    return result
