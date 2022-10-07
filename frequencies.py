"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for i in range(len(items)):
        if (str(items[i])) in frequencies:
            frequencies[str(items[i])] = frequencies.get(str(items[i])) + 1
        else:
            frequencies[str(items[i])] = 0
    return frequencies
