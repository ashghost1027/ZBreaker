
def eligibility(N):
    if N>=6 and N<=8:
        return "Yes"
    return "No"

def count_of_plates(bar,sticks_per_plate,rupees):
    num_of_sticks_after_bar = rupees/30
    return ((bar+num_of_sticks_after_bar)//sticks_per_plate)+1

# print(count_of_plates(15,9,120))

def count_even_values(card_swipe):
    office_in = []
    count = 0
    counts = []
    for i in card_swipe:
        if i not in office_in:
            office_in.append(i)
            count+=1
        else:
            counts.append(count)
            office_in.remove(i)
            count = 0
    
    counts.append(count)
    if len(office_in)>count:
        return len(office_in)
    else:
        return max(counts)
    
            
# print(count_even_values([1, 2, 1, 5, 4]))

def maximize_score(array):
    scores = []
    
    K = 0
    for _ in range(len(array)):
        score = 0
        bucket = []
        for j in range(K):
            bucket.append(array[j])
        for j in range(K,len(array)):
            bucket.append(array[j])
            score += bucket.pop(bucket.index(max(bucket)))
        scores.append(score)
        K+=1
        
    
    return scores


print(maximize_score([5, 8, 3, 2]))


def count_increments(increments):
    inc = []
    count = 0
    count_of_increments = 0
    for i in increments:
        if count<=3:
            if i not in inc:
                inc = [i]
                count_of_increments+=1
                count+=1
            else:
                inc.append(i)
                count+=1
        else:
            count_of_increments+=1
    return count_of_increments
        
        

def divisible_by_3(array):
    start = 0
    end = start+3
    increments = []
    while end<len(array):
        subarray = array[start:end]
        remainder = sum(subarray)%3
        if remainder == 2:
            increments.append(1)
        elif remainder == 1:
            increments.append(2)
        start+=1
        end+=1
    count_increment = count_increments(increments)
    return count_increment



print(divisible_by_3([10, 12, 15, 16, 17, 200, 132]))