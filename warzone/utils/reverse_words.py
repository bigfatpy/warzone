import re


def reverse_words(value):
    """
    Creates a mirror(reverse) the words respecting the punctuation.

    input = 'I am a software engineer. But,, I am also an operations engi.neer.'
    expected = 'I ma a erawtfos reenigne. tuB,, I ma osla na snoitarepo igne.reen.'
    """
    match = re.finditer('[a-zA-Z]+', value)

    for item in match:
        value = value[:item.start()] + item.group()[::-1] + value[item.end():]
    
    return value
