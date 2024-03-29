#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            # Attempt to divide elements, handle exceptions
            try:
                element_1 = my_list_1[i]
            except IndexError:
                raise IndexError("out of range")

            try:
                element_2 = my_list_2[i]
            except IndexError:
                raise IndexError("out of range")

            division_result = element_1 / element_2
            result.append(division_result)

        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except (TypeError, ValueError):
            print("wrong type")
            result.append(0)
        finally:
            pass

    return result
