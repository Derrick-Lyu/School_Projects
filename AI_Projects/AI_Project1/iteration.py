import numpy as np
from preProcessingData import budget, flag, num_O_random_restart, vertices, overall_vertices

"""print(budget)
print(flag)
print(num_O_random_restart)
print(overall_vertices)"""

#%% check if the temp_list is valid
def valid_list(temp_list, budget, vertices):
    overall_edges = overall_vertices.copy()
    weight_sum = 0
    edges = []
    #find the total weight and edges for cur list
    for vertex in temp_list:
        weight_sum += int(vertices[vertex]["weight"])
        for ver in vertices[vertex]["edge"]:
            edges.append([vertex,ver])
            edges.append([ver,vertex])

    #print("edges", edges)
    if weight_sum <= budget:
        for edge in edges:
            if edge in overall_edges:
                overall_edges.pop(overall_edges.index(edge))
        if len(overall_edges) > 0:
            print(temp_list, "cost= ", weight_sum)
            return "adding"
        if len(overall_edges) == 0:
            print("Found solution", temp_list, "cost=", weight_sum)
            return "success"
    else:
        return "failed"


#%% iterative solution

def BFS_solution():
    if flag == "V":
        pq = [[]]
        for depth in range(len(vertices)):
            print("Depth: ", depth+1)
            #print("How many list got poped: ", len(pq))
            for ii in range(len(pq)):
                poped_list = pq.pop(0)
                if len(poped_list) == 0:
                    for vertex in vertices:
                        if vertex not in poped_list:
                            poped_list.append(vertex)
                            temp_list = poped_list.copy()
                            validity = valid_list(temp_list,budget,vertices)
                            if validity == "adding" or validity == "success":
                                pq.append(temp_list)
                            if validity == "success":
                                return None
                            poped_list.pop(-1)
                else:
                    for vertex in vertices:
                        if vertex > poped_list[-1]:
                            poped_list.append(vertex)
                            temp_list = poped_list.copy()
                            validity = valid_list(temp_list, budget, vertices)
                            #print("validity", validity)
                            if validity == "adding" or validity == "success":
                                pq.append(temp_list)
                            if validity == "success":
                                return None
                            poped_list.pop(-1)
        print("Search faield, No solution Found")
        return None
#BFS_solution()

#%% DFS Solution

def DFS_solution():
    if flag == "V":
        for level in range(0,len(vertices)):
            print("Depth:", level+1)
            ans = DFS([],0, level)
            if ans == True:
                return True
        print("Search faield, No solution Found")
        return None


def DFS(vertex_list, cur_level, temp_level):
    validity = valid_list(vertex_list, budget, vertices)
    if validity == "success":
        #print("-----------------------")
        return True

    if validity == "failed":
        return False

    if cur_level > temp_level:
        return False

    for vertex in vertices:
        temp_list = vertex_list.copy()
        ans = False
        if len(vertex_list) > 0:
            if vertex > vertex_list[-1]:
                temp_list.append(vertex)
                ans = DFS(temp_list, cur_level+1,temp_level)
        else:
            temp_list.append(vertex)
            ans = DFS(temp_list, cur_level + 1, temp_level)
        if ans == True:
            return True




DFS_solution()
