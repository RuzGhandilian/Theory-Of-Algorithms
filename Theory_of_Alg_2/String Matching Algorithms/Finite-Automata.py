class Finite_Automata:
    def __init__(self, pattern, alphabet=None):
        self.pattern = pattern
        self.alphabet = alphabet if alphabet else set(pattern)
        self.transitions = self.build_transitions()

    def build_transitions(self):
        m = len(self.pattern)
        transitions = {}

        for state in range(m + 1):
            for char in self.alphabet:
                next_state = state
                while next_state > 0 and (next_state >= m or self.pattern[next_state] != char):
                    next_state -= 1
                if next_state < m and self.pattern[next_state] == char:
                    next_state += 1
                transitions[(state, char)] = next_state

        return transitions

    def search(self, text):
        current_state = 0
        m = len(self.pattern)

        for i, char in enumerate(text):
            current_state = self.transitions.get((current_state, char), 0)
            if current_state == m:
                print(f"Pattern found at index {i - m + 1}")
                current_state = 0


text = "gsfgshshsrgvssrgrsgsrgaFEGRG"
pattern = "vssr"
fin_a = Finite_Automata(pattern)
fin_a.search(text)
