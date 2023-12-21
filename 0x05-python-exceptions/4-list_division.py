#!/usr/bin/python3
"""a function that divides element by element 2 lists."""


def list_division(my_list_1, my_list_2, list_length):
    try:
        newlist = [i / j for i, j in zip(my_list_1, my_list_2)]

    except TypeError:
        print("wrong type")
    except ZeroDivisionError:
        print("division by 0")
    except Exception:
        print("out of range")
    finally:
        return newlist
