import os
from component import Cell, Move

def calculate_move():
    #Start DLV with facts.txt and rules.txt
    result = os.popen("dlv.exe facts.txt rules.txt --no-facts --silent").read().split()
    file = open("result.txt", "w")
    for line in result:
        if line.startswith("{"):
            line = line.replace("{", "")
        
        elif line.endswith("}"):
            line = line.replace("}", "")

        if line.endswith(","):  
            line = line.replace(",", "")

        if line.startswith("move"):
            file.write(line)
    file.close()

    #Read result.txt
    file = open("result.txt", "r")
    moves = list()
    for line in file:
        move = Move(0, 0)
        line = line.replace("move(", "")
        line = line.replace(").", "")
        line = line.replace(" ", "")
        line = line.split(",")
        print(line)
        

    file.close()
    

    
        
        
    