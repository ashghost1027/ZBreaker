from datetime import datetime
def input_age2days():
    b_date = input("Enter your birthdate: ")
    return b_date
def leap_year(year):
        if year%4==0:
            if year%100==0 and year%400 == 0:
                return True
        return False
def date_checker(b_date):
    
    def date_format(b_date):
        if b_date[2]=="-" and b_date[5]=="-":
            return True
        return False
    def numerics(b_date):
        if b_date[:2].isnumeric() and b_date[3:5].isnumeric() and b_date[6:].isnumeric():
            return True
        return False
    def valid_month(month):
        if int(month)<12 :
            return True
    def valid_date(b_date):
        date = int(b_date[:2])
        month = int(b_date[3:5])
        year = int(b_date[6:])
        big_month = [1,3,5,7,8,10,12]
        smol_month = [4,6,9,11]
        feb=2
        if valid_month:
            if leap_year(year):
                if month==feb:
                    if date<30:
                        return True
                elif month in big_month:
                    if date<32:
                        return True
                elif month in smol_month:
                    if date<31:
                        return True
                return False
            else:
                if month==feb:
                    if date<29:
                        return True
                elif month in big_month:
                    if date<32:
                        return True
                elif month in smol_month:
                    if date<31:
                        return True
            return False
        else:
            print("Wrong month ")
            return False
    
    if not(date_format(b_date)) :
        return "Wrong date Format"
    elif not(numerics(b_date)):
        return "Enter only numerics"
    elif not(valid_date(b_date)):
        return "Date exceeding the limit for that month"
    else:
        return True
    
def days_in_months(b_ddmm,t_ddmm,year):
    total_day_count=0
    days = t_ddmm[0]-b_ddmm[0]
    # print(days)
    months = t_ddmm[1] - b_ddmm[1]
    # print(months)
    # month_days = 0
    big_month = [1,3,5,7,8,10,12]
    smol_month = [4,6,9,11]

    feb = 2

    if months>0:

        for i in range(b_ddmm[1],t_ddmm[1]):
            if i in big_month:
                total_day_count+=31
            elif i in smol_month:
                total_day_count+=30
            elif i == feb and leap_year(year):
                total_day_count+=29
            else:
                total_day_count+=28
        total_day_count+=1
    

    elif months<0:

         for i in range(b_ddmm[1],t_ddmm[1],-1):
            # print("hohoho")
            if i in big_month:
                total_day_count-=31
            elif i in smol_month:
                total_day_count-=30
            elif i == feb and leap_year(year):
                total_day_count-=29
            else:
                total_day_count-=28

    # print(total_day_count)
    return total_day_count+days

def days_in_year(byear,tyear):
    totaldays=0
    for i in range(byear,tyear):
        if leap_year(i):
            totaldays+=366
        else:
            totaldays+=365
    # print(totaldays)
    return totaldays

today = str(datetime.today())
# print(today)
b_date = input_age2days()
if date_checker(b_date):
    b_day = int(b_date[:2])
    t_day = int(today[8:10])
    b_month = int(b_date[3:5])
    t_month = int(today[5:7])
    b_year = int(b_date[6:])
    t_year = int(today[:4])
    
    difference_of_days = 0
    difference_of_days+= days_in_months([b_day,b_month],[t_day,t_month],t_year)
    # print("jwbdco",days_in_months([b_day,b_month],[t_day,t_month],t_year))
    difference_of_days+= days_in_year(b_year,t_year)
    print(difference_of_days+4)

def stutter_input():
    stutters = input("Enter word: ")
    while stutters.isalpha()==False:
        stutters = input("Only accepts words as input. Please enter a valid input: ")
    while " " in stutters:
        stutters = input("Cannot take multiple words or spaces. Please enter only the word: ")
    return stutters
def stutter(word):
    uhhhh = word[:2]
    return uhhhh+".."+uhhhh+".."+word

print(stutter(stutter_input()))

def base2_converter(num):
    base2 = ""
    binary = ""
    while num>1:
        base2+=str(num%2)
        num = num//2
    for i in range(len(base2)-1,-1,-1):
        binary+=base2[i]
    return binary

def base2_checker():
    num = input("Enter the decimal to be converted to binary: ")
    while num.isnumeric()!= True:
        num = input("Re-enter only a decimal value: ")
    return int(num)
print(base2_converter(base2_checker()))

def print_multiples(nums):
    list_of_nums = []
    for i in range(1,nums[1]):
        list_of_nums.append(nums[0]*i)
    return list_of_nums
def print_multiple_test():
    nums =[0,0]
    nums[0] = input("Enter the multiple: ")
    while nums[0].isnumeric()!=True:
        nums[0] = input("Enter only numeric value: ")
    nums[1] = input("Enter the number of multiples you want: ")
    while not(nums[1].isnumeric()):
        nums[1] = input("Enter only numeric values: ")

    nums[0] = int(nums[0])
    nums[1] = int(nums[1])
    return nums
    
print(print_multiples(print_multiple_test()))

def hexadecimal_to_binary(hexa):
    hexa = int(hexa,16)
    binary = bin(hexa)
    return binary[2:]

def hexadecimal_tester():
    values = ["1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    value = input("Enter the hexaDecimal value: ")
    for i in value:
        if i not in values:
            value = input("Re-enter the valid answer: ")
    return value
print(hexadecimal_to_binary(hexadecimal_tester()))

def over(balls):
    counter = 0 
    overs =0
    for i in range(balls):
        counter+=1
        if counter==6:
            overs+=1
            counter=0
    overs = str(overs)
    overs+="."+str(counter)
    return overs
def over_test():
    balls = input("Enter the number of bowls bowled: ")
    while not(balls.isnumeric()):
        balls = input("Enter only numeric value: ")

    return int(balls)
print(over(over_test()))

path = [("A","B"),("B","C"),("D","B"),("C","D")]

nodes=[]
for i in path:
    nodes.append(i[0])
    nodes.append(i[1])

nodes=set(nodes)
# print(nodes)
nodes=sorted(list(nodes))
# print(nodes)

adjacency=[]
for i in range(len(nodes)):
    row=([0,0,0,0])
    adjacency.append(row)

for i in path:
    first=nodes.index(i[0])
    second=nodes.index(i[1])
    adjacency[first][second]=1
    adjacency[second][first]=1

for i in adjacency:
    print(i)

def dict_ascii(letters):
    ascii = {}
    for i in letters:
        ascii[i] = ord(i)
    return ascii
def dict_ascii_test():
    lots =[]
    for i in range(4):
        letters = input(f"Enter the letter {i+1}: ")
        while not(letters.isalpha()):
            letters = input("Enter only alphabets: ")
        lots.append(letters)

    return lots
print(dict_ascii(dict_ascii_test()))

def string_operations(string):
    if string[2]=="+":
        return int(string[0])+int(string[len(string)-1])
    elif string[2]=="-":
        return int(string[0])-int(string[len(string)-1])
    elif string[2]=="*":
        return int(string[0])*int(string[len(string)-1])
    elif string[2]=="/":
        return int(string[0])/int(string[len(string)-1])
    else:
        return "That operation does not exit. "
def string_operator():
    string = input("Enter the string containing the mathematical operations: ")
    operators = ["/","+","-","*"," "]
    i = string[0]
    j= string[len(string)-1]
    if  not(i.isnumeric()) or not(j.isnumeric()) :
        string = input("Enter the values properly: ")
    if string[2] not in operators:
        string = input("Enter only the valid operations: ")
    
    return string
print(string_operations(string_operator()))
        
def consecutives(nums):
    sets = []
    for i in nums:
        for j in range(len(i)):
            sets.append(j)
    sets.sort()
    for i in range(min(sets),max(sets)):
        if i not in sets:
            return False
    return True
def consecutives_input():
    nums = []
    for i in range(2):
        tups = []
        for j in range(4):
            num = input("Enter the number to be inputed: ")
            while not(num.isnumeric()):
                num = input("Enter the proper numeric value: ") 
            tups.append(num)
        nums.append(tups)
    return nums

print(consecutives(consecutives_input()))

def stringtohexa(string):
    hexs = []
    for i in string:
        asc = ord(i)
        hexa = str(hex(asc))
        hexs.append(hexa[2:])
    return hexs
def string_get():
    string = input("Enter the string: ")
    if string == "" or string == None:
        string = input("Enter a proper string: ")
    return string
print(stringtohexa(string_get()))

def string_substitute(consonants,vowels):
    count =0
    cons = ""
    start = 0
    for i in consonants:

        if i == "*":
            cons+=vowels[count]
            count+=1
        else:
            cons+=i
    return cons
consonants = "Wh*r* d*d my v*w*ls g*?"
vowels = "eeioeo"
print(string_substitute(consonants,vowels))

        
    


    

    
    




            
    




    


    
    
        








    

                    
            




