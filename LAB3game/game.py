import random
from colorama import init, Fore

init(autoreset=True)

class MazeGame:
    def __init__(self):
        # Inicjalizacja planszy, punktu startowego, końcowego i przeszkód
        self.board, self.start, self.end, self.obstacles = self.generate_board()

    def generate_board(self):
        # Tworzenie pustej planszy o wymiarach 5x5
        board = [['_' for _ in range(5)] for _ in range(5)]

        # Ustawianie punktu startowego na pozycji (0, 0)
        start = (0, 0)
        board[start[0]][start[1]] = 'K'  # 'K' symbolizuje punkt startowy

        # Losowanie pozycji punktu końcowego
        end = (random.randint(0, 4), random.randint(0, 4))
        while end == start:
            end = (random.randint(0, 4), random.randint(0, 4))
        board[end[0]][end[1]] = 'E'  # 'E' symbolizuje punkt końcowy

        # Losowanie pozycji przeszkód
        obstacles = set()
        num_obstacles = random.randint(1, min(5, len(board) * len(board[0]) - 2))  # Maksymalna liczba przeszkód
        for _ in range(num_obstacles):
            obstacle_row = random.randint(0, len(board) - 1)
            obstacle_col = random.randint(0, len(board[0]) - 1)
            while (obstacle_row, obstacle_col) in {start, end} or (obstacle_row, obstacle_col) in obstacles:
                obstacle_row = random.randint(0, len(board) - 1)
                obstacle_col = random.randint(0, len(board[0]) - 1)
            obstacles.add((obstacle_row, obstacle_col))
            board[obstacle_row][obstacle_col] = f'{Fore.RED}U{Fore.RESET}'  # 'U' symbolizuje przeszkodę w czerwonym kolorze

        return board, start, end, obstacles

    def print_board(self):
        # Wyświetlanie aktualnej planszy
        for row in self.board:
            print(' '.join(row))

    def move_player(self, direction):
        current_row, current_col = self.start

        # Aktualizacja pozycji gracza na podstawie wybranego kierunku
        if direction == 'w' and current_row > 0:
            current_row -= 1
        elif direction == 's' and current_row < len(self.board) - 1:
            current_row += 1
        elif direction == 'a' and current_col > 0:
            current_col -= 1
        elif direction == 'd' and current_col < len(self.board[0]) - 1:
            current_col += 1

        # Sprawdzenie, czy nowa pozycja gracza jest w zakresie planszy
        if 0 <= current_row < len(self.board) and 0 <= current_col < len(self.board[0]):
            if (current_row, current_col) == self.end:
                # Jeśli gracz dotarł do punktu końcowego
                self.board[current_row][current_col] = '#'
                self.print_board()
                print("Gratulacje! Dotarłeś do punktu końcowego!")
                return True
            elif 'U' not in self.board[current_row][current_col]:
                # Sprawdzenie czy ruch jest możliwy (brak przeszkody)
                self.board[self.start[0]][self.start[1]] = '_'
                self.start = (current_row, current_col)
                self.board[self.start[0]][self.start[1]] = 'K'
                return False
            else:
                # Informacja, że ruch jest niemożliwy z powodu przeszkody
                print("Nie można tam przejść. Jest przeszkoda!")
                return False
        else:
            # Informacja, że ruch jest poza granicami planszy
            print("Ruch poza planszą! Wybierz inny kierunek.")
            return False

# Główna pętla gry
game = MazeGame()
while True:
    print("\nAktualna plansza:")
    game.print_board()
    move = input("Podaj kierunek ruchu (W - góra, S - dół, A - lewo, D - prawo, Q - wyjście): ").lower()

    if move == 'q':
        # Zakończenie gry
        print("Wychodzisz z gry. Do zobaczenia!")
        break
    elif move in ['w', 's', 'a', 'd']:
        # Wykonanie ruchu gracza
        if game.move_player(move):
            break
    else:
        # Informacja o nieprawidłowym kierunku
        print("Nieprawidłowy kierunek. Podaj poprawny ruch.")
