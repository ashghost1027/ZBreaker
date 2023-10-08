for i in range(17):
    two_stars = [i for i in range(4,13,4)]
    if i==0 or i==16:
        for j in range(5):
            print("*",end="")
        print()
    elif i in two_stars:
        for j in range(2):
            print("*",end=" "*3)
        print()  

print()

for i in range(3):
    print("*"*(i+1))   
print() 
    
for i in range(3,-1,-1):
    print("*"*i)

print()


for i in range(3, 0, -1):
    for j in range(1, 3 - i + 1):
        print(" ", end="")
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1 or i == 3:
            print("*", end="")
        else:
            print(" ", end="")
    print()
print()
          
for i in range(3, 0, -1):
  for j in range(1, 3 - i + 1):
    print(" ", end="")
  for j in range(1, 2 * i):
    print("*", end="")
  print()
for i in range(2, 3 + 1):
  for j in range(1, 3 - i + 1):
    print(" ", end="")
  for j in range(1, 2 * i):
    print("*", end="")
  print()
    
    

    