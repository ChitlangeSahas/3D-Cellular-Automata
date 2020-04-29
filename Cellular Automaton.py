import maya.cmds as cmds

#create cube

NUM_OF_CUBES = 25

Cube_Array = [[ ['*' for col in range(NUM_OF_CUBES)] for col in range(NUM_OF_CUBES)] for row in range(NUM_OF_CUBES)]

# Creates a cune at location
def create_cube(x, y, z):
    cubeObj = cmds.polyCube()
    Cube_Array[x][y][z] = cubeObj
    cmds.move( x, y, z )

def delete_cube(x,y,z):
    cmds.hide(Cube_Array[x][y][z])
    Cube_Array[x][y][z] = '*'
    
# for x in range(NUM_OF_CUBES):
#     for y in range(NUM_OF_CUBES):
#         for z in range(NUM_OF_CUBES):  
#             cubeObj = cmds.polyCube()
#             Cube_Array.append(cubeObj)
#             Cube_Array[x][y][z] = cubeObj
#             cmds.move( x, y, z )


def get_neighbours(x,y,z):
    neighbours = []
    coordinate_max = NUM_OF_CUBES
    
    if (x + 1 < coordinate_max):
        neighbours.append([x+1,y,z])
    if (x - 1 >= 0):          
        neighbours.append([x-1,y,z])
    if (y + 1 < coordinate_max):
        neighbours.append([x,y+1,z])
    if (y - 1 >= 0):
        neighbours.append([x,y-1,z])
    if (z + 1 < coordinate_max):
        neighbours.append([x,y,z+1])
    if (z - 1 >= 0):
        neighbours.append([x,y,z-1])
    
    return neighbours

# Returns if a cube exists at the given coordinates.
def cube_exists_at(x,y,z):
    if type(Cube_Array[x][y][z]) == list:
        return True
    return False

def get_neighbour_count(x,y,z):
    neighbors = get_neighbours(x, y, z)
    
    count = 0
    for neighbor in neighbors:
        if cube_exists_at(neighbor[0], neighbor[1], neighbor[2]):
            count = count + 1
    
    return count

#init

for x in range(NUM_OF_CUBES):
    for y in range(NUM_OF_CUBES):
        for z in range(NUM_OF_CUBES):  
            cubeObj = cmds.polyCube()
            Cube_Array.append(cubeObj)
            Cube_Array[x][y][z] = cubeObj
            cmds.move( x, y, z )
            
print get_neighbour_count(0,0,0)


for i in range(20):
    print i
    for x in range(NUM_OF_CUBES):
        for y in range(NUM_OF_CUBES):
            for z in range(NUM_OF_CUBES):               
                if get_neighbour_count(x, y, z) == 2: # Birth
                    if not cube_exists_at(x, y, z):
                        create_cube(x, y, z)
                else : # Loneliness or Overpopulation
                    if cube_exists_at(x, y, z):
                        delete_cube(x, y, z)
    
