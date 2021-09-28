#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    list_3 = []
    while i < list_length:
        try:
            a = my_list_1[i]
            b = my_list_2[i]
            result = a / b
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
            result = 0
        finally:
            list_3.append(result)
        i += 1
    return list_3
