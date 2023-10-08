
def print_name(name,count):
    if count == 0:
        return 
    else:
        print(name[len(name)-count])
        count-=1
        print_name(name,count)

# print_name("Aswin",10)

def sum_of_list(l1):
    if len(l1)==1:
        return l1[0]
    else:
        x= l1.pop(0)
        return x + sum_of_list(l1)

# print(sum_of_list([1,2,3,4,5]))

def factorial(x):
    if x == 1:
        return x
    else:
        return (x)*factorial(x-1)
    
# print(factorial(3))
def go_through_list(li):
    if len(li)==0:
        return 0
    else:
        x = li[0]
        if type(x)==list:
            return sum(x)+go_through_list(li[1:])
        else:
            return x + go_through_list(li[1:])
        
print(go_through_list([1,2,3,[1],4,5,[3,4],1]))
    
def palindrome(string):
    if len(string)==0 or len(string)==1:
        return True;
    else:
        if string[0]==string[len(string)-1]:
            return True and palindrome(string[1:-1])
        else:
            return False
        
# print(palindrome("malalam"))


def fibonacci(n):
    if n <= 0:
        return "Invalid input. N should be a positive integer."
    elif n == 1:
        return 0 
    elif n == 2:
        return 1  
    else:
        fib1, fib2 = 0, 1
        for _ in range(3, n + 1):
            fib1, fib2 = fib2, fib1 + fib2
        return fib2
# print(fibonacci(10))

# print(fibonacci_seq(10))

def topleft_bottomright(n,m):
    if n==1 or m == 1:
        return 1
    else:
        return topleft_bottomright(m,n-1)+topleft_bottomright(n,m-1) 
# print(topleft_bottomright(2,4))

def sums(string):
    if len(string)==1:
        return int(string[0])
    else:
        return int(string[:1]) + sums(string[1:])
    
# print(sums("12345"))

def find_the_index_of(string,char):
    if string[len(string)-1]==char:
        return len(string)-1
    else:
        return find_the_index_of(string[:len(string)-1],char)
# print(find_the_index_of("Hello How are you","w"))

def numerics_remover(string):
    if string[0].isnumeric():
        return ""
    else:
        return string[0]+numerics_remover(string[1:])

def string_of_words_with_numbers_behind_them(string):
    if len(string)==1:
        if string[0].isnumeric():
            return ""
        return string[0]
    else:
        if string[0].isnumeric():
            return numerics_remover(string)+string_of_words_with_numbers_behind_them(string[1:])
        else:
            return string[0]+string_of_words_with_numbers_behind_them(string[1:])
        
# print(string_of_words_with_numbers_behind_them("Helo90 how8 are you7"))
def average(string):
    return sum(string)/len(string)

def mix_string(string1,string2):
    if len(string2) == 1:
        return string1[0]+string2[0]
    return string1[0]+string2[0]+mix_string(string1[1:],string2[1:])
    
# print(mix_string("helloq","abcder"))

def start_mid_end(string):
    return string[0]+string[len(string)//2]+string[len(string)-1]
# print(start_mid_end("a"))
    
def weighted_grid(grid,rows,cols):
    if rows==0 or cols==0:
        return grid[0][0]
    else:
        y = grid[len(grid)-1][len(grid[(len(grid)-1)])-1]
        x = 0 
        if rows > 0 : x += weighted_grid(grid[rows-1][cols])
        if cols > 0 : x += weighted_grid(grid[rows][cols-1])

        if x < y : y=x
        return y

grid = [[1,2,3],[2,3,4],[3,4,5]]    
# print(weighted_grid(grid,3,3))
def frog(n):
    if n == 0: return 1
    else:
        x = 0
        if n-1 >= 0: x += frog(n-1)
        if n-2 >= 0: x += frog(n-2)
    
    return x
# print(frog(5))

ans = []
def sum_of_T(array,T):
    if T==0: return 1
    if T<0 : return 0
    if array == 0: return 0
    if sum(array)==T:return True
    else:
        x = 0
        x = max(x,sum_of_T((array-1),T-arr[array-1]))
        x = max(x,sum_of_T(array-1,T))
    ans[array][T] = x
    return x
arr = [2,4,6]
# print(sum_of_T(0,6))