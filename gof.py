import pyxes, random, copy

size = 200
rows_count = size
columns_count = int(size+(size/2))

cell_size = 3

board_base = [[0] * columns_count for _ in range(rows_count)]

def gen_board():
    board = copy.deepcopy(board_base)

    for row in range(rows_count):
        for column in range(columns_count):
            if random.random() < 0.25:
                board[row][column] = 1

    return board

board = gen_board()
board_neighbors = copy.deepcopy(board_base)

# extends game because game methods ignore pause
class Game (pyxes.Game):
    def key_down(self, event, key_name):
        global board, board_neighbors

        if key_name == 'p':
            self.toggle_pause()
        elif key_name == 'r':
            board = gen_board()
            board_neighbors = copy.deepcopy(board_base)

    def on_pause(self, pause):
        self.set_cursor_visibility(pause)

    def draw(self):
        for row in range(rows_count):
            for column in range(columns_count):
            # draw cell if alive
                if board[row][column] == 1:
                    self.pygame.draw.rect(self.screen, (255, 255, 255), (column * cell_size, row * cell_size, cell_size, cell_size))

class Scene (pyxes.Scene):
    def update(self):
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

        # logic
        for row in range(rows_count):
            for column in range(columns_count):
                # if cell alive
                if board[row][column] == 1:
                    if board_neighbors[row][column] < 2 or board_neighbors[row][column] > 3:
                        board[row][column] = 0
                # if cell dead and it have 3 neighbors
                elif board_neighbors[row][column] == 3:
                    board[row][column] = 1

if __name__ == '__main__':
    game = Game(width=columns_count * cell_size, height=rows_count * cell_size, cursor=False, title='Game of Life', fps=5, quit_on_escape=True, default_scene=Scene())

    game.run()