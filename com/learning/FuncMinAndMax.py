__author__ = 'anandran'

def clip(lo, x, hi):
    return min(max(x, lo), hi)

print(clip())