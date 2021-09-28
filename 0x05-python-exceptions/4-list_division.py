#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    j = 0
    list_3 = []
    while i < list_length:
        try:
            a = my_list_1[i]
            b = my_list_2[i]
            result = a / b
            j += 1
        except:
            if type(a) is not int or type(b) is not int:
                print("wrong type")
                j += 1
            if b == 0:
                print("division by 0")
                j += 1
            if i + 1 != j:
                print("out of range")
            result = 0
        finally:
            list_3.append(result)
        i += 1
    return list_3
