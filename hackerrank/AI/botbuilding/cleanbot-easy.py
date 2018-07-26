
m = [['-','d','-','-','-'],
     ['-','d','-','-','-'],
     ['-','-','-','d','-'],
     ['-','-','-','d','-'],
     ['-','-','d','-','d']]

def next_move(posr, posc, board):
    w = len(board[0])
    h = len(board)
    if board[posr][posc] == 'd':
        print("CLEAN")
    elif w > posc+1 and board[posr][posc+1] == 'd':
        print("RIGHT")
    elif posc and board[posr][posc-1] == 'd':
        print("LEFT")
    elif h > posr+1 and board[posr+1][posc] == 'd':
        print("DOWN")
    elif posr and board[posr-1][posc] == 'd':
        print("UP")
    elif 'd' in [board[i][posc] for i in range(posr)]:
        print("UP")
    elif 'd' in [board[i][posc] for i in range(posr,h)]:
        print("DOWN")
    elif 'd' in board[posr][:posc]:
        print("LEFT")
    elif 'd' in board[posr][posc:]:
        print("RIGHT")
    elif 'd' in [board[row][col] for row in range(posr,h) for col in range(w)]:
        print("DOWN")
    elif 'd' in [board[row][col] for row in range(posr) for col in range(w)]:
        print("UP")
