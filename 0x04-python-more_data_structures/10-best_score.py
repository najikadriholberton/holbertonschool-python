#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary and len(a_dictionary) > 0:
        best_value = max(a_dictionary.values())
        for key in a_dictionary.keys():
            if a_dictionary[key] == best_value:
                return key
    return None
