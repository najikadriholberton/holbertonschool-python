#!/usr/bin/python3
"""Text Indentation Module"""


def text_indentation(text):
    """Text Indentation Function"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        prev = 0
        for i in range(0, len(text)):
            if text[i] == "." or text[i] == "?" or text[i] == ":":
                print(text[prev:i+1].strip(), end="\n\n")
                prev = i+1
            if i == len(text)-1:
                print(text[prev:i+1].strip(), end="")
