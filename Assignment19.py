def multiply_all_numbers_in_a_list(array, multiply):
    if len(array)==1:
        return array[0]*multiply
    else:
        return [array[0]*multiply, multiply_all_numbers_in_a_list(array[1:],multiply)]
print(multiply_all_numbers_in_a_list([2,3,5,1,4,3,7,5,0,9], 5))

def minimum_number_of_coins(array_of_denominations, amount):
    if amount > 250:
        return "Amount Invalid"

    if len(array_of_denominations)<2:
        return amount*array_of_denominations[0]

    elif amount > array_of_denominations[len(array_of_denominations)-1]:
        return amount//array_of_denominations[len(array_of_denominations)-1] + minimum_number_of_coins(array_of_denominations[:-1], amount%array_of_denominations[len(array_of_denominations)-1])
    elif amount < array_of_denominations[len(array_of_denominations)-1]:
        return  minimum_number_of_coins(array_of_denominations[:-1], amount%array_of_denominations[len(array_of_denominations)-1])
    
print(minimum_number_of_coins([1,5,7,9,11], 13))

def reverse_a_number(number):
    if number == 0:
        return 
    if number<10:
        return number
    else:
        return (number%10)*10**(len(str(number))-1) + reverse_a_number(number//10)
    
print(reverse_a_number(24657658565))


def is_perfect_number(number,divisors):
    if len(divisors)==1:
        return divisors[0]
    else :
        x = divisors[0] + is_perfect_number(number, divisors[1:])
        if x == number:
            return True
        return x 
print(is_perfect_number(28,[1,2,4,7,14]))

# def prime_numbers_below(n):
#     if n == 0:
#         return 0
        
# print(prime_numbers_below(5))
        
