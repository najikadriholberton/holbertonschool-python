#!/usr/bin/python3
print(', '.join(["{}{}".format(i, j) for i in range(10)
                 for j in range(10) if i != j and
                 "{}{}".format(i, j) == ''.join(sorted("{}{}".format(i, j)))]))
