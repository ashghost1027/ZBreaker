def print_a_list_in_reverse_order(list_to_be_reversed):
    if len(list_to_be_reversed)==1:
        return list_to_be_reversed
    else:
        return list_to_be_reversed[-1:] + print_a_list_in_reverse_order(list_to_be_reversed[:-1])

print(print_a_list_in_reverse_order([1,2,3,4,5,7,8,9,10]))

def get_GCD_of(number1, number2):
    if number1>number2:
        return number1
    
def decimal_to_binary(decimal):
    if decimal == "1" or decimal=="0":
        return decimal
    else:
        decimal = int(decimal)
        return  decimal_to_binary(str(decimal//2)) + str(decimal%2)
    
print(decimal_to_binary(10))

def decimal_to_octal(decimal):
    if decimal < 8:
        return str(decimal)
    else:
        return decimal_to_octal(decimal//8) + str(decimal%8)
print(decimal_to_octal(8))

def decimal_to_hexadecimal(decimal):
    x = "0123456789ABCDEF"
    if decimal<16:
        return x[decimal]
    else:
        
        return decimal_to_hexadecimal(decimal//16)+x[decimal%16] 
    
print(decimal_to_hexadecimal(254))

def binary_search(array,element):
    if element not in array: return -1
    if array[len(array)//2]==element:
        return len(array)//2
    else:
        if array[len(array)//2]>element:
            return binary_search(array[:len(array)//2],element)
        else:
            return len(array)//2 + binary_search(array[len(array)//2:],element) 
        
print(binary_search([10,11,12,13,14,15,16],10))

def sum_of_digits_of_a_number(number):
    if number<10:
        return number
    else:
        return number%10 + sum_of_digits_of_a_number(number//10)  
    
print(sum_of_digits_of_a_number(3044))
