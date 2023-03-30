import numpy as np
from preProcessingData import budget, flag, num_O_random_restart, vertices, overall_vertices, verticesName
import random

#sb = ["A","B"]
#%% Cost Function
def cost(templist):
    sum = 0
    for vertex in templist:
        cur_weight = int(vertices[vertex]["weight"])
        sum += cur_weight
    return sum
#print("cost:", cost(sb))
#%% Error Function
def error(tempList):
    overall_edges = overall_vertices.copy()
    uncovered_sum = 0
    edges = []
    # find all existing edges
    for vertex in tempList:
        for ver in vertices[vertex]["edge"]:
            edges.append([vertex,ver])
            edges.append([ver,vertex])
    # pop all existing edges
    for edge in edges:
        if edge in overall_edges:
            overall_edges.pop(overall_edges.index(edge))
    #find the sum of uncovered edges
    i = 1
    while i <= len(overall_edges):
        vertex_1 = overall_edges[i-1][0]
        vertex_2 = overall_edges[i][0]
        weight_1 = int(vertices[vertex_1]["weight"])
        weight_2 = int(vertices[vertex_2]["weight"])
        uncovered_sum += min(weight_1,weight_2)
        i += 2
    first_part = max(0, cost(tempList)-budget)
    return first_part + uncovered_sum
#print("error:", error(sb))

#%% find all the neighbor
def neighbor(curState):
    best_vertex = [curState, error(curState)]
    #add a vertex
    for vertex in vertices:
        temp_state = curState.copy()
        if vertex not in temp_state:
            temp_state.append(vertex)
            cur_cost = cost(temp_state)
            cur_error = error(temp_state)
            print(temp_state, "Cost:", cur_cost, "Error:", cur_error)
            if cur_error < best_vertex[1]:
                best_vertex = [temp_state, cur_error]
    #delete a vertex
    for vertex in range(len(curState)):
        temp_state = curState.copy()
        temp_state.pop(vertex)
        cur_cost = cost(temp_state)
        cur_error = error(temp_state)
        print(temp_state, "Cost:", cur_cost, "Error:", cur_error)
        if cur_error <= best_vertex[1]:
            best_vertex = [temp_state, cur_error]
    if(curState != best_vertex[0]):
        print('\n', "Move to", best_vertex[0], "Cost:", cost(best_vertex[0]), "Error:", best_vertex[1])
    return best_vertex
#print("neighbor", neighbor(sb))

#%%
def climbing_helper(startState, best_val):
    best_neighbor = neighbor(startState)
    if best_neighbor[1] < best_val:
        return climbing_helper(best_neighbor[0], best_neighbor[1])
    else:
        if cost(startState) < budget:
            return [startState, best_val]
        else:
            return False
#print("Find the best", climbing_helper(["E"], np.inf))


#%%
def hill_climbing():
    if flag == "V":
        failed_num = 0
        best = [[],np.inf]
        for restart in range(num_O_random_restart):
            num_O_vertex = np.random.randint(len(vertices))
            start_int = random.sample(range(len(vertices)), num_O_vertex)
            #print(num_O_vertex, start_int)
            start_state = []
            for location in start_int:
                start_state.append(verticesName[location])
            print("\n\n","Randomly Start State", start_state,"Cost:", cost(start_state), "Error", error(start_state))
            ans = climbing_helper(start_state,best[1])

            if ans == False:
                print("Search Failed")
                failed_num += 1
            else:
                print("Found the solution", "State:", ans[0], "Cost:", cost(ans[0]), "Error:",ans[1])
        if failed_num == num_O_random_restart:
            print("No Solution Found")
        else:
            print("Please refer to the previous solutions")
hill_climbing()