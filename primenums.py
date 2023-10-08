import time

def prime_generator(prime_limit):
    if prime_limit < 0:
        return "Get lost with the number being less than 0"
    if type(prime_limit)==str:
        return "Did you just enter a string? Are you dumb?"
    if type(prime_limit) != int:
        return "Brother primes are a subset of whole numbers"
    if prime_limit == 0:
        return "0? Really?"
    else:
        primes = []
        for i in range(2,prime_limit):
            if i%2!=0:
                factorcount = 0
                for j in primes:
                    if i%j == 0:
                        factorcount += 1
                        break
                if factorcount<1:
                    primes.append(i)
        return len(primes)
 
def num_count(num):
    string_num = str(num)
    sum = 0
    for i in len(string_num):
        nums = int(string_num[i])
        sum += nums
    return sum
def prime_factors(num):
    factors = prime_generator(num)
        
    

start = time.time()       
print(prime_generator(100000))
end = time.time()
print(end-start)

def multiple5(a):
    for i in a:
        if i%5==0 and i<150:
            print(i)

def bugsmultiple5(a=[]):
    if type(a) != list:
        print("Only accepts list values")
    elif not(len(a)>0):
        print("Too short. Like you.")
    bools = True
    for i in a:
        if type(i)!=int:
            print("NO Only integer")
            bools = False
            return 
    # if bools:
        # multiple5(a)

# bugsmultiple5([873,75,85,35,0,-125,97,978])

# def countdigits(num):
    # strnum = str(num)

            
            

