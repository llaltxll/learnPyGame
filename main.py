import pygame


def main():
    xpos = 50
    ypos = 50
    step_x = .1
    step_y = .1
    screen_width = 240
    screen_heigth = 180

    pygame.init()
    logo = pygame.image.load("logo32x32.png")
    bgd_image = pygame.image.load("background.png")
    image = pygame.image.load("01_image.png")

    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")
    screen = pygame.display.set_mode((screen_width,screen_heigth))
    image.set_colorkey((255, 0, 255))
    image.set_alpha(128)

    # screen.fill((200,200,200))


    running = True



    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if xpos>screen_width-64 or xpos<0:
            step_x = -step_x
        if ypos>screen_heigth-64 or ypos<0:
            step_y = -step_y
        xpos += step_x
        ypos += step_y
        screen.blit(bgd_image, (0, 0))
        screen.blit(image, (xpos, ypos))
        pygame.display.flip()

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ =="__main__":
    main()