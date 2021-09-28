#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    list_3 = []
    while i < list_length:
        try:
            a = my_list_1[i]
            b = my_list_2[i]
        except:
            print("out of range")

        try:
            a = my_list_1[i]
            b = my_list_2[i]
            result = a / b
        except:
            if type(a) is not int or type(b) is not int:
                print("wrong type")
            if b == 0:
                print("division by 0")
            result = 0
        finally:
            list_3.append(result)
        i += 1
    return list_3
