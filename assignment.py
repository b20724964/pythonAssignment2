import sys
f = open(sys.argv[1], "r")
command = [i.split() for i in f.readlines()]
f.close()
# I used two chessboard,
# one to be shown to the user and the table to be processed
# and the other one with the locations.
coordinate = [[j+str(i) for j in "abcdefgh"] for i in range(8, 0, -1)]
board = [["  " for j in range(8)] for i in range(8)]
black_rock = ["ki", "KI", "R1", "N1", "B1", "QU", "B2", "N2", "R2", "P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8"]
white_rock = ["KI", "ki", "p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8", "r1", "n1", "b1", "qu", "b2", "n2", "r2"]
# kings are double sided spies. :)

def initialize_func():  # to reset chessboard
    global board
    board = [["  " for j in range(8)] for i in range(8)]
    board[0] = ["R1", "N1", "B1", "QU", "KI", "B2", "N2", "R2"]
    board[1] = ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8"]
    board[6] = ["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8"]
    board[7] = ["r1", "n1", "b1", "qu", "ki", "b2", "n2", "r2"]
initialize_func()


def print_func(charts):
    print("----------------------------------")
    for i in range(len(charts)):
        print("|", end="")
        for j in range(len(charts[0])):
            print(f" {charts[i][j]}", end=" ")
        print("|")
    print("----------------------------------")


def print_show_func(commands, rocks_name, lists):  # to print movements of the elements on the screen
    print(f"> {commands} {rocks_name}")
    if len(lists) == 0:
        print("FAILED")
    else:
        lists = sorted(lists)
        for i in range(len(lists)):
            print(lists[i], end=" ")
        print()


def find_func(charts, rocks_name):  # to find out where the elements are
    for i in range(8):
        for j in range(8):
            if charts[i][j] == rocks_name:
                global y, x
                y = i
                x = j

# Functions starting with piece names to calculate where the piece can move
def pawn_ability(rocks_name):
    find_func(board, rocks_name)
    global a
    a = []
    if rocks_name in white_rock:
        if y - 1 >= 0 and not board[y - 1][x] in white_rock:
            a.append(coordinate[y - 1][x])
    else:
        if y + 1 <= 7 and not board[y + 1][x] in black_rock:
            a.append(coordinate[y + 1][x])


def knight_ability(rocks_name):
    find_func(board, rocks_name)
    if rocks_name in white_rock:
        group1 = white_rock
    else:
        group1 = black_rock
    global a
    a = []
    if y + 2 <= 7 and x + 1 <= 7:
        if not board[y + 2][x + 1] in group1:
            a.append(coordinate[y + 2][x + 1])
    if y + 2 <= 7 and x - 1 >= 0:
        if not board[y + 2][x - 1] in group1:
            a.append(coordinate[y + 2][x - 1])
    if y - 2 >= 0 and x + 1 <= 7:
        if not board[y - 2][x + 1] in group1:
            a.append(coordinate[y - 2][x + 1])
    if y - 2 >= 0 and x - 1 >= 0:
        if not board[y - 2][x - 1] in group1:
            a.append(coordinate[y - 2][x - 1])
    if y + 1 <= 7 and x + 2 <= 7:
        if not board[y + 1][x + 2] in group1:
            a.append(coordinate[y + 1][x + 2])
    if y + 1 <= 7 and x - 2 >= 0:
        if not board[y + 1][x - 2] in group1:
            a.append(coordinate[y + 1][x - 2])
    if y - 1 >= 0 and x + 2 <= 7:
        if not board[y - 1][x + 2] in group1:
            a.append(coordinate[y - 1][x + 2])
    if y - 1 >= 0 and x - 2 >= 0:
        if not board[y - 1][x - 2] in group1:
            a.append(coordinate[y - 1][x - 2])
    if y + 1 <= 7 and x + 1 <= 7:
        if board[y + 1][x + 1] == "  ":
            a.append(coordinate[y + 1][x + 1])
    if y + 1 <= 7 and x - 1 >= 0:
        if board[y + 1][x - 1] == "  ":
            a.append(coordinate[y + 1][x - 1])
    if y - 1 >= 0 and x + 1 <= 7:
        if board[y - 1][x + 1] == "  ":
            a.append(coordinate[y - 1][x + 1])
    if y - 1 >= 0 and x - 1 >= 0:
        if board[y - 1][x - 1] == "  ":
            a.append(coordinate[y - 1][x - 1])


def rook_ability(rocks_name):
    find_func(board, rocks_name)
    if rocks_name in white_rock:
        group1, group2 = white_rock, black_rock
    else:
        group1, group2 = black_rock, white_rock
    global a
    a = []
    count = 1
    while y + count <= 7 and not board[y - 1 + count][x] in group2 and not board[y + count][x] in group1:
        a.append(coordinate[y + count][x])
        count += 1
    count = 1
    while y - count >= 0 and not board[y + 1 - count][x] in group2 and not board[y - count][x] in group1:
        a.append(coordinate[y - count][x])
        count += 1
    count = 1
    while x + count <= 7 and not board[y][x - 1 + count] in group2 and not board[y][x + count] in group1:
        a.append(coordinate[y][x + count])
        count += 1
    count = 1
    while x - count >= 0 and not board[y][x + 1 - count] in group2 and not board[y][x - count] in group1:
        a.append(coordinate[y][x - count])
        count += 1


def bishop_ability(rocks_name):
    find_func(board, rocks_name)
    global a
    a = []
    if rocks_name in white_rock:
        count = 1
        while y - count >= 0 and x - count >= 0 and not board[y + 1 - count][x + 1 - count] in black_rock \
                and not board[y - count][x - count] in white_rock:
            a.append(coordinate[y - count][x - count])
            count += 1
        count = 1
        while y - count >= 0 and x + count <= 7 and not board[y + 1 - count][x - 1 + count] in black_rock \
                and not board[y - count][x + count] in white_rock:
            a.append(coordinate[y - count][x + count])
            count += 1
    else:
        count = 1
        while y + count <= 7 and x + count <= 7 and not board[y - 1 + count][x - 1 + count] in white_rock \
                and not board[y + count][x + count] in black_rock:
            a.append(coordinate[y + count][x + count])
            count += 1
        count = 1
        while y + count <= 7 and x - count >= 0 and not board[y - 1 + count][x + 1 - count] in white_rock \
                and not board[y + count][x - count] in black_rock:
            a.append(coordinate[y + count][x - count])
            count += 1


def queen_ability(rocks_name):
    find_func(board, rocks_name)
    if rocks_name in white_rock:
        group1, group2 = white_rock, black_rock
    else:
        group1, group2 = black_rock, white_rock
    global a
    a = []
    count = 1
    while y - count >= 0 and x - count >= 0 and not board[y + 1 - count][x + 1 - count] in group2 \
            and not board[y - count][x - count] in group1:
        a.append(coordinate[y - count][x - count])
        count += 1
    count = 1
    while y - count >= 0 and x + count <= 7 and not board[y + 1 - count][x - 1 + count] in group2 \
            and not board[y - count][x + count] in group1:
        a.append(coordinate[y - count][x + count])
        count += 1
    count = 1
    while y + count <= 7 and x + count <= 7 and not board[y - 1 + count][x - 1 + count] in group2 \
            and not board[y + count][x + count] in group1:
        a.append(coordinate[y + count][x + count])
        count += 1
    count = 1
    while y + count <= 7 and x - count >= 0 and not board[y - 1 + count][x + 1 - count] in group2 \
            and not board[y + count][x - count] in group1:
        a.append(coordinate[y + count][x - count])
        count += 1


def king_ability(rocks_name):
    find_func(board, rocks_name)
    global a
    a = []
    if rocks_name == "KI":
        group = black_rock
    else:
        group = white_rock
    if y - 1 >= 0 and not board[y - 1][x] in group:
        a.append(coordinate[y - 1][x])
    if y - 1 >= 0 and x - 1 >= 0 and not board[y - 1][x - 1] in group:
        a.append(coordinate[y - 1][x - 1])
    if y - 1 >= 0 and x + 1 <= 7 and not board[y - 1][x + 1] in group:
        a.append(coordinate[y - 1][x + 1])
    if x - 1 >= 0 and not board[y][x - 1] in group:
        a.append(coordinate[y][x - 1])
    if x + 1 <= 7 and not board[y][x + 1] in group:
        a.append(coordinate[y][x + 1])
    if y + 1 <= 7 and not board[y + 1][x] in group:
        a.append(coordinate[y + 1][x])
    if y + 1 <= 7 and x - 1 >= 0 and not board[y + 1][x - 1] in group:
        a.append(coordinate[y + 1][x - 1])
    if y + 1 <= 7 and x + 1 <= 7 and not board[y + 1][x + 1] in group:
        a.append(coordinate[y + 1][x + 1])

# Checking the list a resulting from the above functions(lines: 51 - 216) is done.
# The given move order is compared with the place where the piece is intended to go.
# If the position in the order is in the list a, the function operates.
def move_func(rocks_name, commands):
    find_func(coordinate, commands)
    coordinate_y, coordinate_x = y, x
    find_func(board, rocks_name)
    rock_y, rock_x = y, x
    print(f"> {command[i][0]} {rocks_name} {commands}")
    if command[i][2] in a:
        print("OK")
        board[rock_y][rock_x] = "  "
        board[coordinate_y][coordinate_x] = rocks_name
    else:
        print("FAILED")


for i in range(len(command)):
    if command[i][0] == "move" and len(command[i]) == 3:
        if command[i][1] in ("p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8", "P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8"):
            pawn_ability(command[i][1])
            move_func(command[i][1], command[i][2])
        elif command[i][1] in ("r1", "r2", "R1", "R2"):
            rook_ability(command[i][1])
            move_func(command[i][1], command[i][2])
        elif command[i][1] in ("n1", "n2", "N1", "N2"):
            knight_ability(command[i][1])
            move_func(command[i][1], command[i][2])
        elif command[i][1] in ("b1", "b2", "B1", "B2"):
            bishop_ability(command[i][1])
            move_func(command[i][1], command[i][2])
        elif command[i][1] in ("qu", "QU"):
            rook_ability(command[i][1])
            b = a
            queen_ability(command[i][1])
            a += b
            move_func(command[i][1], command[i][2])
        elif command[i][1] in ("ki", "KI"):
            king_ability(command[i][1])
            move_func(command[i][1], command[i][2])
    elif command[i][0] == "showmoves" and len(command[i]) == 2:
        if command[i][1] in ("p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8", "P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8"):
            pawn_ability(command[i][1])
            print_show_func(command[i][0], command[i][1], a)
        elif command[i][1] in ("r1", "r2", "R1", "R2"):
            rook_ability(command[i][1])
            print_show_func(command[i][0], command[i][1], a)
        elif command[i][1] in ("n1", "n2", "N1", "N2"):
            knight_ability(command[i][1])
            print_show_func(command[i][0], command[i][1], a)
        elif command[i][1] in ("b1", "b2", "B1", "B2"):
            bishop_ability(command[i][1])
            print_show_func(command[i][0], command[i][1], a)
        elif command[i][1] in ("qu", "QU"):
            rook_ability(command[i][1])
            b = a
            queen_ability(command[i][1])
            a += b
            print_show_func(command[i][0], command[i][1], a)
        elif command[i][1] in ("ki", "KI", "K1"):
            king_ability(command[i][1])
            print_show_func(command[i][0], command[i][1], a)
    elif command[i][0] == "initialize":
        initialize_func()
        print("> initialize \nOK")
        print_func(board)
    elif command[i][0] == "print":
        print("> print")
        print_func(board)
    elif command[i][0] == "exit":
        print("> exit")
        exit()
    else:
        print("Something you wrote was wrong")
