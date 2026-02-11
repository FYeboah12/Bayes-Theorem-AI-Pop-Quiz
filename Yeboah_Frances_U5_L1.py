def parse_input(prob_file,neh_file): #takes the file, organizes into a data structure with (dict of probabilities and dict of neighbors)
    parents_children = {} #neighbors
    probabilities = {}
    with open(prob_file) as p_file:
        for line in p_file:
            colon_index = line.strip().index(":")
            probabilities[line.strip()[:colon_index]] = float(line.strip()[colon_index+1:])
    with open(neh_file) as n_file:
        for line in n_file:
            colon_index = line.strip().index(":")
            parents_children[line.strip()[:colon_index]] = line.strip()[colon_index+1:]
    return (probabilities,parents_children)

def cond_prob():
    pass
def create_edge():
    pass
def calculate_probability():
    pass

def main():
    probability_file = input("Welcome to the Bayes Network Builder. What is the name of the file with your probabilities? See the user guide for the specific format inside the file.\n")
    neighbors_file = input("What is the name of the file with the nodes and their children? See the user guide for the specific format inside the file.\n")
    graph = parse_input(probability_file + ".txt",neighbors_file+ ".txt")
    print("This is your graph of probabilities.", graph)
    input("Do you want to")
if __name__ == '__main__':
    main()