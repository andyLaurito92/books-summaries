from string import ascii_lowercase


def matching_from_input(pattern: str) -> None:
    letter_to_idx = {letter: i for i, letter in enumerate(ascii_lowercase)}
    m = len(pattern)

    def buildautomaton(pattern: str) -> list[list[int]]:
        k = len(ascii_lowercase)
        automaton = []
        for i in range(k):
            automaton.append([0 for j in range(m+1)])

        for i, letter in enumerate(pattern):
            automaton[letter_to_idx[letter]][i] = i+1

        # To start matching again from the last state
        # Either use lambda transition and without consuming
        # go back to state 0 or add transition from last state
        # to first
        automaton[letter_to_idx[pattern[0]]][m] = 1

        # If we are consuming the first character and
        # we see the first chacater again, then we need
        # to keep in the current state 1!
        automaton[letter_to_idx[pattern[0]]][1] = 1
        return automaton

    automaton = buildautomaton(pattern)

    state = 0
    while True:
        state = automaton[letter_to_idx[input()]][state]
        if state == m:
            print("Pattern found!")


matching_from_input("hola")
