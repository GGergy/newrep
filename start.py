import pygame 
from empity import Character
def main():
    pass
if __name__ == '__main__':
    main()

clock =  pygame.time.Clock()
screen_width = 1920
screen_height = 1080
main_screen = pygame.display.set_mode((screen_width, screen_height))   
character = Character(0, 0)    
events = pygame.event.get()
FPS = 60

while True:
    for event in events:
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                character.direction = 1
                character.move(character.speed)
            elif event.key == pygame.K_a:
                character.direction = -1
                character.move(character.speed)

    character.draw(main_screen)
    pygame.display.update()
    clock.tick(FPS)