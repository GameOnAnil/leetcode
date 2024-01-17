class Solution:
    def interpret(self, command: str) -> str:
        s = 0
        result = ''
        for i in range(0,len(command)):
            if command[i]=="G":
                s = 0
                result+="G"
                continue
            if command[i] == "(":
                s = 1
                continue
            if command[i] == 'a' or command[i] == 'l':
                s = 2
                continue
            if (command[i] == ")") and s == 1:
                result+="o"
                s=0
                continue
            if (command[i] == ")") and s == 2:
                result+="al"
                s=0
                continue
        
        return result