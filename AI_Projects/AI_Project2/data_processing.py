import copy
import math

clauses = []
identifier = {}
identifier_value = []

def toList(input):
    tempList = list(input.split(","))
    for pos in range(len(tempList)):
        tempList[pos] = tempList[pos]
    return tempList

with open("DP_Input.txt","r") as file:
    lines = file.readlines()
    count = 0
    #%% find all clauses
    for line in lines:
        line = line.replace("\n", "")
        line = toList(line)
        clauses.append(line)
        count += 1
        if int(line[0]) == 0:
            break
    clauses.pop(-1) #delete the 0 at the end
    #%% find all identifier value

    #%% set all identifier
    num_of_identifer = len(lines[count:])
    for i in range(1,1+num_of_identifer):
        identifier["%d"%(i)] = None


#%%Propogate method
def propogate(element, clauses):
    neg = str(int(element) * -1)
    returned_list = []
    for pos in range(len(clauses)):
        clause = clauses[pos]
        if neg in clause:
            clause.remove(neg)
            returned_list.append(clause)
        elif element not in clause:
            returned_list.append(clause)
    return (returned_list)

#print(propogate("1",clauses))
#%%
def DPLL(clauses,identifier):
    #print("\n___________New Start______________________\n",clauses)
    #print(identifier)
    round = 1
    while True:
        four_case_used = False
        #print("\n"+ str(round))
        # if every clause is satisfied, return true
        if len(clauses) == 0:
            four_case_used = True
            #print("Done")
            return identifier
        # if any clause is null clause, return false
        for clause in clauses:
            if len(clause) == 0:
                four_case_used = True
                #print("Failed")
                return False
        # if there is any single literal, propogate
        temp_null = {}
        for i in range(1, 1 + num_of_identifer):
            temp_null["%d" % (i)] = None
        for clause in clauses:
            for element in clause:
                element = int(element)
                element_pos_bool = element > 0
                if temp_null[str(abs(element))] == None:
                    temp_null[str(abs(element))] = element_pos_bool
                else:
                    if temp_null[str(abs(element))] != element_pos_bool:
                        temp_null[str(abs(element))] = "nah"
            if len(clause) == 1:
                element = clause[0]
                #print("element choosen by single lit:", element)
                if int(element) > 0:
                    identifier[element] = True
                else:
                    temp_element = str(abs(int(element)))
                    identifier[temp_element] = False
                clauses = propogate(element,clauses)
                four_case_used = True
                break
        #print("temp_nan", temp_null)
        # if there is any pure literal, propogate
        if four_case_used == False:
            for pos in range(1, 1 + num_of_identifer):
                element_bool = temp_null[str(pos)]
                if element_bool != "nah" and element_bool != None:
                    four_case_used = True
                    identifier[str(abs(pos))] = True
                    #print("element choosen by pure lit:", pos)
                    clauses = propogate(str(pos), clauses)
                    break
        #print("clauses",clauses)
        #print("identifier",identifier)
        if four_case_used == False:
            break
        round += 1
    #%% If the previous statement does not make sense
    #print("---randomly assign start---")
    random_element = None
    for element in range(1,1+num_of_identifer):
        if identifier[str(element)] == None:
            random_element = element
            break
    # Try to set the first unkown indentifer true
    #print("random_element IS ", random_element)
    temp_clauses = copy.deepcopy(clauses)
    temp_clauses = propogate(str(random_element),temp_clauses)
    temp_identifier = copy.deepcopy(identifier)
    temp_identifier["%d"%(abs(random_element))] = True
    #print("temp_clauses",temp_clauses)
    #print("temp_identifier", temp_identifier)
    ans = DPLL(temp_clauses,temp_identifier)
    if ans == False:
        #print("before change\n",clauses,"\n identifier\n", identifier)
        #print("random_element change to neg",str(random_element * -1) )
        temp_clauses = copy.deepcopy(clauses)
        temp_clauses = propogate(str(random_element * -1), temp_clauses)
        temp_identifier = copy.deepcopy(identifier)
        temp_identifier["%d" % (abs(random_element))] = False
        ans = DPLL(temp_clauses, temp_identifier)
        return ans
    else:
        return ans


"""def trueValue():
    list = DPLL(clauses,identifier)
    print(list,len(list))
    for i in range(1,len(list)+1):
        if (list[str(i)]== True):"""


#%% Try one
