import re
import gradio as gr

class Scanner:
    Identifiers = []
    Symbols = []
    ReservedWords = []
    Variable = ''
    FinalString = []
    string=''

    def __init__(self):
        self.Identifiers = ["int", "float", "string", "double", "bool", "char"] 
        self.Symbols = ['+', '-', '*', '/', '%', '=', '>', '<', '&&', '||', '!', ';', ',', '(', ')', '[', ']','{','}','#']  # Actually Don'd need this any more
        self.ReservedWords = ['for', 'while', 'if', 'do', 'return', 'break', 'continue', 'end' , 'namespace' , 'define' , 'using', 'std']
        self.Variable = r'^[A-Za-z][A-Za-z0-9]*$'

    def __del__(self):
        print("Destructor called, object destroyed")
        self.Identifiers = []
        self.Symbols = []
        self.ReservedWords = []
        self.Variable = ''
        self.FinalString = []
        self.string=''


    def VariableCheck(self, str):
        result = []
        current = ''
        # Splitting by spaces, commas, and semicolons
        tokens = re.findall(r'\w+|[,;(){}]', str)

        for token in tokens:
            if token in ',;(){}':
                result.append(token)
            else:
                # Splitting words within tokens separated by commas or semicolons
                words = token.split()
                for word in words:
                    result.append(word)

        print(result)
        for i in result:
            if re.match(self.Variable, i) and i not in self.Identifiers and i not in self.ReservedWords:
                print(f"{i} is a Variable")
                self.FinalString.append(i)
                self.string += f"{i} is a Variable *"


    def IdentfiersCheck(self,str):
        result = []
        current = ''
        list = str.split(" ")
        for q in range(len(list)):
            current = ''
            for char in list[q]:
                if char in '()':
                    if current:
                        result.append(current)
                        current = ''
                    result.append(char)
                else:
                    current += char
            if current:
                result.append(current)

        for i in range(len(result)):
            if result[i] in self.Identifiers:
                print(f"The identifier '{result[i]}' is found at index {i}.")
                self.FinalString.append(result[i])
                self.string+=f"'{result[i]}' is an identifier *"



    def SymbolsCheck(self, code):
        # Splitting by spaces, newlines, and separating symbols like [] and ;
        tokens = re.findall(r'\w+|#|[^\w\s]', code)

        for i, token in enumerate(tokens):
            if token in self.Symbols:
                print(f"The Symbol '{token}' is found at index {i}.")
                self.FinalString.append(token)
                self.string += f"'{token}' is a Symbol *"


    def ReserverdWordCheck(self,str):
        list = str.split(" ")
        result = []
        current = ''
        list = str.split(" ")
        for q in range(len(list)):
            current = ''
            for char in list[q]:
                if char in '()':
                    if current:
                        result.append(current)
                        current = ''
                    result.append(char)
                else:
                    current += char
            if current:
                result.append(current)


        for i in range(len(result)):
            if result[i] in self.ReservedWords:
                print(f"The Reserverd Word '{result[i]}' is found at index {i}.")
                self.FinalString.append(result[i])
                self.string+=f"'{result[i]}' is an Reserved Word *"


    def NamespaceCheck(self, code):
        # Pattern to identify namespaces
        pattern = r'\bnamespace\s+\w+\s*{'

        if re.search(pattern, code):
            print("Namespace found.")
            self.FinalString.append("Namespace")
            self.string += "Namespace is found *"


    def ArrayChecker(self,str):
        list = str.split(" ")
        result = []
        current = ''
        list = str.split(" ")
        for q in range(len(list)):
            current = ''
            for char in list[q]:
                if char in '[]':
                    if current:
                        result.append(current)
                        current = ''
                    result.append(char)
                else:
                    current += char
            if current:
                result.append(current)
        pos = -1
        for i, value in enumerate(result):
            if i+1 < len(result):
                if re.match(self.Variable, value) and value not in self.Identifiers and value not in self.ReservedWords and result[i + 1] == '[':
                    print(f"{result[i]} is a Array")
                    pos = i
                    a = ''
                    for w in range(pos, len(result)):
                        if result[w] != ']':
                            a += result[w]
                        elif result[w] == ']':
                            a += ']'
                            break
                    print(a)
                    self.FinalString.append(a)
                    self.string+=f"'{a}' is an Array *"

def scanString(Code):
    s = Scanner()
    test_strings = ["q", "1world", "Python3", "123abc", "AbcDEF", "lowercase", "UPPERCASE"]
    test_string1 = "int x1[] for (x while) (+ -) x2[]"
    s.VariableCheck(Code)
    s.IdentfiersCheck(Code)
    s.SymbolsCheck(Code)
    s.ReserverdWordCheck(Code)
    s.ArrayChecker(Code)
    done=''
    list=[]

    list = s.string.split("*")
    for element in list:
        done += element + "\n"
    ss=s.string
    print(s.FinalString)
    del s
    return done

demo = gr.Interface(
    title='C++ Compiler',
    fn=scanString,
    inputs=["code"],
    outputs=["text"],
    description='This is our Compiler Design project, showing the steps of scanning a code',
    allow_flagging='never',
    submit_btn='Scan...',
)

if __name__ == '__main__':
    demo.launch()
