# Nicole Gray
#CYK algorythm
# 2.8.26
def cyk_parser(words, grammar):
    n = len(words)
    # Initialize the table with empty sets
    table = [[set() for _ in range(n + 1)] for _ in range(n + 1)]

    # Step 1: Fill the diagonal with terminals (Row 1)
    for i, word in enumerate(words):
        for lhs, rhs in grammar.items():
            for rule in rhs:
                if len(rule) == 1 and rule[0] == word:
                    table[i][i+1].add(lhs)

    # Step 2: Fill the rest of the table
    for length in range(2, n + 1):  # Length of the span
        for i in range(n - length + 1):  # Start of the span
            j = i + length              # End of the span
            for k in range(i + 1, j):    # Split point
                for lhs, rhs in grammar.items():
                    for rule in rhs:
                        if len(rule) == 2:
                            B, C = rule
                            if B in table[i][k] and C in table[k][j]:
                                table[i][j].add(lhs)
    return table

# Define the Grammar in CNF
toy_grammar = {
    "NP": [["Noun"], ["NP", "NP_And"], ["NP", "PP"]],
    "VP": [["Verb"], ["VP", "VP_And"], ["VP", "PP"]],
    "S": [["NP", "VP"]],
    "PP": [["Prep", "NP"]],
    "NP_And": [["Conj", "NP"]],
    "VP_And": [["Conj", "VP"]],
    "Noun": [["Sally"], ["pools"], ["streams"], ["swims"]],
    "Verb": [["pools"], ["streams"], ["swims"]],
    "Prep": [["in"]],
    "Conj": [["and"]]
}

sentence = "Sally swims in streams and pools".split()
table = cyk_parser(sentence, toy_grammar)

# Print the final result
print(f"Can the sentence be parsed? {'S' in table[0][len(sentence)]}")

