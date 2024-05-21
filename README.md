# MSA Compiler Project

## Description
This project is a compiler developed using Python and Gradio. It processes input code to perform lexical analysis, syntax checking, and basic semantic analysis. It identifies variables, reserved words, and symbols, handles array definitions and operators, and checks for common errors such as missing semicolons and invalid case statements in switch-case structures.

## Features
- **Lexical Analysis**: Identifies and classifies tokens (variables, reserved words, symbols).
- **Syntax Checking**: Ensures code follows the correct syntax, including proper semicolon usage and valid switch-case constructs.
- **Semantic Analysis**: Handles multiple operators and array definitions, ensuring correct assignment and operations.
- **Error Reporting**: Detects and reports errors such as repeated variable declarations, missing semicolons, and improper switch-case statements.

## Setup Instructions
1. **Clone the Repository**:
    ```sh
    git clone https://github.com/yourusername/msa-compiler.git
    cd msa-compiler
    ```
2. **Install Dependencies**:
    Make sure you have Python installed, then install the required packages:
    ```sh
    pip install gradio
    ```

## Usage
1. **Run the Compiler**:
    ```sh
    python main.py
    ```
2. **Use the Gradio Interface**:
    - Input your code in the provided text area.
    - Click the "Scan..." button to process the code.
    - View the output for code explanation and any error messages.

## Code Structure
- `main.py`: Contains the main logic for the compiler and Gradio interface.
- `Scanner.py`: Includes the `Scanner` class with methods for lexical analysis, syntax checking, and error reporting.
- `memoryc.py`: Defines the `memoryc` class for handling memory operations.

## Example
Here is an example of how to use the scanner:
```python
import gradio as gr

# Define the scanning function
def scanString(Code):
    s = Scanner()
    # Perform various checks
    s.VariableCheck(Code)
    s.IdentfiersCheck(Code)
    s.SymbolsCheck(Code)
    s.ArrayChecker(Code)
    s.NumberCheck(Code)
    s.simicolon(Code)
    s.checker(Code)
    s.definemuloperatorArray(Code)
    s.defineArray(Code)
    s.define(Code)
    s.definemuloperator(Code)
    s.ReserverdWordCheck(Code)

    # Check for switch-case errors
    switch_count, case_count, break_count = 0, 0, 0
    lines = Code.split('\n')
    for line in lines:
        if 'switch' in line:
            switch_count += 1
        elif 'case' in line:
            case_count += 1
        elif 'break' in line:
            break_count += 1

    if switch_count != case_count or case_count != break_count:
        if switch_count < case_count:
            s.errolist.append("Error: Missing 'switch' statement(s)")
        if case_count < break_count:
            s.errolist.append("Error: Missing 'case' statement(s)")
        if case_count > break_count:
            s.errolist.append("Error: Missing 'break' statement(s)")

    done, error_list = '', s.errolist
    for element in s.string.split("*"):
        done += element + "\n"
    errorStmt = '\n'.join(error_list)
    s.errolist.clear()

    return done, errorStmt

# Define the Gradio interface
with gr.Blocks() as demo:
    title = 'MSA Compiler'
    description = 'This is our Compiler Design project, showing the steps of scanning a code'
    allow_flagging = 'never'
    
    with gr.Row():
        Code = gr.Code(label="Code")
        Output = gr.Text(label="Code Explanation")
    
    with gr.Row():
        errorList = gr.Text(label="Error List")
    
    with gr.Row():
        button = gr.Button("Scan...", variant="primary")
        clear = gr.Button("Clear")
    
    button.click(scanString, Code, [Output, errorList])

demo.launch()

# Entry point
if __name__ == '__main__':
    demo.launch()
```
## License
This project is licensed under the [MIT License](LICENSE).

## Author
- Yahia Mohamed Anas
- Seifeldin Amr
- Ahmed Abdelmoneim
- Aly Essam
