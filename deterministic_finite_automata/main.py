import networkx as nx
import matplotlib.pyplot as plt
class dfa:
    def __init__(self, q, alphabet, sigma, initial, final):
        self.q = q
        self.alphabet = alphabet
        self.transitions = sigma
        self.initial = initial
        self.final = final

    def word_process(self, word):
        current_state = self.initial[0]
        for symbol in word:
            if symbol not in self.alphabet:
                print("Error: \"", symbol, "\" is not a valid symbol of your language.")
                return False
            current_state = self.transitions[current_state][symbol]

        return current_state in self.final


#parameters set up
transitions = {
    '0': {'a': '0', 'b': '1'},
    '1': {'a': '1', 'b': '1'}
}
dfa_model = dfa(
    {'0', '1', '3'},
    {'a', 'b'},
    transitions,
    '0',
    {'1', '2'}
)


#word set up
word = "ab"

if dfa_model.word_process(word):
    print("\"", word, "\" is ACCEPTED according to the defined automata.")
else:
    print("\"", word, "\" is NOT ACCEPTED according to the defined automata.")