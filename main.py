import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
SQUARE_SIZE = WIDTH // 8
WHITE = (240, 217, 181)
BROWN = (181, 136, 99)
BLACK = (0, 0, 0)
FONT = pygame.font.Font(None, 50)

# Chessboard class
class ChessBoard:
    def __init__(self):
        self.board = [
            ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜'],
            ['♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙'],
            ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖']
        ]
        self.selected_piece = None

    def draw_board(self, screen):
        for row in range(8):
            for col in range(8):
                color = WHITE if (row + col) % 2 == 0 else BROWN
                pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                piece = self.board[row][col]
                if piece != ' ':
                    text = FONT.render(piece, True, BLACK)
                    text_rect = text.get_rect(center=(col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2))
                    screen.blit(text, text_rect)
    
    def handle_click(self, pos):
        col, row = pos[0] // SQUARE_SIZE, pos[1] // SQUARE_SIZE
        if self.selected_piece:
            self.move_piece(self.selected_piece, (row, col))
            self.selected_piece = None
        else:
            if self.board[row][col] != ' ':
                self.selected_piece = (row, col)

    def move_piece(self, start, end):
        sr, sc = start
        er, ec = end
        if self.board[sr][sc] != ' ':
            self.board[er][ec] = self.board[sr][sc]
            self.board[sr][sc] = ' '

# Main function
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Chess")
    clock = pygame.time.Clock()
    chessboard = ChessBoard()

    running = True
    while running:
        screen.fill(BLACK)
        chessboard.draw_board(screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                chessboard.handle_click(event.pos)

        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
