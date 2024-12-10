from tabulate import tabulate

# Grammar definition
grammar = {
    "E": ["T E'"],
    "E'": ["+ T E'", "ε"],  # ε represents epsilon (empty production)
    "T": ["F T'"],
    "T'": ["* F T'", "ε"],
    "F": ["( E )", "id"]
}

# Terminals and non-terminals
terminals = ["+", "*", "(", ")", "id", "$"]
non_terminals = ["E", "E'", "T", "T'", "F"]

# First and Follow sets
first = {
    "E": {"(", "id"},
    "E'": {"+", "ε"},
    "T": {"(", "id"},
    "T'": {"*", "ε"},
    "F": {"(", "id"}
}

follow = {
    "E": {")", "$"},
    "E'": {")", "$"},
    "T": {"+", ")", "$"},
    "T'": {"+", ")", "$"},
    "F": {"*", "+", ")", "$"}
}

# Initialize the parsing table
parsing_table = {non_terminal: {terminal: None for terminal in terminals} for non_terminal in non_terminals}

# Fill the parsing table based on the grammar, first, and follow sets
for non_terminal, productions in grammar.items():
    for production in productions:
        first_symbol = production.split()[0]

        if first_symbol in non_terminals:  # Starts with a non-terminal
            for terminal in first[first_symbol]:
                parsing_table[non_terminal][terminal] = production
        elif first_symbol in terminals:  # Directly add terminal to table
            parsing_table[non_terminal][first_symbol] = production
        elif first_symbol == "ε":  # Handle epsilon with follow set
            for terminal in follow[non_terminal]:
                parsing_table[non_terminal][terminal] = production

# Display the parsing table in tabular format
parsing_table_display = [[non_terminal] + [parsing_table[non_terminal][terminal] or '' for terminal in terminals] for non_terminal in non_terminals]
headers = [""] + terminals
print("Parsing Table:")
print(tabulate(parsing_table_display, headers=headers, tablefmt="grid"))

# Function to parse input using the predictive parsing table
def predictive_parse(input_string):
    stack = ["$", "E"]
    input_string += "$"  # End-of-input marker
    index = 0
    steps = []  # Track each parsing step

    while stack:
        top = stack.pop()
        current_input = input_string[index]

        # Record current stack, input, and action
        stack_display = ''.join(stack[::-1])
        input_display = input_string[index:]

        if top in terminals:
            if top == current_input:
                steps.append([stack_display, input_display, f"Match: {top}"])
                index += 1
            else:
                steps.append([stack_display, input_display, "Error: Unexpected symbol"])
                return False, steps
        elif top == "$":
            if top == current_input:
                steps.append([stack_display, input_display, "Parsing successful!"])
                return True, steps
            else:
                steps.append([stack_display, input_display, "Error: Stack empty but input remains"])
                return False, steps
        else:
            production = parsing_table[top].get(current_input)
            if production:
                steps.append([stack_display, input_display, f"Output: {top} -> {production}"])
                for symbol in reversed(production.split()):
                    if symbol != "ε":
                        stack.append(symbol)
            else:
                steps.append([stack_display, input_display, "Error: No rule in parsing table"])
                return False, steps

    steps.append(["", "", "Error: Input not fully parsed"])
    return False, steps

# Test the predictive parser with an input string
input_string = "( id + id )"
accepted, trace_steps = predictive_parse(input_string)

# Display the parsing steps in a table
# print("\nParsing Steps:")
# headers = ["Stack", "Input", "Action"]
# print(tabulate(trace_steps, headers=headers, tablefmt="grid"))

# Final result
if accepted:
    print("The input string is accepted by the grammar.")
else:
    print("The input string is not accepted by the grammar.")
