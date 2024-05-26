import re

import gradio as gr

class memoryc:
    def __init__(self):
        self.memory = []

    def add_to_memory(self, st, tmp):
        # Convert tmp to an integer and append as a tuple
        self.memory.append((st, int(tmp)))




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
    flagSemi = 0
    memory = memoryc()
    ArrayList=[]
    arrayName=[]
    memoryArray=[]
    def __init__(self):
        self.Identifiers = ["int", "float", "string", "double", "bool", "char"]
        self.Symbols = ['+', '-', '*', '/', '%', '=', '>', '<', '&', '|', '!', ';', ',', '(', ')', '[', ']', '&&', '||']
        self.operators = ['+', '-', '*', '/', '%', '>=', '<=', '&&', '||', '==', ';', '<', '>']
        self.ReservedWords = ['for', 'while', 'if', 'do', 'return', 'break', 'continue', 'end', 'switch', 'case']
        self.digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.lowercaseLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                                 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.uppercaseLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                                 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.oper = ['+', '-', '*', '/', ';']
        self.Letters = self.uppercaseLetters + self.lowercaseLetters
        self.memory=memoryc()
        self.ArrayList=[]
        self.arrayName=[]
        self.memoryArray=[]

    def __del__(self):
        print("Destructor called, object destroyed")
        self.Identifiers = []
        self.Symbols = []
        self.ReservedWords = []
        self.Variable = ''
        self.FinalString = []
        self.string = ''
        self.valid = []
        self.errolist = []
        self.memory.memory=[]
        self.ArrayList = []
        self.arrayName = []
        self.memoryArray = []

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

        list = new_tokens1

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

        flag = 1
        ct = 0
        for i in result:
            # check if it is declared more than one time
            if i[0] in self.Letters and i not in self.Identifiers and i not in self.ReservedWords:
                if i in self.valid:
                    if result[ct - 1] in self.Identifiers:
                        print('error repeated', i)
                        h = f"error repeated:{i}"
                        self.errolist.append(h)

            if i[0] in self.Letters and i not in self.valid and i not in self.Identifiers and i not in self.ReservedWords:
                flag = 1
                for j in range(len(i)):
                    if (i[j] in self.Letters) or (i[j] in self.digits):
                        flag = 1
                    else:
                        flag = 0
                        break

                if flag == 1:
                    if (result[ct - 1] in self.Identifiers):
                        self.valid.append(i)
                    else:
                        h = f'No identifier for: {i}'
                        self.errolist.append(h)

                    self.FinalString.append(i)
                    self.string += f"{i} is a Variable *"

            ct = ct + 1
        self.verror(result)

    def checker(self, str):
        list = str.split('\n')
        st = ""
        print(type(st))
        ct = 0;
        for i in list:
            st = ''
            oldst = ''
            ct = 1 + ct
            for j in range(len(i)):
                if i[j].isdigit() == False:

                    if i[j] == ' ' or i[j] in self.Symbols:
                        oldst = st
                        print(oldst, st)
                        st = ''
                    else:
                        st = st + i[j]
                    if st in self.valid and oldst in self.Identifiers:
                        o = j
                        print(st, oldst)
                        for k in range(j + 1, len(i)):
                            if (i[k] == ' ' or i[k] in self.Symbols or i[k].isdigit() == True or i[
                                k] in self.Letters) and i[k] != ';':
                                j = k
                                if i[k] == ' ':
                                    break
                            else:
                                break

                        if j + 1 < len(i):
                            # print('checker right',i[o], i[j])
                            if i[j + 1] != ';':
                                print('error check', st)
                                h = f"ERROR Missing simicolon in line:{ct}"
                                self.errolist.append(h)
                        else:
                            if o + 1 < len(i):
                                print('error check', st)
                                h = f"ERROR Missing simicolon in line:{ct}"
                                self.errolist.append(h)

    def defineArray(self, str):
        list = str.split('\n')
        st = ""
        print(type(st))
        ct = 0;
        for i in list:
            st = ''
            oldst = ''
            ct = 1 + ct
            for j in range(len(i)):
                if i[j].isdigit() == False:

                    if i[j] == ' ' or i[j] in self.Symbols:
                        oldst = st
                        print(oldst, st)
                        st = ''
                    else:
                        st = st + i[j]
                    if st in self.valid:
                        o = j
                        print(st, oldst)

                        if j + 1 < len(i):
                            how = ''
                            who = ''
                            flagm3za = 0
                            if len(self.memoryArray)>0:
                                for zed in range(len(self.memoryArray[0])):
                                    if self.memoryArray[0][zed] != '[' and flagm3za == 0:
                                        how += self.memoryArray[0][zed]
                                        who += self.memoryArray[0][zed]
                                    else:
                                        flagm3za = 1
                                        if self.memoryArray[0][zed] != ']':
                                            who += self.memoryArray[0][zed]
                                        else:
                                            who += self.memoryArray[0][zed]
                                            break

                            print(how)
                            print(who)
                            print("er5many")
                            if i[j + 1] == '=' or (i[j + 1] == '[' and st == how):
                                st
                                tmp = ''
                                print("er5many123")
                                for k in range(j + 5, len(i)):
                                    if i[k] != ' ' and i[k] != ';' and i[k] != '[':
                                        tmp += i[k]
                                        print('define', tmp)
                                    else:
                                        print("ana gwa")
                                        if tmp in self.valid:
                                            val = 0
                                            print('define1', tmp)
                                            for l in self.memory.memory:
                                                if l[0] == tmp:
                                                    val = l[1]

                                            self.memory.add_to_memory(who, val)
                                        if tmp.isdigit() == True:
                                            print('define2', tmp)
                                            self.memory.add_to_memory(who, int(tmp))
                                        tmp = ''
                                        break

    def definemuloperatorArray(self, str):
        list = str.split('\n')
        st = ""
        print(list)
        print("ezz")
        ct = 0;
        for i in list:
            st = ''
            oldst = ''
            ct = 1 + ct
            for j in range(len(i)):
                if i[j].isdigit() == False:

                    if i[j] == ' ' or i[j] in self.Symbols:
                        oldst = st

                        st = ''
                    else:
                        st = st + i[j]
                    if st in self.valid or self.ArrayList:
                        o = j
                        print(st)
                        print("yooooooo")
                        if j + 1 < len(i):
                            print(self.memoryArray, st)
                            print("dasada")
                            model = ''
                            how = ''
                            who = ''
                            flagm3 = 0

                            for zed in range(len(self.memoryArray)):
                                if self.memoryArray[zed] != '[' and flagm3 == 0:
                                    how += self.memoryArray[zed]

                                    who += self.memoryArray[0][zed]
                                else:
                                    flagm3 = 1
                                    if self.memoryArray[0][zed] != ']':
                                        who += self.memoryArray[0][zed]
                                    else:
                                        who += self.memoryArray[0][zed]
                                        break

                            print(how)
                            if (i[j + 1] == '[' and st == how):
                                print("ana hna")
                                print(st)
                                tmp = ''
                                tot = 0
                                exp = 0;
                                flag = 0
                                op = ''
                                f = False
                                for k in range(j + 2, len(i)):

                                    if i[k] != ' ' and i[k] != ';' and i[k] not in self.Symbols:
                                        tmp += i[k]


                                    elif i[k] == ';' or i[k] == ' ' or i[k] in self.oper:

                                        print("ana gwa mul")
                                        if tmp in self.valid:
                                            val = 0
                                            print('define1', tmp)
                                            for l in self.memory.memory:
                                                if l[0] == tmp:
                                                    val = l[1]
                                                    f = True
                                            exp = val

                                        if tmp.isdigit() == True:
                                            exp = int(tmp)
                                            f = True
                                        tmp = ''
                                        if i[k] in self.oper:

                                            if op == '+':
                                                tot += exp
                                                flag = 1

                                            if op == '-':
                                                tot -= exp
                                                flag = 1

                                            if op == '*':
                                                if flag == 0:
                                                    tot = 1

                                                tot *= exp
                                                flag = 1
                                            if op == '/':
                                                if flag == 0:
                                                    tot = exp
                                                else:
                                                    tot /= exp
                                                flag = 1

                                            if f:
                                                if i[k] == '+' or i[k] == '-' or i[k] == '*' or i[k] == '/':
                                                    if flag == 0:
                                                        tot = exp
                                                    op = i[k]

                                        if i[k] == ';':

                                            if flag == 1:
                                                self.memory.add_to_memory(who, tot)
                                            break
                                        f = False
                            elif i[j + 1] == '[':
                                print("dsaasaad")
                                yahiaawe = ''

                                for qw in range(len(self.ArrayList)):
                                    if self.ArrayList[qw] != ']':
                                        yahiaawe += self.ArrayList[qw]
                                print(yahiaawe)
                                how = ''
                                for zed in range(len(yahiaawe)):
                                    if yahiaawe[zed] != '[':
                                        how += yahiaawe[zed]
                                    else:
                                        break
                                print(how)

                                yahia = []
                                new_tokens1 = []

                                for token in yahiaawe:
                                    sub_tokens = token.split('[')
                                    for sub_token in sub_tokens:
                                        new_tokens1.append(sub_token)
                                new_tokens2 = []
                                for token in new_tokens1:
                                    sub_tokens = token.split(']')
                                    for sub_token in sub_tokens:
                                        new_tokens2.append(sub_token)
                                print(new_tokens2)
                                final = []

                                for op in new_tokens2:
                                    if op.isdigit() == True:
                                        num = int(op) - 1
                                        final.append(f"{num}")
                                print(final)
                                print("nasy")
                                for qo in range(len(final)):
                                    flagmem = 0
                                    temp = st + '[' + final[qo] + ']'
                                    print(temp)

                                    for t in self.memory.memory:

                                        if temp == t[0]:
                                            flagmem = 1
                                            print("alak")
                                            break
                                    if flagmem == 0:
                                        self.memory.add_to_memory(temp, int(final[qo]) + 1)
                                        self.memoryArray.append(temp)

    def define(self, str):
        list = str.split('\n')
        st = ""
        print(type(st))
        ct = 0;
        for i in list:
            st = ''
            oldst = ''
            ct = 1 + ct
            for j in range(len(i)):
                if i[j].isdigit() == False:

                    if i[j] == ' ' or i[j] in self.Symbols:
                        oldst = st
                        print(oldst, st)
                        st = ''
                    else:
                        st = st + i[j]
                    if st in self.valid:
                        o = j
                        print(st, oldst)
                        if j + 1 < len(i):

                            if i[j + 1] == '=':
                                st
                                tmp = ''
                                for k in range(j + 2, len(i)):
                                    if i[k] != ' ' and i[k] != ';':
                                        tmp += i[k]
                                    # print('define', tmp)
                                    else:
                                        # print("ana gwa")
                                        if tmp in self.valid:
                                            val = 0
                                            # print('define1', tmp)
                                            for l in self.memory.memory:
                                                if l[0] == tmp:
                                                    val = l[1]

                                            self.memory.add_to_memory(st, val)
                                        if tmp.isdigit() == True:
                                            # print('define2', tmp)
                                            self.memory.add_to_memory(st, int(tmp))
                                        tmp = ''
                                        break

    def definemuloperator(self, str):
        list = str.split('\n')
        st = ""
        print(list)
        print("ezz")
        ct = 0;
        for i in list:
            st = ''
            oldst = ''
            ct = 1 + ct
            for j in range(len(i)):
                if i[j].isdigit() == False:

                    if i[j] == ' ' or i[j] in self.Symbols:
                        oldst = st

                        st = ''
                    else:
                        st = st + i[j]
                    if st in self.valid:
                        o = j

                        if j + 1 < len(i):

                            if i[j + 1] == '=' or (i[j + 1] == '+' and i[j + 2] == '=') or (
                                    i[j + 1] == '-' and i[j + 2] == '=') or (i[j + 1] == '*' and i[j + 2] == '=') or (
                                    i[j + 1] == '/' and i[j + 2] == '=')or (i[j + 1] == '+' and i[j + 2] == '+') or (
                                    i[j + 1] == '-' and i[j + 2] == '-')  :
                                st
                                tmp = ''
                                tot = 0
                                alama=0
                                for v in self.memory.memory:
                                    print("aly", st, v[0])
                                    if st == v[0]:
                                        print('define3', tmp)

                                        tot = v[1]
                                        alama = 1
                                        print('mwgod')


                                exp = 0
                                flag = 0
                                op = ''
                                if i[j + 1] == '+' or i[j + 1] == '-' or i[j + 1] == '*' or i[j + 1] == '/':
                                    op = i[j + 1]
                                f = False
                                for k in range(j + 2, len(i)):
                                    if i[j + 2] == '+' or i[j + 2] == '-':
                                        if i[j + 2] == '+':
                                            tot+=1
                                            self.memory.add_to_memory(st, tot)
                                        else:
                                            tot -= 1
                                            self.memory.add_to_memory(st, tot)
                                        break

                                    else:

                                        if i[k] != ' ' and i[k] != ';' and i[k] not in self.Symbols:
                                            tmp += i[k]


                                        elif i[k] == ';' or i[k] == ' ' or i[k] in self.oper:

                                            print("ana gwa mul")
                                            if tmp in self.valid:
                                                val = 0
                                                print('define1', tmp)
                                                for l in self.memory.memory:
                                                    if l[0] == tmp:
                                                        val = l[1]
                                                        f = True
                                                exp = val

                                            if tmp.isdigit() == True:
                                                exp = int(tmp)
                                                f = True

                                            if i[k] in self.oper:

                                                if op == '+':


                                                    if alama == 1:
                                                        tot +=  exp
                                                    else:
                                                        print("alaama", alama)
                                                        tot = tot + exp
                                                    flag = 1

                                                if op == '-':

                                                    if alama == 1:
                                                        tot -= exp
                                                    else:
                                                        tot -= exp
                                                    flag = 1

                                                if op == '*':
                                                    if flag == 0 and alama==0:
                                                        tot = 1

                                                    if alama == 1:
                                                        tot = tot * exp
                                                    else:
                                                        tot *= exp
                                                    flag = 1
                                                if op == '/':

                                                    if alama == 1:
                                                        if flag == 0 and alama==0:
                                                            tot = 1

                                                        else:
                                                            tot =tot / exp
                                                    else:
                                                        if flag == 0:
                                                            tot = exp
                                                        else:
                                                            tot /= exp
                                                    flag = 1

                                                if f:
                                                    if i[k] == '+' or i[k] == '-' or i[k] == '*' or i[k] == '/':
                                                        if flag == 0:
                                                            tot = exp
                                                        op = i[k]

                                            if i[k] == ';':

                                                if flag == 1:
                                                    self.memory.add_to_memory(st, tot)

                                                break
                                            tmp = ''
                                            f = False




    def verror(self, result):
        for i in range(len(result)):
            if result[i] not in self.valid and result[i] not in self.Identifiers and result[
                i] not in self.ReservedWords and result[i].isdigit() == False:
                print('Error', result[i])
                h = f"{result[i]} not defined"

    def simicolon(self, str):
        list = str.split('\n')
        # works also on line with if condition
        ct = 0
        l1 = []
        result = []
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
            ct += 1
            result = []
            l1 = []
            l1 = i.split()
            flag = 0
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
            if self.flagSemi == 0:

                for q in result:
                    if q in self.ReservedWords:
                        flag = 1

            if len(result) == 1:
                if result[0] == '}' or result[0] == '{':
                    flag = 1
            print(flag, ct, '/////////////', i)
            if len(i) != 0:
                print(len(i) - 1)
                if i[len(i) - 1] != ';' and flag == 0:
                    print('simicolon missed')
                    h = f" ERROR Semicolon missing in line:{ct}"
                    self.errolist.append(h)
        self.flagSemi = 0

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
        # do with all symbols
        for op in self.operators:
            temp_split = ""
            flag = 0
            i = 0
            for part in str.split(op):
                if part == '>=' or part == ' <= ':
                    flag = 1

                temp_split += part + f" {op} "
                print(temp_split)

            str = temp_split[:-len(op) - 2]
            if flag == 1:
                break
            print(temp_split[:-len(op) - 2])
            if flag == 2:
                break

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
                        print(ct, result[swa2])

                        if ct % 2 == 0:

                            if result[swa2].isdigit() == False and result[swa2] not in self.valid:  # smart isdigit()

                                print("eh da y3m fen l condition l slem lol")
                                h = f"Error in {result[i]} condition -> {result[swa2]}"
                                self.errolist.append(h)
                                print("kod", result[swa2], ct)
                            else:
                                ct += 1

                        else:
                            if result[swa2] not in self.operators:
                                # display error
                                h = f"Error In {result[i]} condition -> {result[swa2]}"
                                self.errolist.append(h)
                                print('oo', result[swa2])
                            else:
                                ct += 1

                        swa2 += 1
                        if ct > 3:
                            ct = 0

                    if ct % 3 != 0 and ct != 0:
                        h = f"Error In {result[i]} condition"
                        self.errolist.append(h)

                elif result[i] == "for":
                    print("a")
                    swa2 = i + 2
                    flag = 0
                    semiL = []
                    cts = 0
                    sty=''
                    while swa2 < len(result) and result[swa2] != ')':
                        sty+=result[swa2]
                        if result[swa2] == ';':
                            cts += 1
                            semiL.append(swa2)
                        swa2 += 1

                    end=swa2
                    q1=semiL[0]
                    q2=semiL[1]
                    print(cts)
                    if cts == 2:
                        swa2 = semiL[0] + 1
                        while swa2 < len(result) and swa2 != semiL[1]:
                            if ct % 2 == 0:
                                if result[swa2].isdigit() == False and result[
                                    swa2] not in self.valid:  # smart isdigit()
                                    print("eh da y3m fen l condition l slem lol")
                                    h = f"Error in {result[i]} condition -> {result[swa2]}"
                                    self.errolist.append(h)
                                    print(result[swa2])
                                else:
                                    ct += 1

                            else:
                                if result[swa2] not in self.operators:
                                    # display error
                                    h = f"error In {result[i]} condition -> {result[swa2]}"
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
                        h = f"Error In {result[i]} condition -> missing semicolon"
                        self.errolist.append(h)
                    if self.errolist==[]:
                        value=[]
                        value=result[q1-1].split('=')
                        val=value[1]
                        limit=result[q2-1]
                        loop=int(limit)-int(val)
                        print(loop,val,limit)
                        f=end
                        tss=[]

                        while result[f] != '}':
                            f+=1
                            tss.append(result[f])
                        tss.pop(0)
                        tss.pop(-1)
                        stg = "".join(tss)

                        print(stg)
                        for fa in range(int(val), int(limit)-1):
                            self.definemuloperator(sty)
                            self.definemuloperator(stg)






                elif result[i] == "do":
                    self.flagSemi = 1

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


        new_tokens4 = []
        for token in new_tokens2:
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
                    print(xx)
                    print("how")
                    how=''
                    for zed in range (len(xx[0])):
                        if xx[0][zed]!='[':
                            how+=xx[0][zed]
                        else:
                            break

                    print(how)
                    if how not in self.arrayName:
                        for q in xx:
                            ctt += 1
                        self.string += f"'{a}' is an Array of size {ctt}*"
                        self.ArrayList.append(a)
                        self.arrayName.append(how)
                    else:
                        print("ma")



    def check_brackets(self,code):
        stack = []
        lines = code.split('\n')
        for i, line in enumerate(lines):
            for j, char in enumerate(line):
                if char in ['(', '{', '[']:
                    stack.append((char, i + 1, j + 1))
                elif char in [')', '}', ']']:
                    if not stack:
                        self.errolist.append(f"Error: Extra closing bracket '{char}' at line {i + 1}, column {j + 1}")
                    top = stack.pop()
                    if char == ')' and top[0] != '(':
                        self.errolist.append( f"Error: Mismatched closing bracket '{char}' at line {i + 1}, column {j + 1}")
                    elif char == '}' and top[0] != '{':
                        self.errolist.append( f"Error: Mismatched closing bracket '{char}' at line {i + 1}, column {j + 1}")
                    elif char == ']' and top[0] != '[':
                        self.errolist.append( f"Error: Mismatched closing brafcket '{char}' at line {i + 1}, column {j + 1}")
        if stack:
            top = stack.pop()
            self.errolist.append( f"Error: Missing closing bracket '{top[0]}' for opening bracket at line {top[1]}, column {top[2]}")

    def SwitchCheck(self, code):
        print("This is for the switch")
        print("__________________________________________________________________________________")
        lines = code.split('\n')
        for line_num, line in enumerate(lines, start=1):
            if 'switch' in line:
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
                    variable_valid = False
                    for valid_var in self.valid:
                        if variable == valid_var:
                            variable_valid = True
                            break

                    if not variable_valid and variable not in self.Identifiers and variable not in self.ReservedWords:
                        print(f"ERROR: Variable '{variable}' used in switch statement is not defined. Line {line_num}")
                        self.errolist.append(
                            f"Error: Variable '{variable}' used in switch statement is not defined. Line {line_num}")
                else:
                    print(f"ERROR: Missing variable in switch statement. Line {line_num}")
                    self.errolist.append(f"Error: Missing variable in switch statement. Line {line_num}")

                if 'case' not in line:
                    print(f"ERROR: 'case' statement missing in switch statement. Line {line_num}")
                    self.errolist.append(f"Error: 'case' statement missing in switch statement. Line {line_num}")
                if 'break' not in line:
                    print(f"ERROR: 'break' statement missing in switch statement. Line {line_num}")
                    self.errolist.append(f"Error: 'break' statement missing in switch statement. Line {line_num}")





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
    if (var[1] == ')'):
        return False
    # print("THIS IS VAAAAAAAAR:")
    # print(var)
    return True


def scanString(Code):
    s = Scanner()
    s.check_brackets(Code)
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
                temppp = ""
                for j in range(i + 5, len(line)):
                    if line[j] == ':':
                        break
                    temppp += line[j]
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
    table = "<table><tr><th>Type</th><th>Name</th><th>Value</th></tr>"
    for name, value in s.memory.memory:
        table += "<tr><td>int</td><td>{}</td><td>{}</td></tr>".format(name, value)
    table += "</table>"

    list = s.string.split("*")
    for element in list:
        done += element + "\n"
    ss = s.string
    # print(s.valid)
    s.FinalString.clear()
    s.valid.clear()
    error_list = s.errolist
    print(s.errolist, "helloooo")
    errStmt = ""
    for err in error_list:
        errStmt += err + '\n'
    s.errolist.clear()

    # print(s.errolist)
    print(s.memory.memory)
    s.memory.memory.clear()
    s.ArrayList.clear()
    s.errolist.clear()
    s.arrayName.clear()
    s.arrayName.clear()
    s.memoryArray.clear()

    del s

    return (""), errStmt,table


with gr.Blocks() as demo:
    title = 'MSA Compiler',
    description = 'This is our Compiler Design project, showing the steps of scanning a code',
    allow_flagging = 'never',
    with gr.Row():
        Code = gr.Code(label="Code")
        Output = gr.Text(label="Code Explanation")
    with gr.Row():
        # variableDf = gr.Dataframe(label="Memory")
        errorList = gr.Text(label="Error List")
    with gr.Row():
        button = gr.Button("Scan...", variant="primary")
        clear = gr.Button("Clear")
    with gr.Row():
        table = gr.HTML(label="Memory Table")
    button.click(scanString, Code, [Output, errorList,table])

demo.launch()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    demo.launch()
