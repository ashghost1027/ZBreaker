def remove_element_from_list(element,array):
    array_without_element = []
    for i in range(len(array)-1):    
        if array[i] != element:
            array_without_element.append(array[i])
    return array_without_element
print(remove_element_from_list(5,[2,3,5,6,7,4,3,3,5,5,53,3,5,6,4]))

def frequency_greater_than(K,array):
    greater_than_K_array = []
    K_array = []
    for i in array:
        if i not in K_array:
            K_array.append(i)
        elif i in K_array and i not in greater_than_K_array:
            greater_than_K_array.append(i)
    return greater_than_K_array
print(frequency_greater_than(2,[2,2,3,4,2,1,4,2,4,5,7,4,3,2,1,0]))

def elements_in_range(upper_limit, array, lower_limit=0 ):
    array = sorted(array)
    if array[len(array)-1] < upper_limit and array>=lower_limit:
        return True
    return False


def triple_consecutive_numbers(array):
    for i in range(len(array)-3):
        if array[i] == array[i+1] and array[i] == array[i+2]:
            return True
    return False
print(triple_consecutive_numbers([2,3,4,5,5,5,6,4,2,1,0,0]))

def sum_of_integers_in_string(s):
    s+="l"
    sum = 0
    digits = ""
    for i in s:
        if i.isnumeric():
            digits+=i
        elif i.isalpha() and len(digits) :
            sum+=int(digits)
            digits=""
    
    return sum
print(sum_of_integers_in_string("kjdouho23usj048bsh84bkhwr842ohbowu84"))

def any_base_to_decimal(number):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = ""
    while len(number) > 1:
        numbers += str(digits.index(number[len(number)-1])%10)
        print(numbers)
        number = number[:-1]+str(digits.index(number[len(number)-1])//10)
    
    return reversed(numbers)



def invert_number_with_base(number,base):
    if base == 1:
        return "| "*number
    else:
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        reverse_number = ""
        while number > base:
            reverse_number += digits[number%base]
            number = number//base
        return any_base_to_decimal(reverse_number)
# print(invert_number_with_base(20,2))
        
def extricate_the_spaces_slowly(string):
    strings = ""
    array_of_reducing_spaces = []
    for i in string.split():
        strings+=string[:string.index(i)].strip()
        string = string[string.index(i):]
        array_of_reducing_spaces.append(strings)
    return array_of_reducing_spaces

# print(extricate_the_spaces_slowly("Hello man, Good morning to you. I'm running out of space."))

def is_the_first_digit_divisible_by_followers(array):
    number_to_be_divided = array[0]
    for i in range(1,len(array)):
        if number_to_be_divided%array[i]!=0:
            return False
    return True
print(is_the_first_digit_divisible_by_followers((20,2,4,40,10)))

def remove_fake_friends(friend_group):
    real_friends = []
    for friend in friend_group:
        if len(friend)==4:
            real_friends.append(friend)
    return real_friends
print(remove_fake_friends(["yusuf","Godwin", "Monst", "Jake", "Ryan", "Ronda"]))


def sum_of_all_equals_zero(array):
    distance_from_zero = sum(array)
    if distance_from_zero<0:
        return False
    i = 1
    while sum(array)>=0:
        if i > len(array):
            i = 1
        if array[i-1]> 0:
            array[i-1]-=i
            if sum(array)==0: return array
        i+=1
    return False
print(sum_of_all_equals_zero([4,-5,0,-7,15]))

def convert_A_to_B(B):
    A = [x for x in range(1,len(B)+1)]
    print(A)

# list_of_word = []
# def word_for_every_letter(string1,string2):
    
