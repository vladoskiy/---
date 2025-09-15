def condition_game():
    return [[" "] * 3 for _ in range(3)]

def print_list_game(list_game):
    print("  0   1   2") # заголовок
    for i, row in enumerate(list_game): #
        print(f"{i} {row[0]} | {row[1]} | {row[2]}")
        if i < 2: #разделитель между строками
            print(" --------- ")

def game_process(player, list_game):
    while True:
        x = int(input("Введите номер строки: "))
        y = int(input("Введите номер столбца: "))
        print(f"Координаты: {x} {y}")
        if 0 <= x <= 2 and 0 <= y <= 2:
            if list_game[x][y] == " ":
                list_game[x][y] = player
                break
            else:
                print("Ячейка занята")
        else:
            print("Координаты вне поля")

def check_win(player, list_game):
    for row in list_game:
        if all(cell == player for cell in row):
            return True
    for i in range(3):
        if list_game[0][i] == list_game[1][i] == list_game[2][i] == player:
            return True
    if list_game[0][0] == list_game[1][1] == list_game[2][2] == player:
        return True
    if list_game[0][2] == list_game[1][1] == list_game[2][0] == player:
        return True
    return False

def check_draw(list_game):
    for row in list_game:
        if " " in row:
            return False
    return True

def start_game():
    list_game = condition_game()
    current_player = "X"
    while True:
        print_list_game(list_game)
        game_process(current_player, list_game)
        if check_win(current_player, list_game):
            print(f"Игрок {current_player} победил!")
            break

        if check_draw(list_game):
            print_list_game(list_game)
            print("Ничья!")
            break
        current_player = "0" if current_player == "X" else "X"

