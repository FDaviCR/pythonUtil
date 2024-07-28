import pygame
import random

# Inicialização do Pygame
pygame.init()

# Definições de cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Tamanho da janela
WIDTH, HEIGHT = 600, 600

# Definições do labirinto
ROWS = 20
COLS = 20
CELL_SIZE = WIDTH // COLS
#maze = [[random.choice([0, 1]) for _ in range(COLS)] for _ in range(ROWS)]
maze = [
		[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1],
		[1,1,1,0,1,1,1,0,0,1,0,0,0,1,0,0,0,0,0,1],
		[1,0,0,0,0,0,1,0,1,1,1,1,1,1,0,1,1,1,1,1],
		[1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,1,0,0,1,1,1,1,1,1,1,1,1,0,1],
		[1,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,1],
		[1,0,1,1,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1],
		[1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1],
		[1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1],
		[1,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1],
		[1,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1],
		[1,0,0,1,0,0,1,1,1,0,1,1,1,1,1,0,1,1,1,1],
		[1,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1],
		[1,0,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1],
		[1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]
maze[0][0] = 0
maze[ROWS-1][COLS-1] = 0

# Definições do jogador
player_pos = [1, 1]

# Inicialização da janela
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Labirinto")

# Função para desenhar o labirinto
def draw_maze():
    for row in range(ROWS):
        for col in range(COLS):
            color = WHITE if maze[row][col] == 0 else BLACK
            pygame.draw.rect(win, color, (col*CELL_SIZE, row*CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Função para desenhar o jogador
def draw_player():
    pygame.draw.circle(win, RED, (player_pos[1]*CELL_SIZE + CELL_SIZE//2, player_pos[0]*CELL_SIZE + CELL_SIZE//2), CELL_SIZE//4)

# Função principal
def main():
    global player_pos
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and player_pos[0] > 0 and maze[player_pos[0]-1][player_pos[1]] == 0:
                    player_pos[0] -= 1
                elif event.key == pygame.K_DOWN and player_pos[0] < ROWS - 1 and maze[player_pos[0]+1][player_pos[1]] == 0:
                    player_pos[0] += 1
                elif event.key == pygame.K_LEFT and player_pos[1] > 0 and maze[player_pos[0]][player_pos[1]-1] == 0:
                    player_pos[1] -= 1
                elif event.key == pygame.K_RIGHT and player_pos[1] < COLS - 1 and maze[player_pos[0]][player_pos[1]+1] == 0:
                    player_pos[1] += 1

        win.fill(WHITE)
        draw_maze()
        draw_player()
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
