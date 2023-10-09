maze = [["S",0 , 1, 1, 1, 0, 0, 1],
        [1, 0, 0, 0, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, "G", 0, 1, 1],
        [1, 1, 1, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1]]

starting_and_ending_co_ords = []
desirable_results = [1, "G"]
for i in range(len(maze)):
    for j in range(len(maze)):
        if maze[i][j] == "S":
            starting_and_ending_co_ords.append([i,j])
        elif maze[i][j] == "G":
            starting_and_ending_co_ords.append([i,j])

print(starting_and_ending_co_ords)
def maze_printer(maze):
    for i in maze:
        for j in i:
            print(j, end = "  ")
        print()
maze_printer(maze)

co_ords_of_path = []
def maze_runner(): 

    for i in range(len(maze)):
        for j in range(len(maze)):
            if maze[i][j]:
                co_ords_of_path.append([i,j])

maze_runner()
start = starting_and_ending_co_ords[0]
end = starting_and_ending_co_ords[1]
def maze_down(row, col):
    if row+1 < len(maze):
        if maze[row+1][col] in desirable_results :
            if type(maze[row][col]) != str:
                maze[row][col] += 1
            return True
    return False
     
def maze_up(row,col):
    if row-1>=0 : 
        if maze[row-1][col] in desirable_results:
            if type(maze[row][col]) != str:
                maze[row][col] += 1
            return True
    return False

def maze_right(row,col):
    if col+1 < len(maze): 
        if maze[row][col+1] in desirable_results :
            if type(maze[row][col]) != str:
                maze[row][col] += 1
            return True
    return False

def maze_left(row, col):
    if col-1 >= 0:
        if maze[row][col-1] in desirable_results  :
            if type(maze[row][col]) != str:
                maze[row][col] += 1
            return True
    return False

co_ords = []
# print()
all_co = []

def travel(start):
    # all_co = []

    while start != end :
        if start == end:
            break
        if start == end:
            break
        paths_available = 0
        # print("start ", start)
        # print(maze_down(start[0], start[1]))
        if maze_down(start[0], start[1]) and start[0]+1 < len(maze) :
            paths_available+=1
            # print(start[0])
            start[0]+=1
            all_co.append(start)


        if maze_right(start[0], start[1]) and start[1]+1 < len(maze) :
            paths_available+=1
            # print(start)
            start[1]+=1
            all_co.append(start)


        if maze_up(start[0],start[1]) and start[0] - 1 >= 0:
            paths_available+=1
            start[0]-=1
            # print(start)
            all_co.append(start)


        if maze_left(start[0],start[1]) and start[1] - 1 >= 0:
            paths_available+=1
            start[1]-=1
            # print(start)
            all_co.append(start)
        
        # print(start)
        
        if maze_down(start[0], start[1]) == False and maze_right(start[0], start[1]) == False and maze_up(start[0],start[1]) == False and maze_left(start[0],start[1]) == False:
            if end in all_co:
                break
            maze[start[0]][start[1]] += 1
            
            for i in range(len(maze)):
                for j in range(len(maze)):
                    if maze[i][j] == 2:
                        co_ords.append([i,j])  
                        maze[i][j] += 1
            # all_co = []
            break

travel(start)
print(co_ords)
for i in co_ords :
    # co_ords.remove(i)
    # maze_printer(maze)
    # print(all_co)
    if end in all_co:
        break
    # print(co_ords)
    travel(i)

co_ordinates = []
for i in range(len(maze)):
    for j in range(len(maze)):
        if maze[i][j] == "S" or maze[i][j] == "G":
            co_ordinates.append([i,j])
        elif maze[i][j]<=3  and maze[i][j] >= 2:
            co_ordinates.append([i,j])
print(co_ordinates)   
        


# print(travel())

# print(paths_available)




# while maze_down(start[0], start[1]):
#     start[0]+=1 
#     print(start)

#     co_ords.append((start[0],start[1]))
    
# while maze_right(start[0],start[1]):
#     start[1]+=1
#     print(start)

#     co_ords.append((start[0],start[1]))

# while maze_up(start[0], start[1]):
#     start[0]-=1
#     print(start)

#     co_ords.append((start[0],start[1]))

# while maze_left(start[0], start[1]):
#     start[1]-=1
    # print(start)

    # co_ords.append((start[0],start[1]))

# print(co_ords)
maze_printer(maze)