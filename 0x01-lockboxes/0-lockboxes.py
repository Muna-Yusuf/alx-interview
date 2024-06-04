#!/usr/bin/python3
""" DOC """

def canUnlockAll(boxes):
    """ function that determines if all the 
        boxes in a given list can be unlocked."""
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = [0]

    while keys:
        current_key = keys.pop()
        for key in boxes[current_key]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                keys.append(key)
    return all(unlocked)
