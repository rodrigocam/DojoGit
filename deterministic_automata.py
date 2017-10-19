sigma = {
    ("Q0", "0"): "Q1", 
    ("Q1", "0"): "Q2",
    ("Q2", "0"): "Q3",
    ("Q2", "1"): "Q4",
    ("Q3", "0"): "Q2",
    ("Q4", "1"): "Q2",
}


def make_automaton(state, sigma, valid_states):
    def automaton(string):
        for c in string:
            try:
                state = sigma[state, c]
            except KeyError:
                return False
        return state in valid_states
    
    return automaton


s = "0011001100111111"
valid_states = {"Q2"}


zero_one_automata = make_automaton("Q0", sigma, valid_states)

print(zero_one_automata("000011"))
print(zero_one_automata("0000111"))