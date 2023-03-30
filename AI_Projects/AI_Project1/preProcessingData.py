
budget = 0
flag = ""
num_O_random_restart = 0
vertices = {}
overall_vertices = []
verticesName = []


#%% Find the first line
#asking_input = input(" Enter the file name \n ")
input1 = input("Please enter the Path of the File \n")
input = open(input1, "r")
line1 = input.readline()
line1 = line1.rstrip()
blank_indices = [i for i in range(len(line1)) if line1[i] == " "]
#print(blank_indices)
budget = int(line1[0:blank_indices[0]])
if len(blank_indices)== 2:
    flag += line1[blank_indices[0]+1:blank_indices[1]]
    num_O_random_restart = int(line1[blank_indices[1]+1:])
else:
    flag += line1[blank_indices[0]+1:]
"""print("Budget:", budget,type(budget))
print("Flag: ", flag, type(flag))
print("Number of Random Restart: ", num_O_random_restart, type(num_O_random_restart))
print("________________________________________________________________________________________________")"""
#%% find all the vertices and weight
while True:
    line = input.readline()
    if line == "\n":
        break
    else:
        line = line.rstrip()
        #print(line)
        blank_space = line.index(" ")
        vertexName = line[:blank_space]
        vertexWeight = line[blank_space+1:]
        vertices[vertexName] = {}
        vertices[vertexName]["weight"] = vertexWeight
        vertices[vertexName]["edge"] = []
        #print(vertices)
#print("________________________________________________________________________________________________")
#%% find all the edges
lines = input.readlines()
#print(lines)
for line in lines:
    line = line.rstrip()
    blank_space = line.index(" ")
    vertex_1 = line[:blank_space]
    vertex_2 = line[blank_space+1:]
    overall_vertices.append([vertex_1, vertex_2])
    overall_vertices.append([vertex_2, vertex_1])
    vertices[vertex_1]["edge"].append(vertex_2)
    vertices[vertex_2]["edge"].append(vertex_1)
    #print(vertices)
#%% create a vertex name list
for i in vertices:
    #print(i, vertices[i]["weight"], vertices[i]["edge"])
    verticesName.append(i)
#print(verticesName)


