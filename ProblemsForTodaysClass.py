import math
def runnerUp(score):
    n = score[0]
    for i in score:
        if i>n:
            maximum = i
    score.remove(maximum)
    for i in score:
        if i>n:
            runner = i
    return runner

def align(alignment,string,no_of_hyphens):
    if alignment=="Center":
        hyphs = no_of_hyphens//2
        return "-"*hyphs+string+hyphs*"-"
    elif alignment == "Left":
        return string+hyphs*"-"
    elif alignment == "Right":
        return hyphs*"-"+string
    else:
        return "That alignment is not supported."
    

# print(align("Center" , "hello", 10))


students_list=[["Abinaya", 67, 68, 69],
["Arjun" ,70 ,98 ,63],
["Prasanth" ,52, 56, 60]]
def average_marks(name):
    for i in students_list:
        if name in i:
            return ((i[1]+i[2]+i[3])/3)
    return "That student does not exist."

# print(average_marks("Abinaya"))

def replace_with_hyphen(string):
    strings=""
    for i in string:
        if i == " ":
            strings+="-"
        else:
            strings+=i
    return strings
# print(replace_with_hyphen("Hello Man"))

# def pattern(n):

def cut_string(string,number):
    cut_up_string = ""
    for i in range(0,len(string),number):
        try:
            cut_up_string+=string[i:i+number]
            cut_up_string+="\n"
        except IndexError:
            cut_up_string+=string[i:]
    return cut_up_string
    


print(cut_string("wkhcvwlirvclkqrwhfbioe2udb2oeubdou2begfodu2b",3))

def unique_of_three(string):
    unique = []
    if len(string)%3>0:
        return "Length of string has to be divisible by 3."
    else:
        try:
            for i in range(0,len(string),3):
                unique.append(set(string[i:i+3]))
        except IndexError:
            unique.append({string[i:]})

    return unique
print(unique_of_three("AABCBCDDA"))

def find_product_and_sum(number):
    nums = str(number)
    sums =0
    product = 1
    for i in nums:
        sums += int(i)
        product *= int(i)
    return [sums,product]
def LCM(multiples):
    common_factors = []
    higher = max(multiples)
    for i in range(higher):
        if multiples[0]%i==0 and multiples[1]%i==0:
            common_factors.append(i)

    if len(common_factors)>0:
        product =1
        for i in range(len(common_factors)):
            product *= common_factors[i]
        return product
    


print(LCM(find_product_and_sum(546)))


    