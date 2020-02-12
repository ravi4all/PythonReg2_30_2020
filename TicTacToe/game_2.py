import random

combinations = [[1,2,3],[4,5,6],[7,8,9],
                [1,4,7],[2,5,8],[3,6,9],
                [1,5,9],[3,5,7]]

occupied = []
positions = [1,2,3,4,5,6,7,8,9]

def gameBoard():
    print("""
      {}  |  {}  |  {}
    -----|-----|------
      {}  |  {}  |  {}  
    -----|-----|------
      {}  |  {}  |  {}
    """.format(positions[0],positions[1],positions[2],
                positions[3],positions[4],positions[5],
                positions[6],positions[7],positions[8]))

def checkWinner(pos,ch):
    for i in range(len(combinations)):
        if pos in combinations[i]:
            index = combinations[i].index(pos)
            combinations[i][index] = ch

    print(combinations)

    for i in range(len(combinations)):
        if combinations[i][0] == ch and combinations[i][1] == ch and combinations[i][2] == ch:
            return "win"

def userMoves(ch):
    pos = int(input("Enter the position : "))
    positions[pos - 1] = ch
    occupied.append(pos - 1)
    gameBoard()
    win = checkWinner(pos,ch)
    return win

def cpuMoves(cpu_ch):
    while True:
        if len(occupied) < 8:
            cpu_pos = random.randint(0, 8)
            if cpu_pos in occupied:
                print("Position Already Occupied...")
            else:
                print("CPU Moved at",cpu_pos+1)
                positions[cpu_pos] = cpu_ch
                occupied.append(cpu_pos)
                break
        else:
            break
    gameBoard()
    win = checkWinner(cpu_pos+1,cpu_ch)
    return win

def main():
    print("Welcome to Tic Tac Toe".center(40,"*"))
    gameBoard()
    ch = input("Please Enter a choice : X or 0 : ")
    print("You have picked :",ch)
    if ch == "X" or ch == "x":
        cpu_ch = 0
    else: cpu_ch = "X"
    while True:
        result = userMoves(ch)
        if result == "win":
            print("User win")
            break

        result = cpuMoves(cpu_ch)
        if result == "win":
            print("CPU Win")
            break

main()