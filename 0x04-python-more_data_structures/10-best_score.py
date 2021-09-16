#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    order = sorted(a_dictionary.values())
    best = order[-1]
    for k, v in a_dictionary.items():
        if v == best:
            return k
