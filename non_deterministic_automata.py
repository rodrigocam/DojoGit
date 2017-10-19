sigma = {
    ("Q0", "0"): {"Q1"}, 
    ("Q1", "0"): {"Q2"},
    ("Q2", "0"): {"Q3"},
    ("Q2", "1"): {"Q4"},
    ("Q3", "0"): {"Q2"},
    ("Q4", "1"): {"Q2"},
}


def make_automaton(initial_state, sigma, valid_states):
    def automaton(string):
        states = {initial_state}
        for c in string:
            new_states = set()
            for state in states:
                try:
                    new_states.update(sigma[state, c])
                except KeyError:
                    return False
            states = new_states

        return any(state in valid_states for state in states)
    
    return automaton


s = "0011001100111111"
valid_states = {"Q2"}


zero_one_automata = make_automaton("Q0", sigma, valid_states)

print(zero_one_automata("000011"))
print(zero_one_automata("0000111"))