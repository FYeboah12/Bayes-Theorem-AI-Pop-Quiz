import sys
'''
what is done: 
-parsing from the text file and creating the data structure with neighbors and probabilities
-calculating all possible probabilities from the data given
what needs to be done:
-conditional probability/actual calculations
'''
def parse_input(prob_file,neh_file): #takes the file, organizes into a data structure with (dict of probabilities and dict of neighbors)
    parents_children = {} #neighbors
    probabilities = {}
    try:
        p_file = open(prob_file)
    except OSError:
        print("Could not open/read file:", prob_file, ". Check the file name and try again.")
        sys.exit()
    for line in p_file:
                colon_index = line.strip().index(":")
                probabilities[line.strip()[:colon_index]] = float(line.strip()[colon_index+1:])

    try:
        n_file = open(neh_file)
    except OSError:
        print("Could not open/read file:", neh_file, ". Check the file name and try again.")
        sys.exit()
    for line in n_file:
            colon_index = line.strip().index(":")
            parents_children[line.strip()[:colon_index]] = line.strip()[colon_index+1:]
    return [probabilities,parents_children]

def cond_prob():
    pass

def all_possibilities(grf):
    probs = grf[0]
    new_probs = {node:probs[node] for node in probs}
    for p in probs:
         if "|" not in p and "~" not in p:
              new_probs["~" + p] = 1 - probs[p]
         elif "|" not in p and "~" in p:
              new_probs[p[1:]] = 1 - probs[p]
         elif "|" in p:
            first_term = p[:p.index("|")]
            sec_term = p[p.index("|") + 1:]
            if "~" not in first_term and "," not in first_term:
                new_probs["~" + first_term + "|" + sec_term] = 1 - probs[p]
            elif "~" not in sec_term and "," not in sec_term:
                new_probs[first_term + "|~" + sec_term] = 1 - probs[p]
            elif "," in first_term:
                first_com = first_term[:p.index(",")]
                sec_com = first_term[p.index(",") + 1:]
                if "~" not in first_com:
                    new_probs["~"+ first_com + "," + sec_com + "|" + sec_term] = 1 - probs[p]
                if "~" not in sec_com:
                    new_probs[first_com + ",~" + sec_com + "|" + sec_term] = 1 - probs[p]
    grf[0] = new_probs           
              

def calculate_probability(user_input,grf):
    #grf = ({probs},{nehs})
    if user_input in grf[0]: return grf[0][user_input] #this is if it is present, it currently doesn't calculate anything
    return 0


def main():
    verify_check = False
    while not verify_check:
        probability_file = input("Welcome to the Bayes Network Builder. What is the name of the file with your PROBABILITIES? See the user guide for the specific format inside the file.\n")
        neighbors_file = input("What is the name of the file with the NODES AND THEIR CHILDREN? See the user guide for the specific format inside the file.\n")
        graph = parse_input(probability_file + ".txt",neighbors_file+ ".txt")
        all_possibilities(graph)
        print("This is your graph of probabilities.", graph,"\n")
        answer = input("If this is correct, type 'y.' Else, type 'n.'\n").lower()
        verify_check = True if answer  == "y" else False
    probability = input("Calculate probability. Type your desired probability as specified in the user guide.\n")
    print("P(",probability, ") = ", calculate_probability(probability,graph))
    #A / A|B / A,B / A|B,C / A,B|C
if __name__ == '__main__':
    main()
