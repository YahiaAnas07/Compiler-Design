import re
import gradio as gr

class Scanner:
    Identifiers = []
    Symbols = []
    ReservedWords = []
    Variable = ''
    FinalString = []
    string=''
    lowercaseLetters=[]
    uppercaseLetters=[]
    digits=[]
    Letters=[]
    valid=[]

    def __init__(self):
        self.Identifiers = ["int", "float", "string", "double", "bool", "char"]
        self.Symbols = ['+', '-', '*', '/', '%', '=', '>', '<', '&', '|', '!', ';', ',', '(', ')', '[', ']', '&&','||']
        self.operators = ['+', '-', '*', '/', '%', '=', '>', '<', '&&','||']
        self.ReservedWords = ['for', 'while', 'if', 'do', 'return', 'break', 'continue', 'end']
        self.digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.lowercaseLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.uppercaseLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.Letters=self.uppercaseLetters+self.lowercaseLetters
    def __del__(self):
        print("Destructor called, object destroyed")
        self.Identifiers = []
        self.Symbols = []
        self.ReservedWords = []
        self.Variable = ''
        self.FinalString = []
        self.string=''
        self.valid = []
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
                        print("error",i)


                    self.FinalString.append(i)
                    self.string+=f"{i} is a Variable *"

            ct=ct+1
        self.verror(result)




    def checker(self,str):
        list = str.split('\n')
        st=""
        print (type(st))
        for i in list:
            st = ''
            oldst=''
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
                        print("3lhady" ,st,oldst)
                        for k in range(j+1,len(i)):
                            if (i[k] ==' ' or i[k] in self.Symbols or i[k].isdigit() ==True or i[k] in self.Letters) and i[k]!=';' :
                                j=k
                                if i[k]==' ':
                                    break
                            else:
                                break

                        if  j+1<len(i):
                            print('checker right',i[o], i[j])
                            if  i[j+1]!=';':
                                print('error check' , st)
                        else:
                            if o+1<len(i):
                                print('error check', st)


    def verror(self,result):
        for i in range(len(result)):
            if result[i] not in self.valid and result[i] not in self.Identifiers and result[i] not in self.ReservedWords and  result[i].isdigit() ==False  :
                print('Error',result[i])

    def simicolon(self,str):
        list=str.split('\n')
        for i in list:
            if i[len(i)-1] != ';':
                print('simicolon missed')
    def IdentfiersCheck(self,str):
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
                self.string+=f"'{result[i]}' is an identifier *"

    def NumberCheck(self,str):
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

    def SymbolsCheck(self,str):
        result = []
        current = ''
        list = str.split()
        for q in range(len(list)):
            current=''
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
                self.string+=f"'{i}' is a Symbol *"
            else:
                for j in range (len(i)):
                    if i[j] in self.Symbols :
                        print(f"The Symbol '{i[j]}' is found at index {j}.")
                        self.FinalString.append(i[j])
                        self.string += f"'{i[j]}' is a Symbol *"



    def ReserverdWordCheck(self,str):
        list = str.split()
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

        # result {}
        for i in range(len(result)):
            if result[i] in self.ReservedWords:
                ct  = 0
                if result[i] == "while" or result[i] == "if":
                    swa2 = i+1
                    while swa2 < len(result) and result[swa2]!= ')':
                        if ct % 2 == 0:
                            if result[i].isdigit() == True or result[i] in self.valid: # smart isdigit()
                                ct+=1
                                continue
                            else:
                                # we must display an error here
                                print("eh da y3m fen l condition l slem")
                                break
                        else:
                            if  result[i] not in self.Symbols:
                                # display error
                                print("eh da y3m fen l condition l slem")
                                break
                            else:
                                ct+=1
                print(f"The Reserverd Word '{result[i]}' is found at index {i}.")
                self.FinalString.append(result[i])
                self.string+=f"'{result[i]}' is an Reserved Word *"


    def ArrayChecker(self,str):
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
                    xx = a.split(',')
                    ctt = 0
                    for q in xx:
                        ctt += 1
                    self.string += f"'{a}' is an Array of size {ctt}*"


    
def check_brackets(code):
    stack = []
    lines = code.split('\n')
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char in ['(', '{', '[']:
                stack.append((char, i+1, j+1))
            elif char in [')', '}', ']']:
                if not stack:
                    return f"Error: Extra closing bracket '{char}' at line {i+1}, column {j+1}"
                top = stack.pop()
                if char == ')' and top[0] != '(':
                    return f"Error: Mismatched closing bracket '{char}' at line {i+1}, column {j+1}"
                elif char == '}' and top[0] != '{':
                    return f"Error: Mismatched closing bracket '{char}' at line {i+1}, column {j+1}"
                elif char == ']' and top[0] != '[':
                    return f"Error: Mismatched closing brafcket '{char}' at line {i+1}, column {j+1}"
    if stack:
        top = stack.pop()
        return f"Error: Missing closing bracket '{top[0]}' for opening bracket at line {top[1]}, column {top[2]}"
    return "All brackets are properly opened and closed."


def scanString(Code):
    s = Scanner()
    s.VariableCheck(Code)
    s.IdentfiersCheck(Code)
    s.SymbolsCheck(Code)
    s.ReserverdWordCheck(Code)
    s.ArrayChecker(Code)
    s.NumberCheck(Code)
    #s.verror(Code)
    s.simicolon(Code)
    s.checker(Code)
    done=''
    list=[]

    list = s.string.split("*")
    for element in list:
        done += element + "\n"
    ss=s.string
    print(s.valid)
    s.FinalString.clear()
    s.valid.clear()
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




