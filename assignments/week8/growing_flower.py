import pygame
import random
import math
import sys

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (255, 255, 255)  # White background

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

class Flower:
    def __init__(self, image_path):
        self.base_image = pygame.image.load(image_path).convert_alpha()

        # Start position at bottom center
        self.start_x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT + 20

        # Slight horizontal wave motion
        self.amplitude = 30
        self.frequency = 0.02

        # Growth
        self.scale = 0.5
        self.max_scale = 3.0  # Larger maximum size
        self.growth_speed = 0.003  # Very slow growth

        # Upward speed
        self.speed = 0.5  # Slow upward movement

    def move(self):
        # Move upward
        self.y -= self.speed

        # Gradually grow
        if self.scale < self.max_scale:
            self.scale += self.growth_speed

    def draw(self, surface):
        # Calculate image size based on scale
        size = int(60 * self.scale)
        image = pygame.transform.scale(self.base_image, (size, size)).copy()

        # Fade out slowly based on growth
        fade_start = 2.6  # Start fading when scale is large
        if self.scale > fade_start:
            fade_ratio = (self.scale - fade_start) / (self.max_scale - fade_start)
            alpha = max(0, 255 - int(fade_ratio * 80))  # Very gentle fade
        else:
            alpha = 255
        image.set_alpha(alpha)

        # Horizontal wave motion
        x = self.start_x + self.amplitude * math.sin(self.frequency * self.y)

        # Draw flower centered and growing upward
        surface.blit(image, (x - size // 2, self.y - size))

# Create one flower instance
flower = Flower("flower.jpeg")

# Main loop
running = True
while running:
    clock.tick(60)
    screen.fill(BACKGROUND_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    flower.move()
    flower.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()
