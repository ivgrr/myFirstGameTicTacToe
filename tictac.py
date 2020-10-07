# TIC TAC TOE GAME BY IVGRR

board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

winner = None
play_game = True

def show_board():
    print('|' + board[0] + '|' + board[1] + '|' + board[2] + '|')
    print('|' + board[3] + '|' + board[4] + '|' + board[5] + '|')
    print('|' + board[6] + '|' + board[7] + '|' + board[8] + '|')


def main():
    show_board()
    while play_game:
        whoWinner()
        input_num()
        show_board()


def input_num():
    x_or_o = input('Введите кем вы ходите(X или О): ').upper()
    if x_or_o == 'X':
        PLAYER = input('Введите позицию: ')
        if PLAYER.isdigit():
            PLAYER = int(PLAYER) - 1
            board[PLAYER] = 'X'
        else:
            print('Введите цифру от 1 до 9')
    elif x_or_o == 'O':
        PLAYER = input('Введите позицию: ')
        if PLAYER.isdigit():
            PLAYER = int(PLAYER) - 1
            board[PLAYER] = 'O'
        else:
            print('Введите цифру от 1 до 9')

def whoWinner():
    if board[0] == board[1] == board[2] == 'X' or \
       board[3] == board[4] == board[5] == 'X' or \
       board[6] == board[7] == board[8] == 'X' or \
       board[0] == board[3] == board[6] == 'X' or \
       board[1] == board[4] == board[7] == 'X' or \
       board[2] == board[5] == board[8] == 'X' or \
       board[0] == board[4] == board[8] == 'X' or \
       board[2] == board[4] == board[6] == 'X':
        print('X Winner')
        exit()
    elif board[0] == board[1] == board[2] == 'O' or \
         board[3] == board[4] == board[5] == 'O' or \
         board[6] == board[7] == board[8] == 'O' or \
         board[0] == board[3] == board[6] == 'O' or \
         board[1] == board[4] == board[7] == 'O' or \
         board[2] == board[5] == board[8] == 'O' or \
         board[0] == board[4] == board[8] == 'O' or \
         board[2] == board[4] == board[6] == 'O':
        print('O Winner')
        exit()
    elif '-' not in board:
        print('No one Winner')
        exit()

main()
