import front_end as main

def precondition_axioms(aString):
    jump = -1 * main.atom_list.index(aString)
    aString=aString.replace("Jump(", "").replace(")", "").replace("\n","").split(",")
    vertex_1 = "Peg(%s,%s)"%(aString[0],aString[3])
    vertex_2 = "Peg(%s,%s)"%(aString[1],aString[3])
    vertex_3 = "Peg(%s,%s)"%(aString[2],aString[3])
    statement_1 = "%s,%s\n"%(jump,main.atom_list.index(vertex_1))
    statement_2 = "%s,%s\n" % (jump, main.atom_list.index(vertex_2))
    statement_3 = "%s,%s\n" % (jump, -1*main.atom_list.index(vertex_3))
    return statement_1,statement_2,statement_3



def causal_axiom(aString):
    jump = -1 * main.atom_list.index(aString)
    aString=aString.replace("Jump(", "").replace(")", "").replace("\n","").split(",")
    vertex_1 = "Peg(%s,%s)" % (aString[0], str(int(aString[3])+1))
    vertex_2 = "Peg(%s,%s)" % (aString[1], str(int(aString[3])+1))
    vertex_3 = "Peg(%s,%s)" % (aString[2], str(int(aString[3])+1))
    statement_1 = "%s,%s\n" % (jump, -1 * main.atom_list.index(vertex_1))
    statement_2 = "%s,%s\n" % (jump, -1 * main.atom_list.index(vertex_2))
    statement_3 = "%s,%s\n" % (jump, main.atom_list.index(vertex_3))
    return statement_1, statement_2, statement_3


def frame_axiom_A(aString):
    #print(aString)
    aString = aString.replace("Peg(","").replace(")", "").split(",")
    vertex_1 = aString[0]
    time = int(aString[1])
    #print("vertex_1",vertex_1,"time",time)
    if time < main.numOfVertex-1:
        time_1 = "Peg(%s,%s)"%(vertex_1,time)
        time_2 = "Peg(%s,%s)"%(vertex_1,time+1)
        #print(time_1,time_2)
        statement_1 = main.atom_list.index(time_1) * -1
        statement_2 = main.atom_list.index(time_2)
        overall_statement = "%d,%d"%(statement_1,statement_2)
        #print(overall_statement)
        #print(main.atom_list[145],main.atom_list[146])
        for jump in range(1,main.jump_number+1):
            #print(main.atom_list[jump])
            temp_jump = main.atom_list[jump].replace("Jump(", "").replace(")", "").replace("\n","").split(",")
            #print("temp_jump",temp_jump)
            if ((vertex_1 == temp_jump[0]
                or vertex_1 == temp_jump[1]) \
                    and time == int(temp_jump[3])):
                #print(main.atom_list[jump])
                temp_list = main.atom_list[jump]
                #print(temp_list)
                temp_statement = main.atom_list.index(temp_list)
                overall_statement += ","
                overall_statement += str(temp_statement)
        return overall_statement
    else:
        return None

def frame_axiom_B(aString):
    aString = aString.replace("Peg(", "").replace(")", "").split(",")
    vertex_1 = aString[0]
    time = int(aString[1])
    if time < main.numOfVertex -1:
        time_1 = "Peg(%s,%s)"%(vertex_1,time)
        time_2 = "Peg(%s,%s)"%(vertex_1,time+1)
        statement_1 = main.atom_list.index(time_1)
        statement_2 = main.atom_list.index(time_2) * -1
        overall_statement = "%d,%d"%(statement_1,statement_2)
        #print("overall",overall_statement)
        for jump in range(1,main.jump_number+1):
            #print(main.atom_list[jump])
            temp_jump = main.atom_list[jump].replace("Jump(", "").replace(")", "").replace("\n", "").split(",")
            if (vertex_1 == temp_jump[2]
                    and time == int(temp_jump[3])):
                #print(main.atom_list[jump])
                temp_list = main.atom_list[jump]
                temp_statement = main.atom_list.index(temp_list)
                overall_statement += ","
                overall_statement += str(temp_statement)
        return overall_statement

def one_Action(aString):
    input_index = main.atom_list.index(aString)
    aString = aString.replace("Jump(", "").replace(")", "").replace("\n", "").split(",")
    time = aString[3]
    statement = []
    for jump in main.atom_list[input_index+1:main.jump_number+1]:
        jumpT = jump.replace("Jump(", "").replace(")", "").replace("\n", "").split(",")
        if int(jumpT[3]) == int(time):
            statement.append("%d,%d\n"%(-1 * input_index, -1 * main.atom_list.index(jump)))
    return statement

def starting_state(aString):
    if main.atom_list.index(aString) != int(main.null_vertex):
        return main.atom_list.index(aString)
    else:
        return int(main.null_vertex)*-1

def Ending_state():
    output = []

    for ii in range(1, main.numOfVertex+1):
        vertex_1 = "Peg(%d,%d)"%(ii,main.numOfVertex-1)
        for jj in range(ii+1, main.numOfVertex+1):
            vertex_2 = "Peg(%d,%d)"%(jj,main.numOfVertex-1)
            temp_list = "%d,%d\n"%(main.atom_list.index(vertex_1)*-1, main.atom_list.index(vertex_2)*-1)
            output.append(temp_list)

    return(output)


#%% test section
"""print(precondition_axioms("Jump(1,2,4,7)"))
print(causal_axiom("Jump(1,2,4,7)"))
print(frame_axiom_A("Peg[1,1]"))
print(frame_axiom_B("Peg[1,2]"))
print(one_Action("Jump(1,2,4,7)"))
print(starting_state("Peg(1,2)"))"""
#Ending_state()
#print(frame_axiom_A("Peg[1,1]"))