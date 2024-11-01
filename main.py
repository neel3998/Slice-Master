import pygame
import random
#for extracting image and sound files
from os import path
#we took help from the following link:
#https://www.youtube.com/channel/UCNaPQ5uLX5iIEHUCLmfAgKg
#Defining screen parameters
width=370
height=490
fps=50

#defining colours
white=(255,255,255)
black=(0,0,0)
blue=(0,0,255)
red=(255,0,0)
green=(0,255,0)
violet=(255,0,255)
lblue=(0,255,255)

#directories for initialising graphics and sound
image_dir = path.join(path.dirname(__file__), 'image')
sound_dir = path.join(path.dirname(__file__), 'sound')

#initialsing pygame          
pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Slice Master")
clock=pygame.time.Clock()
font_name=pygame.font.match_font('calibiri')

#function for displaying the score on top
#Reference:https://www.youtube.com/watch?v=U8yyrpuplwc&index=10&list=PLsk-HSGFjnaH5yghzu7PcOzm9NhsW0Urw
def textbox( surf, text,size,x,y):
    font= pygame.font.Font(font_name,size)
    text_surface=font.render(text,True,white)
    text_rect=text_surface.get_rect()
    text_rect.midtop=(x,y)
    surf.blit(text_surface,text_rect)
    
#class for knife
#Reference:https://www.youtube.com/watch?v=Eltz-XJMxuU&index=2&list=PLsk-HSGFjnaH5yghzu7PcOzm9NhsW0Urw    
class Player(pygame.sprite.Sprite):
#initialising the features of knife
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)        
        self.image=pygame.transform.scale(player_img,(30,60))
        self.image.set_colorkey(black)
        self.rect =self.image.get_rect()
        self.rect.centerx = (width/2)
        self.rect.bottom= height-5
        self.speedx1=0
        
#updating the movement of knife        
    def update(self):
        self.speedx1=0
        keystate=pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx1= -10
        if keystate[pygame.K_RIGHT]:
            self.speedx1=10
        self.rect.x += self.speedx1
#updating the movement of knife        
        if self.rect.right > width:
            self.rect.right=width
        if self.rect.left<0:
            self.rect.left=0
            
#class for bombs dropping down            
class Bomb(pygame.sprite.Sprite):
#initialsing the features of bomb    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=bomb_img
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.x=random.randrange(width -self.rect.width)
        self.rect.y= random.randrange(-90,-30)
        self.speedy1=random.randrange(3,6)
        
#updating the speed and postion of apple to be dropped
    def update(self):        
        self.rect.y+=self.speedy1
        if self.rect.top> height+5 or self.rect.left<-30 or self.rect.right> width +20:
            self.rect.x=random.randrange(width -self.rect.width)
            self.rect.y= random.randrange(-90,-30)
            self.speedy1=random.randrange(3,6)
            
#class for banana
class Fruit2(pygame.sprite.Sprite):
#initialsing features of banana    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=fruit2_img
        self.image.set_colorkey(white)
        self.rect= self.image.get_rect()
        self.rect.x=random.randrange(width -self.rect.width)
        self.rect.y= random.randrange(-90,-30)
        self.speedy1=random.randrange(3,6)        
#randomly setting speed and position of banana to be dropped
        
    def update(self):
        self.rect.y+=self.speedy1
        if self.rect.top> height+5 or self.rect.left<-30 or self.rect.right> width +20:
            self.rect.x=random.randrange(width -self.rect.width)
            self.rect.y= random.randrange(-90,-30)
            self.speedy1=random.randrange(3,6)
            
#class for apple
class Fruit3(pygame.sprite.Sprite):
   #initialsing the features of apple    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=fruit3_img
        self.image.set_colorkey(white)
        self.rect= self.image.get_rect()
        self.rect.x=random.randrange(width -self.rect.width)
        self.rect.y= random.randrange(-90,-30)
        self.speedy1=random.randrange(3,6)
        #updating the speed and postion of apple to be dropped
        
    def update(self):
        self.rect.y+=self.speedy1
        if self.rect.top> height+5 or self.rect.left<-30 or self.rect.right> width +20:
            self.rect.x=random.randrange(width -self.rect.width)
            self.rect.y= random.randrange(-90,-30)
            self.speedy1=random.randrange(3,6)
            
#class for pear 
class Fruit4(pygame.sprite.Sprite):
#initialising the features of pear
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=fruit4_img
        self.image.set_colorkey(white)
        self.rect= self.image.get_rect()
        self.rect.x=random.randrange(width -self.rect.width)
        self.rect.y= random.randrange(-90,-30)
        self.speedy1=random.randrange(3,6)
        
#updating the speed and position of pear to be dropped
#Reference:https://www.youtube.com/watch?v=fcryHcZE_sM&index=3&list=PLsk-HSGFjnaH5yghzu7PcOzm9NhsW0Urw
    def update(self):
       # self.rect.x+=self.speedx1
        self.rect.y+=self.speedy1
        if self.rect.top> height+5 or self.rect.left<-30 or self.rect.right> width +20:
            self.rect.x=random.randrange(width -self.rect.width)
            self.rect.y= random.randrange(-90,-30)
            self.speedy1=random.randrange(3,6)
            
#function for displaying the start screen            
def start_scr():
    #displaying text and instructions
#Reference:https://www.youtube.com/watch?v=Z2K2Yttvr5g&list=PLsk-HSGFjnaH5yghzu7PcOzm9NhsW0Urw&index=17    
    textbox(screen,"SLICE MASTER",50, width/2,height/4)
    textbox(screen," Fruits to be sliced.",24,width/2,height/2)
    textbox(screen,"Use left and right arrow keys to move the knife",24,width/2,height/2+30)
    textbox(screen,"Press a key to begin", 24, width/2,height/2+80)
    textbox(screen,"Press X at top of the screen to exit",24, width/2,height/2 +130)
#creation of text file for saving high score
    fin=open("highscore.txt")
    hs=int(fin.readline())
    fin.close()
    #updating and saving the highscore
    if score>hs:
        hs=score
        fout=open("highscore.txt", "w")
        fout.write(str(score))
        fout.close()
    #Displaying highscore 
    textbox(screen,"HIGHSCORE: " + str(hs), 24, width//2, height//2 + 100)
    pygame.display.flip()
    
    waiting=True
    #displaying the screen till user presses a key
    while waiting:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            if event.type==pygame.KEYUP:
                waiting=False
                
#setting graphics for background and objects                
#Reference:https://www.youtube.com/watch?v=mOckdKp3V38&list=PLsk-HSGFjnaH5yghzu7PcOzm9NhsW0Urw&index=7                
background =pygame.image.load(path.join(image_dir,"scroll.png")).convert()
background_rect = background.get_rect()
player_img = pygame.image.load(path.join(image_dir,"sword1.png")).convert()
bomb_img = pygame.image.load(path.join(image_dir,"bomb.png")).convert()
fruit2_img = pygame.image.load(path.join(image_dir,"banana.png")).convert()
fruit3_img = pygame.image.load(path.join(image_dir,"apple.png")).convert()
fruit4_img = pygame.image.load(path.join(image_dir,"pear.png")).convert()
#setting the sound for slicing of fruit
fruit4_sound = pygame.mixer.Sound(path.join(sound_dir, 'Pickup_Coin3.wav'))
fruit3_sound = pygame.mixer.Sound(path.join(sound_dir, 'Pickup_Coin3.wav'))
fruit2_sound = pygame.mixer.Sound(path.join(sound_dir, 'Pickup_Coin3.wav'))

#initialising score as zero
score=0 
game_over =True
running=True
#main game loop

while running:
#check for game over and restart the game 
    if game_over:
        start_scr()
        game_over = False
#to allow classes to hold and manage sprite objects
        all_sprites= pygame.sprite.Group()
        bomb=pygame.sprite.Group()
        fruit2=pygame.sprite.Group()
        fruit3=pygame.sprite.Group()
        fruit4=pygame.sprite.Group()
#creating an object of class Player
        player= Player()
#adding player to all_sprites
        all_sprites.add(player)
#loop for controlling the amount of fruits and bombs falling
        for i in range(3,6):
            m=Bomb()
            l=Fruit2()
            o=Fruit3()
            p=Fruit4()
            all_sprites.add(m)
            all_sprites.add(l)
            all_sprites.add(o)
            all_sprites.add(p)
            bomb.add(m)
            fruit2.add(l)
            fruit3.add(o)
            fruit4.add(p)
#to run the screen at given fps        
    clock.tick(fps)
#to check for quitting 
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    all_sprites.update()
#check for collision of required sprites
#Reference:https://www.youtube.com/watch?v=33g62PpFwsE&list=PLsk-HSGFjnaH5yghzu7PcOzm9NhsW0Urw&index=6
    hits=pygame.sprite.spritecollide(player, fruit2,True)
#making neccesary changes
    for hit in hits:
        score+=10
        n=Fruit2()
        all_sprites.add(n)
        fruit2.add(n)
        fruit2_sound.play()
    hits=pygame.sprite.spritecollide(player, fruit3,True)
    for hit in hits:
        score+=10
        n=Fruit3()
        all_sprites.add(n)
        fruit3.add(n)
        fruit3_sound.play()
    hits=pygame.sprite.spritecollide(player, fruit4,True)
    for hit in hits:
        score+=10
        n=Fruit4()
        all_sprites.add(n)
        fruit4.add(n)
        fruit4_sound.play()
    #to check for collision of bomb and knife    
    hits=pygame.sprite.spritecollide(player, bomb,False)
    if hits:
        game_over = True
    #sprites for background screen    
    screen.fill(blue)
    screen.blit( background, background_rect)  
    all_sprites.draw(screen)
    #display score while the game is running
    textbox(screen,"score"+' '+str(score),30,width/2, 14)
    pygame.display.flip()

pygame.quit()
