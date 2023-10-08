import math

def test_amidz_string(string):
    for i in string:
        if i.isalpha()!=True:
            print("Cannot take in numerical values.")
            return False
    return True
def amidz_string(string):
    if (test_amidz_string):
        return string[0]+string[len(string)//2]+string[len(string)-1]
    else:
        return "Error with your input."
print(amidz_string("wkhdbcwohwjwnco"))

def test_mixture_string(str1,str2):
    if len(str1)==0 or len(str2)==0:
        print("You've entered an empty string.")
        return False
    elif len(str1)!=len(str2):
        return False
    return True
def mixture_string(str1,str2):
    if test_mixture_string(str1,str2):
        str3 = ""
        for i in range(len(str1)):
                str3 += str1[i]
                str3+=str2[i]
        return str3
    else:
        return "There is some error with your code."
print(mixture_string("Hello","Drape"))

num_test_case = False  


def test_nums(string):
    num_count = 0
    numbers = ""
    spls = "!@#$%^&*()_+-=[]}{\|:\"?';,./'"
    for i in string:
        if i.isalpha()!=True:
            if i not in spls:
                num_count+=1
                numbers+=i
    if num_count>0:
        num_test_case=True
        return numbers
    else:
        return "No numbers in the string."
def nums(string):
    numbers = test_nums(string)
    if num_test_case:
        sum_and_average = []
        sums = 0
        for i in range(len(numbers)-1):
            sums += int(numbers[i])
        sum_and_average.append(sums,sums/len(numbers))


def find_occurences(string,substring):
    occurence_index = []
    len_of_sub = len(substring)
    string=string.lower()
    substring = substring.lower()
    for i in range(len(string)-1):
        if string[i:i+len_of_sub] == substring:
            occurence_index.append(i)
    for i in range(len(string)-1,-1,-1):
        if string[len_of_sub+i:i]==substring:
            occurence_index.append(i)

    print(occurence_index)
print(find_occurences("Hello man what are you upto? I'm pretty bored. what is the string i need to see. ","i n"))

def nums_string(string):
    string +=" "
    string_of_Doom = ""
    substring= ""
    for i in range(len(string)-1):
        if string[i]==" ":
            string_of_Doom = string[:i]
    final_char = len(string_of_Doom)-1
    if string_of_Doom[final_char].isalpha()!= True:
        substring+=string_of_Doom+" "
        print("string of doom ",substring)
    return substring
print(nums_string("Helo90 how9 are you today8"))


def equilater_triangle(index):
    num = 1
    trinums = []
    for i in range(index):
        trinums.append(num+i)
        num += i

    return trinums[index-1]
print(equilater_triangle(2))
        

            


    
    
    
    
        
            
    

    