#!/usr/bin/python3
def canUnlockAll(boxes):
    """ function to check if all the boxes can be opened"""
    if boxes is None:
        raise TypeError("boxes can't be NoneType")
    elif len(boxes) == 1:
        return True
    else:
        list = []
        if 0 not in list:
            list.append(0)
        for i in list:
            if i in range(len(boxes)):
                for j in range(len(boxes[i])):
                    if boxes[i][j] not in list and boxes[i][j] < len(boxes):
                        list.append(boxes[i][j])
        if len(list) == len(boxes):
            return True
        else:
            return False
