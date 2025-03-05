import pygame
import sys
import os

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
SQUARE_SIZE = WIDTH // 8
WHITE = (240, 217, 181)
BROWN = (181, 136, 99)
BLACK = (0, 0, 0)

# Load piece images
piece_images = {}
piece_names = ['black_rook', 'black_knight', 'black_bishop', 'black_queen', 'black_king', 'black_pawn',
               'white_rook', 'white_knight', 'white_bishop', 'white_queen', 'white_king', 'white_pawn']
for piece in piece_names:
    path = os.path.join("pieces", f"{piece}.png")
    piece_images[piece] = pygame.image.load(path)
    piece_images[piece] = pygame.transform.scale(piece_images[piece], (SQUARE_SIZE, SQUARE_SIZE))

# Chessboard class
class ChessBoard:
    def __init__(self):
        self.board = [
            ['black_rook', 'black_knight', 'black_bishop', 'black_queen', 'black_king', 'black_bishop', 'black_knight', 'black_rook'],
            ['black_pawn'] * 8,
            [' '] * 8,
            [' '] * 8,
            [' '] * 8,
            [' '] * 8,
            ['white_pawn'] * 8,
            ['white_rook', 'white_knight', 'white_bishop', 'white_queen', 'white_king', 'white_bishop', 'white_knight', 'white_rook']
        ]
        self.selected_piece = None

    def draw_board(self, screen):
        for row in range(8):
            for col in range(8):
                color = WHITE if (row + col) % 2 == 0 else BROWN
                pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                piece = self.board[row][col]
                if piece in piece_images:
                    screen.blit(piece_images[piece], (col * SQUARE_SIZE, row * SQUARE_SIZE))
    
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

