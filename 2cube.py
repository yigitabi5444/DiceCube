# Format [x+, x-, y+, y-, z+, z-]

def rotate(die, axis):
    # axis is the axis to rotate around
    # direction is the direction to rotate in
    # 1 is clockwise, -1 is counterclockwise
    # 0 is no rotation
    # die is the die to rotate
    # returns the rotated die
    if axis == 0:
        return [die[0], die[1], die[4], die[5], die[3], die[2]]
    elif axis == 1:
        return [die[4], die[5], die[2], die[3], die[1], die[0]]
    elif axis == 2:
        return [die[2], die[3], die[1], die[0], die[4], die[5]]
    return die
        
import numpy as np

die_states = []
die_states.append([1, 6, 2, 5, 3, 4])

def get_new_die_states(die_state):
    for axis in range(3):
        new_state = rotate(die_state, axis)
        if new_state not in die_states:
            die_states.append(new_state)
            get_new_die_states(new_state)

get_new_die_states(die_states[0])


die_cube = [[[0 for x in range(2)] for y in range(2)] for z in range(2)]
#2x2x2 die cube
for x in range(2):
    for y in range(2):
        for z in range(2):
            die_cube[x][y][z] = 0 #die state
            
test_count = 0

def all_faces_equal():
    # returns true if all faces are equal
    # false otherwise
    global die_cube
    global test_count
    test_count+=1
    
    last_sum = 0
    sum=0
    for x in range(2):
        sum= 0
        for y in range(2):
            for z in range(2):
                sum+= die_states[die_cube[x][y][z]][x]
        if last_sum != 0 and last_sum != sum:
            return False
        last_sum = sum
    
    for y in range(2):
        sum= 0
        for x in range(2):
            for z in range(2):
                sum+= die_states[die_cube[x][y][z]][y+2]
        if last_sum != 0 and last_sum != sum:
            return False
        last_sum = sum
    
    for z in range(2):
        sum= 0
        for x in range(2):
            for y in range(2):
                sum+= die_states[die_cube[x][y][z]][z+4]
        if last_sum != 0 and last_sum != sum:
            return False
        last_sum = sum
    
    return True

def get_face_sums():
    # returns a list of the sums of the faces
    global die_cube
    sums = []
    for x in range(2):
        sum= 0
        for y in range(2):
            for z in range(2):
                sum+= die_states[die_cube[x][y][z]][x]
        sums.append(sum)
    
    for y in range(2):
        sum= 0
        for x in range(2):
            for z in range(2):
                sum+= die_states[die_cube[x][y][z]][y+2]
        sums.append(sum)
    
    for z in range(2):
        sum= 0
        for x in range(2):
            for y in range(2):
                sum+= die_states[die_cube[x][y][z]][z+4]
        sums.append(sum)
    
    return sums

def get_face_numbers():
    # returns a list of the numbers on the faces
    global die_cube
    face_numbers = []
    numbers = []
    for x in range(2):
        numbers = []
        for y in range(2):
            for z in range(2):
                numbers.append(die_states[die_cube[x][y][z]][x])
        face_numbers.append(numbers)
        
    for y in range(2):  
        numbers = []
        for x in range(2):
            for z in range(2):
                numbers.append(die_states[die_cube[x][y][z]][y+2])
        face_numbers.append(numbers)
        
    for z in range(2):
        numbers = []
        for x in range(2):
            for y in range(2):
                numbers.append(die_states[die_cube[x][y][z]][z+4])
        face_numbers.append(numbers)
        
    return face_numbers
                
        
def print_die_cube():
    global die_cube
    print ("Die Cube:")
    for x in range(2):
        for y in range(2):
            for z in range(2):
                print("x:" + str(x) + " y:" + str(y) + " z:" + str(z), end=": ")
                print(die_states[die_cube[x][y][z]])
                
total_cases = len(die_states)**8
#map to hold the number of times a face sum has been seen
face_sum_map = {}
        
while die_cube[0][0][0] < len(die_states):
    while die_cube[0][0][1] < len(die_states):
        while die_cube[0][1][0] < len(die_states):
            while die_cube[0][1][1] < len(die_states):
                while die_cube[1][0][0] < len(die_states):
                    while die_cube[1][0][1] < len(die_states):
                        while die_cube[1][1][0] < len(die_states):
                            while die_cube[1][1][1] < len(die_states):
                                if all_faces_equal():
                                    print("Solved, Solution:")
                                    print_die_cube()
                                    print("Tested Cases : " + str(test_count)+ "/"+str(len(die_states)**8))
                                    print("Face Sums:")
                                    print(get_face_sums())
                                    print("Face Numbers:")
                                    print(get_face_numbers()) 
                                    face_sum_map[get_face_sums()] += 1
                                    percent_complete = (test_count/total_cases)*100
                                    print("Percent Complete: " + str(percent_complete))
                                    #exit()
                                die_cube[1][1][1]+=1
                            die_cube[1][1][1]=0
                            die_cube[1][1][0]+=1
                        die_cube[1][1][0]=0
                        die_cube[1][0][1]+=1
                    die_cube[1][0][1]=0
                    die_cube[1][0][0]+=1
                die_cube[1][0][0]=0
                die_cube[0][1][1]+=1
            die_cube[0][1][1]=0
            die_cube[0][1][0]+=1
        die_cube[0][1][0]=0
        die_cube[0][0][1]+=1
    die_cube[0][0][1]=0
    die_cube[0][0][0]+=1


print("Not solved")
print(test_count)