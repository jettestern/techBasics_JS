import pygame
import sys
import random

# --- Setup ---
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Emoji Drawing Game")

# Use emoji-friendly font for macOS
font = pygame.font.SysFont("Apple Color Emoji", 50)

# --- Base Class ---
class Brush:
    def __init__(self, emoji):
        self._emoji = emoji
        self._size = 40

    def draw(self, surface, position):
        emoji_surface = font.render(self._emoji, True, (0, 0, 0))
        rect = emoji_surface.get_rect(center=position)
        surface.blit(emoji_surface, rect)

    def get_emoji(self):
        return self._emoji

    def set_emoji(self, new_emoji):
        self._emoji = new_emoji

    def get_size(self):
        return self._size

    def set_size(self, new_size):
        self._size = new_size

# --- Subclasses ---
class FlowerBrush(Brush):
    def __init__(self):
        super().__init__("🌸")

    def change_flower(self):
        self.set_emoji(random.choice(["🌸", "🌻", "🌼", "🌷"]))

class AnimalBrush(Brush):
    def __init__(self):
        super().__init__("🐱")

    def change_animal(self):
        self.set_emoji(random.choice(["🐱", "🐶", "🐸", "🐵"]))

# --- Game State ---
clock = pygame.time.Clock()
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255, 255, 255))

current_brush = FlowerBrush()
drawing = False

# --- Main Loop ---
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                current_brush = FlowerBrush()
            elif event.key == pygame.K_a:
                current_brush = AnimalBrush()
            elif event.key == pygame.K_c:
                background.fill((255, 255, 255))
            elif event.key == pygame.K_SPACE:
                if isinstance(current_brush, FlowerBrush):
                    current_brush.change_flower()
                elif isinstance(current_brush, AnimalBrush):
                    current_brush.change_animal()

    if drawing:
        mouse_pos = pygame.mouse.get_pos()
        current_brush.draw(background, mouse_pos)

    screen.blit(background, (0, 0))
    pygame.display.flip()
    clock.tick(60)

# --- Controls & Instructions ---
# - Hold Left Click: Draw emoji at mouse position
# - Press F: Switch to Flower Brush (🌸, 🌼, 🌷, 🌻)
# - Press A: Switch to Animal Brush (🐱, 🐶, 🐸, 🐵)
# - Press SPACE: Randomize current emoji in selected brush
# - Press C: Clear the canvas
