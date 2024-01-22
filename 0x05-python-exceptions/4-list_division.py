#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
        result_list = []
        
        for i in range(list_length):
                try:
                        num1 = my_list_1[i] if i < len(my_list_1) else 0
                        num2 = my_list_2[i] if i < len(my_list_2) else 0
                        
                        if isinstance(num1, (int, float)) and \
                                isinstance(num2, (int, float)):
                                if num2 == 0:
                                        raise ZeroDivisionError
                                quotient = num1 / num2
                        else:
                                print("wrong type")
                                quotient = 0
                except ZeroDivisionError:
                        print("division by 0")
                        quotient = 0
                except IndexError:
                        print("out of range")
                        quotient = 0
                finally:
                        result_list.append(quotient)
                        return result_list
