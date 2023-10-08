import math;

arrays = [[85,75,65,85,75],[90,180,66,90,78],[75,66,57,75,69],[80,72,60,80,72],[76,64,56,72,68]]

for i in range(len(arrays)):
    minim = min(arrays[i])
    for j in range(len(arrays[i])):
        
        arrays[i][j] -= minim

lizzy = []
for i in range(len(arrays)):
    for j in range(len(arrays[i])):
        
        if arrays[i][j] == 0:
            lizzy.append(j)

print(lizzy)


minfind = []
for i in range(len(arrays)):
    for j in range(len(arrays[i])):
        if j not in lizzy:
            minfind.append(arrays[i][j])
        else:
            continue

minimus = min(minfind)
        
for i in range(len(arrays)):
    for j in range(len(arrays[i])):
        if j not in lizzy:
            arrays[i][j] -= minimus


for i in range(len(arrays)):
    for j in range(len(arrays[i])):
        
        if arrays[i][j] == 0:
            lizzy.append(j)

print(lizzy)
            
countrow = 0
countcol = 0 
lisa =[]
for i in range(len(arrays)):
    # for j in arrays[i]:
    if 0 in arrays[i]:
        countrow += 1    
    for j in lizzy:
        if j not in lisa:
            lisa.append(j)
    countcol = len(lisa)

if countrow<countcol:
    minval = countrow
elif countcol < countrow:
    minval = countcol
else:
    minval= countrow
            
while minval != len(arrays[0]):
    minimus = min(minfind)
        
    for i in range(len(arrays)):
        for j in range(len(arrays[i])):
            if j not in lizzy:
                arrays[i][j] -= minimus


    for i in range(len(arrays)):
        for j in range(len(arrays[i])):
            
            if arrays[i][j] == 0:
                lizzy.append(j)

    print(lizzy)
                
    countrow = 0
    countcol = 0 
    lisa =[]
    for i in range(len(arrays)):
        # for j in arrays[i]:
        if 0 in arrays[i]:
            countrow += 1    
        for j in lizzy:
            if j not in lisa:
                lisa.append(j)
        countcol = len(lisa)

    if countrow<countcol:
        minval = countrow
    elif countcol < countrow:
        minval = countcol
    else:
        minval= countrow

print(countrow)
print(countcol)
# print(minfind)      
print(arrays)



