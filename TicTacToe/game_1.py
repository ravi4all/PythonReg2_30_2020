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

def main():
    print("Welcome to Tic Tac Toe".center(40,"*"))
    gameBoard()
    ch = input("Please Enter a choice : X or 0 : ")
    print("You have picked :",ch)
    if ch == "X":
        cpu_ch = 0
    else: cpu_ch = "X"
    pos = int(input("Enter the position : "))
    positions[pos-1] = ch
    gameBoard()

main()