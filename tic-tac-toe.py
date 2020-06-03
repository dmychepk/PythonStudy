i = [i for i in range(9)]

def current_position(i):
    print(f'{i[0]}|{i[1]}|{i[2]}')
    print(f'{i[3]}|{i[4]}|{i[5]}')
    print(f'{i[6]}|{i[7]}|{i[8]}')
    
def check(i):
    for side in ['X', 'O']:
        winning_lines = ['012','345','678','036','147','258','048','246']
        for line in winning_lines:
            if i[int(line[0])] == side and i[int(line[1])] == side and i[int(line[2])] == side:
                print(f'{side} win!')
                return True
            else:
                continue


current_position(i)

player = 1
turn = 1
while turn <= 9:
    while True:
        cell = input('Enter your cell: ')
        if not cell.isdigit():
            print('Enter valid cell number between 0 and 8. Cell number should be digit.')
        elif not 0<= int(cell) <=8:
            print('Enter valid cell number between 0 and 8.')
        else:
            cell = int(cell)
            break
        
    i[cell] = 'X' if player == 1 else 'O'
    current_position(i)
    # check here
    if check(i):
        break
    # next round
    player = 2 if player == 1 else 1
    turn += 1
