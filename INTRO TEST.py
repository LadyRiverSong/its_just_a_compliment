
import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
pygame.font.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("It' Not Just a Compliment")

text_font = pygame.font.Font('ByteBounce.ttf', 30)

def draw_text (text, font, color, size, x, y):
    img = font.render(text, True, color)
    screen.blit(img,(x ,y))
pygame.display.flip()

show_message = False
message_counter = 0  # this is the advancing mechanism, triggers when you press spce
clock = pygame.time.Clock() #adding clock function here used to set global time, usually useful.
number_answer = 0

active = False
running = True
# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # User clicked the close button
            running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if message_counter < 11:
                message_counter += 1

        #setting up all the incorrect answers
        if event.type == pygame.KEYDOWN and event.key == pygame.K_9:
            number_answer = 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_8:
            number_answer = 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_7:
            number_answer = 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_6:
            number_answer = 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_5:
            number_answer = 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_3:
            number_answer = 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
            number_answer = 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
            number_answer = 1
        #setting up correct answer
        if event.type == pygame.KEYDOWN and event.key == pygame.K_4:
            number_answer = 4

    screen.fill((0, 0, 0))
    if message_counter == 0:
        draw_text("It's Not Just a Compliment", text_font, (255, 255, 255), 100, 200, 200)
        draw_text("Press Space to start", text_font, (255, 0, 255), 20,200, 300)
    elif message_counter == 1:
        draw_text("You are walking down the street, when you notice a girl.", text_font, (255, 255, 255), 40, 100, 200)
        draw_text("She's on the other side of the road, head down.", text_font, (255, 255, 255), 40, 100, 250)
        draw_text("She looks like she's had a rough day, but so have you.", text_font, (255, 255, 255), 40, 100, 300)
        draw_text("Press Space to continue", text_font, (255, 0, 255), 40, 100, 450)
    elif message_counter == 2:
        draw_text("You call out to her.", text_font, (255, 255, 255), 40,100, 200)
        draw_text("'Hey sweetie, give me a smile.'", text_font, (255, 255, 255), 40,100, 250)
        draw_text("She glances at you, grabs her bag tight, and speeds up.", text_font, (255, 255, 255), 40, 100, 300)
        draw_text("Press Space to continue", text_font, (255, 0, 255), 40, 100, 450)
    elif message_counter == 3:
        draw_text("You keep walking, a smirk on your face.", text_font, (255, 255, 255), 40,100, 200)
        draw_text("You see another girl, 20 or so, up ahead.", text_font, (255, 255, 255), 40, 100, 250)
        draw_text("You speed up and continue ahead.", text_font, (255, 255, 255), 40, 100, 300)
        draw_text("Press Space to continue", text_font, (255, 0, 255), 40, 100, 450)
    elif message_counter == 4:
        draw_text("As she walks past, you turn around, looking down.", text_font, (255, 255, 255), 40,100, 200)
        draw_text("'Nice Arse' you yell out.", text_font, (255, 255, 255), 40, 100, 250)
        draw_text("You look up to see her scowl", text_font, (255, 255, 255), 40, 100, 300)
        draw_text("Press Space to continue", text_font, (255, 0, 255), 40, 100, 450)
    elif message_counter == 5:
        draw_text("You keep going, feeling like a top dog.", text_font, (255, 255, 255), 40, 100, 200)
        draw_text("You see another young woman, wearing black", text_font, (255, 255, 255), 40, 100, 250)
        draw_text("As you approach you let out a whistle.", text_font, (255, 255, 255), 40, 100, 300)
        draw_text("Press Space to continue", text_font, (255, 0, 255), 40, 100, 450)
    elif message_counter == 6:
        draw_text("She stops in front of you, looking angry", text_font, (255, 255, 255), 40, 100, 200)
        draw_text("'What? Can't a man appreciate a woman?' you joke.", text_font, (255, 255, 255), 40, 100, 250)
        draw_text("She looks down, then back up.", text_font, (255, 255, 255), 40, 100, 300)
        draw_text("Press Space to continue", text_font, (255, 0, 255), 40, 100, 450)
    elif message_counter == 7:
        draw_text("'You want my number?' She asks", text_font, (255, 255, 255), 40, 100, 200)
        draw_text("It's your lucky day. You nod.", text_font, (255, 255, 255), 40, 100, 250)
        draw_text("She rustles in her bag for her phone.", text_font, (255, 255, 255), 40, 100, 300)
        draw_text("Press Space to continue", text_font, (255, 0, 255), 40, 100, 450)
    elif message_counter == 8:
        draw_text("She pulls something out, a silver shine flashing.", text_font, (255, 255, 255), 40, 100, 200)
        draw_text("She grips it tight, pointing at you.", text_font, (255, 255, 255), 40, 100, 250)
        draw_text("It's a knife.", text_font, (255, 255, 255), 40, 100, 300)
        draw_text("Press Space to continue", text_font, (255, 0, 255), 40, 100, 450)
    elif message_counter == 9:
        draw_text("'Back off or I'll fuck you up' she says.", text_font, (255, 255, 255), 40, 100, 200)
        draw_text("'Woah' you say, taking a step back, then another", text_font, (255, 255, 255), 40, 100, 250)
        draw_text("She keeps pointing it at you, as you back away and leave", text_font, (255, 255, 255), 40, 100, 300)
        draw_text("Press Space to continue", text_font, (255, 0, 255), 40, 100, 450)
    elif message_counter == 10:
        draw_text("In this game, how many threats of violence occurred?", text_font, (255, 255, 255), 40, 100, 200)
        draw_text("Press the number on your keyboard to answer.", text_font, (255, 0, 255), 40, 100, 250)
    if number_answer == 4: #this is the correct answer
        screen.fill((0, 0, 0))
        draw_text("You got the answer correct. There were 4 threats,", text_font, (255, 255, 255), 40, 100, 200)
        draw_text("Cat-calling is a threat of violence.", text_font, (255, 255, 255), 40, 100, 250)
        draw_text("Thank you for playing 'It's Not Just A Compliment'.", text_font, (255, 0, 255), 40, 100, 400)
    if number_answer == 1: #for incorrect answers
        screen.fill((0, 0, 0))
        draw_text("Incorrect answer.", text_font, (255, 255, 255), 40, 100, 200)
        draw_text("Cat-calling is a threat of violence.", text_font, (255, 255, 255), 40, 100, 250)
        draw_text("It often is followed by real violence.", text_font, (255, 255, 255), 40, 100, 300)
        draw_text("It can cause fear of the same level as a physical threat.", text_font, (255, 255, 255), 40, 100, 350)
        draw_text("You can try again by pressing a new number.", text_font, (255, 0, 255), 40, 100, 400)


    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()








