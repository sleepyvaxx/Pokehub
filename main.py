import requests
import pygame
import button

# declaring variables
choice1 = False
choice2 = False
choice3 = False
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800

pygame.init()
# creating the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pokehub")

# creating images
# berry images
back_img = pygame.image.load("back.png").convert_alpha()
berry_img = pygame.image.load("Berry.png").convert_alpha()
berry1_img = pygame.image.load("Berry1.png").convert_alpha()
berry2_img = pygame.image.load("Berry2.png").convert_alpha()
berry3_img = pygame.image.load("Berry3.png").convert_alpha()
berry4_img = pygame.image.load("Berry4.png").convert_alpha()
berry5_img = pygame.image.load("Berry5.png").convert_alpha()
berry6_img = pygame.image.load("Berry6.png").convert_alpha()
berry7_img = pygame.image.load("Berry7.png").convert_alpha()
berry8_img = pygame.image.load("Berry8.png").convert_alpha()
berry9_img = pygame.image.load("Berry9.png").convert_alpha()
berry10_img = pygame.image.load("Berry10.png").convert_alpha()
# item images
it_img = pygame.image.load("item.png").convert_alpha()
it1_img = pygame.image.load("item1.png").convert_alpha()
it2_img = pygame.image.load("item2.png").convert_alpha()
it3_img = pygame.image.load("item3.png").convert_alpha()
it4_img = pygame.image.load("item4.png").convert_alpha()
it5_img = pygame.image.load("item5.png").convert_alpha()
it6_img = pygame.image.load("item6.png").convert_alpha()
it7_img = pygame.image.load("item7.png").convert_alpha()
it8_img = pygame.image.load("item8.png").convert_alpha()
it9_img = pygame.image.load("item9.png").convert_alpha()
it10_img = pygame.image.load("item10.png").convert_alpha()

# pokemon images
pok_img = pygame.image.load("pok.png").convert_alpha()
pok1_img = pygame.image.load("pok1.png").convert_alpha()
pok2_img = pygame.image.load("pok2.png").convert_alpha()
pok3_img = pygame.image.load("pok3.png").convert_alpha()
pok4_img = pygame.image.load("pok4.png").convert_alpha()
pok5_img = pygame.image.load("pok5.png").convert_alpha()
pok6_img = pygame.image.load("pok6.png").convert_alpha()
pok7_img = pygame.image.load("pok7.png").convert_alpha()
pok8_img = pygame.image.load("pok8.png").convert_alpha()
pok9_img = pygame.image.load("pok9.png").convert_alpha()
pok10_img = pygame.image.load("pok10.png").convert_alpha()

# creating the buttons attributes
# berry attributes
back = button.Button(670, 670, back_img, 0.25)
bryButton = button.Button(10, 10, berry_img, 0.5)
bry1 = button.Button(10, 310, berry1_img, 3)
bry2 = button.Button(100, 310, berry2_img, 3)
bry3 = button.Button(200, 310, berry3_img, 3)
bry4 = button.Button(300, 310, berry4_img, 3)
bry5 = button.Button(400, 310, berry5_img, 3)
bry6 = button.Button(500, 310, berry6_img, 3)
bry7 = button.Button(600, 310, berry7_img, 3)
bry8 = button.Button(10, 400, berry8_img, 3)
bry9 = button.Button(100, 400, berry9_img, 3)
bry10 = button.Button(200, 400, berry10_img, 3)
# item attributes
itemButton = button.Button(160, 30, it_img, 3)
it1 = button.Button(10, 310, it1_img, 3)
it2 = button.Button(100, 310, it2_img, 3)
it3 = button.Button(200, 310, it3_img, 3)
it4 = button.Button(300, 310, it4_img, 3)
it5 = button.Button(400, 310, it5_img, 3)
it6 = button.Button(500, 310, it6_img, 3)
it7 = button.Button(600, 310, it7_img, 3)
it8 = button.Button(10, 400, it8_img, 3)
it9 = button.Button(100, 400, it9_img, 3)
it10= button.Button(200, 400, it10_img, 3)

# pokemon attributes
pokButton = button.Button(300, 20, pok_img, 3)
pok1 = button.Button(10, 160, pok1_img, 1)
pok2 = button.Button(150, 160, pok2_img, 1)
pok3 = button.Button(300, 160, pok3_img, 1)
pok4 = button.Button(450, 160, pok4_img, 1)
pok5 = button.Button(600, 160, pok5_img, 1)
pok6 = button.Button(10, 350, pok6_img, 1)
pok7 = button.Button(150, 350, pok7_img, 1)
pok8 = button.Button(300, 350, pok8_img, 1)
pok9 = button.Button(450, 350, pok9_img, 1)
pok10= button.Button(600, 350, pok10_img, 1)


# clock pogchamp
clock = pygame.time.Clock()


# requests definitions
def link():
    link = "https://pokeapi.co/api/v2/" + all_menus.userin + "/" + all_menus.userin2 + "/"
    print(link)
    api = requests.get(link)
    dataget = api.json()
    data.all_data = dataget
    print(dataget)
    data.get_keys_create_buttons()


class data:
    """
    all_data never changes, entire thing

    key_chain which keeps track of the buttons (properties of pokemon) that they clicked

    buttons: list of buttons to be drawn on the screen

    property_value_text is text (pygame surface) to be created on the screen
    """
    all_data: dict
    key_chain: list = []
    buttons: list = []
    property_value_text: pygame.surface.Surface = None

    @staticmethod
    def go_back():
        if not data.key_chain:
            # clear the first buttons!
            data.buttons = []
            return False
        data.key_chain.pop()
        data.get_keys_create_buttons()
        return True

    @staticmethod
    def go_forward_add_key_to_chain(key_name):
        data.key_chain.append(key_name)
        data.get_keys_create_buttons()

    @staticmethod
    def get_keys_create_buttons():
        nested_data = data.all_data
        for key in data.key_chain:
            if type(nested_data) == list:
                key = int(key)
            nested_data = nested_data[key]
        data.buttons = []

        print(nested_data)
        if type(nested_data) != dict and type(nested_data) != list:
            data.property_value_text = font.render(str(nested_data), True, (0, 0, 0))
            return
        else:
            # make it go away!
            data.property_value_text = None

        if type(nested_data) == list:
            keylist = list(range(len(nested_data)))
        else:
            keylist = list(nested_data.keys())
        xb = 10
        yb = 10
        for i in range(0, len(keylist)):
            print(keylist[i])
            xb = xb + 150
            if xb > 750:
                xb = 10
                yb = yb + 100
            bryi = button.Button(xb, yb, all_menus.img, 3, str(keylist[i]))
            # this line below, makes sure that the button does not get clicked
            bryi.clicked = True  # pretending that it was clicked already
            data.buttons.append(bryi)

        # call generate_buttons

    @staticmethod
    def draw_all_buttons():
        # print("all buttons are being drawn")
        if not data.buttons:
            return

        for i in range(0, len(data.buttons)):
            # print("drawing button i = ", i)
            if data.buttons[i].draw(screen):
                print("something was clicked!!!!!!!")
                data.go_forward_add_key_to_chain(data.buttons[i].key_name)
                break


class menus:
    def __init__(self):
        self.img = None
        self.userin = None
        self.userin2 = None
        self.choice1 = False
        self.choice2 = False
        self.choice3 = False

    def menu1(self):
        if bryButton.draw(screen):
            self.userin = "berry"
            self.choice1 = True
        if itemButton.draw(screen):
            self.userin = "item"
            self.choice2 = True
        if pokButton.draw(screen):
            self.userin = "pokemon"
            self.choice3 = True

    def menu2(self):
        if data.buttons:
            # at this current frame, whatever buttons are in the list, they will be drawn
            data.draw_all_buttons()
        else:
            if bry1.draw(screen):
                self.userin2 = "1"
                self.img = berry1_img
                link()
            if bry2.draw(screen):
                self.userin2 = "2"
                self.img = berry2_img
                link()
            if bry3.draw(screen):
                self.userin2 = "3"
                self.img = berry3_img
                link()
            if bry4.draw(screen):
                self.userin2 = "4"
                self.img = berry4_img
                link()
            if bry5.draw(screen):
                self.userin2 = "5"
                self.img = berry5_img
                link()
            if bry6.draw(screen):
                self.userin2 = "6"
                self.img = berry6_img
                link()
            if bry7.draw(screen):
                self.userin2 = "7"
                self.img = berry7_img
                link()
            if bry8.draw(screen):
                self.userin2 = "8"
                self.img = berry8_img
                link()
            if bry9.draw(screen):
                self.userin2 = "9"
                self.img = berry9_img
                link()
            if bry10.draw(screen):
                self.userin2 = "10"
                self.img = berry10_img
                link()

            if data.property_value_text is not None:
                screen.blit(data.property_value_text, (400, 400))

    def menu3(self):
        if data.buttons:
            # at this current frame, whatever buttons are in the list, they will be drawn
            data.draw_all_buttons()
        else:
            if it1.draw(screen):
                self.userin2 = "1"
                self.img = it1_img
                link()
            if it2.draw(screen):
                self.userin2 = "2"
                self.img = it2_img
                link()
            if it3.draw(screen):
                self.userin2 = "3"
                self.img = it3_img
                link()
            if it4.draw(screen):
                self.userin2 = "4"
                self.img = it4_img
                link()
            if it5.draw(screen):
                self.userin2 = "5"
                self.img = it5_img
                link()
            if it6.draw(screen):
                self.userin2 = "6"
                self.img = it6_img
                link()
            if it7.draw(screen):
                self.userin2 = "7"
                self.img = it7_img
                link()
            if it8.draw(screen):
                self.userin2 = "8"
                self.img = it8_img
                link()
            if it9.draw(screen):
                self.userin2 = "9"
                self.img = it9_img
                link()
            if it10.draw(screen):
                self.userin2 = "10"
                self.img = it10_img
                link()

            if data.property_value_text is not None:
                screen.blit(data.property_value_text, (50, 50))

    def menu4(self):
        if data.buttons:
            # at this current frame, whatever buttons are in the list, they will be drawn
            data.draw_all_buttons()
        else:
            if pok1.draw(screen):
                self.userin2 = "1"
                self.img = pok_img
                link()
            if pok2.draw(screen):
                self.userin2 = "2"
                self.img = pok_img
                link()
            if pok3.draw(screen):
                self.userin2 = "3"
                self.img = pok_img
                link()
            if pok4.draw(screen):
                self.userin2 = "4"
                self.img = pok_img
                link()
            if pok5.draw(screen):
                self.userin2 = "5"
                self.img = pok_img
                link()
            if pok6.draw(screen):
                self.userin2 = "6"
                self.img = pok_img
                link()
            if pok7.draw(screen):
                self.userin2 = "7"
                self.img = pok_img
                link()
            if pok8.draw(screen):
                self.userin2 = "8"
                self.img = pok_img
                link()
            if pok9.draw(screen):
                self.userin2 = "9"
                self.img = pok_img
                link()
            if pok10.draw(screen):
                self.userin2 = "10"
                self.img = pok_img
                link()

            if data.property_value_text is not None:
                screen.blit(data.property_value_text, (50, 50))


all_menus = menus()

font = pygame.font.SysFont("Comic Sans MS", 50)
run = True
while run:
    screen.fill((202, 228, 241))
    if back.draw(screen):
        there_are_berries = data.go_back()

        if not there_are_berries:
            if all_menus.choice1:
                all_menus.choice1 = False
                all_menus.userin2 = None
                all_menus.userin1 = None
            elif all_menus.choice2:
                all_menus.choice2 = False
                all_menus.userin2 = None
                all_menus.userin1 = None
            elif all_menus.choice3:
                all_menus.choice3 = False
                all_menus.userin2 = None
                all_menus.userin = None
            else:
                print("at the start moron")
    else:
        if all_menus.choice1:
            all_menus.menu2()
        elif all_menus.choice2:
            all_menus.menu3()
        elif all_menus.choice3:
            all_menus.menu4()
        else:
            all_menus.menu1()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()
