import os

pointer = 50 #Starting pointer
sumTurns = 0 #Number of times the pointer reach 0

#Function to check the position after de command
def checkPosition(number):
    if number <= 0:
        turn = 1
        turn += abs(number) // 100           
        position = (100 - abs(number)) % 100
        return position, turn
    if 0 < number <= 99:
        turn = 0
        position = number
        return position, turn
    if number > 99:
        turn = 1        
        turn += abs(number - 100) // 100 
        position = abs(number - 100) % 100
        return position, turn

#Function to update the safe pointer and update the sumTurns
def password(command):
    side = command[:1]
    number = command[1:]
    global pointer
    global sumTurns

    if side == 'L':
        pointerInit = pointer   
        pointer = pointer - int(number)
        pointer, turn = checkPosition(pointer)
        #When the initial position is 0 and the command if for the left, it decreases 1 from the turn to not count 2 times
        if pointerInit == 0:
            turn -= 1
    if side == 'R':
        pointer = pointer + int(number)
        pointer, turn = checkPosition(pointer)
    
    #Sums the turns
    sumTurns += turn

#Read the file with the commands and apply the function
os.chdir(r'C:\Users\rapha\Documents\VsCode Files\Advent of Code\2025\Day 1')
with open('commands.txt') as f:
    commandList = f.read()
    current = ""

    for ch in commandList:
        if ch == "\n":
            password(current)
            current = ''
        else:
            current += ch

#Answer
print(f'The safe password is: {sumTurns}')