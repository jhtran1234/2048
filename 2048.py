#Jason Lee
#Jeffrey Tran
#Period 8
import random
import turtle

points = 0
first = True
counter = 0
board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
value_decide = random.randint(1,4)
if value_decide == 4:
    board[random.randint(0,3)][random.randint(0,3)] = 4
else:
    board[random.randint(0,3)][random.randint(0,3)] = 2
while True:
    i = random.randint(0,3)
    j = random.randint(0,3)
    if board[i][j] == 0:
        value_decide = random.randint(1,4)
        if value_decide == 4:
            board[i][j] = 4
        else:
            board[i][j] = 2
        break

def up_movement(board):
    """Moves all the pieces on the board up."""
    i = 0
    for j in range(0,4):
        if (board[i][j] != 0) or (board[i+1][j] != 0) or (board[i+2][j] != 0) or (board[i+3][j] != 0):
            if board[i][j] == 0:
                while board[i][j] == 0:
                    board[i][j] = board[i+1][j]
                    board[i+1][j] = board[i+2][j]
                    board[i+2][j] = board[i+3][j]
                    board[i+3][j] = 0
            if (board[i+1][j] == 0) and ((board[i+2][j] != 0) or (board[i+3][j] != 0)):
                while board[i+1][j] == 0:
                    board[i+1][j] = board[i+2][j]
                    board[i+2][j] = board[i+3][j]
                    board[i+3][j] = 0
            if (board[i+2][j] == 0) and (board[i+3][j] != 0):
                while board[i+2] == 0:
                    board[i+2][j] = board[i+3][j]
                    board[i+3][j] = 0

def up_addition(board):
    """After shifting up, this function combines all like pieces."""
    i = 0
    global points
    for j in range(0,4):
        if board[i][j] == board[i+1][j]:
            board[i][j] = board[i][j] + board[i+1][j]
            points += board[i][j]
            board[i+1][j] = board[i+2][j]
            board[i+2][j] = board[i+3][j]
            board[i+3][j] = 0
        if board[i+1][j] == board[i+2][j]:
            board[i+1][j] = board[i+1][j] + board[i+2][j]
            points += board[i+1][j]
            board[i+2][j] = board[i+3][j]
            board[i+3][j] = 0
        if board[i+2][j] == board[i+3][j]:
            board[i+2][j] = board[i+2][j] + board[i+3][j]
            points += board[i+2][j]
            board[i+3][j] = 0

def down_movement(board):
    """Moves all the pieces on the board down."""
    i = 0
    for j in range(0,4):
        if (board[i][j] != 0) or (board[i+1][j] != 0) or (board[i+2][j] != 0) or (board[i+3][j] != 0):
            if board[i+3][j] == 0:
                while board[i+3][j] == 0:
                    board[i+3][j] = board[i+2][j]
                    board[i+2][j] = board[i+1][j]
                    board[i+1][j] = board[i][j]
                    board[i][j] = 0
            if (board[i+2][j] == 0) and ((board[i+1][j] != 0) or (board[i][j] != 0)):
                while board[i+2][j] == 0:
                    board[i+2][j] = board[i+1][j]
                    board[i+1][j] = board[i][j]
                    board[i][j] = 0
            if (board[i+1][j] == 0) and (board[i][j] != 0):
                while board[i+1][j] == 0:
                    board[i+1][j] = board[i][j]
                    board[i][j] = 0

def down_addition(board):
    """After shifting down, this function combines all like pieces."""
    i = 0
    global points
    for j in range(0,4):
        if board[i+3][j] == board[i+2][j]:
            board[i+3][j] = board[i+3][j] + board[i+2][j]
            points += board[i+3][j]
            board[i+2][j] = board[i+1][j]
            board[i+1][j] = board[i][j]
            board[i][j] = 0
        if board[i+2][j] == board[i+1][j]:
            board[i+2][j] = board[i+2][j] + board[i+1][j]
            points += board[i+2][j]
            board[i+1][j] = board[i][j]
            board[i][j] = 0
        if board[i+1][j] == board[i][j]:
            board[i+1][j] = board[i+1][j] + board[i][j]
            points += board[i+1][j]
            board[i][j] = 0

def left_movement(board):
    """Moves all the pieces on the board left."""
    j = 0
    for i in range(0,4):
        if (board[i][j] != 0) or (board[i][j+1] != 0) or (board[i][j+2] != 0) or (board[i][j+3] != 0):
            if board[i][j] == 0:
                while board[i][j] == 0:
                    board[i][j] = board[i][j+1]
                    board[i][j+1] = board[i][j+2]
                    board[i][j+2] = board[i][j+3]
                    board[i][j+3] = 0
            if (board[i][j+1] == 0) and ((board[i][j+2] != 0) or (board[i][j+3] != 0)):
                while board[i][j+1] == 0:
                    board[i][j+1] = board[i][j+2]
                    board[i][j+2] = board[i][j+3]
                    board[i][j+3] = 0
            if (board[i][j+2] == 0) and (board[i][j+3] != 0):
                while board[i][j+2] == 0:
                    board[i][j+2] = board[i][j+3]
                    board[i][j+3] = 0

def left_addition(board):
    """After shifting left, this function combines all like pieces."""
    j = 0
    global points
    for i in range(0,4):
        if board[i][j] == board[i][j+1]:
            board[i][j] = board[i][j] + board[i][j+1]
            points += board[i][j]
            board[i][j+1] = board[i][j+2]
            board[i][j+2] = board[i][j+3]
            board[i][j+3] = 0
        if board[i][j+1] == board[i][j+2]:
            board[i][j+1] = board[i][j+1] + board[i][j+2]
            points += board[i][j+1]
            board[i][j+2] = board[i][j+3]
            board[i][j+3] = 0
        if board[i][j+2] == board[i][j+3]:
            board[i][j+2] = board[i][j+2] + board[i][j+3]
            points += board[i][j+2]
            board[i][j+3] = 0

def right_movement(board):
    """Moves all the pieces on the board right."""
    j = 0
    for i in range(0,4):
        if (board[i][j] != 0) or (board[i][j+1] != 0) or (board[i][j+2] != 0) or (board[i][j+3] != 0):
            if board[i][j+3] == 0:
                while board[i][j+3] == 0:
                    board[i][j+3] = board[i][j+2]
                    board[i][j+2] = board[i][j+1]
                    board[i][j+1] = board[i][j]
                    board[i][j] = 0
            if (board[i][j+2] == 0) and ((board[i][j+1] != 0) or (board[i][j] != 0)):
                while board[i][j+2] == 0:
                    board[i][j+2] = board[i][j+1]
                    board[i][j+1] = board[i][j]
                    board[i][j] = 0
            if (board[i][j+1] == 0) and (board[i][j] != 0):
                while board[i][j+1] == 0:
                    board[i][j+1] = board[i][j]
                    board[i][j] = 0

def right_addition(board):
    """After shifting right, this function combines all like pieces."""
    j = 0
    global points
    for i in range(0,4):
        if board[i][j+3] == board[i][j+2]:
            board[i][j+3] = board[i][j+3] + board[i][j+2]
            points += board[i][j+3]
            board[i][j+2] = board[i][j+1]
            board[i][j+1] = board[i][j]
            board[i][j] = 0
        if board[i][j+2] == board[i][j+1]:
            board[i][j+2] = board[i][j+2] + board[i][j+1]
            points += board[i][j+2]
            board[i][j+1] = board[i][j]
            board[i][j] = 0
        if board[i][j+1] == board[i][j]:
            board[i][j+1] = board[i][j+1] + board[i][j]
            points += board[i][j+1]
            board[i][j] = 0

#Gameplay begins
print("2048 is a game that uses the arrow keys to move and combine the pieces on the board.")
print("The pieces of the board are represented by a numerical amount.")
print("When two of the same pieces are combined, they merge into a piece double their amount.")
print("The entire goal of the game is to create the “2048” tile.")
print("To start the game, random tiles are placed randomly in a 4x4 grid. (They can be either “2” or “4”)")
print("You then use the w (up), a (left), s (down), d (right) keys to move the tiles and combine them.")
print("Random “2” or “4” tiles are spawned after every move.")
print("The game ends when the player gets the “2048” tile, which results in a win,")
print("Or the grid fills up with no more possible moves, which results in a loss.")
screen = turtle.Screen()
griddy = turtle.Turtle()
griddy.speed(0)
for n in range(5):
    griddy.up()
    griddy.goto(-200, -100*n+200)
    griddy.down()
    griddy.forward(400)
griddy.right(90)
for n in range(5):
    griddy.up()
    griddy.goto(100*n-200, 200)
    griddy.down()
    griddy.forward(400)
griddy.hideturtle()
griddy.up()
while True:
    print ("Points: " + str(points))
    print ("\n\n")
    if first == True:
        first = False
    else:
        for n in range(2 * counter):
            griddy.undo()
    counter = 0
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                counter += 1
                griddy.goto(100*j-150, -100*i+137)
                griddy.write(board[i][j], True, align = "center", font = ("Arial", 16, "normal"))
    movement_choice = input("Make your move:").lower()
    while (movement_choice != "w") and (movement_choice != "a") and (movement_choice != "s") and (movement_choice != "d"):        
        print ("Please enter one of the following: w, a, s, or d.")
        movement_choice = input("Make your move:").lower()
    if movement_choice == "w":
        up_movement(board)
        up_addition(board)
    elif movement_choice == "s":
        down_movement(board)
        down_addition(board)
    elif movement_choice == "a":
        left_movement(board)
        left_addition(board)
    else:
        right_movement(board)
        right_addition(board)
    row_zero = []
    column_zero = []
    for i in range(0,4):
        for j in range(0,4):
            if board[i][j] == 0:
                row_zero.append(i)
                column_zero.append(j)
            if board[i][j] == 2048:
                print ("Congratulations! You have reached 2048!")
                break
    value_decide = random.randint(1,4)
    if len(row_zero) > 1:
        rand_index = random.randint(1, len(row_zero))
        row_entry = row_zero[rand_index - 1]
        column_entry = column_zero[rand_index - 1]
        if value_decide == 4:
            board[row_entry][column_entry] = 4
        else:
            board[row_entry][column_entry] = 2
    elif len(row_zero) == 1:
        row_entry = row_zero[0]
        column_entry = column_zero[0]
        if value_decide == 4:
            board[row_entry][column_entry] = 4
        else:
            board[row_entry][column_entry] = 2
    else:
        break

print ("Game is finished! Your score is " + str(points))
