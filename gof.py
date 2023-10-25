import random, copy

import pyxes

rows_count = int(720 / 6)
columns_count = int(1280 / 6)

cell_size = 5

board = [[0] * columns_count for _ in range(rows_count)]
board_neighbors = copy.deepcopy(board)

# random alive cells
for row in range(rows_count):
    for column in range(columns_count):
        if random.random() < 0.5:
            board[row][column] = 1

class Game (pyxes.Game):
    def update(self):
        if self.pause == False:
            # calc cell neighbors
            for row in range(rows_count):
                for column in range(columns_count):
                    neighbors = 0
                    for dr in [-1, 0, 1]:
                        for dc in [-1, 0, 1]:
                            if dr == 0 and dc == 0:
                                continue
                            r, c = row + dr, column + dc
                            if 0 <= r < rows_count and 0 <= c < columns_count and board[r][c] == 1:
                                neighbors += 1
                    board_neighbors[row][column] = neighbors

            # game of life logic
            for row in range(rows_count):
                for column in range(columns_count):
                    # if cell alive
                    if board[row][column] == 1:
                        if board_neighbors[row][column] < 2 or board_neighbors[row][column] > 3:
                            board[row][column] = 0
                    # if cell dead
                    elif board_neighbors[row][column] == 3:
                        board[row][column] = 1

    def draw(self):
        for row in range(rows_count):
            for column in range(columns_count):
                # draw cell if alive
                if board[row][column] == 1:
                    self.pygame.draw.rect(self.screen, (255, 255, 255), (column * cell_size, row * cell_size, cell_size, cell_size))

    def key_down(self, event, key_name):
        if key_name == 'p': self.toggle_pause()

    def on_pause(self, pause):
        self.set_cursor_visibility(pause)

if __name__ == '__main__':
    game = Game(width=columns_count * cell_size, height=rows_count * cell_size, cursor=False, title='Game of Life', fps=5)

    game.run()