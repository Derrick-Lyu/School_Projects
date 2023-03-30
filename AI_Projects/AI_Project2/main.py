import front_end
import propositional_encoding

#import back_end

atom_list, jump_number, null_vertex, numOfVertex = front_end.atom_list, front_end.jump_number, front_end.null_vertex, front_end.numOfVertex
#print(atom_list, jump_number, "null_vertex", null_vertex, numOfVertex)
#print(atom_list)
def pd_input():
    with open("DP_Input.txt", "w") as file:
        # Write all the precondition Axioms
        for jump_statement in range(1,jump_number+1):
            line1,line2,line3 = propositional_encoding.precondition_axioms(atom_list[jump_statement])
            file.writelines([line1,line2,line3])
        # Write all the causal axioms
        for jump_statement in range(1, jump_number + 1):
            line1, line2, line3 = propositional_encoding.causal_axiom(atom_list[jump_statement])
            #print([line1, line2, line3])
            file.writelines([line1, line2, line3])
        # Write all the Frame Axioms A
        for peg_statement in range(jump_number+1,len(atom_list)):
            #print("______",atom_list[peg_statement])
            #print("???",propositional_encoding.frame_axiom_A(atom_list[peg_statement]))
            if (propositional_encoding.frame_axiom_A(atom_list[peg_statement]) != None):
                #print(propositional_encoding.frame_axiom_A(atom_list[peg_statement]))
                file.write(propositional_encoding.frame_axiom_A(atom_list[peg_statement]))
                file.write("\n")
        # Write all the Frame Axioms B
        for peg_statement in range(jump_number+1,len(atom_list)):
            if (propositional_encoding.frame_axiom_B(atom_list[peg_statement]) != None):
                #print(propositional_encoding.frame_axiom_B(atom_list[peg_statement]))
                file.write(propositional_encoding.frame_axiom_B(atom_list[peg_statement]))
                file.write("\n")
        # Write all the One action at a time
        for jump_statement in range(1, jump_number + 1):
            ans = propositional_encoding.one_Action(atom_list[jump_statement])
            file.writelines(ans)
            #print(ans)
        # Write all the Starting State
        for peg_statement in range(1,numOfVertex+1):
            temp_statement = "Peg(%d,1)"%(peg_statement)
            #print(propositional_encoding.starting_state(temp_statement))
            file.write(str(propositional_encoding.starting_state(temp_statement)))
            file.write('\n')
        #Writing all the Ending State
        ending_states = propositional_encoding.Ending_state()
        file.writelines(ending_states)
        #Write all the Pegs and Jumps
        for position in range(len(atom_list)):
            if position > 0:
                file.write(str(position))
                file.write(" ")
                file.write(atom_list[position])
                file.write("\n")
            else:
                file.write("0\n")


def main():
    pd_input()
    import back_end
    #print(atom_list)
    list = back_end.DPLL(back_end.clauses, back_end.identifier)
    if list != False:
        for ii in range(1,jump_number+1):
            if list[str(ii)] == True:
                print(atom_list[ii])
    else:
        print("There is no answer for this")


if __name__ == "__main__":
    main()
