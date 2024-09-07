
import pygame
import random as r
from itertools import product
import time
# Initialize pygame
pygame.init()

# Constants for the game
GRID_SIZE = 3
TILE_SIZE = 100
MINE_COUNT =1
WINDOW_SIZE = GRID_SIZE * TILE_SIZE
FPS = 30

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (255, 255,255)
GRAY = (0, 0, 0)

# Initialize the screen
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("THE MINESWEEPER GAME")
# pygame.display.set_caption()
font = pygame.font.SysFont("SF pro", 12)

# Sound Effects
explosion_sounds = ["explosion-42132.wav", "explosion2.wav"]
explosion_sound = pygame.mixer.Sound(f"/media/apsync/Codes/mini_projects/the Minesweeper/{explosion_sounds[r.randint(0, 1)]}")
success_sound = pygame.mixer.Sound("/media/apsync/Codes/mini_projects/the Minesweeper/success.wav")


class Minesweeper:
    def __init__(self):
        self.grid = [["#" for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.mines = self.generate_mines()
        self.win_grids = self.get_win_grids()
        self.score = 0
        self.game_over = False

    def generate_mines(self):
        mines = []
        while len(mines) < MINE_COUNT:
            mine = (r.randint(0, GRID_SIZE - 1), r.randint(0, GRID_SIZE - 1))
            if mine not in mines:
                mines.append(mine)
        return mines

    def get_win_grids(self):
        grid_ord = list(product(range(GRID_SIZE), range(GRID_SIZE)))
        for mine in self.mines:
            if mine in grid_ord:
                grid_ord.remove(mine)
        return grid_ord

    def check_win(self, tries):
        return set(tries) == set(self.win_grids)

    def draw_grid(self):
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                rect = pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(screen, WHITE, rect, 1)
                if self.grid[row][col] == "X":
                    pygame.draw.rect(screen, GREEN, rect)
                elif self.grid[row][col] == "M":
                    pygame.draw.rect(screen, RED, rect)

    def reveal_tile(self, row, col):
        if (row, col) in self.mines:
            self.grid[row][col] = "M"
            self.game_over = True
            pygame.mixer.Sound.play(explosion_sound)
        else:
            self.grid[row][col] = "X"
            self.score += 10
            rect = pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(screen,GREEN,rect)
            pygame.mixer.Sound.play(success_sound)

    def reset_game(self):
        self.__init__()


# Game loop
def game_loop():
    clock = pygame.time.Clock()
    game = Minesweeper()
    tries = []

    while True:
        # print(game.grid_ord)
        # time.sleep(5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.MOUSEBUTTONDOWN and not game.game_over:
                x, y = pygame.mouse.get_pos()
                row, col = y // TILE_SIZE, x // TILE_SIZE
                if (row, col) not in tries:
                    tries.append((row, col))
                    game.reveal_tile(row, col)

                    if game.check_win(tries):
                        game.game_over = True
                        game_over_text = font.render("CONGRATULATIONS YOU WON", True, WHITE)
                        game.score += 50  # Bonus points for winning

            if game.game_over:
                screen.fill(BLACK)
                game_over_text = font.render("GAME OVER", True, WHITE)
                screen.blit(game_over_text, (WINDOW_SIZE // 2 - game_over_text.get_width() // 2, WINDOW_SIZE // 2 - game_over_text.get_height() // 2))

                score_text = font.render(f"Score: {game.score}", True, WHITE)
                screen.blit(score_text, (WINDOW_SIZE // 2 - score_text.get_width() // 2, WINDOW_SIZE // 2 + game_over_text.get_height()))

                pygame.display.flip()

                pygame.time.wait(2000)  # Pause for 2 seconds
                game.reset_game()
                tries.clear()

        screen.fill(GRAY)
        game.draw_grid()

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    game_loop()
