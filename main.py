import re
import gradio as gr

class Scanner:
    Identifiers = []
    Symbols = []
    ReservedWords = []
    Variable = ''
    FinalString = []
    string = ''
    lowercaseLetters = []
    uppercaseLetters = []
    digits = []
    Letters = []
    valid = []
    errolist = []

    def __init__(self):
        self.Identifiers = ["int", "float", "string", "double", "bool", "char"]
        self.Symbols = ['+', '-', '*', '/', '%', '=', '>', '<', '&', '|', '!', ';', ',', '(', ')', '[', ']', '&&', '||']
        self.operators = ['+', '-', '*', '/', '%', '>', '<', '&&', '||', '==', ';']
        self.ReservedWords = ['for', 'while', 'if', 'do', 'return', 'break', 'continue', 'end','switch','case']
        self.digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.lowercaseLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                                'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.uppercaseLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                                'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.Letters = self.uppercaseLetters + self.lowercaseLetters

    def __del__(self):
        print("Destructor called, object destroyed")
        self.Identifiers = []
        self.Symbols = []
        self.ReservedWords = []
        self.Variable = ''
        self.FinalString = []
        self.string = ''
        self.valid = []
        self.errolist=[]
    def VariableCheck(self, str):
        result = []
        current = ''
        list = str.split()
        new_tokens1 = []

        new_tokens2 = []
        for token in list:
            sub_tokens = token.split('=')
            for sub_token in sub_tokens:
                new_tokens2.append(sub_token)
        new_tokens3 = []
        for token in new_tokens2:
            sub_tokens = token.split(',')
            for sub_token in sub_tokens:
                new_tokens3.append(sub_token)
        new_tokens4 = []
        for token in new_tokens3:
            sub_tokens = token.split('+')
            for sub_token in sub_tokens:
                new_tokens4.append(sub_token)
        new_tokens5 = []
        for token in new_tokens4:
            sub_tokens = token.split('-')
            for sub_token in sub_tokens:
                new_tokens5.append(sub_token)
        new_tokens6 = []
        for token in new_tokens5:
            sub_tokens = token.split('*')
            for sub_token in sub_tokens:
                new_tokens6.append(sub_token)
        new_tokens7 = []
        for token in new_tokens6:
            sub_tokens = token.split('/')
            for sub_token in sub_tokens:
                new_tokens7.append(sub_token)
        new_tokens8 = []
        for token in new_tokens7:
            sub_tokens = token.split('&')
            for sub_token in sub_tokens:
                new_tokens8.append(sub_token)
        new_tokens9 = []
        for token in new_tokens8:
            sub_tokens = token.split('[')
            for sub_token in sub_tokens:
                new_tokens9.append(sub_token)
        new_tokens10 = []
        for token in new_tokens9:
            sub_tokens = token.split(']')
            for sub_token in sub_tokens:
                new_tokens10.append(sub_token)
        new_tokens11 = []
        for token in new_tokens10:
            sub_tokens = token.split('(')
            for sub_token in sub_tokens:
                new_tokens11.append(sub_token)
        new_tokens12 = []
        for token in new_tokens11:
            sub_tokens = token.split(')')
            for sub_token in sub_tokens:
                new_tokens12.append(sub_token)
        new_tokens13 = []
        for token in new_tokens12:
            sub_tokens = token.split('{')
            for sub_token in sub_tokens:
                new_tokens13.append(sub_token)
        new_tokens14 = []
        for token in new_tokens13:
            sub_tokens = token.split('}')
            for sub_token in sub_tokens:
                new_tokens14.append(sub_token)
        new_tokens15 = []
        for token in new_tokens14:
            sub_tokens = token.split('%')
            for sub_token in sub_tokens:
                new_tokens15.append(sub_token)
        new_tokens16 = []
        for token in new_tokens15:
            sub_tokens = token.split('>')
            for sub_token in sub_tokens:
                new_tokens16.append(sub_token)
        new_tokens17 = []
        for token in new_tokens16:
            sub_tokens = token.split('<')
            for sub_token in sub_tokens:
                new_tokens17.append(sub_token)

        for token in new_tokens17:
            sub_tokens = token.split(';')
            for sub_token in sub_tokens:
                new_tokens1.append(sub_token)

        list=new_tokens1

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


        flag=1
        ct=0
        for i in result:
            #check if it is declared more than one time
            if i[0] in self.Letters and i not in self.Identifiers and i not in self.ReservedWords:
                if i in self.valid:
                    if result[ct - 1] in self.Identifiers:
                        print('error repeated', i)
                        h = f"error rpeated:{i}"
                        self.errolist.append(h)

            if i[0] in self.Letters and i not in self.valid and i not in self.Identifiers and i not in self.ReservedWords:
                flag=1
                for j in range (len(i)):
                    if (i[j] in self.Letters) or (i[j]  in self.digits):
                        flag=1
                    else:
                        flag=0
                        break


                if flag==1:
                    if  (result[ct-1]in self.Identifiers):
                        self.valid.append(i)
                    else:
                        h=f'no identfier for:{i}'
                        self.errolist.append(h)


                    self.FinalString.append(i)
                    self.string+=f"{i} is a Variable *"

            ct=ct+1
        self.verror(result)



    def checker(self,str):
        list = str.split('\n')
        st=""
        print (type(st))
        ct=0;
        for i in list:
            st = ''
            oldst=''
            ct=1+ct
            for j in range(len(i)):
                if i[j].isdigit() ==False  :

                    if i[j] ==' ' or i[j]  in self.Symbols :
                        oldst =st
                        print(oldst, st)
                        st=''
                    else:
                        st = st + i[j]
                    if st in self.valid and oldst in self.Identifiers :
                        o=j
                        print( st,oldst)
                        for k in range(j+1,len(i)):
                            if (i[k] ==' ' or i[k] in self.Symbols or i[k].isdigit() ==True or i[k] in self.Letters) and i[k]!=';' :
                                j=k
                                if i[k]==' ':
                                    break
                            else:
                                break

                        if  j+1<len(i):
                            #print('checker right',i[o], i[j])
                            if  i[j+1]!=';':
                                print('error check' , st)
                                h = f"error missing simicolon in line:{ct}"
                                self.errolist.append(h)
                        else:
                            if o+1<len(i):
                                print('error check', st)
                                h =f"error missing simicolon in line:{ct}"
                                self.errolist.append(h)


    def verror(self,result):
        for i in range(len(result)):
            if result[i] not in self.valid and result[i] not in self.Identifiers and result[i] not in self.ReservedWords and  result[i].isdigit() ==False  :
                print('Error',result[i])
                h=f"{result[i]} not defined"

    def simicolon(self,str):
        list=str.split('\n')
        #works also on line with if condition
        ct=0
        l1=[]
        result=[]
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
        print("alo")
        print(result)
        for i in list:
            ct+=1
            result = []
            l1=[]
            l1 = i.split()
            flag=0
            for q in range(len(l1)):
                current = ''
                for char in l1[q]:
                    if char in '()':
                        if current:
                            result.append(current)
                            current = ''
                        result.append(char)
                    else:
                        current += char
                if current:
                    result.append(current)
            print(result)
            for q in result:
                if q in self.ReservedWords:
                    flag=1
            if len(result)==1:
                if result[0]=='}' or  result[0]=='{' :
                    flag=1

            print(flag,ct)
            if i[len(i)-1] != ';' and flag==0:
                print('simicolon missed')
                h = f" simicolonmissed in line:{ct}"
                self.errolist.append(h)


    def IdentfiersCheck(self, str):
        result = []
        current = ''
        list = str.split()
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
                self.string += f"'{result[i]}' is an identifier *"

    def NumberCheck(self, str):
        result = []
        current = ''
        list = str.split()
        new_tokens1 = []
        for token in list:
            sub_tokens = token.split(';')
            for sub_token in sub_tokens:
                new_tokens1.append(sub_token)
        new_tokens2 = []
        for token in new_tokens1:
            sub_tokens = token.split('=')
            for sub_token in sub_tokens:
                new_tokens2.append(sub_token)
        new_tokens3 = []
        for token in new_tokens2:
            sub_tokens = token.split(',')
            for sub_token in sub_tokens:
                new_tokens3.append(sub_token)
        new_tokens4 = []
        for token in new_tokens3:
            sub_tokens = token.split('+')
            for sub_token in sub_tokens:
                new_tokens4.append(sub_token)
        new_tokens5 = []
        for token in new_tokens4:
            sub_tokens = token.split('-')
            for sub_token in sub_tokens:
                new_tokens5.append(sub_token)
        new_tokens6 = []
        for token in new_tokens5:
            sub_tokens = token.split('*')
            for sub_token in sub_tokens:
                new_tokens6.append(sub_token)
        new_tokens7 = []
        for token in new_tokens6:
            sub_tokens = token.split('/')
            for sub_token in sub_tokens:
                new_tokens7.append(sub_token)
        new_tokens8 = []
        for token in new_tokens7:
            sub_tokens = token.split('&')
            for sub_token in sub_tokens:
                new_tokens8.append(sub_token)
        new_tokens9 = []
        for token in new_tokens8:
            sub_tokens = token.split('[')
            for sub_token in sub_tokens:
                new_tokens9.append(sub_token)
        new_tokens10 = []
        for token in new_tokens9:
            sub_tokens = token.split(']')
            for sub_token in sub_tokens:
                new_tokens10.append(sub_token)
        new_tokens11 = []
        for token in new_tokens10:
            sub_tokens = token.split('(')
            for sub_token in sub_tokens:
                new_tokens11.append(sub_token)
        new_tokens12 = []
        for token in new_tokens11:
            sub_tokens = token.split(')')
            for sub_token in sub_tokens:
                new_tokens12.append(sub_token)
        new_tokens13 = []
        for token in new_tokens12:
            sub_tokens = token.split('{')
            for sub_token in sub_tokens:
                new_tokens13.append(sub_token)
        new_tokens14 = []
        for token in new_tokens13:
            sub_tokens = token.split('}')
            for sub_token in sub_tokens:
                new_tokens14.append(sub_token)
        new_tokens15 = []
        for token in new_tokens14:
            sub_tokens = token.split('%')
            for sub_token in sub_tokens:
                new_tokens15.append(sub_token)
        new_tokens16 = []
        for token in new_tokens15:
            sub_tokens = token.split('>')
            for sub_token in sub_tokens:
                new_tokens16.append(sub_token)
        new_tokens17 = []
        for token in new_tokens16:
            sub_tokens = token.split('<')
            for sub_token in sub_tokens:
                new_tokens17.append(sub_token)

        list = new_tokens17

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
            if result[i].isdigit() == True:
                print(f"The Number '{result[i]}' is found at index {i}.")
                self.FinalString.append(result[i])
                self.string += f"'{result[i]}' is a Number *"

    def SymbolsCheck(self, str):
        result = []
        current = ''
        list = str.split()
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

        for i in result:
            if i in self.Symbols:
                print(f"The Symbol '{i}' is found at index {i}.")
                self.FinalString.append(i)
                self.string += f"'{i}' is a Symbol *"
            else:
                for j in range(len(i)):
                    if i[j] in self.Symbols:
                        print(f"The Symbol '{i[j]}' is found at index {j}.")
                        self.FinalString.append(i[j])
                        self.string += f"'{i[j]}' is a Symbol *"

    def ReserverdWordCheck(self, str):
        os = ''
        #do with all symbols
        for op in self.operators:
            temp_split = ""
            for part in str.split(op):
                temp_split += part + f" {op} "
            str = temp_split[:-len(op) - 2]

        print(str)


        result = []
        current = ''
        list = str.split()
        print(list)
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

        print(result)
        print("this is the list ")
        print(list)
        for i in range(len(result)):
            if result[i] in self.ReservedWords:
                ct = 0
                if result[i] == "while" or result[i] == "if":
                    swa2 = i + 2
                    flag = 0
                    while swa2 < len(result) and result[swa2] != ')':

                        if ct % 2 == 0:
                            if result[swa2].isdigit() == False and result[swa2] not in self.valid:  # smart isdigit()

                                print("eh da y3m fen l condition l slem lol")
                                h = f"Error In {result[i]} condition {result[swa2]}"
                                self.errolist.append(h)
                                print(result[swa2])
                            else:
                                ct += 1

                        else:
                            if result[swa2] not in self.operators:
                                # display error
                                h = f"Error In {result[i]} condition {result[swa2]}"
                                self.errolist.append(h)
                                print(result[swa2])
                            else:
                                ct += 1


                        swa2+=1
                        if ct>3:
                            ct=0

                    if ct % 3 != 0 and ct!=0:
                        h = f"Error In {result[i]} condition"
                        self.errolist.append(h)

                elif result[i] == "for":
                    print("a")
                    swa2 = i + 2
                    flag = 0
                    semiL=[]
                    cts=0
                    while swa2 < len(result) and result[swa2] != ')':
                        if result[swa2]==';':
                            cts+=1
                            semiL.append(swa2)
                        swa2+=1

                    print(cts)
                    if cts==2:
                        swa2=semiL[0]+1
                        while swa2 < len(result) and swa2 != semiL[1]:
                            if ct % 2 == 0:
                                if result[swa2].isdigit() == False and result[swa2] not in self.valid:  # smart isdigit()
                                    print("eh da y3m fen l condition l slem lol")
                                    h = f"Error In {result[i]} condition {result[swa2]}"
                                    self.errolist.append(h)
                                    print(result[swa2])
                                else:
                                    ct += 1

                            else:
                                if result[swa2] not in self.operators:
                                    # display error
                                    h = f"Error In {result[i]} condition {result[swa2]}"
                                    self.errolist.append(h)
                                    print(result[swa2])
                                else:
                                    ct += 1

                            swa2 += 1
                            if ct > 3:
                                ct = 0

                        if ct % 3 != 0 and ct != 0:
                            h = f"Error In {result[i]} condition"
                            self.errolist.append(h)
                    else:
                        h = f"Error In {result[i]} condition Missing semicolon"
                        self.errolist.append(h)

                print(f"The Reserverd Word '{result[i]}' is found at index {i}.")
                self.FinalString.append(result[i])
                self.string += f"'{result[i]}' is an Reserved Word *"
                    
    def ArrayChecker(self, str):
        list = str.split()
        result = []
        current = ''
        list = str.split()
        new_tokens1 = []
        for token in list:
            sub_tokens = token.split(';')
            for sub_token in sub_tokens:
                new_tokens1.append(sub_token)
        new_tokens2 = []
        for token in new_tokens1:
            sub_tokens = token.split('=')
            for sub_token in sub_tokens:
                new_tokens2.append(sub_token)
        new_tokens3 = []
        for token in new_tokens2:
            sub_tokens = token.split(',')
            for sub_token in sub_tokens:
                new_tokens3.append(sub_token)
        new_tokens4 = []
        for token in new_tokens3:
            sub_tokens = token.split('+')
            for sub_token in sub_tokens:
                new_tokens4.append(sub_token)
        new_tokens5 = []
        for token in new_tokens4:
            sub_tokens = token.split('-')
            for sub_token in sub_tokens:
                new_tokens5.append(sub_token)
        new_tokens6 = []
        for token in new_tokens5:
            sub_tokens = token.split('*')
            for sub_token in sub_tokens:
                new_tokens6.append(sub_token)
        new_tokens7 = []
        for token in new_tokens6:
            sub_tokens = token.split('/')
            for sub_token in sub_tokens:
                new_tokens7.append(sub_token)
        new_tokens8 = []
        for token in new_tokens7:
            sub_tokens = token.split('&')
            for sub_token in sub_tokens:
                new_tokens8.append(sub_token)

        new_tokens11 = []
        for token in new_tokens8:
            sub_tokens = token.split('(')
            for sub_token in sub_tokens:
                new_tokens11.append(sub_token)
        new_tokens12 = []
        for token in new_tokens11:
            sub_tokens = token.split(')')
            for sub_token in sub_tokens:
                new_tokens12.append(sub_token)
        new_tokens13 = []
        for token in new_tokens12:
            sub_tokens = token.split('{')
            for sub_token in sub_tokens:
                new_tokens13.append(sub_token)
        new_tokens14 = []
        for token in new_tokens13:
            sub_tokens = token.split('}')
            for sub_token in sub_tokens:
                new_tokens14.append(sub_token)
        new_tokens15 = []
        for token in new_tokens14:
            sub_tokens = token.split('%')
            for sub_token in sub_tokens:
                new_tokens15.append(sub_token)
        new_tokens16 = []
        for token in new_tokens15:
            sub_tokens = token.split('>')
            for sub_token in sub_tokens:
                new_tokens16.append(sub_token)
        new_tokens17 = []
        for token in new_tokens16:
            sub_tokens = token.split('<')
            for sub_token in sub_tokens:
                new_tokens17.append(sub_token)

        list = new_tokens17
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
            if i + 1 < len(result):
                if re.match(self.Variable,
                            value) and value not in self.Identifiers and value not in self.ReservedWords and result[
                    i + 1] == '[':
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
                    xx = a.split(',')
                    ctt = 0
                    for q in xx:
                        ctt += 1
                    self.string += f"'{a}' is an Array of size {ctt}*"

    def SwitchCheck(self, code):
        print("This is for the switch")
        print("__________________________________________________________________________________")
        lines = code.split('\n')
        for line_num, line in enumerate(lines, start=1):
            if 'switch' in line:
                # Extracting the variable used in the switch statement
                variable = ''
                switch_flag = False
                for char in line:
                    if char == '(':
                        switch_flag = True
                    elif char == ')':
                        break
                    elif switch_flag and char != ' ':
                        variable += char
                
                if variable:
                    # Checking if the variable is valid
                    variable_valid = False
                    for valid_var in self.valid:
                        if variable == valid_var:
                            variable_valid = True
                            break
                    
                    if not variable_valid and variable not in self.Identifiers and variable not in self.ReservedWords:
                        print(f"Error: Variable '{variable}' used in switch statement is not defined. Line {line_num}")
                        self.errolist.append(f"Error: Variable '{variable}' used in switch statement is not defined. Line {line_num}")
                else:
                    print(f"Error: Missing variable in switch statement. Line {line_num}")
                    self.errolist.append(f"Error: Missing variable in switch statement. Line {line_num}")

                # Checking for missing 'case' or 'break' statements
                if 'case' not in line:
                    print(f"Error: 'case' statement missing in switch statement. Line {line_num}")
                    self.errolist.append(f"Error: 'case' statement missing in switch statement. Line {line_num}")
                if 'break' not in line:
                    print(f"Error: 'break' statement missing in switch statement. Line {line_num}")
                    self.errolist.append(f"Error: 'break' statement missing in switch statement. Line {line_num}")



def check_brackets(code):
    stack = []
    lines = code.split('\n')
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char in ['(', '{', '[']:
                stack.append((char, i + 1, j + 1))
            elif char in [')', '}', ']']:
                if not stack:
                    return f"Error: Extra closing bracket '{char}' at line {i + 1}, column {j + 1}"
                top = stack.pop()
                if char == ')' and top[0] != '(':
                    return f"Error: Mismatched closing bracket '{char}' at line {i + 1}, column {j + 1}"
                elif char == '}' and top[0] != '{':
                    return f"Error: Mismatched closing bracket '{char}' at line {i + 1}, column {j + 1}"
                elif char == ']' and top[0] != '[':
                    return f"Error: Mismatched closing brafcket '{char}' at line {i + 1}, column {j + 1}"
    if stack:
        top = stack.pop()
        return f"Error: Missing closing bracket '{top[0]}' for opening bracket at line {top[1]}, column {top[2]}"
    return "All brackets are properly opened and closed."

def count_occurrences(code, word):
    count = 0
    word_length = len(word)
    code_length = len(code)
    i = 0
    while i < code_length:
        if code[i:i + word_length] == word:
            count += 1
            i += word_length - 1
        i += 1
    return count

def has_variable_switch(line):
    
    var = line.split('(')
    if(var[1]==')'):
        return False
    # print("THIS IS VAAAAAAAAR:")
    # print(var)
    return True

def scanString(Code):
    s = Scanner()
    s.VariableCheck(Code)
    s.IdentfiersCheck(Code)
    s.SymbolsCheck(Code)
    s.ArrayChecker(Code)
    s.NumberCheck(Code)
    s.simicolon(Code)
    s.checker(Code)
    s.ReserverdWordCheck(Code)
    # s.SwitchCheck(Code)
    
    # Initialize counters for switch, case, and break
    switch_count = 0
    case_count = 0
    break_count = 0

    # Initialize error list
    error_list = []

    # Initialize flag to check if switch has a variable
    switch_has_variable = False

    # Split the code into lines
    lines = Code.split('\n')
    
    # Iterate over each line in the code
    for line in lines:
        # Iterate over each character in the line to count occurrences
        for i in range(len(line)):
            if line[i:i + 6] == 'switch':
                switch_count += 1
                if has_variable_switch(line):
                    switch_has_variable = True
                else:
                    switch_has_variable = False
            elif line[i:i + 4] == 'case':
                case_count += 1
                temppp =""
                for j in range(i+5,len(line)):
                    if line[j] == ':':
                        break
                    temppp+=line[j]
                if temppp.isdigit() or temppp in s.valid:
                    print("good")
                else:
                    s.errolist.append("Error: not a valid thing for case")
                if line[len(line) - 1] != ':':
                    s.errolist.append("Error: missing colon for case")
                
                if not switch_has_variable:
                    h = "Error: Case statement without a preceding switch"
                    s.errolist.append(h)
            elif line[i:i + 5] == 'break':
                break_count += 1

    # Check if switch, case, and break counts are equal
    if switch_count != case_count or case_count != break_count:
        # Update error list for missing elements
        if switch_count < case_count:
            s.errolist.append("Error: Missing 'switch' statement(s)")
        if case_count < break_count:
            s.errolist.append("Error: Missing 'case' statement(s)")
        if case_count > break_count:
            s.errolist.append("Error: Missing 'break' statement(s)")

 

    
    done = ''
    list = []

    list = s.string.split("*")
    for element in list:
        done += element + "\n"
    ss = s.string
    #print(s.valid)
    s.FinalString.clear()
    s.valid.clear()
    print(s.errolist)
    s.errolist.clear()

    del s
    bracket_check_result = check_brackets(Code)
    return bracket_check_result + "\n" + done


demo = gr.Interface(
    title='MSA Compiler',
    fn=scanString,
    inputs=["code"],
    outputs=["text"],
    description='This is our Compiler Design project, showing the steps of scanning a code',
    allow_flagging='never',
    submit_btn='Scan...',
)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    demo.launch()


