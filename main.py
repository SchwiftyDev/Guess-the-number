import pygame, sys, random
pygame.init()

# /* Classes */
class text(object):
    def __init__(self, text, color, position = None):
        self.font = pygame.font.Font("arial.ttf", 32)
        self.text = self.font.render(text,True, color)
        self.object = self.text.get_rect()
        self.color = color
        self.currentText = text
        if position:
            self.position = position
            self.object.center = position

    def draw(self, surface):
        surface.blit(self.text, self.object)

    def change(self, text):
        self.text = self.font.render(text, True, self.color)
        self.object = self.text.get_rect()
        self.currentText = text
        try:
            self.object.center = self.position
        except:
            print("No position")

    def add(self, text):
        self.text = self.font.render(self.currentText + text, True, self.color)
        self.object = self.text.get_rect()
        self.currentText += text
        try:
            self.object.center = self.position
        except:
            print("No position")

    def subtract(self):
        try:
            lis = list(self.currentText)
            lis.pop()
            self.currentText = ''.join(lis)
            self.text = self.font.render(self.currentText, True, self.color)
            self.object = self.text.get_rect()
            try:
                self.object.center = self.position
            except:
                print("No position")
        except:
            print("pop from empty list")

# Colors
BLACK = (30,30,30)
WHITE = (180,180,180)
RED = (180,40,40)

# /* Variables */
WIDTH,HEIGHT = 1280,720
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Guess the number!")
TEXT = text("", WHITE, ((WIDTH/2), HEIGHT/2 + 50))
TEXT2 = text("Guess the number!", RED, (WIDTH/2,HEIGHT/2))
RANDOM_NUMBER = random.randint(0,10)
clock = pygame.time.Clock()

# /* Functions */
def up(event):
    if event.unicode == "\x08":
        TEXT.subtract()
    elif event.unicode == "\r":
        global RANDOM_NUMBER
        if str(TEXT.currentText) == str(RANDOM_NUMBER):
            TEXT2.change(f"{TEXT.currentText} is right! C:")
            RANDOM_NUMBER = random.randint(0,10)
        elif not TEXT.currentText.isdigit():
            TEXT2.change(f"{TEXT.currentText} is not a number! :C")
        elif int(TEXT.currentText) > 10:
            TEXT2.change(f"{TEXT.currentText} is wayyy too high! :C")
        else:
            TEXT2.change(f"{TEXT.currentText} is wrong! :C")
    else:
        TEXT.add(event.unicode)

def draw():
    pygame.display.flip()
    SCREEN.fill(BLACK)
    TEXT.draw(SCREEN)
    TEXT2.draw(SCREEN)

def main():
    clock.tick(5)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit(); pygame.quit()
            if event.type == pygame.KEYUP: up(event)
        draw()

if __name__ == "__main__":
    main()

