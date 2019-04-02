# THE PROGRAM IS FLAWED IN THE WAY THAT IT TAKES ANY WORD WITH THE SUFFIx -AR, -ER OR -IR AS A VERB AND CONJUGATES IT.
# IDEALLY IT SHOULD PEFORM A BINARY SEACH ON A LIST CONTAINING ALL VERBS INSTEAD.

import pygame

pygame.init()
def pronouns():

    if pronouns_on:
        pronoun1_text = smallFont.render('Yo', True, black)
        pronoun2_text = smallFont.render('Tú', True, black)
        pronoun3_text = smallFont.render('El/Ella/Usted', True, black)
        pronoun4_text = smallFont.render('Nosotros', True, black)
        pronoun5_text = smallFont.render('Vosotros', True, black)
        pronoun6_text = smallFont.render('Ellos/Ustedes', True, black)

        window.blit(pronoun1_text, (15, 175))
        window.blit(pronoun2_text, (15, 175 + 35))
        window.blit(pronoun3_text, (15, 175 + 70))
        window.blit(pronoun4_text, (15, 175 + 105))
        window.blit(pronoun5_text, (15, 175 + 140))
        window.blit(pronoun6_text, (15, 175 + 175))

        pygame.draw.rect(window, color_inactive, (10, 170, 340, 215), 1)

        pygame.draw.line(window, color_inactive, (10, 205), (350, 205), 1)
        pygame.draw.line(window, color_inactive, (10, 240), (350, 240), 1)
        pygame.draw.line(window, color_inactive, (10, 275), (350, 275), 1)
        pygame.draw.line(window, color_inactive, (10, 315), (350, 315), 1)
        pygame.draw.line(window, color_inactive, (10, 350), (350, 350), 1)
        pygame.draw.line(window, color_inactive, (190, 170), (190, 385), 1)


def filled_square():
    if filled_square_on == True:
        pygame.draw.rect(window, white, (10, 170, 340, 215))



# colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')

size = 600, 400
window = pygame.display.set_mode(size)
FPS = 30
clock = pygame.time.Clock()

# fonts
xsmallFont = pygame.font.SysFont('Arial', 15)
smallFont = pygame.font.SysFont('Arial', 25)
largeFont = pygame.font.SysFont('Arial', 40)

done = False
active = False
pronouns_on = False
filled_square_on = False
color = color_inactive

input_text = smallFont.render('Verb:', True, black)
input_text_rect = input_text.get_rect()
input_text_rect.center = 45, 110


input_box = pygame.Rect(100, 90, 140, 40)
verb = ''
conjugated_verb1 = ''
conjugated_verb2 = ''
conjugated_verb3 = ''
conjugated_verb4 = ''
conjugated_verb5 = ''
conjugated_verb6 = ''

irreg_message_string = ''
irreg_verbs_dict = {'ir': ['voy', 'vas', 'va', 'vamos', 'vais', 'van'], 'venir': ['vengo', 'vienes', 'viene', 'venimos', 'venís', 'vienen'], 'tener': ['tengo', 'tienes', 'tiene', 'tenemos', 'tenéis', 'tienen'], 'ver': ['veo', 'ves', 've', 'vemos', 'veis', 'ven']}

while not done:
    window.fill(white)
    input_txt_surface = smallFont.render(verb, True, color)
    irreg_message = xsmallFont.render(irreg_message_string, True, red)
    output_txt_surface1 = smallFont.render(conjugated_verb1, True, color_inactive)
    output_txt_surface2 = smallFont.render(conjugated_verb2, True, color_inactive)
    output_txt_surface3 = smallFont.render(conjugated_verb3, True, color_inactive)
    output_txt_surface4 = smallFont.render(conjugated_verb4, True, color_inactive)
    output_txt_surface5 = smallFont.render(conjugated_verb5, True, color_inactive)
    output_txt_surface6 = smallFont.render(conjugated_verb6, True, color_inactive)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                active = True
            else:
                active = False
            color = color_active if active else color_inactive
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    filled_square_on = False
                    pronouns_on = True
                    # see if verb is irregular
                    if verb in irreg_verbs_dict:
                        irreg_message_string = 'Irregular verb. ' \
                                               'Special rules apply for conjugation.'
                        # if there's a match with a key ,return all the corresponding values,
                        # and store them in their respective variables.
                        for key, value in irreg_verbs_dict.items():
                            if key == verb:
                                conjugated_verb1 = value[0]
                                conjugated_verb2 = value[1]
                                conjugated_verb3 = value[2]
                                conjugated_verb4 = value[3]
                                conjugated_verb5 = value[4]
                                conjugated_verb6 = value[5]
                    # see what kind of regular verb it is
                    elif verb.endswith('ar'):
                        # reset string irreg_message_sting
                        irreg_message_string = ''
                        conjugated_verb1 = verb[:-2] + 'o'
                        conjugated_verb2 = verb[:-2] + 'as'
                        conjugated_verb3 = verb[:-2] + 'a'
                        conjugated_verb4 = verb[:-2] + 'amos'
                        conjugated_verb5 = verb[:-2] + 'ais'
                        conjugated_verb6 = verb[:-2] + 'an'
                    elif verb.endswith('er'):
                        # reset string irreg_message_sting
                        irreg_message_string = ''
                        conjugated_verb1 = verb[:-2] + 'o'
                        conjugated_verb2 = verb[:-2] + 'es'
                        conjugated_verb3 = verb[:-2] + 'e'
                        conjugated_verb4 = verb[:-2] + 'emos'
                        conjugated_verb5 = verb[:-2] + 'eis'
                        conjugated_verb6 = verb[:-2] + 'en'
                    elif verb.endswith('ir'):
                        # reset string irreg_message_sting
                        irreg_message_string = ''
                        conjugated_verb1 = verb[:-2] + 'o'
                        conjugated_verb2 = verb[:-2] + 'es'
                        conjugated_verb3 = verb[:-2] + 'e'
                        conjugated_verb4 = verb[:-2] + 'imos'
                        conjugated_verb5 = verb[:-2] + 'is'
                        conjugated_verb6 = verb[:-2] + 'en'
                    # if not a verb:
                    else:
                        irreg_message_string = str(verb)
                        irreg_message_string += ' is not a verb'
                        filled_square_on = True

                    verb = ''
                # delete last character
                elif event.key == pygame.K_BACKSPACE:
                    verb = verb[:-1]
                # add letter of pushed key to string
                else:
                    verb += event.unicode


    #####------#####
    pronouns()
    width = max(200, input_txt_surface.get_width()+10)
    input_box.w = width
    window.blit(input_txt_surface, (input_box.x+5, input_box.y+5))
    # window.blit(output_text, output_text_rect)
    window.blit(output_txt_surface1, (200, 175))
    window.blit(output_txt_surface2, (200, 175 + 35))
    window.blit(output_txt_surface3, (200, 175 + 70))
    window.blit(output_txt_surface4, (200, 175 + 105))
    window.blit(output_txt_surface5, (200, 175 + 140))
    window.blit(output_txt_surface6, (200, 175 + 175))
    window.blit(input_text, input_text_rect)
    pygame.draw.rect(window, color, input_box, 2)
    window.blit(irreg_message, (10, 150))

    filled_square()
    pygame.display.update()
    clock.tick(FPS)
    #####------#####

pygame.quit()
