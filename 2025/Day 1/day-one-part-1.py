import os

pointer = 50 #Starting pointer
sumTurns = 0 #Number of times the pointer reach 0

#Function to check the position after de command
def checkPosition(number):
    if number < 0:                   
        position = (100 - abs(number)) % 100
        return position
    if 0 <= number <= 99:
        position = number
        return position
    if number > 99:
        position = abs(number - 100) % 100
        return position

#Function to update the safe pointer and update the sumTurns
def password(command):
    side = command[:1]
    number = command[1:]
    global pointer
    global sumTurns

    if side == 'L':
        pointer = pointer - int(number)
        pointer = checkPosition(pointer)
    if side == 'R':
        pointer = pointer + int(number)
        pointer = checkPosition(pointer)
    
    #If the pointer is 0, add to the sumTurns
    if pointer == 0:
            sumTurns += 1

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