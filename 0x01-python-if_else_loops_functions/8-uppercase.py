#!/usr/bin/python3
def uppercase(str):
    text = ""
    for letter in str:
        if ord(letter) >= 92 and ord(letter) <= 122:
            text += chr(ord(letter)-32)
        else:
            text += letter
    print(text)
