import math

def even_fibonacci_sum_to_4_million():
    #4000000
    fibonacci = [0,1]
    sum_of_even_fibonacci_numbers = 0
    for i in range(4000000):
        if fibonacci[len(fibonacci)-1] + fibonacci[len(fibonacci)-2] == i:
            fibonacci.append(i)
    for i in fibonacci:
        if i%2==0:
            sum_of_even_fibonacci_numbers+=i
    
    return sum_of_even_fibonacci_numbers

# print(even_fibonacci_sum_to_4_million())

#600851475143?
def largest_prime_factor():
    primes = [2]
    prime_limit  = 600851475143
    for i in range(2,prime_limit):
      if i%2!=0 :
        if i<10 and i!=9: primes.append(i)
        if i%10==3 or i%10==7:
            factorcount = 0
            for j in primes:
                if i%j == 0:
                  factorcount += 1
                  break
            if factorcount<1:
                print(i)
                primes.append(i)
                    
    return primes[len(primes)-1]
# print(largest_prime_factor())

# def lcm_of_20_numbers():
    
def prime10001():
        primes = []
        for i in range(2,200000):
            if i%2!=0:
                factorcount = 0
                for j in primes:
                    if i%j == 0:
                        factorcount += 1
                        break
                if factorcount<1:
                    primes.append(i)
        return primes[10001]
# print(prime10001())


def product(array):
    product = 1
    for i in array:
        product*=int(i)
    return product

def max_product_of_13():
    number = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
    start = 0
    max_product = 0
    end = 13
    while end<len(str(number)):
        products = product(str(number)[start:end])
        if products>max_product: max_product=products
        start+=1 
        end+=1
    return max_product
# print(max_product_of_13())

def pythogoran_triplet():
  # a+b+c=1000
  # a < b < c
  # a^2 + b^2 = c^2
  # find abc
  a = 0
  b = 0
  c = 0
  while a+b+c < 1001:
      for i in range(1000):
          a+=1
          c = math.sqrt(a**2 + b**2)
          b = math.sqrt(c**2 - a**2)
          c+=1
          b+=1
  else: return a*b*c

print(pythogoran_triplet())
          