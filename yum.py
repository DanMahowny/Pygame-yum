import random
import pygame


pygame.init()
pygame.display.set_caption('YUM')
########### Sounds ##############
SOUNDSLIB = \
('BURGER',
 'CESTJUSTEUNFORDF150',
 'CRISS',
 'DEADOBIES',
 'MONAK',
 'PAQUETTE',
 'RAISONNABLE',
 'SCUSEFILLE',
 'SPAUNCHEVROLET',
 'SPAUNGMC')
burger = pygame.mixer.Sound("Soundeffects\\" + SOUNDSLIB[0] + ".wav")
############# COLORS ############
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
LIME = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN__AQUA = (0, 255, 255)
MAGENTA__FUCHSIA = (255, 0, 255)
SILVER = (192, 192, 192)
GRAY = (128, 128, 128)
MAROON = (128, 0, 0)
OLIVE = (128, 128, 0)
GREEN = (0, 128, 0)
PURPLE = (128, 0, 128)
TEAL = (0, 128, 128)
NAVY = (0, 0, 128)
MAROON = (128, 0, 0)
DARK_RED = (139, 0, 0)
BROWN = (165, 42, 42)
FIREBRICK = (178, 34, 34)
CRIMSON = (220, 20, 60)
RED = (255, 0, 0)
TOMATO = (255, 99, 71)
CORAL = (255, 127, 80)
INDIAN_RED = (205, 92, 92)
LIGHT_CORAL = (240, 128, 128)
DARK_SALMON = (233, 150, 122)
SALMON = (250, 128, 114)
LIGHT_SALMON = (255, 160, 122)
ORANGE_RED = (255, 69, 0)
DARK_ORANGE = (255, 140, 0)
ORANGE = (255, 165, 0)
GOLD = (255, 215, 0)
DARK_GOLDEN_ROD = (184, 134, 11)
GOLDEN_ROD = (218, 165, 32)
PALE_GOLDEN_ROD = (238, 232, 170)
DARK_KHAKI = (189, 183, 107)
KHAKI = (240, 230, 140)
OLIVE = (128, 128, 0)
YELLOW = (255, 255, 0)
YELLOW_GREEN = (154, 205, 50)
DARK_OLIVE_GREEN = (85, 107, 47)
OLIVE_DRAB = (107, 142, 35)
LAWN_GREEN = (124, 252, 0)
CHART_REUSE = (127, 255, 0)
GREEN_YELLOW = (173, 255, 47)
DARK_GREEN = (0, 100, 0)
GREEN = (0, 128, 0)
FOREST_GREEN = (34, 139, 34)
LIME = (0, 255, 0)
LIME_GREEN = (50, 205, 50)
LIGHT_GREEN = (144, 238, 144)
PALE_GREEN = (152, 251, 152)
DARK_SEA_GREEN = (143, 188, 143)
MEDIUM_SPRING_GREEN = (0, 250, 154)
SPRING_GREEN = (0, 255, 127)
SEA_GREEN = (46, 139, 87)
MEDIUM_AQUA_MARINE = (102, 205, 170)
MEDIUM_SEA_GREEN = (60, 179, 113)
LIGHT_SEA_GREEN = (32, 178, 170)
DARK_SLATE_GRAY = (47, 79, 79)
TEAL = (0, 128, 128)
DARK_CYAN = (0, 139, 139)
AQUA = (0, 255, 255)
CYAN = (0, 255, 255)
LIGHT_CYAN = (224, 255, 255)
DARK_TURQUOISE = (0, 206, 209)
TURQUOISE = (64, 224, 208)
MEDIUM_TURQUOISE = (72, 209, 204)
PALE_TURQUOISE = (175, 238, 238)
AQUA_MARINE = (127, 255, 212)
POWDER_BLUE = (176, 224, 230)
CADET_BLUE = (95, 158, 160)
STEEL_BLUE = (70, 130, 180)
CORN_FLOWER_BLUE = (100, 149, 237)
DEEP_SKY_BLUE = (0, 191, 255)
DODGER_BLUE = (30, 144, 255)
LIGHT_BLUE = (173, 216, 230)
SKY_BLUE = (135, 206, 235)
LIGHT_SKY_BLUE = (135, 206, 250)
MIDNIGHT_BLUE = (25, 25, 112)
NAVY = (0, 0, 128)
DARK_BLUE = (0, 0, 139)
MEDIUM_BLUE = (0, 0, 205)
BLUE = (0, 0, 255)
ROYAL_BLUE = (65, 105, 225)
BLUE_VIOLET = (138, 43, 226)
INDIGO = (75, 0, 130)
DARK_SLATE_BLUE = (72, 61, 139)
SLATE_BLUE = (106, 90, 205)
MEDIUM_SLATE_BLUE = (123, 104, 238)
MEDIUM_PURPLE = (147, 112, 219)
DARK_MAGENTA = (139, 0, 139)
DARK_VIOLET = (148, 0, 211)
DARK_ORCHID = (153, 50, 204)
MEDIUM_ORCHID = (186, 85, 211)
PURPLE = (128, 0, 128)
THISTLE = (216, 191, 216)
PLUM = (221, 160, 221)
VIOLET = (238, 130, 238)
MAGENTA__FUCHSIA = (255, 0, 255)
ORCHID = (218, 112, 214)
MEDIUM_VIOLET_RED = (199, 21, 133)
PALE_VIOLET_RED = (219, 112, 147)
DEEP_PINK = (255, 20, 147)
HOT_PINK = (255, 105, 180)
LIGHT_PINK = (255, 182, 193)
PINK = (255, 192, 203)
ANTIQUE_WHITE = (250, 235, 215)
BEIGE = (245, 245, 220)
BISQUE = (255, 228, 196)
BLANCHED_ALMOND = (255, 235, 205)
WHEAT = (245, 222, 179)
CORN_SILK = (255, 248, 220)
LEMON_CHIFFON = (255, 250, 205)
LIGHT_GOLDEN_ROD_YELLOW = (250, 250, 210)
LIGHT_YELLOW = (255, 255, 224)
SADDLE_BROWN = (139, 69, 19)
SIENNA = (160, 82, 45)
CHOCOLATE = (210, 105, 30)
PERU = (205, 133, 63)
SANDY_BROWN = (244, 164, 96)
BURLY_WOOD = (222, 184, 135)
TAN = (210, 180, 140)
ROSY_BROWN = (188, 143, 143)
MOCCASIN = (255, 228, 181)
NAVAJO_WHITE = (255, 222, 173)
PEACH_PUFF = (255, 218, 185)
MISTY_ROSE = (255, 228, 225)
LAVENDER_BLUSH = (255, 240, 245)
LINEN = (250, 240, 230)
OLD_LACE = (253, 245, 230)
PAPAYA_WHIP = (255, 239, 213)
SEA_SHELL = (255, 245, 238)
MINT_CREAM = (245, 255, 250)
SLATE_GRAY = (112, 128, 144)
LIGHT_SLATE_GRAY = (119, 136, 153)
LIGHT_STEEL_BLUE = (176, 196, 222)
LAVENDER = (230, 230, 250)
FLORAL_WHITE = (255, 250, 240)
ALICE_BLUE = (240, 248, 255)
GHOST_WHITE = (248, 248, 255)
HONEYDEW = (240, 255, 240)
IVORY = (255, 255, 240)
AZURE = (240, 255, 255)
SNOW = (255, 250, 250)
BLACK = (0, 0, 0)
DIM_GRAY__DIM_GREY = (105, 105, 105)
GRAY__GREY = (128, 128, 128)
DARK_GRAY__DARK_GREY = (169, 169, 169)
SILVER = (192, 192, 192)
LIGHT_GRAY__LIGHT_GREY = (211, 211, 211)
GAINSBORO = (220, 220, 220)
WHITE_SMOKE = (245, 245, 245)
WHITE = (255, 255, 255)

############ FONTS ##########
H1 = pygame.font.SysFont('times new roman', 18)
H2 = pygame.font.SysFont('times new roman', 16)
H3 = pygame.font.SysFont('times new roman', 18)
H4 = pygame.font.SysFont('times new roman', 20)
H5 = pygame.font.SysFont('times new roman', 25)
H6 = pygame.font.SysFont('times new roman', 30)
A_FONT = pygame.font.SysFont('times new roman', 40)

gametotal = 0
appliedbonus = False

# (1) initial dice number, (2) Bool "keep dice" flag, (3) Rect GUI position
dices = [[None, False, None] for x in range(5)]

DICEFACES = {1: DARK_KHAKI, 2: DARK_MAGENTA, 3: DARK_GOLDEN_ROD, 4:DARK_ORCHID, 5: DARK_SEA_GREEN, 6: DARK_VIOLET}
NUMTURNS = 3
turnsremaining = NUMTURNS
SHORTSTRAIGHTS = ((1, 2, 3, 4), (1, 2, 3, 4, 6), (2, 3, 4, 5), (3, 4, 5, 6), (1, 3, 4, 5, 6), (1, 2, 3, 4, 5), (2, 3, 4, 5, 6))
LONGSTRAIGHTS = ((1, 2, 3, 4, 5), (2, 3, 4, 5, 6))
FIELDS = [  # [Field name, rule, top/down flag, rect position, Field score]
    ['Ones' ,'sum(x for (x, _, _ ) in dices if x==1)' ,True ,None ,None],
    ['Twos' ,'sum(x for (x, _, _ ) in dices if x==2)' ,True ,None ,None],
    ['Trees' ,'sum(x for (x, _, _ ) in dices if x==3)' ,True ,None ,None],
    ['Fours' ,'sum(x for (x, _, _ ) in dices if x==4)' ,True ,None ,None],
    ['Fives' ,'sum(x for (x, _, _ ) in dices if x==5)' ,True ,None ,None],
    ['Sixes' ,'sum(x for (x, _, _ ) in dices if x==6)' ,True ,None ,None],
    ['Bonus' ,None ,None ,None ,None],
    ['' ,'' ,None ,None ,None],
    ['Three of a kind' ,'sum(puredices) if max(dicesfreq.values())>=3 else 0',False ,None ,None],
    ['Four of a kind' ,'sum(puredices) if max(dicesfreq.values())>=4 else 0' ,False ,None ,None],
    ['Short straight' ,'15 if tuple(sorted(set(puredices))) in SHORTSTRAIGHTS else 0' ,False ,None ,None],
    ['Long straight' ,'20 if tuple(sorted(set(puredices))) in LONGSTRAIGHTS else 0' ,False ,None ,None],
    ['High Roll' ,'sum(x for (x, _, _ ) in dices)' ,False ,None ,None],
    ['Full house' ,'25 if len(set(puredices))<=2 else 0' ,False ,None ,None],
    ['YUM' ,'30 if len(set(puredices)) == 1 else 0' ,False ,None ,None]               
    ]
NOPRINTFIELDS = ('Bonus', '')
###########GAME OPTIONS
FPS= 30
CLOCK = pygame.time.Clock()
done = False
roll = True
turnend = False # Will become True if I assign points to the board, else False
rouley = 150
STARTWRITE = rouley + 60
####GUI APPEARANCE OPTIONS #######
WINDOWWIDTH = 500
WINDOWHEIGHT = 600
SCREEN = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
background = pygame.Surface((WINDOWWIDTH, WINDOWHEIGHT))
background.fill(YELLOW)
SCREEN.blit(background,(0,0))
SCORINGBOXESX = 150
##### Default dice GUI output settings ####
SIZE = 50
CORNERSIZE = 20
HALFCORNER = int(CORNERSIZE / 2)
DOTSIZE = int(SIZE / 10)
DICEPADDING = int((WINDOWWIDTH - (5 * SIZE + CORNERSIZE)) / (len(dices) + 1) )
DICEXPOSITIONS = range(DICEPADDING, len(dices) * (DICEPADDING + SIZE), DICEPADDING + SIZE)
assert DICEPADDING >= 15, 'DICES TOO BIG FOR OUR SURFACE'

def initbackground(textandboxY):
    """my background surface"""
    #Title, well centered
    text = A_FONT.render('ANTICIPE UN YUM', True, BLACK)
    textrect = text.get_rect()
    textx = int(background.get_rect().centerx - textrect.width / 2)
    background.blit(text, (textx, 10))
    #Write the "Roll" box
    text = A_FONT.render('ROULE!', True, BLACK)
    roulex = int(background.get_rect().centerx - text.get_rect().width / 2 )

    pygame.draw.rect(background, GREEN_YELLOW, (roulex , rouley , text.get_rect().width+ 20, 50), 0)
    ROLLBOX = pygame.draw.rect(background, BLACK, (roulex , rouley , text.get_rect().width+ 20, 50), 2)
    background.blit(text, (roulex + 10, rouley +5))   
    #Write all text fields and the boxes to click
    for index, fielddata in enumerate(FIELDS):
        if fielddata[0] not in NOPRINTFIELDS:
            FIELDS[index][3] = pygame.draw.rect(background, LIGHT_CORAL, (SCORINGBOXESX, textandboxY, 35 ,H1.get_height() + 2), 0)
        text = H1.render(fielddata[0], True, BLACK)
        background.blit(text, (30, textandboxY))
        textandboxY += H1.get_height() + 4   
    return ROLLBOX

def wipeboxes(boxesstart, *args):
    for x in FIELDS:
        if x[4] == None and x[0] not in NOPRINTFIELDS:
            pygame.draw.rect(background, LIGHT_CORAL, (150, boxesstart, 35 ,H1.get_height() + 2), 0)
        boxesstart += H1.get_height() + 4
def keepboxesanim():
    pixeloffset = -2    
    for diceidx, (_ , keepflag, (x, y, xsize, ysize) ) in enumerate(dices):
        if keepflag:
            pygame.draw.rect(background, GREEN, (x, y + ysize+ pixeloffset, xsize, 10), 0)
        if not keepflag:
            pygame.draw.rect(background, RED, (x, y + ysize+ pixeloffset, xsize, 10), 0)
            
def printadice(xcoord, ycoord, dicevalue):
    """prints a cute dice on screen"""
    #This is my prettified square
    dicecolor = DICEFACES[dicevalue]
    o =pygame.draw.rect(background, dicecolor, (xcoord , ycoord - HALFCORNER, SIZE, SIZE + CORNERSIZE), 0)
    pygame.draw.rect(background, dicecolor, (xcoord - HALFCORNER, ycoord, SIZE + CORNERSIZE, SIZE), 0)
    pygame.draw.circle(background, dicecolor, (xcoord, ycoord), HALFCORNER, 0)
    pygame.draw.circle(background, dicecolor, (int(xcoord + SIZE), ycoord), HALFCORNER, 0)
    pygame.draw.circle(background, dicecolor, (xcoord, int(ycoord + SIZE)), HALFCORNER, 0)
    pygame.draw.circle(background, dicecolor, (xcoord + SIZE, ycoord + SIZE), HALFCORNER, 0)
    #####These are my dots!!! ###
    if dicevalue in (1, 3, 5):
        pygame.draw.circle(background, BLACK, o.center, DOTSIZE, 0)
    if dicevalue in (2, 3, 4 ,5 , 6):
        pygame.draw.circle(background, BLACK, (xcoord + 10, ycoord + 10), DOTSIZE, 0)
    if dicevalue in (4, 5, 6):
        pygame.draw.circle(background, BLACK, (xcoord - 10 + SIZE, ycoord + 10), DOTSIZE, 0)
    if dicevalue == 6:
        pygame.draw.circle(background, BLACK, (xcoord + 10, o.centery), DOTSIZE, 0)
        pygame.draw.circle(background, BLACK, (xcoord -10 + SIZE, o.centery), DOTSIZE, 0)
    if dicevalue in (4, 5, 6):
        pygame.draw.circle(background, BLACK, (xcoord + 10, ycoord - 10 + SIZE), DOTSIZE, 0)
    if dicevalue in (2, 3, 4, 5, 6):
        pygame.draw.circle(background, BLACK, (xcoord - 10 + SIZE, ycoord - 10 + SIZE), DOTSIZE, 0)

def rolldices():
    """Returns shuffled dices"""
    global burger
    for diceidx, (_ , keepflag, _ ) in enumerate(dices):
        if not keepflag:
            dices[diceidx][0] = random.choice(list(DICEFACES.keys()))
    
    pygame.mixer.Sound.stop(burger)
    burger = pygame.mixer.Sound("Soundeffects\\" + random.choice(SOUNDSLIB) + ".wav")
    pygame.mixer.Sound.play(burger)
    return dices

def checkdone():
    """Switched the 'done' variable to True if we are done playing"""
    global gametotal
    for _ ,_ ,keepflag ,_ , score  in FIELDS:
        if keepflag == True or keepflag == False:
            if score == None:
                return False
    gametotal = 0
    return True

def printscore():
    #The total score, on screen!
    pygame.draw.rect(background, LIGHT_YELLOW, (325, 215, 106, 65), 0)
    text = H6.render('TOTAL', True, BLACK)
    background.blit(text, (330, 220))
    text = H5.render(str(gametotal), True, BLACK)
    background.blit(text, (340, 250))
    
def printsubtotals():
    topscore = 0
    bottomscore = 0
    for _ ,_ ,bflag ,_ ,score in FIELDS:      
        if bflag == True and score != None:
            topscore += score
        elif bflag == False and score != None:
            bottomscore += score
    pygame.draw.rect(background, LIGHT_YELLOW, (325, 315, 150, 65), 0)
    text = H5.render('Score en haut', True, BLACK)
    background.blit(text, (330, 320))
    text = H5.render(str(topscore), True, BLACK)
    background.blit(text, (340, 350))
    pygame.draw.rect(background, LIGHT_YELLOW, (325 ,WINDOWHEIGHT - 100 ,150 ,65),0)
    text = H5.render('Score en bas', True, BLACK)
    background.blit(text, (330, WINDOWHEIGHT - 95)) 
    text = H5.render(str(bottomscore), True, BLACK)
    background.blit(text, (330, WINDOWHEIGHT - 65))
def applyandshowbonus():
    global appliedbonus, gametotal
    topscore = 0
    for _ ,_ ,flag ,_ ,score in FIELDS:      
        if flag == True and score != None:
            topscore +=score
    bonus = 25 if topscore >= 63 else 0
    if bonus == 25:
        text = H5.render(str(bonus), True, BLACK)
        background.blit(text, (SCORINGBOXESX, 365))
    if not appliedbonus and bonus == 25:
        gametotal += 25
        appliedbonus = True
    return None
        
ROLLBOXcoords = initbackground(STARTWRITE)

while not done:
    #Event handling!
    done = checkdone()
    mouse = (0,0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouse = pygame.mouse.get_pos()
          
    if ROLLBOXcoords.collidepoint(mouse):
        
        roll = True
        
        if turnend:
            turnsremaining = 3
            turnline[4] = turnpoints
            FIELDS = [turnline if x[0] == turnline[0] else x for x in FIELDS]
#            Resets "Keep" flag to False
            dices = [[a , False, c] for a, b, c in dices]
#            makes it pretty at the GUI level
            keepboxesanim()
            turnline = None
            gametotal += turnpoints
            turnend = False
            print(gametotal)
        else: 
            pass

    #this is the part that actually rolls dices   
    if turnsremaining > 0 and roll:
        dices = rolldices()
        #so we wont roll twice
        roll = False
        turnsremaining -= 1
        #prints them on screen
        for dicenum, (diceval, _, _ ) in enumerate(dices):
            xstart = DICEPADDING + dicenum * (SIZE + DICEPADDING)
            ystart = 65
            realsize = SIZE + CORNERSIZE
            printadice(xstart ,ystart , diceval)
            #adds the rect coordinates to the dice's data structure
            dices[dicenum][2] = pygame.Rect(xstart - HALFCORNER ,ystart ,realsize ,realsize)
    
    for position, (_ ,flag ,rect) in enumerate(dices):
        if rect.collidepoint(mouse):
            # We switch True to False and the other way around if we clicked!
            dices[position][1] = not dices[position][1]
            keepboxesanim()
            
        for dicenum, (diceval ,_ ,_ ) in enumerate(dices):
            printadice(DICEPADDING + dicenum * (SIZE + DICEPADDING) ,65 , diceval)
            
    #Only for points computation: ugly and shouldnt be used!
    puredices = [x for x, y, z in dices]
    dicesfreq = {x : puredices.count(x) for x in puredices}
        
    #Writes down our points where we assign them, or reverses previously written points
    for position, line in enumerate(FIELDS):
        if line[0] not in NOPRINTFIELDS:
            if line[3].collidepoint(mouse):
                
                if turnend == True:
                    #We already had something in, we need to erase it!
                    turnend = False
                    wipeboxes(STARTWRITE)                    
                else:   
                    turnend = True
                    wipeboxes(STARTWRITE)
                    #Tentatively write my score in proper field
                    turnpoints = eval(line[1])
                    turnline = line
                    scoretext = H1.render(str(turnpoints), True, BLACK)
                    background.blit(scoretext, (line[3][0] + 10, line[3][1] + 1))   
                    
    SCREEN.blit(background, (0,0))
    
    applyandshowbonus()
    printsubtotals()
    printscore()   
    pygame.display.flip()
    CLOCK.tick(FPS)

#Delay only if we are done with the game  
CLOCK.tick(.333) if checkdone() else None
pygame.quit()