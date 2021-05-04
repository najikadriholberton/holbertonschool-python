#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    a_dictionary.update({key: value})
    new_dic = a_dictionary.copy()
    return new_dic
