
def preprocessing_data():
    file_name = input("Please enter the file path\n")
    input_file = open(file_name, "r")
    line1 = input_file.readline()
    line1 = line1.rstrip('\n').split(' ')
    numOfVertex = int(line1[0])
    null_vertex = line1[1]
    #print("null_vertex",null_vertex,type(null_vertex))
    jump_list = []
    jump_number = 0
    #print("numOfVertex, null_vertex", numOfVertex, null_vertex)
    lines = input_file.readlines()
    #find all the jump list
    for line in lines:
        line = line.rstrip("\n").split(" ")
        #print(line)
        vertex_1 = line[0]
        vertex_2 = line[1]
        vertex_3 = line[2]
        temp_list = [vertex_1,vertex_2,vertex_3]
        temp_list_2 = [vertex_3,vertex_2,vertex_1]
        jump_list.append(temp_list)
        jump_list.append(temp_list_2)
    #print("Jump_list", jump_list)
    #create dictionary mapping number to key
    ii = 1
    numberOfElements = (len(jump_list)*(numOfVertex-2) + numOfVertex *(numOfVertex-1)) + 1
    outputdict = ["0"] * numberOfElements
    while True:
        for list in jump_list:
            for time in range(1,numOfVertex-1):
                temp_list  = list.copy()
                temp_list.append(time)
                insert_1 = "Jump(%d,%d,%d,%d)"%(int(temp_list[0]),int(temp_list[1]),int(temp_list[2]), int(temp_list[3]))
                outputdict[ii] = insert_1
                ii += 1
            jump_number = ii - 1
        for peg in range(1,numOfVertex+1):
            for time in range(1,numOfVertex):
                outputdict[ii] = "Peg(%d,%d)"%(peg,time)
                ii += 1
        break
    null_index = outputdict.index("Peg(%d,1)"%(int(null_vertex)))
    #print(outputdict, jump_number, null_index, numOfVertex)
    return(outputdict, jump_number, null_index, numOfVertex)


atom_list, jump_number, null_vertex, numOfVertex = preprocessing_data()

