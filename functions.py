import pygame

def LoadImage(path, scale):
    """Loads an image path using pygame's methods.

    Args:
        path (str): Path of image to load.
        scale (tuple): Scale to resize image to.

    Returns:
        image: Resized image that can be rendered using pygame.
    """
    image = pygame.image.load(path)
    image = pygame.transform.scale(image, scale)
    return image

def DrawText(screen, text, font, color, pos):
    """Draws text on the screen at the specified position.

    Args:
        screen (surface): Screen to draw text on.
        text (str): Text to draw.
        font (font): Font to render text in.
        color (tuple): Colour of text.
        pos (tuple): Position of text.
    """
    text = font.render(text, True, color)
    screen.blit(text, pos)
    
def GetAdjacentBuilding(tile, direction):
    if direction == 'north':
        adjacenttile = (tile[0], tile[1] - 1)
        return 
    elif direction == 'east':
        adjacenttile = (tile[0] + 1, tile[1])
        return 
    elif direction == 'south':
        adjacenttile = (tile[0], tile[1] + 1)
        return 
    elif direction == 'west':
        adjacenttile = (tile[0] - 1, tile[1])
        return 