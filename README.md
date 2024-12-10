# Predictive Parsing ReadMe

## Overview

This project implements a **Predictive Parser** for a given context-free grammar using FIRST and FOLLOW sets and a parsing table. The parser reads an input string and validates whether it belongs to the defined grammar. It displays the parsing steps and actions in a tabular format.

---

## Grammar Definition

The grammar used in this parser is:

- **E → T E'**  
- **E' → + T E' | ε**  
- **T → F T'**  
- **T' → * F T' | ε**  
- **F → ( E ) | id**

### Terminals
`+`, `*`, `(`, `)`, `id`, `$` (end-of-input marker)

### Non-Terminals
`E`, `E'`, `T`, `T'`, `F`

---

## Features

1. **Parsing Table Construction**  
   A parsing table is generated dynamically based on the grammar, FIRST, and FOLLOW sets.

2. **Predictive Parsing**  
   The parser uses a stack-based approach to process the input string.

3. **Traceability**  
   Parsing steps are displayed in a tabular format for better understanding.

4. **Error Handling**  
   Handles unexpected symbols and missing rules gracefully.

---

## Usage Instructions

### Prerequisites
Ensure Python is installed on your system and the `tabulate` library is available. Install `tabulate` using:
```bash
pip install tabulate
```

### Steps to Run

1. Save the script to a file, e.g., `predictive_parser.py`.
2. Modify the `input_string` variable with the desired input.
3. Run the script:
   ```bash
   python predictive_parser.py
   ```
4. View the parsing table and steps in the terminal output.

---

## Example Input and Output

### Input String
```python
input_string = "( id + id )"
```

### Parsing Table Output
The program prints the parsing table in a grid format.

### Parsing Steps
The parser traces each step:
- Stack contents
- Remaining input string
- Performed action

---

## Code Structure

### Modules and Functions

1. **Grammar and Parsing Table Initialization**  
   - Defines the grammar, terminals, non-terminals, FIRST, and FOLLOW sets.
   - Generates the parsing table based on these definitions.

2. **Predictive Parser**  
   - Implements the `predictive_parse` function to process the input using the parsing table.

3. **Output and Visualization**  
   - Displays the parsing table and step-by-step parsing process in a readable tabular format.

---

## Key Highlights

1. **FIRST and FOLLOW Sets**  
   Used to determine which production to apply during parsing.

2. **Epsilon (ε) Handling**  
   Epsilon productions are added to the parsing table based on FOLLOW sets.

3. **Error Detection**  
   Identifies and reports mismatches or missing rules in the parsing table.

---

## Extending the Code

1. **Modify Grammar**  
   Update the `grammar`, `FIRST`, and `FOLLOW` definitions for new rules.

2. **Error Recovery**  
   Add strategies to skip or correct invalid tokens.

3. **Advanced Visualizations**  
   Enhance output with graphical representations of parsing trees.

---

## Sample Results

### Parsing Steps
```
+----------------+------------+-------------------------------+
| Stack          | Input      | Action                        |
+----------------+------------+-------------------------------+
| $E             | ( id + id )$ | Output: E -> T E'           |
| $E'T           | ( id + id )$ | Output: T -> F T'           |
| $E'T'F         | ( id + id )$ | Output: F -> ( E )          |
| ...            | ...        | ...                           |
|                |            | Parsing successful!          |
+----------------+------------+-------------------------------+
```

### Final Output
```
The input string is accepted by the grammar.
```

---

## License
This project is open-source and available for educational purposes.
