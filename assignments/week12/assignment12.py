# This is a first idea for our project of a food ordering system:
# We thought about using pygame's Surface class to render a virtual receipt at the end of the ordering process.

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Receipt")
font = pygame.font.SysFont(None, 24)

# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_GRAY = (220, 220, 220)
BLUE = (0, 120, 200)

# Button for order
order_button = pygame.Rect(200, 500, 200, 50)

# Bon-Surface und Rect
bon_surface = pygame.Surface((300, 200))
bon_rect = bon_surface.get_rect(center=(300, 250))
show_receipt = False

# Order example
order_items = [
    ("Poke Bowl", 12.5),
    ("Coke 0.5l", 2.0),
    ("Vegan Brownie", 4.5)
]

# Function for drawing receipt
def draw_receipt(surface):
    surface.fill(WHITE)
    y = 10
    total = 0
    for item, price in order_items:
        text = font.render(f"{item} - €{price:.2f}", True, BLACK)
        surface.blit(text, (10, y))
        y += 30
        total += price
    pygame.draw.line(surface, BLACK, (10, y), (290, y), 1)
    y += 10
    total_text = font.render(f"Total: €{total:.2f}", True, BLACK)
    surface.blit(total_text, (10, y))

# Mainloop
while True:
    screen.fill(LIGHT_GRAY)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if order_button.collidepoint(mouse_pos):
                show_receipt = True
            if show_receipt and bon_rect.collidepoint(mouse_pos):
                print("Receipt got clicked")

    # Complete order-Button
    pygame.draw.rect(screen, BLUE, order_button)
    order_text = font.render("Complete order", True, WHITE)
    screen.blit(order_text, (order_button.x + 20, order_button.y + 15))

    # Show receipt
    if show_receipt:
        draw_receipt(bon_surface)
        screen.blit(bon_surface, bon_rect)

    pygame.display.flip()
