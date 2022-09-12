from typing import Any
from pip import main


def simpleTextEditor(self, operations):
    resArr = []

    string = ""

    stack = [] # used to tell the most recent command

    remove = 0

    for i in range(len(operations)):
        # if "string" placed here, a new string would always be produced, hence it wont work.
        if "INSERT" in operations[i]:
            x = operations[i].split(" ")
            string += x[1]
            resArr.append(string)
            stack.append(0) # zero means INSERT was last
            remove = len(x[1])
        
        if "BACKSPACE" in operations[i]:
            newString = string[:-1]
            resArr.append(newString)
            stack.append(1) # one means BACKSPACE was last
        
        if "UNDO" in operations[i]:
            if stack and stack[-1] == 1: # if the last command was BACKSPACE
                resArr.append(string)
            elif stack and stack[-1] == 0: # if the last command was INSERT
                resArr.append(string[:-remove])

                
            


    # the string is not staying current, it is updating to much, when we want it to not change and just add on
        
    print(resArr)       


# text editor is a type of computer program that allows users to edit plain text.
# Your task is to simulate a simplified text editor which can handle three types of operations:
# * INSERT <text> - adds <text> to the end of the current text, where <text> is a string consisting of 20 English letters at most.
# * BACKSPACE - erases the last character of the current text. If the current text is empty, this does nothing.
# * UNDO - undo the last successful INSERT or BACKSPACE operation. If there is nothing to undo, this does nothing.

inputBackspace = ["INSERT code", "INSERT signal", "BACKSPACE", "UNDO"] # CORRECT
# desired output ['code', 'codesignal', 'codesign', 'codesignal']
inputInsert = ["INSERT code", "INSERT signal", "INSERT hello", "UNDO"]
# desired output ['code', 'codesignal', 'codesignalhello', 'codesignal']
simpleTextEditor(Any, inputInsert)
