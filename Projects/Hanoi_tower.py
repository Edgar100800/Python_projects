class TableGame:
    def __init__(self, number_of_towers, number_of_disks):
        self.number_of_towers = number_of_towers
        self.number_of_disks = number_of_disks
        self.game = "No table created"

    def create_board_game(self):
        game = []
        for i in range(self.number_of_towers):
            if i == 0:
                empty_list = list(range(self.number_of_disks, 0, -1))
                game.append(empty_list)
            else:
                empty_list = []
                game.append(empty_list)
        self.game = game

    def show_board_game(self):
        print(self.game)

    def test_last_element_array(self, array1, array2):
        if not array1:
            return False
        if not array2:
            return True
        elif array1[-1] < array2[-1]:
            return True
        else:
            return False

    def move_to_right(self, tower_selected):
        if 0 < tower_selected < self.number_of_towers and \
                self.test_last_element_array(self.game[tower_selected-1], self.game[tower_selected]):
            # print("Resultado valido")
            pop_value = self.game[tower_selected-1].pop()
            # print(pop_value)
            self.game[tower_selected].append(pop_value)
        else:
            print("Movimiento invalido")

    def move_to_left(self, tower_selected):
        if 1 < tower_selected <= self.number_of_towers and \
                self.test_last_element_array(self.game[tower_selected-1], self.game[tower_selected-2]):
            # print("Resultado valido")
            pop_value = self.game[tower_selected-1].pop()
            # print(pop_value)
            self.game[tower_selected-2].append(pop_value)
        else:
            print("Movimiento invalido")

    def move_to_somewhere(self, tower_selected, tower_to_move):
        if 0 < tower_selected <= self.number_of_towers and \
                self.test_last_element_array(self.game[tower_selected-1], self.game[tower_to_move-1]):
            # print("Resultado valido")
            pop_value = self.game[tower_selected-1].pop()
            # print(pop_value)
            self.game[tower_to_move-1].append(pop_value)
        else:
            print("Movimiento invalido")

    def verify_win_condition(self):
        new_list = list(range(self.number_of_disks, 0, -1))
        # print(new_list)
        # print(new_array)
        if new_list == self.game[-1]:
            # print("True")
            return False
        else:
            # print("False")
            return True


tableGame1 = TableGame(4, 3)
tableGame1.create_board_game()
movimientos = 0
print("Bienvenido al juego de Hanoi"
      "Inserte la columna que quiere mover y  R o L segun desee mover")

while tableGame1.verify_win_condition():
    tableGame1.show_board_game()
    columna = int(input("Ingrese columna: "))
    columna2 = int(input("Ingrese columna donde quiere mover: "))
    movimientos += 1
    tableGame1.move_to_somewhere(columna, columna2)

if not tableGame1.verify_win_condition():
    print("Genial ganaste en {} movimientos".format(movimientos))


