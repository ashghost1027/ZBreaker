total_vehicle_count = 204
i = 0
count_of_motorbikes_in_second_half = 0
row = []
while total_vehicle_count > 0:
    row.append("car")
    i+=1
    total_vehicle_count -= 1
    for _ in range(i):
        row.append("bike")
        total_vehicle_count -= 1
    
for i in row[len(row)//2:]:
    if i == "bike":
        count_of_motorbikes_in_second_half += 1
print(count_of_motorbikes_in_second_half)
print(row)
    

